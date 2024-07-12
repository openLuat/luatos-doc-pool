
@[TOC]

# link

模块功能：数据链路激活(创建、连接、状态维护)

## link.setAuthApn(prot, apn, user, pwd)

设置专网卡APN(注意：在main.lua中，尽可能靠前的位置调用此接口)

第一次设置成功之后，软件会自动重启，因为重启后才能生效

* 参数

|名称|传入值类型|释义|
|-|-|-|
|prot|number|**可选参数，默认为`0`** 加密方式，0:不加密，1:PAP，2:CHAP|
|apn|string|**可选参数，默认为`""`** apn名称|
|user|string|**可选参数，默认为`""`** apn用户名|
|pwd|string|**可选参数，默认为`""`** apn密码|

* 返回值

nil

* 例子

```lua
c = link.setAuthApn(2,"MYAPN","MYNAME","MYPASSWORD")
```

---

## link.openNetwork(mode, para)

打开链路层网络类型

注意：设置网络类型后，并不会关机保存，下次开机会自动恢复为默认的link.CELLULAR类型

* 参数

|名称|传入值类型|释义|
|-|-|-|
|mode|number|**可选参数，默认为`link.CELLULAR`** 取值如下：<br>link.CELLULAR：蜂窝模组数据网络<br>link.CH395：CH395以太网络<br>link.ESP8266：ESP8266WIFI网络|
|para|table|**可选参数，默认为`nil`** 取值如下：<br>当mode为link.CELLULAR时，参数para无意义，可以直接传入nil<br>当mode为link.CH395，para为table类型，表示以太网的配置参数，参数结构如下：<br>para= {<br>mode = 1,      --1表示客户端；2表示服务器；默认为1<br>intPin = pio.P0_22,      --以太网芯片中断通知引脚<br>rstPin = pio.P0_23,      --复位以太网芯片引脚<br>spiCs = pio.P0_23,      --spi片选<br>serverAddr = "192.168.1.112",      --做服务器应用时，本机的地址<br>serverPort = 1888,      --做服务器应用时，本机的端口<br>serverGateway = "192.168.1.1",      --做服务器应用时，本机的网关地址<br>powerFunc=function(state) end           --控制以太网模块的供电开关函数，ret为true开启供电，false关闭供电<br>spi = {spi.SPI_1,0,0,8,800000},      --SPI通道参数，id,cpha,cpol,dataBits,clock，默认spi.SPI_1,0,0,8,800000<br>}|

* 返回值

true/false,执行成功返回true,失败返回false。

* 例子

```lua
-- 设置为蜂窝数据网络：
c = link.setNetwork(link.CELLULAR, para)
-- 设置为CH395以太网络：
link.setNetwork(link.CH395, para)
-- 设置为ESP8266WIFI网络:
link.setNetwork(link.ESP8266, para)
```

---

## link.closeNetWork()

关闭链路层网络类型

注意：关闭链路层网络类型，不会改变链路层网络类型，需要打开链路层网络类型配置才能切换。

* 参数

无

* 返回值

true/false,执行成功返回true,失败返回false。

* 例子

```lua
-- 关闭链路层网络类型：
link.closeNetWork()
```

---

## link.getNetwork()

获取链路层网络类型

* 参数

无

* 返回值

network，number类型，取值如下：<br>link.CELLULAR：蜂窝模组数据网络<br>link.CH395：CH395以太网络<br>link.ESP8266：ESP8266WIFI网络

* 例子

```lua
-- 获取数据网络类型：
mode = link.getNetwork()
```

---
