
## 一、MQTT 协议简介

### 1.1 MQTT 概述

MQTT 是一种轻量级的消息传输协议，旨在在物联网（IoT）应用中实现设备间的可靠通信。它使用发布-订阅模式，其中包括一个 MQTT 服务端（代理或服务器）和多个 MQTT 客户端之间的通信。MQTT 协议具有以下特点：

- 轻量级：MQTT 协议设计简单，协议头部开销小，适用于资源受限的设备和网络。
- 低带宽消耗：MQTT 采用二进制编码，有效地利用网络带宽。
- 异步通信：客户端可以随时发布和订阅消息，无需等待对方的响应。
- 发布-订阅模式：消息发布者将消息发布到特定的主题，而订阅者则订阅感兴趣的主题。这种模式支持松耦合的通信和灵活的消息传递。

### 1.2 MQTT 协议中重要名词

- username 用户名，password 密码，clientid 用户标识，mqtt 可以通过前两个参数保证连接的安全，通过 clientid 确保设备唯一性。
- qos 消息质量，分为 0，1，2 三个等级，分别表示只发一次，至少收到一次和只收到一次，通过 qos 可以根据数据的重要性灵活选择发送方式以节省带宽和保证数据可靠。例如不重要的数据采集可使用 qos0 只发一次不关心服务器是否收到，重要的消息通过 qos1 确保能收到，付款信息危险设备开关等场景使用 qos2 保证数据到达的同时且不重复。
- host 主机，port 端口，mqtt 需要连接的服务器参数。host 可以说 ip 或者域名。
- topic 主题，根据主题区别消息类型和来源，主要用来分类数据。同时 mqtt 是发布订阅模型，topic 是发布和订阅者通信的重要通道。
- payload 消息内容，发布和订阅的具体数据。
- retain 保留消息，保留消息是一条将保留标志（retained flag）置为 true 的普通 MQTT 消息。broker 会针对主题依照 QoS 级别保留最后一条保留消息，当订阅者订阅主题时会立即收到保留消息。broker 仅为每个主题保留一条保留消息。

## 二、本教程实现的功能概述

本文教你合宙 4G 模组使用 AT 命令连接 MQTT 服务器，实现模组和服务器之间数据的双向传输！

本教程实现的功能定义是：
1. 准备一个 MQTT 服务器;
2. 4G 模组插卡开机后，连接上 MQTT 服务器,订阅一个消息 `/mqtt/pub`;
3. 使用 MQTT 协议的 PC 工具（本篇演示时使用的是 mqttx），用工具连接 mqtt 服务器,同时订阅消息 `/mqtt/sub`;
4. 4G 模组向工具订阅的消息 `/mqtt/sub` 发布消息 `data from 4G module`，工具可以接收到并显示出来；
5. 工具向 4G 模组订阅的消息 `/mqtt/pub` 发布消息 `data from tcp server`，模组可以接收到数据并通过串口输出显示
6. 演示加密 mqtt 通信流程
7. 演示专网卡和设置 apn 等特殊情况连接 mqtt 服务器

## 三、准备硬件环境

工欲善其事，必先利其器。在正式介绍本功能示例之前，需要先准备好以下硬件环境。

### 3.1 Air780E 开发板

使用的开发板是 Air780E 核心板，如下图所示：

![](image/KdWObqXHIoE7Jxx4h46cAStZnRb.png)

点击链接购买：[Air780E 核心板淘宝购买链接](https://item.taobao.com/item.htm?id=693774140934&pisk=f1eiwOqL25l1_HYiV6D1ize3wN5d5FMjRrpxkx3VT2uIHCCskWm4kysffAEqor4KRRIskGT0ooqi_coq7DWE000qbVr2mmzKQjNtkV3mnoalvaBRelZshA7RyTFdpD4xQco2_VS2Tcnvc89h5lZshq-pu_FUfEDVVdOmgrkET0ir3mkq_MDEmmM2QjJaY2uI0UGAoNueWRjiw4YTC-_opNr-zluaXleFpfR_X2fhTJVn94W--KJ4KcqQreCDEs3zNVh-DyWpIxqEmyc8savgoor7gX2D7GUzmW4jBJS2_4PTWjestFRZqA0iaRlwjdkIgW2nBR7XNkEn7bDL96_tMA4gN4GNOwa0xVU4IX8G4iReapZyhDSYLIOj_DinyhbSB2IHjbEhxMA51foIXaIhxItMPKJlyMjHNEGZAcQR.&spm=a1z10.5-c-s.w4002-24045920841.33.639f1fd1YrS4b6&skuId=5098266470883) ；

此核心板的详细使用说明参考：[Air780E 产品手册](https://docs.openluat.com/air780e/product/) 中的 << 开发板 Core_Air780E 使用说明 VX.X.X.pdf>>，写这篇文章时最新版本的使用说明为：[开发板 Core_Air780E 使用说明 V1.0.5.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240419155721583_%E5%BC%80%E5%8F%91%E6%9D%BFCore_Air780E%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8EV1.0.5.pdf) ；核心板使用过程中遇到任何问题，可以直接参考这份使用说明 pdf 文档。

### 3.2 SIM 卡

准备一张可以上网的 SIM 卡，可以是物联网卡，也可以是自己的手机卡；
注意：SIM 卡不能欠费，可以正常上网！！！

### 3.3 PC 电脑

准备一台电脑；
注意：电脑有 USB 口，并且可以正常上网！！！

### 3.4 数据通信线

准备一根数据线，此数据线的作用是，连接 Air780E 开发板和 PC 电脑，通过 AT 命令完成业务逻辑的控制和交互；
有两种数据线可以使用，二选一即可；
第一种数据线是 USB 数据线（连接 Air780E 开板的一段是 Type-C 接口），一般来说这种数据线如下图所示：

![](image/Xv16bko9voAoEVxlLzucnRabntd.png)

普通的手机 USB 数据线一般都可以直接使用；

第二种数据线是 USB 转 TTL 串口线，一般来说这种数据线如下图所示：

![](image/RapibzmMjo9aLMxgRWdccAdSnMh.png)

在本教程中，使用的是第一种 USB 数据线。

### 3.5 组装硬件环境

按照 SIM 卡槽上的插入方向，插入 SIM 卡，注意不要插反！
如下图所示，将 SIM 卡用力推入卡槽，听到咔嚓声音后即可。

![](image/F4oHbholSoFAPRxAbXgcIO5rnUA.png)

![](image/GyhRb6TdJo5Y1SxJrmkccwWQned.png)

USB 数据线，连接电脑和 Air780E 开发板，如下图所示：

![](image/IrukbStYeopEn7xSo7VcPxFTnjf.png)

## 四、准备软件环境

在正式使用之前，需要安装装备好以下软件。

### 4.1 Luatools 工具

要想烧录 AT 固件到 4G 模组中，需要用到合宙的强大的调试工具：Luatools；
详细使用说明参考：[Luatools 工具使用说明](https://docs.openluat.com/Luatools/) 。

### 4.2 AT 固件

4G 模组中必须烧录正确的 AT 固件才能支持 AT 命令功能；
通过 Luatools 可以烧录 AT 固件；
有两种方式可以获取到 Air780E 模组的最新 AT 固件，二选一即可；
第一种方式是通过 Luatools 获取，如下图所示，可以直接选中最新版本的 AT 固件：
![](image/LUmebBzjQoiTLfxO6QNczjrjnKg.png)

第二种方式是访问：[Air780E 固件版本](https://docs.openluat.com/air780e/at/firmware/) ，找到最新版本的固件即可。

### 4.3 合宙 MQTT 测试服务器

为了方便测试，合宙提供了免费的不可商用的 MQTT 测试服务器；

```
host:airtest.openluat.com
port:1883
sslport:8883
username:root
password:luat123456
```

ssl 加密链接所需要的证书文件：[mqttcerts.zip](https://cdn.openluat-luatcommunity.openluat.com/attachment/20220914171655607_mqttcerts.zip)

### 4.4 PC 端串口工具

在量产的项目硬件设计中，一般都是由主控 MCU 通过 UART 给 4G 模组发送命令实现具体的业务逻辑；
在本教程中，为了测试方便，没有使用主控 MCU；
而是使用了 PC 电脑上的一个串口工具 SSCOM 给 4G 模组发送命令来实现演示功能。

### 4.5 mqttx 工具下载

MQTTX 是一款功能强大的 MQTT 客户端应用，专为物联网 (IoT) 和消息传递设计。它提供了直观的用户界面，支持多种连接配置，方便用户进行设备的快速连接、消息发布与订阅，以及数据监控与管理。安装教程可参考这篇文章：[MQTTX 下载使用详解](https://mqttx.app/zh/docs)

## 五、MQTT 相关指令

[点击链接查看合宙 4G 模组 MQTT 指令](https://docs.openluat.com/air780e/at/app/at_command/#mqtt)

## 六、使用方法举例

### 6.1 确认开发板正常开机并联网正常

本次教程所用固件版本是 v1169，通过 luatools 烧录过固件后可以通过打印来判断设备情况，具体参考下图：

![](image/CECEbDcmuotrdgxMo8QcIkL0nAc.png)

### 6.2 普通不带证书使用流程举例

下面演示及普通连接流程，并进行收发测试。

查看流程时需要注意指令后面注释的内容，有助于理解指令具体作用

```
ATI                     //查询版本号

AirM2M_780E_V1169_LTE_AT

OK

AT+CGREG?               //查询当前GPRS注册状态

+CGREG: 0,1             //<stat>=1，标识已经注册GPRS网络，而且是本地网

OK

AT+CGATT?               //查看当前GPRS附着状态

+CGATT: 1               //<state>=1，标明当前GPRS已经附着

OK

AT+MCONFIG=868488076771714,root,luat123456              //填写clientid、用户名、密码；可以带引号可以不带

OK

AT+MIPSTART="airtest.openluat.com","1883"               //填写mqtt服务器的域名和端口号；注意，如果是无证书ssl加密连接时，指令格式需要换成 AT+SSLMIPSTART=<svraddr>,<port>

OK

CONNECT OK

AT+MCONNECT=1,60                //建立mqtt会话；注意需要返回CONNECT OK后才能发此条指令，并且要立即发，否则就会被服务器踢掉

OK

CONNACK OK                  //连接成功，成功后才能发布消息或者订阅消息

AT+MSUB="mqtt/pub",0        //订阅主题

OK

SUBACK

AT+MPUB="mqtt/sub",0,0,"data from 4G module"        //发布主题

OK

+MSUB: "mqtt/pub",20 byte,data from tcp server          //收到服务器下发的消息，+MSUB的URC上报

AT+MDISCONNECT              //模块需要先关闭mqtt连接

OK

AT+MIPCLOSE                 //关闭tcp连接

OK
```

可以通过工具看到模组正常上报了数据，服务器下发模组也能正常收到并通过串口打印出来：

![](image/KlEPbrLefoEfktxRqHhcTnfsnEc.png)

### 6.3 SSL 带证书单向认证流程举例

MQTT 单向认证加密是指，在 MQTT 通信中仅服务端验证客户端身份，以此确保通信数据的安全传输。

下面演示单向认证加密连接的流程，并进行收发测试

本次测试需要准备好单向认证的加密证书，如果使用的是合宙测试服务器的话需要下载上面服务器信息除的加密证书文件。如图所示：

![](image/WjijbbWP6ogvfhxrMNwczLVUn0H.png)

工具选择加密端口，同时配置 ca 证书文件，具体如图所示：

![](image/EMuwbqFrtocKpSxC1NycxU7gnid.png)

单向认证测试流程如下：

```
^MODE: 17,17

+E_UTRAN Service

+CGEV: ME PDN ACT 1,0

+NITZ: 2024/10/11,07:38:35+0,0
AT+CGATT?

+CGATT: 1

OK
AT+FSCREATE="ca.crt"                          //创建ca证书文件

OK
AT+FSWRITE="ca.crt",0,1212,15                //写入证书文件，测试服务器证书文件长度是1212,15是超时时间，需要根据自己实际情况填写。

>
-----BEGIN CERTIFICATE-----
MIIDUTCCAjmgAwIBAgIJAPPYCjTmxdt/MA0GCSqGSIb3DQEBCwUAMD8xCzAJBgNV
BAYTAkNOMREwDwYDVQQIDAhoYW5nemhvdTEMMAoGA1UECgwDRU1RMQ8wDQYDVQQD
DAZSb290Q0EwHhcNMjAwNTA4MDgwNjUyWhcNMzAwNTA2MDgwNjUyWjA/MQswCQYD
VQQGEwJDTjERMA8GA1UECAwIaGFuZ3pob3UxDDAKBgNVBAoMA0VNUTEPMA0GA1UE
AwwGUm9vdENBMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzcgVLex1
EZ9ON64EX8v+wcSjzOZpiEOsAOuSXOEN3wb8FKUxCdsGrsJYB7a5VM/Jot25Mod2
juS3OBMg6r85k2TWjdxUoUs+HiUB/pP/ARaaW6VntpAEokpij/przWMPgJnBF3Ur
MjtbLayH9hGmpQrI5c2vmHQ2reRZnSFbY+2b8SXZ+3lZZgz9+BaQYWdQWfaUWEHZ
uDaNiViVO0OT8DRjCuiDp3yYDj3iLWbTA/gDL6Tf5XuHuEwcOQUrd+h0hyIphO8D
tsrsHZ14j4AWYLk1CPA6pq1HIUvEl2rANx2lVUNv+nt64K/Mr3RnVQd9s8bK+TXQ
KGHd2Lv/PALYuwIDAQABo1AwTjAdBgNVHQ4EFgQUGBmW+iDzxctWAWxmhgdlE8Pj
EbQwHwYDVR0jBBgwFoAUGBmW+iDzxctWAWxmhgdlE8PjEbQwDAYDVR0TBAUwAwEB
/zANBgkqhkiG9w0BAQsFAAOCAQEAGbhRUjpIred4cFAFJ7bbYD9hKu/yzWPWkMRa
ErlCKHmuYsYk+5d16JQhJaFy6MGXfLgo3KV2itl0d+OWNH0U9ULXcglTxy6+njo5
CFqdUBPwN1jxhzo9yteDMKF4+AHIxbvCAJa17qcwUKR5MKNvv09C6pvQDJLzid7y
E2dkgSuggik3oa0427KvctFf8uhOV94RvEDyqvT5+pgNYZ2Yfga9pD/jjpoHEUlo
88IGU8/wJCx3Ds2yc8+oBg/ynxG8f/HmCC1ET6EHHoe2jlo8FpU/SgGtghS1YL30
IWxNsPrUP+XsZpBJy/mvOhE5QXo6Y35zDqqj8tI7AGmAWu22jg==
-----END CERTIFICATE-----

OK
AT+SSLCFG="cacert",88,"ca.crt"                //设置ca证书文件名称，ca.crt为证书文件名称

OK
AT+SSLCFG="seclevel",88,1                    //设置认证模式为只对服务器认证

OK
AT+MCONFIG=868488076771714,root,luat123456

OK
AT+SSLMIPSTART="airtest.openluat.com","8883"            //注意本次是ssl加密所以使用的是SSLMIPSTART

OK

CONNECT OK
AT+MCONNECT=1,60

OK

CONNACK OK
AT+MSUB="mqtt/pub",0                        //订阅主题

OK

SUBACK

+MSUB: "mqtt/pub",20 byte,data from tcp server        //收到服务器下发消息
AT+MPUB="mqtt/sub",0,0,"data from 4G module"            //上报消息到服务器

OK
```

模组与服务器交互过程通过工具监控如图：

![](image/UYaUbOCGaofUpbxNcAIc2qBwnbg.png)

### 6.4 SSL 带证书双向认证流程举例

MQTT 协议双向认证加密是指客户端和服务器在通信时都使用数字证书进行身份验证，并使用 TLS 协议对通信数据进行加密，确保数据的机密性和完整性。

下面演示双向认证加密连接的流程，并进行收发测试

所需证书文件如图所示：

![](image/VSyub84BGovJPAxVChecjDJFnJf.png)

工具配置加密证书如图：

![](image/Vl7jbW68loIP7uxJAfkcMBDknwc.png)

双向认证测试流程：

```
AT+CGATT?

+CGATT: 1

OK
AT+FSCREATE="ca.crt"

OK
AT+FSWRITE="ca.crt",0,1212,15

>
-----BEGIN CERTIFICATE-----
MIIDUTCCAjmgAwIBAgIJAPPYCjTmxdt/MA0GCSqGSIb3DQEBCwUAMD8xCzAJBgNV
BAYTAkNOMREwDwYDVQQIDAhoYW5nemhvdTEMMAoGA1UECgwDRU1RMQ8wDQYDVQQD
DAZSb290Q0EwHhcNMjAwNTA4MDgwNjUyWhcNMzAwNTA2MDgwNjUyWjA/MQswCQYD
VQQGEwJDTjERMA8GA1UECAwIaGFuZ3pob3UxDDAKBgNVBAoMA0VNUTEPMA0GA1UE
AwwGUm9vdENBMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzcgVLex1
EZ9ON64EX8v+wcSjzOZpiEOsAOuSXOEN3wb8FKUxCdsGrsJYB7a5VM/Jot25Mod2
juS3OBMg6r85k2TWjdxUoUs+HiUB/pP/ARaaW6VntpAEokpij/przWMPgJnBF3Ur
MjtbLayH9hGmpQrI5c2vmHQ2reRZnSFbY+2b8SXZ+3lZZgz9+BaQYWdQWfaUWEHZ
uDaNiViVO0OT8DRjCuiDp3yYDj3iLWbTA/gDL6Tf5XuHuEwcOQUrd+h0hyIphO8D
tsrsHZ14j4AWYLk1CPA6pq1HIUvEl2rANx2lVUNv+nt64K/Mr3RnVQd9s8bK+TXQ
KGHd2Lv/PALYuwIDAQABo1AwTjAdBgNVHQ4EFgQUGBmW+iDzxctWAWxmhgdlE8Pj
EbQwHwYDVR0jBBgwFoAUGBmW+iDzxctWAWxmhgdlE8PjEbQwDAYDVR0TBAUwAwEB
/zANBgkqhkiG9w0BAQsFAAOCAQEAGbhRUjpIred4cFAFJ7bbYD9hKu/yzWPWkMRa
ErlCKHmuYsYk+5d16JQhJaFy6MGXfLgo3KV2itl0d+OWNH0U9ULXcglTxy6+njo5
CFqdUBPwN1jxhzo9yteDMKF4+AHIxbvCAJa17qcwUKR5MKNvv09C6pvQDJLzid7y
E2dkgSuggik3oa0427KvctFf8uhOV94RvEDyqvT5+pgNYZ2Yfga9pD/jjpoHEUlo
88IGU8/wJCx3Ds2yc8+oBg/ynxG8f/HmCC1ET6EHHoe2jlo8FpU/SgGtghS1YL30
IWxNsPrUP+XsZpBJy/mvOhE5QXo6Y35zDqqj8tI7AGmAWu22jg==
-----END CERTIFICATE-----
OK
AT+FSCREATE="client.crt"                    //创建客户端证书文件

OK
AT+FSWRITE="client.crt",0,1127,15            //文件大小根据实际情况填写

>
-----BEGIN CERTIFICATE-----
MIIDEzCCAfugAwIBAgIBATANBgkqhkiG9w0BAQsFADA/MQswCQYDVQQGEwJDTjER
MA8GA1UECAwIaGFuZ3pob3UxDDAKBgNVBAoMA0VNUTEPMA0GA1UEAwwGUm9vdENB
MB4XDTIwMDUwODA4MDY1N1oXDTMwMDUwNjA4MDY1N1owPzELMAkGA1UEBhMCQ04x
ETAPBgNVBAgMCGhhbmd6aG91MQwwCgYDVQQKDANFTVExDzANBgNVBAMMBkNsaWVu
dDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMy4hoksKcZBDbY680u6
TS25U51nuB1FBcGMlF9B/t057wPOlxF/OcmbxY5MwepS41JDGPgulE1V7fpsXkiW
1LUimYV/tsqBfymIe0mlY7oORahKji7zKQ2UBIVFhdlvQxunlIDnw6F9popUgyHt
dMhtlgZK8oqRwHxO5dbfoukYd6J/r+etS5q26sgVkf3C6dt0Td7B25H9qW+f7oLV
PbcHYCa+i73u9670nrpXsC+Qc7Mygwa2Kq/jwU+ftyLQnOeW07DuzOwsziC/fQZa
nbxR+8U9FNftgRcC3uP/JMKYUqsiRAuaDokARZxVTV5hUElfpO6z6/NItSDvvh3i
eikCAwEAAaMaMBgwCQYDVR0TBAIwADALBgNVHQ8EBAMCBeAwDQYJKoZIhvcNAQEL
BQADggEBABchYxKo0YMma7g1qDswJXsR5s56Czx/I+B41YcpMBMTrRqpUC0nHtLk
M7/tZp592u/tT8gzEnQjZLKBAhFeZaR3aaKyknLqwiPqJIgg0pgsBGITrAK3Pv4z
5/YvAJJKgTe5UdeTz6U4lvNEux/4juZ4pmqH4qSFJTOzQS7LmgSmNIdd072rwXBd
UzcSHzsJgEMb88u/LDLjj1pQ7AtZ4Tta8JZTvcgBFmjB0QUi6fgkHY6oGat/W4kR
jSRUBlMUbM/drr2PVzRc2dwbFIl3X+ZE6n5Sl3ZwRAC/s92JU6CPMRW02muVu6xl
goraNgPISnrbpR6KjxLZkVembXzjNNc=
-----END CERTIFICATE-----
OK

AT+FSCREATE="client.key"                //创建客户端key文件

OK
AT+FSWRITE="client.key",0,1679,15        //注意大小根据实际情况填写

>

-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAzLiGiSwpxkENtjrzS7pNLblTnWe4HUUFwYyUX0H+3TnvA86X
EX85yZvFjkzB6lLjUkMY+C6UTVXt+mxeSJbUtSKZhX+2yoF/KYh7SaVjug5FqEqO
LvMpDZQEhUWF2W9DG6eUgOfDoX2milSDIe10yG2WBkryipHAfE7l1t+i6Rh3on+v
561LmrbqyBWR/cLp23RN3sHbkf2pb5/ugtU9twdgJr6Lve73rvSeulewL5BzszKD
BrYqr+PBT5+3ItCc55bTsO7M7CzOIL99BlqdvFH7xT0U1+2BFwLe4/8kwphSqyJE
C5oOiQBFnFVNXmFQSV+k7rPr80i1IO++HeJ6KQIDAQABAoIBAGWgvPjfuaU3qizq
uti/FY07USz0zkuJdkANH6LiSjlchzDmn8wJ0pApCjuIE0PV/g9aS8z4opp5q/gD
UBLM/a8mC/xf2EhTXOMrY7i9p/I3H5FZ4ZehEqIw9sWKK9YzC6dw26HabB2BGOnW
5nozPSQ6cp2RGzJ7BIkxSZwPzPnVTgy3OAuPOiJytvK+hGLhsNaT+Y9bNDvplVT2
ZwYTV8GlHZC+4b2wNROILm0O86v96O+Qd8nn3fXjGHbMsAnONBq10bZS16L4fvkH
5G+W/1PeSXmtZFppdRRDxIW+DWcXK0D48WRliuxcV4eOOxI+a9N2ZJZZiNLQZGwg
w3A8+mECgYEA8HuJFrlRvdoBe2U/EwUtG74dcyy30L4yEBnN5QscXmEEikhaQCfX
Wm6EieMcIB/5I5TQmSw0cmBMeZjSXYoFdoI16/X6yMMuATdxpvhOZGdUGXxhAH+x
xoTUavWZnEqW3fkUU71kT5E2f2i+0zoatFESXHeslJyz85aAYpP92H0CgYEA2e5A
Yozt5eaA1Gyhd8SeptkEU4xPirNUnVQHStpMWUb1kzTNXrPmNWccQ7JpfpG6DcYl
zUF6p6mlzY+zkMiyPQjwEJlhiHM2NlL1QS7td0R8ewgsFoyn8WsBI4RejWrEG9td
EDniuIw+pBFkcWthnTLHwECHdzgquToyTMjrBB0CgYEA28tdGbrZXhcyAZEhHAZA
Gzog+pKlkpEzeonLKIuGKzCrEKRecIK5jrqyQsCjhS0T7ZRnL4g6i0s+umiV5M5w
fcc292pEA1h45L3DD6OlKplSQVTv55/OYS4oY3YEJtf5mfm8vWi9lQeY8sxOlQpn
O+VZTdBHmTC8PGeTAgZXHZUCgYA6Tyv88lYowB7SN2qQgBQu8jvdGtqhcs/99GCr
H3N0I69LPsKAR0QeH8OJPXBKhDUywESXAaEOwS5yrLNP1tMRz5Vj65YUCzeDG3kx
gpvY4IMp7ArX0bSRvJ6mYSFnVxy3k174G3TVCfksrtagHioVBGQ7xUg5ltafjrms
n8l55QKBgQDVzU8tQvBVqY8/1lnw11Vj4fkE/drZHJ5UkdC1eenOfSWhlSLfUJ8j
ds7vEWpRPPoVuPZYeR1y78cyxKe1GBx6Wa2lF5c7xjmiu0xbRnrxYeLolce9/ntp
asClqpnHT8/VJYTD7Kqj0fouTTZf0zkig/y+2XERppd8k+pSKjUCPQ==
-----END RSA PRIVATE KEY-----
OK

AT+SSLCFG="cacert",88,"ca.crt"                //设置ca证书文件为ca.crt

OK
AT+SSLCFG="clientcert",88,"client.crt"        //设置客户端证书文件为client.crt

OK
AT+SSLCFG="clientkey",88,"client.key"         //设置客户端密钥文件为client.key

OK
AT+SSLCFG="seclevel",88,2                     //设置认证模式为双向认证

OK
AT+MCONFIG=868488076771714,root,luat123456

OK
AT+SSLMIPSTART="airtest.openluat.com","8883"

OK

CONNECT OK
AT+MCONNECT=1,60

OK

CONNACK OK
AT+MSUB="mqtt/pub",0                        //订阅主题

OK

SUBACK

+MSUB: "mqtt/pub",20 byte,data from tcp server        //收到服务器下发消息
AT+MPUB="mqtt/sub",0,0,"data from 4G module"            //上报消息到服务器

OK
```

交互日志如下：

![](image/DpGzbJ8HOoZQs9xMr44cWOQKn0g.png)

## 七、APN 设置与专网卡

用户根据自己使用的网络类型来区分，sim 卡可以分为公网卡和专网卡两种；对于如何判断自己手里的 sim 卡是公网卡还是专网卡可以通过下面两种办法区分：

- 咨询 sim 卡供应商；
- 如果有 apn 账号、或者有密码、或者有加密类型，则可以认为是专网卡。

对于公网卡和专网卡设置和查询有不同的指令，合宙 780E 4G 模组设置和查询 APN 相关指令可以参考下图：

![](image/RBozbAc0koj9O8xzPMTckuTQnsl.png)

```bash
设置apn指令流程：
AT+CPIN?                                        //检查卡是否正常
AT+CPNETAPN=2,jscmiot,u9682,iot98765,2         //举例，根据实际填写，不能照抄
AT+CGATT?                                      //查询是否附着上数据网络，如果返回+CGATT: 0表示未附着上,1表示正常
```

**APN 及专网卡常见问题**

1. 模块如何设置 APN
  ```text
    1、如果是公网SIM卡，不需要用户主动设置APN，软件自动去网络端查询APN进行设置。
    2、如果是专网SIM卡，首先咨询SIM卡提供商APN参数，然后通过AT+CPNETAPN=mode,“apnname”,“user”,“pwd”,authmoded进行专网卡的参数设置。
```
2. 专网卡连接服务器失败
  ```text
    1、有的专网卡没设置APN的情况下也能激活PDP，但是不能连专网卡指定的服务器，或者开机后模块没自动激活PDP，这个时候参考1，检查APN参数是否设置正确。
    2、如果有其他厂家的模块，对比测试下是否连接正常。
    3、如果无法百分百保证服务器配置没问题，最好在服务器端用wireshark抓包，或者在服务器上安装一个第三方工具，开启一个服务器端口来对比测试。
    4、用定向Ip的物联网卡，需要把域名或IP加入白名单才能使用。
  ```

3. 专网卡访问白名单
用定向 IP 的物联网卡，需要把域名或 IP 加入白名单才能使用，下面列出模块会访问的域名或 IP 服务器。
![](image/EXHWbqdIgojDqLx7gJUcwIjWn5V.png)


## 八、常见问题和注意事项

### 8.1  注意事项

1、发送 MIPSTART 命令后，收到 OK 仅仅表示 4G 模块开始处理这条命令，并不表示 TCP 已经连接成功；只有收到 CONNECT OK 才是成功的应答；

2、发送 MCONNECT 命令后，收到 OK 仅仅表示 4G 模块开始处理这条命令，并不表示 MQTT 已经连接成功；只有收到 CONNACK OK 才是成功的应答；

3、发送 MSUB 命令后，收到 OK 仅仅表示 4G 模块开始处理这条命令，并不表示 MQTT 已经订阅成功；只有收到 SUBACK 才是成功的应答；

4、发送 MPUB 命令后，如果 QOS 不是 0，则收到 OK 仅仅表示 4G 模块开始处理这条命令，并不表示 MQTT 已经发布成功；只有收到 PUBACK（QOS 为 1 时）或者 PUBCOMP（QOS 为 2 时）才是成功的应答；

### 8.2 常见问题

1. **780E 支持的 MQTT 版本**
   ```text
    MQTT3.1.1
   ```

2. **连接服务器失败**
   ```
    1、检查下模块信号、网络注册、网络附着、PDP激活状态。

    2、检查下SIM卡是否欠费【4G模块有一种欠费表现：无法注册4G网络，可以注册2G网络】。

    3、使用mqtt.fx，连接服务器确认一下是否可以连接成功，排除服务器故障。

    4、部分国外的开源项目提供免费的MQTT代理服务器，因为网络的原因，国内存在严重的延迟或者丢包现象，导致程序运行出现问题。

    5、确认是不是域名解析失败导致，可以通过AT+CDNSGIP=<domain name>确认一下域名是否能正常解析（注意：该命令只有在执行完at+cstt、at+ciicr、at+cifsr后才能正常工作），不能正常解析，可以通过AT+CDNSCFG=ip1,ip2设置域名解析服务器。

    6、在 MIPSTART /SSLMIPSTART返 回 CONNECT OK后 才 能 发 MCONNECT命令，而且要立即发，否则会被服务器踢掉。
    ```

3. **频繁掉线是什么原因**
   ```
    1、检查下是否存在代码逻辑错误，导致异常。

    2、检查下是否不断重启，导致异常。

    3、检查下服务器网络是否稳定，不要用内网穿透方式搭建服务器。

    4、检查下使用环境是否网络覆盖不好，例如车库、地下、电梯、山区等。

    5、检查下模块信号、网络注册、网络附着、PDP激活状态。

    6、排查是否为设备天线问题：发出来设备的天线调试指标参数给合宙技术支持人员；曾经有一个客户天线指标明显有问题，导致10几个小时出现30次左右掉线；后来重新调试天线之后，40个小时出现几次掉线。

    7、如果经常出现连接被动断开：
      1) 检查下mqtt keep alive的时间，一般建议使用2分钟【如果每2分钟内都有应用数据收发，则可以把mqtt keep alive的时间设置的长一点儿】，除非有强制要求，否则不能太长，也不能太短。不建议超过4分钟，基站策略会关闭长时间没有数据传输的连接，太长时间可能会导致连接被基站关闭；不建议少于1分钟，太短时间可能会因为网络环境波动导致上行数据发送超时，可能超过1.5倍的心跳时间，从而被服务器主动断开连接。

      2) 检查下是否在1.5倍的mqtt keep alive的时间，没有成功发送数据到服务器，就会被被服务器主动断开，这种情况一般都是发送数据超时引起的。

    8、如果要降低掉线率，可通过如下方式设置【注意：在网络环境不变的情况下，降低掉线率意味着会增加响应延时】
    A. mqtt keep alive的时间，一般建议使用2分钟【如果每2分钟内都有应用数据收发，则可以把mqtt keep alive的时间设置的长一点儿】，除非有强制要求，否则不能太长，也不能太短。不建议超过4分钟，基站策略会关闭长时间没有数据传输的连接，太长时间可能会导致连接被基站关闭；不建议少于1分钟，太短时间可能会因为网络环境波动导致上行数据发送超时，可能超过1.5倍的心跳时间，从而被服务器主动断开连接。

    B. 减少Qos1和Qos2的publish使用，允许的话建议都使用Qos0。
    ```

4. **有没有认证机制**
   ```
    有，每个设备有clientid、username、password。
    ```

5. **client id 是否允许重复**
   ```bash
    不允许重复，重复的话，服务器会踢掉上一个相同id的设备。
    ```

6. **Qos0、1、2 如何选择**
   ```
    应用允许的情况下，建议使用Qos0，Qos1和Qos2会加重网络负担，在网络拥堵和较差的情况下，数据传输的次数越多，掉线的概率就会越高。
    ```

7. 是否支持 ssl
   ```bash
    支持证书配置，支持单向认证和双向认证
    支持如下六种加密套件：
    0X0035 TLS_RSA_WITH_AES_256_CBC_SHA
    0X002F TLS_RSA_WITH_AES_128_CBC_SHA
    0X0005 TLS_RSA_WITH_RC4_128_SHA
    0X0004 TLS_RSA_WITH_RC4_128_MD5
    0X000A TLS_RSA_WITH_3DES_EDE_CBC_SHA
    0X003D TLS_RSA_WITH_AES_256_CBC_SHA256
    ```

8. MQTT SSL 如何使用
   ```bash
    参考上面流程或者翻阅AT手册，如果SSL的参数配置不变，则每次开机运行过程中，仅设置一次即可
    ```

9. 为什么 mqtt ssl 访问失败
    ```bash
    1、检查服务器是否支持模块支持的加密套件。
    2、发日志文件给合宙技术支持人员分析。
    ```

10. MQTT 支持多连接吗
    ```bash
    目前MQTT仅支持单连接，不支持多连接。
    ```

11. MQTT 的遗嘱如何使用
    ```bash
    通过AT+MCONFIG命令可以设置遗嘱的qos、retain标志、topic、payload；在如下几种（包含但是又不仅限于如下情况）情况下，服务器会主动发布遗嘱消息到订阅的客户端：
    1、模块和服务器通信异常（例如模块突然关机、模块进入了一个没有网络信号的环境等）超过1.5倍（一般是1.5倍，但不排除服务器可以修改这个时间）的 keep alive时间（可以通过AT+MCONNECT设置keep alive时间）。

    2、模块主动执行AT+MDISCONNECT或者AT+MIPCLOSE。
    ```

12. MPUB 命令中，payload 包含"如何发送？
    ```bash
    1、消息中内嵌的双引号请用\22 表达；控制字符回车\r(0x0D) 请用\0D 表达； ； 控制字符换行\n（0x0A ）请用\0A 表达 ； 控制字符反斜杠\ （0x5C ） 请用\5C表达。

    2、如果是 MCU 发消息，可能需要用\\22 ，\\0D ，\\0A ，\\5C 来表达，即\ 需要转义成\\ 。
    ```


13. 重试多次 PDP，MQTT 应用一直连接失败
    ```bash
    如果重试多次PDP激活，PDP一直激活失败，或者MQTT一直连接失败，则尝试使用如下手段恢复：
    1、使用RESET引脚复位模块。

    2、极端情况下，直接给模块断电，再上电，POWER KEY引脚拉低开机。
    ```


14. 数据接收缓存问题
    ```bash
    可通过AT+MQTTMSGSET命令设置是否缓存，详情参考AT手册。
    1、不缓存：通过AT+MQTTMSGSET=0设置；收到订阅的publish报文后，立即通过AT口输出主题、payload长度、payload内容，每个报文中支持的payload内容最长1360字节。
    2、内存缓存：通过AT+MQTTMSGSET=1设置；内存中有一个缓存表，最多支持缓存4条publish报文；收到订阅的publish报文后，插入缓冲表中的空闲位置，然后通过AT口输出存储位置；缓存表满之后，新收到的publish报文会覆盖最旧的publish报文。
    注意：缓存表位于内存中，断电或者重启后，缓存表中的数据会被清空；建议收到数据时，通过AT+MQTTMSGGET及时读取出来，以防缓冲区满覆盖丢失数据。
    ```


15. 数据发送问题
    ```bash
    AT+MPUB最大publish 2384字节,AT+MPUBEX长度取值范围1-4100
    ```



## 给读者的话

> 本篇文章由`孟伟`开发；
>
> 本篇文章描述的内容，如果有错误、细节缺失、细节不清晰或者其他任何问题，总之就是无法解决您遇到的问题；
>
> 请登录[合宙技术交流论坛](https://chat.openluat.com/)，点击[文档找错赢奖金-Air780E-AT-软件指南-应用实例-MQTT](https://chat.openluat.com/#/page/matter?125=1848635733875752962&126=%E6%96%87%E6%A1%A3%E6%89%BE%E9%94%99%E8%B5%A2%E5%A5%96%E9%87%91-Air780E-AT-%E8%BD%AF%E4%BB%B6%E6%8C%87%E5%8D%97-%E5%BA%94%E7%94%A8%E5%AE%9E%E4%BE%8B-MQTT&askid=1848635733875752962)
> 用截图标注+文字描述的方式跟帖回复，记录清楚您发现的问题；
>
> 我们会迅速核实并且修改文档；
>
> 同时也会为您累计找错积分，您还可能赢取月度找错奖金！
