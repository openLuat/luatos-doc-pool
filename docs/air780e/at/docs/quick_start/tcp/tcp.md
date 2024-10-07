## 一、AT命令概述

AT 命令是一种古老的使用方式，从有线通信就开始使用了。

距离到2024年的今天， 已经有超过40年的使用历史。

AT 命令的使用场景是，把4G模组当做一个黑盒配件，设备必须有一个主控CPU。

设备的主控CPU， 通过串口，（也可以是SPI或者USB，但是99%的场景都是通过串口），发送一个 "AT"字符串开头的指令， 像4G模组请求各种服务。

4G模组完成服务后， 回复一个字符串，向主控CPU做应答。

通过这样一系列的发送请求，应答的交互方式， 使设备具备了通信能力。

AT 命令发展到今天， 功能日趋完善。

厂家的 4G 模组的 AT 指令至少具备如下完善的功能：

1. 基本的网络查询指令 信号强度查询，运营商查询，SIM卡状态查询，IMEI 查询，注册网络状态查询，等等；
2. 各种通信协议的支持 TCP/UDP协议， HTTP协议，SSL协议，FTP协议，MQTT协议，等等；
3. 模组内部资源的使用 电话本，文件系统的存入，删除，查询，等等。

尽管 AT 使用起来很便利，但是 AT 指令方式依然有几个明显的缺点：

1. 运行效率低 只能是两个物理CPU通过串口这样的介质做异步通信， 沟通效率很低，如果要做高效的业务和通信的整合动作的话， 代价更大。
2. 需要一个额外的主控CPU；
   1. 对于复杂度不高的物联网设备，虽然4G模组本身的运算资源和存储资源已经过剩， 但是为了使用 AT 指令，依然需要一个额外的主控CPU。
   2. 为了节约成本，主控CPU往往会选择一个资源不太大的型号，通常无法运行高级语言， 所以往往要用C语言开发业务逻辑。
   3. 这需要研发团队熟悉主控CPU 的开发架构，仍然是一个不小的学习成本。
   4. 而 4G 模组因为资源足够大， 大多数 4G 模组已经支持脚本开发应用了，
   5. 所以省掉设备主控 CPU，直接用 4G 模组开发应用， 研发成本更低。

尽管 AT 指令有这些缺点， 但是由于 AT 指令有庞大的用户群， 基于使用的惯性， AT 指令在今天仍然有非常大的使用比例。

## 二、本教程实现的功能概述

本文教你怎么使用AT命令，通过几个简单的步骤，就可以让合宙4G模组连接上一个TCP服务器，并且模组和服务器之间实现数据的双向传输！

本教程实现的功能定义是：

1. 通过网页端启动一个TCP服务器；
2. 4G模组插卡开机后，连接上TCP服务器；
3. 4G模组向TCP服务器发送 `data from 4G module`，服务器可以收到数据并且在网页端显示；
4. TCP服务器网页端向4G模组发送 `data from tcp server`，4G模组可以收到数据并且通过串口输出显示；

## 三、准备硬件环境

工欲善其事，必先利其器。在正式介绍本功能示例之前，需要先准备好以下硬件环境。

### 3.1 Air780E开发板

准备一块开发板，有两种开发板可以使用，二选一即可；

第一种开发板是Air780E核心板，如下图所示：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MzAxZTVlZGFiZWVmNDQyZmVhMDk1ZTMyZTc2ZTBjODFfMDljVURkS3pod3JZSlBrNW1ZeU1EVUpCSm9acGU5ODRfVG9rZW46U1lhQWJMQXBrb0s0MXV4Q0NzY2NKbEdMbllkXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

点击链接购买：[Air780E核心板淘宝购买链接](https://item.taobao.com/item.htm?id=693774140934&pisk=f1eiwOqL25l1_HYiV6D1ize3wN5d5FMjRrpxkx3VT2uIHCCskWm4kysffAEqor4KRRIskGT0ooqi_coq7DWE000qbVr2mmzKQjNtkV3mnoalvaBRelZshA7RyTFdpD4xQco2_VS2Tcnvc89h5lZshq-pu_FUfEDVVdOmgrkET0ir3mkq_MDEmmM2QjJaY2uI0UGAoNueWRjiw4YTC-_opNr-zluaXleFpfR_X2fhTJVn94W--KJ4KcqQreCDEs3zNVh-DyWpIxqEmyc8savgoor7gX2D7GUzmW4jBJS2_4PTWjestFRZqA0iaRlwjdkIgW2nBR7XNkEn7bDL96_tMA4gN4GNOwa0xVU4IX8G4iReapZyhDSYLIOj_DinyhbSB2IHjbEhxMA51foIXaIhxItMPKJlyMjHNEGZAcQR.&spm=a1z10.5-c-s.w4002-24045920841.33.639f1fd1YrS4b6&skuId=5098266470883) ；

此核心板的详细使用说明参考：[Air780E产品手册](https://docs.openluat.com/air780e/product/) 中的 <<开发板Core_Air780E使用说明VX.X.X.pdf>>，写这篇文章时最新版本的使用说明为：[开发板Core_Air780E使用说明V1.0.5.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240419155721583_%E5%BC%80%E5%8F%91%E6%9D%BFCore_Air780E%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8EV1.0.5.pdf) ；核心板使用过程中遇到任何问题，可以直接参考这份使用说明pdf文档。

第二种开发板是Air780E低功耗验证板，如下图所示：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTc1NWMyNzc2YWFiMDIwMzUyOTcyYWUwMmI1Zjc2YzRfeFdmdFdWcVZwazZqZUZpMHRiMXVxN05CWThHbHF4aDJfVG9rZW46TDdaWGJDc0pMb2dxVDF4RU1HM2NjbHRSbk1jXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

点击链接购买：[Air780E低功耗验证板淘宝购买链接](https://item.taobao.com/item.htm?id=724722276597&pisk=fDkqNlGOsKpVRM8fOryaYfTXvzeYhJLQoAa_jcmgcr4m5owajzoHDrO9MVlrS4FboEdYjOunylsjmSfurkEVns2gizcrkDVj7cKYjP0i7PGXNpixDReMRVJBdmdqGyxxutXcrhqQvPj9-TzZDReM7jctEonx-RQoXlPM48qaxO2gsR2k4lZ_mR40samujz4MuKF2ZFS8aemLrfZhF_hf0baPI9SL0SmWpzXMgYqq4PoD6OXiUoPqCo-xqmPjsDFKh2pNe-iEZ8qZBHfa7Wlih8DDrpV8sfug2bLN_ylicXH7NGfm4Az4txVPYTmoDl0g_bLFdoyjaWkqMhQom2aqt-n1YEizTbPLq7jNigyOWubjzAhVS1P02uzB43RpbhS6iNACU1CTZJEzRnZf61F0uO1qL95O67484ytbc&spm=a1z10.5-c-s.w4002-24045920841.23.639f1fd1YrS4b6&skuId=5208106143672) ；

此低功耗验证板的详细使用说明参考：[Air780E产品手册](https://docs.openluat.com/air780e/product/) 中的 <<开发板EVB-Air780E-IO使用说明VX.X.X.pdf>>，写这篇文章时最新版本的使用说明为：[开发板EVB-Air780E-IO使用说明V1.2.0.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20231009103600243_%E5%BC%80%E5%8F%91%E6%9D%BFEVB-Air780E-IO%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8EV1.2.0.pdf) ；低功耗验证板使用过程中遇到任何问题，可以直接参考这份使用说明pdf文档。

在本教程中，使用的是第一种Air780E核心板。

### 3.2 SIM卡

准备一张可以上网的SIM卡，可以是物联网卡，也可以是自己的手机卡；

注意：SIM卡不能欠费，可以正常上网！！！

### 3.3 PC电脑

准备一台电脑；

注意：电脑有USB口，并且可以正常上网！！！

### 3.4 数据通信线

准备一根数据线，此数据线的作用是，连接Air780E开发板和PC电脑，通过AT命令完成业务逻辑的控制和交互；

有两种数据线可以使用，二选一即可；

第一种数据线是USB数据线（连接Air780E开板的一段是Type-C接口），一般来说这种数据线如下图所示：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ODQxYWM1MjZlOWIxYTViM2JiMmRmYTFiNmFjMDBkNThfVkJ4MTh3NUtZcjg2MkN6UzJwU2hIMG9mV01wNE1WTXpfVG9rZW46RHpYUGI3Y1BqbzB2ZDh4TnhpMWNhY3hJbkVlXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

普通的手机USB数据线一般都可以直接使用；

第二种数据线是USB转TTL串口线，一般来说这种数据线如下图所示：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NzRiMzQ3ZjU0ZmZiZGZiYmNhOTE5ZTVlYWM2MGFhNWRfbGdLdXNmYWhyTUtDQ2lUeU0xRUE4bjRQQnpvU1VKYjZfVG9rZW46S01JWWJMNVI0b3VlSWR4dnBaV2MwU2ZmbnlkXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

在本教程中，使用的是第一种USB数据线。

### 3.5 组装硬件环境

按照SIM卡槽上的插入方向，插入SIM卡，注意不要插反！

如下图所示，将SIM卡用力推入卡槽，听到咔嚓声音后即可。

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MDA0OWM0OWE2OWQyYTkyNDg5MWJkYzFhNGFmODExZjlfbFd1UmVhM3M4RVFYRFdGZGptUklHMno0SjlMaWtxa0FfVG9rZW46SGZpNGJyMGRtb2pUcXJ4TUpxWmNNd29DbkhmXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZWZlNjA3NjNkYWVhYmVlNzNjNTk2Y2M1ZTYxYjdkN2ZfVUl5WUxER0xoVjZTRmI2dk9Ed01zdGVsYUdlSzFvbWNfVG9rZW46U0FGeGI5Z202b0pPMjZ4SGVlR2NhOUw1bjBnXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

USB数据线，连接电脑和Air780E开发板，如下图所示：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MzIxNjI5MDMzNWVmZTJiZTlhODcwOTEyNTM3MDE1Y2ZfOHlqanNrVXJUbDdGdGxXTmFnSmxIYnF2bElodVRVRXJfVG9rZW46RElsNGI5ZDVCb2lrVDJ4eGtRdWNuTTBqbmZkXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

## 四、准备软件环境

工欲善其事，必先利其器。在正式介绍本功能示例之前，需要先准备好以下软件环境。

### 4.1 Luatools工具

要想烧录AT固件到4G模组中，需要用到合宙的强大的调试工具：Luatools；

详细使用说明参考：[Luatools工具使用说明](https://docs.openluat.com/Luatools/) 。

### 4.2 AT固件

4G模组中必须烧录正确的AT固件才能支持AT命令功能；

通过Luatools可以烧录AT固件；

有两种方式可以获取到Air780E模组的最新AT固件，二选一即可；

第一种方式是通过Luatools获取，如下图所示，可以直接选中最新版本的AT固件：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTliNDI2MjViNzMzMDdlZjYzNjdhOTQ2ZTU5YzViOTFfVjBzZWJ0RlZUQ1d0MVZLT3lHdG5vSnU0MXBFTVNjdVNfVG9rZW46VGpCbGJmSzVMbzFlTll4OURuV2NVdnB4bjFmXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

第二种方式是访问：[Air780E固件版本](https://docs.openluat.com/air780e/at/firmware/) ，找到最新版本的固件即可。

### 4.3 合宙TCP/UDP web测试工具

为了方便测试，合宙提供了免费的不可商用的TCP/UDP web测试工具；

详细使用说明参考：[合宙TCP/UDP web测试工具使用说明](https://docs.openluat.com/TCPUDP_Test/) 。

### 4.4 PC端串口工具

在量产的项目硬件设计中，一般都是由主控MCU通过UART给4G模组发送命令实现具体的业务逻辑；

在本教程中，为了测试方便，没有使用主控MCU；

而是使用了PC电脑上的一个串口工具LLCOM给4G模组发送命令来实现演示功能；

LLCOM的下载链接：[LLCOM](https://llcom.papapoi.com/index.html) ，详细使用说明可以直接参考下载网站。

## 五、开发板开机，确认固件正确

### 5.1 开发板开机

打开Luatools工具，用来监控Air780E的运行状态；

长按开发板上的POW按键1到2秒，绿灯开始闪烁，可以初步判断开发板已经正常开机；

此时打开电脑设备管理器中的端口，如果出现下图中的三个端口，则可以确定已经正常开机：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDYxOTk0MDMwMmE3ZjBhNTViYTJmMjY2YWNmNDZiNzJfUFRkYjYxVXR5TkVNVEdhSm56Z1VjTEdoS1BYTUliWHFfVG9rZW46UzlueGJTM1Fjb3RMZ0d4M1l6MmMxZkVCbktiXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

### 5.2 如何判断开发板中运行的是正确的AT固件

此时再观察Luatools的主界面，如果有以下典型的日志信息，则表示Air780E模组中为AT版本的固件，是本教程期望的固件：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NWE5ODcxODgxYWQ5ZDc1YjU3ZGZkNDEyZTZkY2EzMzdfckJreUxSTjhVRVNaajREblBqNk1wR0ZhNHUxQ0EzS21fVG9rZW46TW5QamI1TDdDbzJpd0t4aERmQWNRNjRtbldkXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

### 5.3 如何给开发板中烧录正确的AT固件

如果Luatools显示不是AT固件，则需要手动烧录正确的AT固件，烧录方法如下：

1、Luatools选择正确的AT固件版本文件，如下图所示，编写本教程时，最新版本为V1165；你实际烧录时，和这个版本号不一定一致，没有关系，直接使用Luatools默认识别的版本文件即可。

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=Y2IxODhmOTQ5MDM1MzE3OGE3ZmY2YWQ1MmUyNDQ2NWNfOVBHVnU3NHZRRFZwbm9iMFUyY0xHZEdKZnRheEp4U05fVG9rZW46V25yYmJITVdUbzlFZEh4NFpXSGM2T0htblJlXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MTU0ZDQ4YmNlMTI5NzU5OGY3YmQ5NzE3MGFiZGMyMjlfNU84SWY1ZmJMR2F1bWlMcEg3RXFXSVF0MVlXMEtUM3VfVG9rZW46U2VZQ2J3eDNpb3hUdU14TGE3U2M5TkRsblNjXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

2、Air780E开发板进入BOOT模式，分为以下两种情况：

    （1）如果开发板处于开机状态，则长按BOOT按键，然后短按一下RST按键会进入BOOT模式；

    （2）如果开发板处于关机状态，则长按BOOT按键，然后长按POW按键会进入BOOT模式；

    可以通过观察电脑设备管理器中的端口，如果出现下图中的一个端口，则表示进入了BOOT模式；

3、点击Luatools工具上的下载按钮即可

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZmQ4ODgyMDZlN2UxYjYwNjdmYzg0N2Q4MTdjMWUwM2FfdG9pZ1lQQm5LNlhRYXVGdEZmZk9LRDRjUnZvY1RETkdfVG9rZW46RWFCaGJqNzZQb09UZTV4M3F3RmN3RmFZbkJlXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=OTg0NjA4YjkwMjE2NDJlODBkOTdiODRjYWM2OTE3MDlfbWZlMlVLNlNLRWx6ZU1TcWZzMGpGb1ZTaUVzWlFNZWNfVG9rZW46TUoyT2JHWVB4b1Faend4VFk4bGNMSTFXbnplXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MWRiODlkZjZhZDMzNjk0N2U5ZDU2YzNhOWFlNzI2NGFfZWZSQzFrdHpNSDd6ODZod0tvSW5YdHlSdTNYN1k4OExfVG9rZW46RW9UdWI1aXhsb1Zacmx4bzdHMmNvWEh3bkJnXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

4、下载完成后，Air780E开发板会自动重启，Luatools的监控界面如下图所示：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=N2ZlM2MxY2NhMTgxMDk3MGI2Yjk4MDc0ZTNjMGM5NTlfejE1VU5XUERTM3dRSHZHWXFhWVRmT1B3SGh1WlJvMDFfVG9rZW46VlE4MWI1bkdDb05oSmN4OHZ4ZWNscXhNbkJmXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

## 六、打开LLCOM和WEB测试工具

### 6.1 打开LLCOM并且配置正确

此时需要关闭Luatools工具，因为Luatools会占用AT命令端口！！！

打开LLCOM工具后，按照下图提示进行配置并且验证

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=YTc2YmEzMDM1NDJkYzBiMWQwYWY5ZmQ3NDE1MDE5NzNfY1pCVVF2WDZITnlMWDdaV1pFZnp2MWpWMklqeHdZS0FfVG9rZW46RWVnS2I2dk55b1hZNmp4ZTBWS2NhWUNlbkNiXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

### 6.2 打开WEB测试工具，启动一个TCP服务器

访问[WEB测试工具](https://netlab.luatos.com/) ，启动一个TCP服务器，如下图所示：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=Njc2YzM1MGRlZTVhYzUwZjZhNmUyOWZjYjU0MDUwYmZfRlN6SXZ2MENKV1hCUWU1MVQyRnBBUlg3S01RREkxamlfVG9rZW46R1pUSmJ2SWswb2xLcm54a1o5TWMwVDdabnFkXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=YTI5NDA3MDA5YzVhNjM2MWFkMDAzYmRhYzc1MzYyOWZfcDJDeEJrdndGZEdTOWtMSW9SQ0VxRjg5TUR1RXNKdGlfVG9rZW46Q0JJa2JGb1BGbzB3end4bU5tMGNER3B1bm1kXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

## 七、AT命令控制实现具体的业务逻辑

### 7.1 查询SIM卡状态

每隔1秒发送AT+CPIN?查询SIM卡状态，直到收到+CPIN: READY表示正常识别的SIM卡；

如果模组主动上报SIM REMOVED或者查询返回+CME ERROR: 10，表示没有检测到SIM卡；

如果10s内没有仍然没有识别到SIM卡，建议重启模块，如果重启后问题依旧，需要检查卡是否有插好，或者排查板子的硬件连接。

正常如下图所示：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZWZmYjg2ZmE2NTUwY2FhMTZjZDA5ZmJiMWE3ZjExYmVfRHR2ZGpWSlE2eUJOdEgyQVgwanpKY1Nmcms0cXhPRDRfVG9rZW46VllxY2J2UGNJbzFBcEd4bHhHNWNTTlJtbk9mXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

### 7.2 查询模组信号强度

每隔1秒发送AT+CSQ查询信号强度，直到信号强度正常；

一般来说，信号强度18以上才能稳定通讯；

11-17存在断网的可能；

10以下基本连接不上；

正常如下图所示：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NzhjMzllNDI0NTU1YWE3ZWVlNTY3NjkzYzFlOTY5NGZfTFU5WmhHZUw3TWJybWtMd0E0emhVTkhrU3ZKS1JOSm1fVG9rZW46WDZ0SGI0bDhrb2ZJeGx4bEw5bmM2d2pXbkRoXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

### 7.3 查询网络注册情况

每隔1秒发送AT+CGATT?查询是否成功注册网络，直到收到+CGATT: 1；

值为1表示注册成功，正常情况下注册时间不会超过两分钟，如果超过两分钟没有注册可以重启开发板再试下；

值为0表示没有注册成功；

正常如下图所示：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZGZjOTdiNWUyNzkzMzY1YjA0OWU0MzFlMTdhYWM2YWNfZGZKWFhPTm5lYWh3Q21tQ3NQTG9sM3FuNGp3Mm5JREtfVG9rZW46RURlamJkYVlab1RwbG94MTBqdGNLam9FblRMXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

### 7.4 激活数据网络

AT+CSTT命令表示配置数据网络；

AT+CIICR表示激活数据网络；

AT+CIFSR表示查询是否激活成功，如果返回一个ip地址，表示激活成功；

正常如下图所示：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MzE1NTZjYTNiZmRjODYzM2JhNjM2OTEzZmMyMmM0MjVfT0dQVE5XS3lvU2p5MWpBNEtiRHJrZXJvaVZvT0FQNUVfVG9rZW46Sm1WYmJNTmYzb05nRTJ4WTV3NGNrbjBhbkVmXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

### 7.5 连接TCP服务器

使用AT+CIPSTART命令连接WEB测试工具启动的TCP服务器，返回CONNECT OK表示连接成功；

正常如下图所示：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTlhYmJjNGU2ZTk3ZTdjMDkyNTQzNjBiNDViMmQ0ZTlfdjN2ZEU0THJwRnc0NnkycnN5ajRpbmpMektLVkluTjVfVG9rZW46TEdwWGJOQVRobzdnWEd4ZkFvQmNlMU54bmxkXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

### 7.6 4G模组发送数据给TCP服务器

AT+CIPSEND命令可以发送指定长度的数据给服务器；

本示例中，要发送 `data from 4G module`数据给服务器，这段数据有19个字符，但是因为LLCOM工具上勾选了发送回车换行选项，所有在这19个字符后面会紧跟着回车和换行两个字符，所以一共要发送21个字符给服务器；

正常如下图所示：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NDUxYjIyYzk4NzEwNTcyYTcyYzNjYzdhYzQ2ZjAxODNfZ0VSY213V0ZSaDdvZmMzbXhaa1FqUWgzTm9yR2lsekFfVG9rZW46UzVJQ2JjSnBqbzhCNXh4c0JSWGNjS3ZIbnFlXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

此时再观察下WEB测试工具网页，可以看到已经收到了模组发送的数据，如下图所示：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NGI2ZjU4ZDliZjhjYTk5ZmEzZjdiM2VmNjU1ZjdjYmZfMUZkMmJncTFha05hbDVld1ZoWURXUHY5dlZSbGpSNjdfVG9rZW46VEdhYmJvaWhlbzg3ZHV4cDRkSGNEanJJblNmXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

### 7.7 TCP服务器发送数据给4G模组

在WEB测试工具网页端，输入 `data from tcp server`，然后点击发送按钮，如下图所示：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NDcyNGM3YzIyODRmNjQ0NGI5MGI3NDQ2ZTliY2E5OTZfRnRRazVpUUVoTjhLa1hNZWRyblNMN083VkhHTUwxa3NfVG9rZW46RmxQNmJqVVUxb1dMMU94MEgxdmNtdDh4bktkXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)

此时观察LLCOM，可以看到4G模组收到了数据，如下图所示：

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MDM1YjdjODQzZGNjNGU3YzlkODRkZmYwYWU2NjE3YzFfSmZBM1plUzJiZ0lQbWZQaWdLaVRTaWwwWHh5eHRMNmJfVG9rZW46WkMyc2JsU3pSb2RodTR4WFZIT2NsaXBqbjNiXzE3MjgzMTA3NDY6MTcyODMxNDM0Nl9WNA)
