
@[TOC]

# socketESP8266

模块功能：数据链路激活、socketESP8266管理(创建、连接、数据收发、状态维护)

## socketESP8266.tcp(ssl, cert)

创建基于TCP的socket对象

* 参数

|名称|传入值类型|释义|
|-|-|-|
|ssl|bool|**可选参数，默认为`nil`** 是否为ssl连接，true表示是，其余表示否|
|cert|table|**可选参数，默认为`nil`** ssl连接需要的证书配置，只有ssl参数为true时，才参数才有意义，cert格式如下：<br>{<br>caCert = "ca.crt", --CA证书文件(Base64编码 X.509格式)，如果存在此参数，则表示客户端会对服务器的证书进行校验；不存在则不校验<br>clientCert = "client.crt", --客户端证书文件(Base64编码 X.509格式)，服务器对客户端的证书进行校验时会用到此参数<br>clientKey = "client.key", --客户端私钥文件(Base64编码 X.509格式)<br>clientPassword = "123456", --客户端证书文件密码[可选]<br>}|

* 返回值

client，创建成功返回socket客户端对象；创建失败返回nil

* 例子

```lua
c = socketESP8266.tcp()
c = socketESP8266.tcp(true)
c = socketESP8266.tcp(true, {caCert="ca.crt"})
c = socketESP8266.tcp(true, {caCert="ca.crt", clientCert="client.crt", clientKey="client.key"})
c = socketESP8266.tcp(true, {caCert="ca.crt", clientCert="client.crt", clientKey="client.key", clientPassword="123456"})
```

---

## socketESP8266.udp()

创建基于UDP的socket对象

* 参数

无

* 返回值

client，创建成功返回socket客户端对象；创建失败返回nil

* 例子

```lua
c = socketESP8266.udp()
```

---

## mt:connect(address, port, timeout)

连接服务器

* 参数

|名称|传入值类型|释义|
|-|-|-|
|address|string|服务器地址，支持ip和域名|
|port|param|string或者number类型，服务器端口|

* 返回值

bool result true - 成功，false - 失败<br>@number timeout, 链接服务器最长超时时间

* 例子

```lua
c = socketESP8266.tcp(); c:connect("www.baidu.com",80,5);
```

---

## mt:asyncSelect(keepAlive, pingreq)

异步收发选择器

* 参数

|名称|传入值类型|释义|
|-|-|-|
|keepAlive|number|服务器和客户端最大通信间隔时间,也叫心跳包最大时间,单位秒|
|pingreq|string|心跳包的字符串|

* 返回值

boole,false 失败，true 表示成功

* 例子

无

---

## mt:asyncSend(data)

异步发送数据

* 参数

|名称|传入值类型|释义|
|-|-|-|
|data|string|数据|

* 返回值

result true - 成功，false - 失败

* 例子

```lua
c = socketESP8266.tcp(); c:connect(); c:asyncSend("12345678");
```

---

## mt:asyncRecv()

异步接收数据

* 参数

无

* 返回值

nil, 表示没有收到数据
data 如果是UDP协议，返回新的数据包,如果是TCP,返回所有收到的数据,没有数据返回长度为0的空串

* 例子

```lua
c = socketESP8266.tcp(); c:connect()
data = c:asyncRecv()
```

---

## mt:send(data)

发送数据

* 参数

|名称|传入值类型|释义|
|-|-|-|
|data|string|数据|

* 返回值

result true - 成功，false - 失败

* 例子

```lua
c = socketESP8266.tcp(); c:connect(); c:send("12345678");
```

---

## mt:recv(timeout, msg, msgNoResume)

接收数据

* 参数

|名称|传入值类型|释义|
|-|-|-|
|timeout|number|**可选参数，默认为`0`** 可选参数，接收超时时间，单位毫秒|
|msg|string|**可选参数，默认为`nil`** 可选参数，控制socket所在的线程退出recv阻塞状态|
|msgNoResume|bool|**可选参数，默认为`nil`** 可选参数，控制socket所在的线程退出recv阻塞状态，false或者nil表示“在recv阻塞状态，收到msg消息，可以退出阻塞状态”，true表示不退出|

* 返回值

result 数据接收结果，true表示成功，false表示失败
data 如果成功的话，返回接收到的数据；超时时返回错误为"timeout"；msg控制退出时返回msg的字符串
param 如果是msg返回的false，则data的值是msg，param的值是msg的参数

* 例子

```lua
c = socketESP8266.tcp(); c:connect()
result, data = c:recv()
false,msg,param = c:recv(60000,"publish_msg")
```

---

## mt:close(slow)

销毁一个socket

* 参数

无

* 返回值

nil

* 例子

```lua
c = socket.tcp(); c:connect(); c:send("123"); c:close()
```

---
