
@[TOC]

# ril

模块功能：虚拟串口AT命令交互管理

## ril.regRsp(head, fnc, typ, formt)

注册某个AT命令应答的处理函数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|head|param|此应答对应的AT命令头，去掉了最前面的AT两个字符|
|fnc|param|AT命令应答的处理函数|
|typ|param|AT命令的应答类型，取值范围NORESULT,NUMBERIC,SLINE,MLINE,STRING,SPECIAL|
|formt|param|typ为STRING时，进一步定义STRING中的详细格式|

* 返回值

bool ,成功返回true，失败false

* 例子

```lua
ril.regRsp("+CSQ", rsp)
```

---

## ril.regUrc(prefix, handler)

注册某个urc的处理函数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|prefix|param|urc前缀，最前面的连续字符串，包含+、大写字符、数字的组合|
|handler|param|urc的处理函数|

* 返回值

无

* 例子

```lua
ril.regUrc("+CREG", neturc)
```

---

## ril.deRegUrc(prefix)

解注册某个urc的处理函数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|prefix|param|urc前缀，最前面的连续字符串，包含+、大写字符、数字的组合|

* 返回值

无

* 例子

```lua
deRegUrc("+CREG")
```

---

## ril.request(cmd, arg, onrsp, delay)

发送AT命令到底层软件

* 参数

|名称|传入值类型|释义|
|-|-|-|
|cmd|param|AT命令内容|
|arg|param|AT命令参数，例如AT+CMGS=12命令执行后，接下来会发送此参数；AT+CIPSEND=14命令执行后，接下来会发送此参数|
|onrsp|param|AT命令应答的处理函数，只是当前发送的AT命令应答有效，处理之后就失效了|
|delay|param|延时delay毫秒后，才发送此AT命令|

* 返回值

无

* 例子

```lua
ril.request("AT+CENG=1,1")
ril.request("AT+CRSM=214,28539,0,0,12,\"64f01064f03064f002fffff\"", nil, crsmResponse)
```

---
