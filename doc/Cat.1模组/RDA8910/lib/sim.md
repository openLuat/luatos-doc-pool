
@[TOC]

# sim

模块功能：查询sim卡状态、iccid、imsi、mcc、mnc

## sim.getIccid()

获取sim卡的iccid

* 参数

无

* 返回值

string ,返回iccid，如果还没有读取出来，则返回nil

* 例子

```lua
-- 注意：开机lua脚本运行之后，会发送at命令去查询iccid，所以需要一定时间才能获取到iccid。开机后立即调用此接口，基本上返回nil
sim.getIccid()
```

---

## sim.getImsi()

获取sim卡的imsi

* 参数

无

* 返回值

string ,返回imsi，如果还没有读取出来，则返回nil

* 例子

```lua
-- 开机lua脚本运行之后，会发送at命令去查询imsi，所以需要一定时间才能获取到imsi。开机后立即调用此接口，基本上返回nil
sim.getImsi()
```

---

## sim.getMcc()

获取sim卡的mcc

* 参数

无

* 返回值

string ,返回值：mcc，如果还没有读取出来，则返回""

* 例子

```lua
-- 注意：开机lua脚本运行之后，会发送at命令去查询imsi，所以需要一定时间才能获取到imsi。开机后立即调用此接口，基本上返回""
sim.getMcc()
```

---

## sim.getMnc()

获取sim卡的getmnc

* 参数

无

* 返回值

string ,返回mnc，如果还没有读取出来，则返回""

* 例子

```lua
-- 注意：开机lua脚本运行之后，会发送at命令去查询imsi，所以需要一定时间才能获取到imsi。开机后立即调用此接口，基本上返回""
sim.getMnc()
```

---

## sim.getStatus()

获取sim卡的状态

* 参数

无

* 返回值

bool ,true表示sim卡正常，false或者nil表示未检测到卡或者卡异常

* 例子

```lua
-- 开机lua脚本运行之后，会发送at命令去查询状态，所以需要一定时间才能获取到状态。开机后立即调用此接口，基本上返回nil
sim.getStatus()
```

---

## sim.setQueryNumber(flag)

设置“是否打开查询本机号码”的功能

* 参数

|名称|传入值类型|释义|
|-|-|-|
|flag|bool|开启或者关闭查询功能的标志，false或者nil为关闭，其余为开启|

* 返回值

nil

* 例子

```lua
sim.setQueryNumber(true)
```

---

## sim.getNumber()

获取sim卡的本机号码

* 参数

无

* 返回值

string ,返回值：sNumber，如果还没有读取出来或者读取失败，则返回""

* 例子

```lua
-- 注意：开机lua脚本运行之后，会发送at命令去查询本机号码，所以需要一定时间才能获取到本机号码。开机后立即调用此接口，基本上返回""
-- 注意：此功能需要卡商支持，卡商必须把卡写到sim卡中，模块才能从卡中读出号码；目前市场上的很多卡，没有写入号码，是无法读取得
sim.getNumber()
```

---

## sim.setId(id, cbFnc)

设置双卡单待sim id

* 参数

|名称|传入值类型|释义|
|-|-|-|
|id|number|双卡单待的simid，仅支持0和1|
|cbFnc|function|**可选参数，默认为`nil`** 设置结果回调函数，回调函数的调用形式为：<br>cnFnc(result)，result为true表示成功，false或者nil为失败|

* 返回值

nil

* 例子

```lua
sim.setId(0)
sim.setId(1,cbFnc)
```

---

## sim.getId()

获取目前设置的双卡单待id

* 参数

无

* 返回值

number ,返回id(0或者1)，如果还没有读取出来，则返回nil

* 例子

```lua
-- 注意：开机lua脚本运行之后，会发送at命令去查询id，所以需要一定时间才能获取到id。开机后立即调用此接口，基本上返回nil
sim.getId()
```

---
