# Air780E模块开发项目遇到的吐血经历-休眠唤醒篇

## 前情提要

这周接手了另一个同事用合宙-Air780E模块没做完的项目，刚上手之后就发现了一个问题，在通过AT+CSCLK=2 进入休眠之后，连接MQTT服务器，从服务器端下行消息到模块 唤醒，并且触发RI脚的下降沿，以此唤醒MCU，但实际却唤醒不了。

## 通过自测缩小问题范围

在做过以下测试后，问题基本上锁定了。

1. 进入休眠后，mqtt链接是否有断开。
   1. 在使用 **AT+MQTTSTATU** 指令查看MQTT链接状态时，返回结果是 **+MQTTSTATU :1** 说明链接是存在的，没有断开
2. 服务端下行的数据模块是否有收到。
   1. 检测main_uart串口的URC上报，发现在下发消息的时候，模块是有上报 **+MSUB: "/topic",10 byte,1234567890** 的，可以收到
3. 用逻辑分析仪或者示波器检测下RI脚波形。
   1. 发现在进入休眠后，和服务器下发消息，模块收到URC整个流程中，RI脚都没有出现下拉的波形，说明RI脚的功能有问题？

从[Air780E](http://Air780e.cn)官网资料的硬件设计手册里面找下RI脚的位置有没有量错，嗯~ 是20脚没有错。

![img](image/780e%E7%AE%A1%E8%84%9A%E5%9B%BE.png)

## 找到了解决方法

通过摸索了一小下，看到[AT手册](https://doc.openluat.com/article/4985)中有一条指令，**AT+CFGRI** 这条指令的功能就是打开在780E模块接收到 TCP/UDP/FTP/HTTP/MQTT的URC时，RI脚就会产生120ms的低脉冲，也就是给予mcu的下降沿。

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=YjJhOWQ5YjZhMTczZThhNTg1ODA1NDI4N2E4MzBiZmZfMlNSRkVXd1FsSkF5TlhDRG43RHhkSnZCU29BOVhPYjhfVG9rZW46TExrdWJ5c0RHb0xHVE94NldQU2NmSlhJbjVmXzE3MjcxNjAyNjg6MTcyNzE2Mzg2OF9WNA)

在休眠流程中，进入休眠之前加一条这个 **AT+CFGRI=1** 的指令后，重新尝试了下，果然可以了。在收到MQTT下行数据时，RI脚正确产生一个下降沿，唤醒了主控，大致业务逻辑没问题了！

## 总结

要想Air780E模块可以通过网络服务端下行数据以此来唤醒模块以及唤醒主控，节省功耗的话，需要接入模块的RI脚，并且在流程中（最好是开机后就配置，作为初始化的流程）加入一条 **AT+CFGRI=1** 指令才可以。

并且通过实测不管进入任何休眠模式（例 AT+CSCLK=1、AT+POWERMODE="PSM+"），都需要配置 **AT+CFGRI=1** 这个指令后，才可以触发RI中断，看样子是和休眠模式没有关系的。
