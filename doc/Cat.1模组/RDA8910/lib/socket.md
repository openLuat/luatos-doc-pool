
@[TOC]

# socket

模块功能：数据链路激活、SOCKET管理(创建、连接、数据收发、状态维护)

## socket.isReady()

SOCKET 是否有可用

* 参数

无

* 返回值

可用true,不可用false

* 例子

无

---

## socket.tcp(ssl, cert, tCoreExtPara, ipv6)

创建基于TCP的socket对象

* 参数

|名称|传入值类型|释义|
|-|-|-|
|ssl|bool|**可选参数，默认为`nil`** 是否为ssl连接，true表示是，其余表示否|
|cert|table|**可选参数，默认为`nil`** ssl连接需要的证书配置，只有ssl参数为true时，此参数才有意义，cert格式如下：<br>{<br>caCert = "ca.crt", --CA证书文件(Base64编码 X.509格式)，如果存在此参数，则表示客户端会对服务器的证书进行校验；不存在则不校验<br>clientCert = "client.crt", --客户端证书文件(Base64编码 X.509格式)，服务器对客户端的证书进行校验时会用到此参数<br>clientKey = "client.key", --客户端私钥文件(Base64编码 X.509格式)<br>clientPassword = "123456", --客户端证书文件密码[可选]<br>}|
|tCoreExtPara|table|**可选参数，默认为`nil`** 建立链接扩展参数，4G链接和ch395链接所需扩展参数不一样|

* 返回值

client，创建成功返回socket客户端对象；创建失败返回nil

* 例子

```lua
c = socket.tcp()
c = socket.tcp(true)
c = socket.tcp(true, {caCert="ca.crt"})
c = socket.tcp(true, {caCert="ca.crt", clientCert="client.crt", clientKey="client.key"})
c = socket.tcp(true, {caCert="ca.crt", clientCert="client.crt", clientKey="client.key", clientPassword="123456"})
```

---

## socket.udp(ipv6)

创建基于UDP的socket对象

* 参数

无

* 返回值

client，创建成功返回socket客户端对象；创建失败返回nil

* 例子

```lua
c = socket.udp()
```

---

## socket.setTcpResendPara(retryCnt, retryMaxTimeout)

设置TCP层自动重传的参数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|retryCnt|number|**可选参数，默认为`4`** 重传次数；取值范围0到12|
|retryMaxTimeout|number|**可选参数，默认为`16`** 限制每次重传允许的最大超时时间(单位秒)，取值范围1到16|

* 返回值

nil

* 例子

```lua
setTcpResendPara(3,8)
setTcpResendPara(4,16)
```

---

## socket.setDnsParsePara(retryCnt, retryTimeoutMulti)

设置域名解析参数

注意：0027以及之后的core版本才支持此功能

* 参数

|名称|传入值类型|释义|
|-|-|-|
|retryCnt|number|**可选参数，默认为`4`** 重传次数；取值范围1到8|
|retryTimeoutMulti|number|**可选参数，默认为`4`** 重传超时时间倍数，取值范围1到5<br>第n次重传超时时间的计算方式为：第n次的重传超时基数*retryTimeoutMulti，单位为秒<br>重传超时基数表为{1, 1, 2, 4, 4, 4, 4, 4}<br>第1次重传超时时间为：1*retryTimeoutMulti 秒<br>第2次重传超时时间为：1*retryTimeoutMulti 秒<br>第3次重传超时时间为：2*retryTimeoutMulti 秒<br>...........................................<br>第8次重传超时时间为：8*retryTimeoutMulti 秒|

* 返回值

nil

* 例子

```lua
socket.setDnsParsePara(8,5)
```

---

## socket.printStatus()

打印所有socket的状态

* 参数

无

* 返回值

无

* 例子

```lua
socket.printStatus()
```

---

## socket.setLowPower(tm)

设置数据传输后，允许进入休眠状态的延时时长

3024版本以及之后的版本才支持此功能<br>此功能设置的参数，设置成功后，掉电会自动保存

* 参数

|名称|传入值类型|释义|
|-|-|-|
|tm|number|数据传输后，允许进入休眠状态的延时时长，单位为秒，取值范围1到20<br>注意：此时间越短，允许进入休眠状态越快，功耗越低；但是在某些网络环境中，此时间越短，可能会造成数据传输不稳定<br>建议在可以接受的功耗范围内，此值设置的越大越好<br>如果没有设置此参数，此延时时长是和基站的配置有关，一般来说是10秒左右|

* 返回值

nil

* 例子

```lua
socket.setLowPower(5)
```

---

## socket.setIpStatis(interval)

设置IP数据流量统计上报间隔

此功能设置的参数，设置成功后，掉电不会保存，每次开机，应用脚本需要重新设置

* 参数

|名称|传入值类型|释义|
|-|-|-|
|interval|number|IP数据流量统计上报间隔，单位为秒，建议取值不要小于60秒；0表示关闭此功能，默认为0|

* 返回值

nil

* 例子

```lua
socket.setIpStatis(60)
-- 每隔60秒会通过sys.publish("LIB_IP_STATIS_RPT", dataFlow)
-- 应用脚本通过sys.subscribe("LIB_IP_STATIS_RPT", function(dataFlow)
--自行处理interval间隔内，新增的数据流量dataFlow，单位字节
end)
```

---
