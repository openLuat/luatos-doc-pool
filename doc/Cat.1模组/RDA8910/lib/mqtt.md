
@[TOC]

# mqtt

模块功能：MQTT客户端

## mqtt.client(clientId, keepAlive, username, password, cleanSession, will, version)

创建一个mqtt client实例

* 参数

|名称|传入值类型|释义|
|-|-|-|
|clientId|string|确保设备唯一性|
|keepAlive|number|**可选参数，默认为`300`** 心跳间隔(单位为秒)，默认300秒|
|username|string|**可选参数，默认为`""`** 用户名，用户名为空配置为""或者nil|
|password|string|**可选参数，默认为`""`** 密码，密码为空配置为""或者nil|
|cleanSession|number|**可选参数，默认为`1`** 1/0|
|will|table|**可选参数，默认为`nil`** 遗嘱参数，格式为{qos=,retain=,topic=,payload=}|
|version|string|**可选参数，默认为`"3.1.1"`** MQTT版本号，仅支持"3.1"和"3.1.1"|

* 返回值

table mqttc client实例

* 例子

```lua
mqttc = mqtt.client("clientid-123")
mqttc = mqtt.client("clientid-123",200)
mqttc = mqtt.client("clientid-123",nil,"user","password")
mqttc = mqtt.client("clientid-123",nil,"user","password",nil,{qos=0,retain=0,topic="willTopic",payload="willTopic"},"3.1")
```

---

## mqttc:connect(host, port, transport, cert, timeout)

连接mqtt服务器

* 参数

|名称|传入值类型|释义|
|-|-|-|
|host|string|服务器地址|
|port|param|string或者number类型，服务器端口|
|transport|string|**可选参数，默认为`"tcp"`** "tcp"或者"tcp_ssl"|
|cert|table|**可选参数，默认为`nil`** table或者nil类型，ssl证书，当transport为"tcp_ssl"时，此参数才有意义。cert格式如下：<br>{<br>caCert = "ca.crt", --CA证书文件(Base64编码 X.509格式)，如果存在此参数，则表示客户端会对服务器的证书进行校验；不存在则不校验<br>clientCert = "client.crt", --客户端证书文件(Base64编码 X.509格式)，服务器对客户端的证书进行校验时会用到此参数<br>clientKey = "client.key", --客户端私钥文件(Base64编码 X.509格式)<br>clientPassword = "123456", --客户端证书文件密码[可选]<br>}|
|timeout|number|**可选参数，默认为`120`** 可选参数，socket连接超时时间，单位秒|

* 返回值

result true表示成功，false或者nil表示失败

* 例子

```lua
mqttc = mqtt.client("clientid-123", nil, nil, false); mqttc:connect("mqttserver.com", 1883, "tcp", 5)
```

---

## mqttc:subscribe(topic, qos)

订阅主题

* 参数

|名称|传入值类型|释义|
|-|-|-|
|topic|param|string或者table类型，一个主题时为string类型，多个主题时为table类型，主题内容为UTF8编码|
|qos|param|**可选参数，默认为`0`** number或者nil，topic为一个主题时，qos为number类型(0/1/2，默认0)；topic为多个主题时，qos为nil|

* 返回值

bool true表示成功，false或者nil表示失败

* 例子

```lua
mqttc:subscribe("/abc", 0) -- subscribe topic "/abc" with qos = 0
mqttc:subscribe({["/topic1"] = 0, ["/topic2"] = 1, ["/topic3"] = 2}) -- subscribe multi topic
```

---

## mqttc:unsubscribe(topic)

取消订阅主题

* 参数

|名称|传入值类型|释义|
|-|-|-|
|topic|param|string或者table类型，一个主题时为string类型，多个主题时为table类型，主题内容为UTF8编码|

* 返回值

bool true表示成功，false或者nil表示失败

* 例子

```lua
mqttc:unsubscribe("/abc") -- unsubscribe topic "/abc"
mqttc:unsubscribe({"/topic1", "/topic2", "/topic3"}) -- unsubscribe multi topic
```

---

## mqttc:publish(topic, payload, qos, retain)

发布一条消息

* 参数

|名称|传入值类型|释义|
|-|-|-|
|topic|string|UTF8编码的字符串|
|payload|string|用户自己控制payload的编码，mqtt.lua不会对payload做任何编码转换|
|qos 0/1/2, default|number|**可选参数，默认为`0`** 0|
|retain|number|**可选参数，默认为`0`** 0或者1|

* 返回值

bool 发布成功返回true，失败返回false

* 例子

```lua
mqttc = mqtt.client("clientid-123", nil, nil, false)
mqttc:connect("mqttserver.com", 1883, "tcp")
mqttc:publish("/topic", "publish from luat mqtt client", 0)
```

---

## mqttc:receive(timeout, msg)

接收消息

* 参数

|名称|传入值类型|释义|
|-|-|-|
|timeout|number|接收超时时间，单位毫秒|
|msg|string|**可选参数，默认为`nil`** 可选参数，控制socket所在的线程退出recv阻塞状态|

* 返回值

result 数据接收结果，true表示成功，false表示失败
data <br>如果result为true，表示服务器发过来的mqtt包<br><br>如果result为false，超时失败,data为"timeout"<br>如果result为false，msg控制退出，data为msg的字符串<br>如果result为false，socket连接被动断开控制退出，data为"CLOSED"<br>如果result为false，PDP断开连接控制退出，data为"IP_ERROR_IND"<br><br>如果result为false，mqtt不处于连接状态，data为nil<br>如果result为false，收到了PUBLISH报文，发送PUBACK或者PUBREC报文失败，data为nil<br>如果result为false，收到了PUBREC报文，发送PUBREL报文失败，data为nil<br>如果result为false，收到了PUBREL报文，发送PUBCOMP报文失败，data为nil<br>如果result为false，发送PINGREQ报文失败，data为nil
param 如果是msg控制退出，param的值是msg的参数；其余情况无意义，为nil

* 例子

```lua
true, packet = mqttc:receive(2000)
false, error_message = mqttc:receive(2000)
false, msg, para = mqttc:receive(2000,"APP_SEND_DATA")
```

---

## mqttc:disconnect()

断开与服务器的连接

* 参数

无

* 返回值

nil

* 例子

```lua
mqttc = mqtt.client("clientid-123", nil, nil, false)
mqttc:connect("mqttserver.com", 1883, "tcp")
process data
mqttc:disconnect()
```

---
