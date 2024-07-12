
@[TOC]

# aLiYun

模块功能：阿里云物联网套件客户端功能.

目前的产品节点类型仅支持“设备”，设备认证方式支持“一机一密和“一型一密”

## aLiYun.sleep()

断开阿里云物联网套件的连接，并且不再重连

* 参数

无

* 返回值

nil

* 例子

```lua
aLiYun.sleep()
```

---

## aLiYun.wakeup()

重新打开阿里云物联网套件的连接

* 参数

无

* 返回值

nil

* 例子

```lua
aLiYun.wakeup()
```

---

## aLiYun.sleepStatus()

查看打开阿里云物联网套件的是否允许连接状态

* 参数

无

* 返回值

bool 是否允许连接阿里云

* 例子

```lua
local ar = aLiYun.sleepStatus()
```

---

## aLiYun.Authsleep()

断开阿里云物联网套件的鉴权连接，并且不再重连

* 参数

无

* 返回值

nil

* 例子

```lua
aLiYun.Authsleep()
```

---

## aLiYun.Authwakeup()

重新打开阿里云物联网套件的鉴权连接

* 参数

无

* 返回值

nil

* 例子

```lua
aLiYun.Authwakeup()
```

---

## aLiYun.AuthSleepStatus()

查看打开阿里云物联网套件的是否允许鉴权状态

* 参数

无

* 返回值

bool 是否允许连接阿里云

* 例子

```lua
local ar = aLiYun.AuthSleepStatus()
```

---

## aLiYun.setup(productKey, productSecret, getDeviceNameFnc, getDeviceSecretFnc, setDeviceSecretFnc)

配置阿里云物联网套件的产品信息和设备信息

* 参数

|名称|传入值类型|释义|
|-|-|-|
|productKey|string|产品标识|
|productSecret|string|**可选参数，默认为`nil`** 产品密钥<br>一机一密认证方案时，此参数传入nil<br>一型一密认证方案时，此参数传入真实的产品密钥|
|getDeviceNameFnc|function|获取设备名称的函数|
|getDeviceSecretFnc|function|获取设备密钥的函数|
|setDeviceSecretFnc|function|**可选参数，默认为`nil`** 设置设备密钥的函数，一型一密认证方案才需要此参数|

* 返回值

nil

* 例子

```lua
aLiYun.setup("b0FMK1Ga5cp",nil,getDeviceNameFnc,getDeviceSecretFnc)
aLiYun.setup("a1AoVqkCIbG","7eCdPyR6fYPntFcM",getDeviceNameFnc,getDeviceSecretFnc,setDeviceSecretFnc)
```

---

## aLiYun.setMqtt(cleanSession, will, keepAlive)

设置MQTT数据通道的参数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|cleanSession|number|**可选参数，默认为`1`** 1/0|
|will|table|**可选参数，默认为`nil`** 遗嘱参数，格式为{qos=,retain=,topic=,payload=}|
|keepAlive|number|**可选参数，默认为`240`** 单位秒|

* 返回值

nil

* 例子

```lua
aLiYun.setMqtt(0)
aLiYun.setMqtt(1,{qos=0,retain=1,topic="/willTopic",payload="will payload"})
aLiYun.setMqtt(1,{qos=0,retain=1,topic="/willTopic",payload="will payload"},120)
```

---

## aLiYun.setRegion(region)

设置地域region id

* 参数

|名称|传入值类型|释义|
|-|-|-|
|region|string|地域id字符串，参考：https://help.aliyun.com/document_detail/40654.html?spm=a2c4g.11186623.2.16.c0a63f82Z7qCtA#concept-h4v-j5k-xdb|

* 返回值

nil

* 例子

```lua
-- 设置华北1：aLiYun.setRegion("cn-qingdao")
-- 设置华东1：aLiYun.setRegion("cn-hangzhou")
-- 设置华南1：aLiYun.setRegion("cn-shenzhen")
```

---

## aLiYun.setConnectMode(mode, host, port, getClientIdFnc, getUserNameFnc, getPasswordFnc)

设置连接方式

* 参数

|名称|传入值类型|释义|
|-|-|-|
|mode|string|连接方式，支持如下几种方式：<br>"direct"表示MQTT-TCP直连|
|host|string|服务器地址|
|port|number|服务器端口|
|getClientIdFnc|function|获取mqtt，client，id的函数|
|getUserNameFnc|function|获取mqtt，client，userName的函数|
|getPasswordFnc|function|获取mqtt，client，password的函数|

* 返回值

nil

* 例子

```lua
-- 设置为MQTT-TCP直连：aLiYun.setConnectMode("direct")
```

---

## aLiYun.subscribe(topic, qos)

订阅主题

* 参数

|名称|传入值类型|释义|
|-|-|-|
|topic|param|string或者table类型，一个主题时为string类型，多个主题时为table类型，主题内容为UTF8编码|
|qos|param|number或者nil，topic为一个主题时，qos为number类型(0/1，默认0)；topic为多个主题时，qos为nil|

* 返回值

nil

* 例子

```lua
aLiYun.subscribe("/b0FMK1Ga5cp/862991234567890/get", 0)
aLiYun.subscribe({["/b0FMK1Ga5cp/862991234567890/get"] = 0, ["/b0FMK1Ga5cp/862991234567890/get"] = 1})
```

---

## aLiYun.publish(topic, payload, qos, cbFnc, cbPara)

发布一条消息

* 参数

|名称|传入值类型|释义|
|-|-|-|
|topic|string|UTF8编码的主题|
|payload|string|负载|
|qos|number|**可选参数，默认为`0`** 质量等级，0/1，默认0|
|cbFnc|function|**可选参数，默认为`nil`** 消息发布结果的回调函数<br>回调函数的调用形式为：cbFnc(result,cbPara)。result为true表示发布成功，false或者nil表示订阅失败；cbPara为本接口中的第5个参数|
|cbPara|param|**可选参数，默认为`nil`** 消息发布结果回调函数的回调参数|

* 返回值

nil

* 例子

```lua
aLiYun.publish("/b0FMK1Ga5cp/862991234567890/update","test",0)
aLiYun.publish("/b0FMK1Ga5cp/862991234567890/update","test",1,cbFnc,"cbFncPara")
```

---

## aLiYun.on(evt, cbFnc)

注册事件的处理函数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|evt|string|事件<br>"auth"表示鉴权服务器认证结果事件<br>"connect"表示接入服务器连接结果事件<br>"reconnect"表示重连事件<br>"receive"表示接收到接入服务器的消息事件|
|cbFnc|function|事件的处理函数<br>当evt为"auth"时，cbFnc的调用形式为：cbFnc(result)，result为true表示认证成功，false或者nil表示认证失败<br>当evt为"connect"时，cbFnc的调用形式为：cbFnc(result)，result为true表示连接成功，false或者nil表示连接失败<br>当evt为"receive"时，cbFnc的调用形式为：cbFnc(topic,qos,payload)，topic为UTF8编码的主题(string类型)，qos为质量等级(number类型)，payload为原始编码的负载(string类型)<br>当evt为"reconnect"时，cbFnc的调用形式为：cbFnc()，表示lib中在自动重连阿里云服务器|

* 返回值

nil

* 例子

```lua
aLiYun.on("connect",cbFnc)
```

---

## aLiYun.setErrHandle(cbFnc, tmout)

设置阿里云task连续一段时间工作异常的处理程序

* 参数

|名称|传入值类型|释义|
|-|-|-|
|cbFnc|function|异常处理函数，cbFnc的调用形式为：cbFnc()|
|tmout|number|**可选参数，默认为`150`** 连续工作异常的时间，当连续异常到达这个时间之后，会调用cbFnc()|

* 返回值

nil

* 例子

```lua
aLiYun.setErrHandle(function() sys.restart("ALIYUN_TASK_INACTIVE") end, 300)
```

---
