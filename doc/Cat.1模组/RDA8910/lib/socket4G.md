
@[TOC]

# socket4G



## socket4G.tcp(ssl, cert, tCoreExtPara, ipv6)

创建基于TCP的socket对象

* 参数

|名称|传入值类型|释义|
|-|-|-|
|ssl|bool|**可选参数，默认为`nil`** 是否为ssl连接，true表示是，其余表示否|
|cert|table|**可选参数，默认为`nil`** ssl连接需要的证书配置，只有ssl参数为true时，此参数才有意义，cert格式如下：<br>{<br>caCert = "ca.crt", --CA证书文件(Base64编码 X.509格式)，如果存在此参数，则表示客户端会对服务器的证书进行校验；不存在则不校验<br>clientCert = "client.crt", --客户端证书文件(Base64编码 X.509格式)，服务器对客户端的证书进行校验时会用到此参数<br>clientKey = "client.key", --客户端私钥文件(Base64编码 X.509格式)<br>clientPassword = "123456", --客户端证书文件密码[可选]<br>insist = 1, --证书中的域名校验失败时，是否坚持连接，默认为1，坚持连接，0为不连接<br>hostNameFlag = 0, --服务器域名是否上报，默认为0，不上报，1为上报<br>}|
|tCoreExtPara|number|**可选参数，默认为`nil`** 建立链接扩展参数<br>{<br>rcvBufferSize = "num" --接收缓冲区大小，默认为0<br>}|

* 返回值

client，创建成功返回socket客户端对象；创建失败返回nil

* 例子

```lua
c = socket4G.tcp()
c = socket4G.tcp(true)
c = socket4G.tcp(true, {caCert="ca.crt"})
c = socket4G.tcp(true, {caCert="ca.crt", clientCert="client.crt", clientKey="client.key"})
c = socket4G.tcp(true, {caCert="ca.crt", clientCert="client.crt", clientKey="client.key", clientPassword="123456"})
```

---

## socket4G.udp(ipv6)

创建基于UDP的socket对象

* 参数

无

* 返回值

client，创建成功返回socket客户端对象；创建失败返回nil

* 例子

```lua
c = socket4G.udp()
```

---

## mt:connect(address, port, timeout)

连接服务器

* 参数

|名称|传入值类型|释义|
|-|-|-|
|address|string|服务器地址，支持ip和域名|
|port|param|string或者number类型，服务器端口|
|timeout|number|**可选参数，默认为`120`** 可选参数，连接超时时间，单位秒|

* 返回值

bool result true - 成功，false - 失败
string ,id '0' -- '8' ,返回通道ID编号

* 例子

```lua
socketClient = socket4G.tcp()
socketClient:connect("www.baidu.com","80")
```

---

## mt:asyncSelect(keepAlive, pingreq)

异步发送数据

* 参数

|名称|传入值类型|释义|
|-|-|-|
|keepAlive|number|**可选参数，默认为`nil`** 服务器和客户端最大通信间隔时间,也叫心跳包最大时间,单位秒|
|pingreq|string|**可选参数，默认为`nil`** 心跳包的字符串|

* 返回值

boole,false 失败，true 表示成功

* 例子

```lua
socketClient = socket4G.tcp()
socketClient:connect("www.baidu.com","80")
while socketClient:asyncSelect() do end
```

---

## mt:asyncSend(data, timeout)

异步缓存待发送的数据

* 参数

|名称|传入值类型|释义|
|-|-|-|
|data|string|数据|
|timeout|number|**可选参数，默认为`nil`** 可选参数，发送超时时间，单位秒；为nil时表示不支持timeout|

* 返回值

result true - 成功，false - 失败

* 例子

```lua
socketClient = socket4G.tcp()
socketClient:connect("www.baidu.com","80")
socketClient:asyncSend("12345678")
```

---

## mt:asyncRecv()

异步接收数据

* 参数

无

* 返回值

data 表示接收到的数据(如果是UDP，返回最新的一包数据；如果是TCP,返回所有收到的数据)<br>""表示未收到数据

* 例子

```lua
socketClient = socket4G.tcp()
socketClient:connect("www.baidu.com","80")
data = socketClient:asyncRecv()
```

---

## mt:send(data, timeout)

同步发送数据

* 参数

|名称|传入值类型|释义|
|-|-|-|
|data|string|数据<br>此处传入的数据长度和剩余可用内存有关，只要内存够用，可以随便传入数据<br>虽然说此处的数据长度没有特别限制，但是调用core中的socket发送接口时，每次最多发送11200字节的数据<br>例如此处传入的data长度是112000字节，则在这个send接口中，会循环10次，每次发送11200字节的数据|
|timeout|number|**可选参数，默认为`120`** 可选参数，发送超时时间，单位秒|

* 返回值

result true - 成功，false - 失败

* 例子

```lua
socketClient = socket4G.tcp()
socketClient:connect("www.baidu.com","80")
socketClient:send("12345678")
```

---

## mt:recv(timeout, msg, msgNoResume)

同步接收数据

* 参数

|名称|传入值类型|释义|
|-|-|-|
|timeout|number|**可选参数，默认为`0`** 可选参数，接收超时时间，单位毫秒|
|msg|string|**可选参数，默认为`nil`** 可选参数，控制socket所在的线程退出recv阻塞状态|
|msgNoResume|bool|**可选参数，默认为`nil`** 可选参数，控制socket所在的线程退出recv阻塞状态<br>false或者nil表示“在recv阻塞状态，收到msg消息，可以退出阻塞状态”，true表示不退出<br>此参数仅lib内部使用，应用脚本不要使用此参数|

* 返回值

result 数据接收结果<br>true表示成功（接收到了数据）<br>false表示失败（没有接收到数据）
data <br>如果result为true，data表示接收到的数据(如果是UDP，返回最新的一包数据；如果是TCP,返回所有收到的数据)<br>如果result为false，超时失败，data为"timeout"<br>如果result为false，msg控制退出，data为msg的字符串<br>如果result为false，socket连接被动断开控制退出，data为"CLOSED"<br>如果result为false，PDP断开连接控制退出，data为"IP_ERROR_IND"
param 如果是msg控制退出，param的值是msg的参数

* 例子

```lua
socketClient = socket4G.tcp()
socketClient:connect("www.baidu.com","80")
result,data = socketClient:recv(60000,"APP_SOCKET_SEND_DATA")
```

---

## mt:close()

主动关闭并且销毁一个socket

* 参数

无

* 返回值

nil

* 例子

```lua
socketClient = socket4G.tcp()
socketClient:connect("www.baidu.com","80")
socketClient:close()
```

---

## socket4G.setTcpResendPara(retryCnt, retryMaxTimeout)

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

## socket4G.setDnsParsePara(retryCnt, retryTimeoutMulti)

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
socket4G.setDnsParsePara(8,5)
```

---

## socket4G.setLowPower(tm)

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
socket4G.setLowPower(5)
```

---
