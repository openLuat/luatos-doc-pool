
@[TOC]

# websocket

模块功能：websocket客户端

## websocket.new(url, cert)

创建 websocket 对象

* 参数

|名称|传入值类型|释义|
|-|-|-|
|url|string|websocket服务器的连接地址,格式为ws(或wss)://xxx开头|
|cert|table|**可选参数，默认为`nil`** ssl连接需要的证书配置，cert格式如下：<br>{<br>caCert = "ca.crt", --CA证书文件(Base64编码 X.509格式)，如果存在此参数，则表示客户端会对服务器的证书进行校验；不存在则不校验<br>clientCert = "client.crt", --客户端证书文件(Base64编码 X.509格式)，服务器对客户端的证书进行校验时会用到此参数<br>clientKey = "client.key", --客户端私钥文件(Base64编码 X.509格式)<br>clientPassword = "123456", --客户端证书文件密码[可选]<br>insist = 1, --证书中的域名校验失败时，是否坚持连接，默认为1，坚持连接，0为不连接<br>}|

* 返回值

table 返回1个websocket对象

* 例子

```lua
local ws = websocket.new("ws://121.40.165.18:8800")
```

---

## ws:on(event, callback)

ws:on 注册函数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|event|string|事件，可选值"open","message","close","error","pong"|
|callback|function|回调方法，message|error|pong形参是该方法需要的数据。|

* 返回值

无

* 例子

```lua
mt:on("message",function(message) local print(message)end)
```

---

## ws:connect(timeout)

websocket 与 websocket 服务器建立连接

* 参数

|名称|传入值类型|释义|
|-|-|-|
|timeout|number|与websocket服务器建立连接最长超时|

* 返回值

bool,true,表示连接成功,false or nil 表示连接失败

* 例子

```lua
while not ws:connect(20000) do sys.wait(2000) end
```

---

## ws:sendFrame(fin, opcode, data)

websocket发送帧方法

* 参数

|名称|传入值类型|释义|
|-|-|-|
|fin|bool|true表示结束帧,false表示延续帧|
|opcode|number|0x0--0xF,其他值非法,代码意义参考websocket手册|
|data|string|用户要发送的数据|

* 返回值

无

* 例子

```lua
self:sendFrame(true, 0x1, "www.openluat.com")
```

---

## ws:recv()

处理 websocket 发过来的数据并拼包

* 参数

无

* 返回值

result, boolean: 返回数据的状态 true 为正常, false 为失败
data, string: result为true时为数据,false时为报错信息

* 例子

```lua
local result, data = ws:recv()
```

---

## ws:close(code, reason)

关闭 websocket 与服务器的链接

* 参数

|名称|传入值类型|释义|
|-|-|-|
|code|number|1000或1002等,请参考websocket标准|
|reason|string|关闭原因|

* 返回值

nil

* 例子

```lua
ws:close()
ws:close(1002,"协议错误")
```

---

## websocket.exit(ws)

主动退出一个指定的websocket任务

* 参数

无

* 返回值

nil

* 例子

```lua
wesocket.exit(ws)
```

---

## ws:state()

获取websocket当前状态

* 参数

无

* 返回值

string,状态值("CONNECTING","OPEN","CLOSING","CLOSED")

* 例子

```lua
ws:state()
```

---

## ws:online()

获取websocket与服务器连接状态

* 参数

无

* 返回值

boolean: true 连接成功,其他值连接失败

* 例子

```lua
ws:online()
```

---

## ws:start(keepAlive, proc, reconnTime)

websocket 需要在任务中启动,带自动重连,支持心跳协议

* 参数

|名称|传入值类型|释义|
|-|-|-|
|keepAlive|number|**可选参数，默认为`nil`** websocket心跳包，建议30秒|
|proc|function|**可选参数，默认为`nil`** 处理服务器下发消息的函数|
|reconnTime|number|**可选参数，默认为`1000`** 断开链接后的重连时间|

* 返回值

nil

* 例子

```lua
sys.taskInit(ws.start,ws,30)
sys.taskInit(ws.start,ws,30,function(msg)u1:send(msg) end)
```

---
