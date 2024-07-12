
@[TOC]

# sys

模块功能：Luat协程调度框架

## sys.restart(r)

软件重启

* 参数

|名称|传入值类型|释义|
|-|-|-|
|r|string|重启原因，用户自定义，一般是string类型，重启后的trace中会打印出此重启原因|

* 返回值

无

* 例子

```lua
sys.restart('程序超时软件重启')
```

---

## sys.wait(ms)

task任务延时函数

只能直接或者间接的被task任务主函数调用，如果定时器创建成功，则本task会挂起

* 参数

|名称|传入值类型|释义|
|-|-|-|
|ms|number|延时时间，单位毫秒，最小1，最大0x7FFFFFFF<br>实际上支持的最小超时时间是5毫秒，小于5毫秒的时间都会被转化为5毫秒|

* 返回值

result，分为如下三种情况：<br>1、如果定时器创建失败，本task不会被挂起，直接返回nil<br>2、如果定时器创建成功，本task被挂起，超时时间到达后，会激活本task，返回nil<br>3、如果定时器创建成功，本task被挂起，在超时时间到达之前，其他业务逻辑主动激活本task，<br>返回激活时携带的可变参数（如果不是故意为之，可能是写bug了）

* 例子

```lua
task延时5秒：
sys.taskInit(function()
sys.wait(5000)
end)
```

---

## sys.waitUntil(id, ms)

task任务条件等待函数（支持事件消息和定时器消息）

只能直接或者间接的被task任务主函数调用，调用本接口的task会挂起

* 参数

|名称|传入值类型|释义|
|-|-|-|
|id|string|消息ID，建议使用string类型|
|ms|number|**可选参数，默认为`nil`** 延时时间，单位毫秒，最小1，最大0x7FFFFFFF<br>实际上支持的最小超时时间是5毫秒，小于5毫秒的时间都会被转化为5毫秒|

* 返回值

result,data，分为如下三种情况：<br>1、如果存在超时时间参数：<br>(1)、在超时时间到达之前，如果收到了等待的消息ID，则result为true，data为消息ID携带的参数（可能是多个参数）<br>(2)、在超时时间到达之前，如果没收到等待的消息ID，则result为false，data为nil<br>2、如果不存在超时时间参数：如果收到了等待的消息ID，则result为true，data为消息ID携带的参数（可能是多个参数）<br>(1)、如果收到了等待的消息ID，则result为true，data为消息ID携带的参数（可能是多个参数）<br>(2)、如果没收到等待的消息ID，则task一直挂起<br>3、还存在一种特殊情况，本task挂起时，可能被task的外部应用逻辑给主动激活（如果不是故意为之，可能是写bug了）

* 例子

```lua
task延时120秒或者收到"SIM_IND"消息：
sys.taskInit(function()
local result, data = sys.waitUntil("SIM_IND",120000)
end)
```

---

## sys.waitUntilExt(id, ms)

Task任务的条件等待函数扩展（包括事件消息和定时器消息等条件），只能用于任务函数中。

* 参数

|名称|传入值类型|释义|
|-|-|-|
|id|param|消息ID|
|ms|number|等待超时时间，单位ms，最大等待126322567毫秒|

* 返回值

message 接收到消息返回message，超时返回false
data 接收到消息返回消息参数

* 例子

```lua
result, data = sys.waitUntilExt("SIM_IND", 120000)
```

---

## sys.taskInit(fun, ...)

创建一个任务并且运行该任务

* 参数

|名称|传入值类型|释义|
|-|-|-|
|fun|param|任务主函数，激活task时使用|
|...|param|任务主函数fun的可变参数|

* 返回值

co  返回该任务的线程ID

* 例子

```lua
sys.taskInit(task1,'a','b')
```

---

## sys.init(mode, lprfnc)

Luat平台初始化

* 参数

|名称|传入值类型|释义|
|-|-|-|
|mode|param|充电开机是否启动GSM协议栈，1不启动，否则启动|
|lprfnc|param|用户应用脚本中定义的“低电关机处理函数”，如果有函数名，则低电时，本文件中的run接口不会执行任何动作，否则，会延时1分钟自动关机|

* 返回值

无

* 例子

```lua
sys.init(1,0)
```

---

## sys.timerStop(val, ...)

关闭sys.timerStart和sys.timerLoopStart创建的定时器

有两种方式可以唯一标识一个定时器：<br>1、定时器ID<br>2、定时器回调函数和可变参数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|val|param|有两种形式：<br>1、为number类型时，表示定时器ID<br>2、为function类型时，表示定时器回调函数|
|...|param|可变参数，当val为定时器回调函数时，此可变参数才有意义，表示定时器回调函数的可变回调参数|

* 返回值

nil

* 例子

```lua
-- 通过定时器ID关闭一个定时器：
local timerId = sys.timerStart(publicTimerCbFnc,8000,"second")
sys.timerStop(timerId)
-- 通过定时器回调函数和可变参数关闭一个定时器：
sys.timerStart(publicTimerCbFnc,8000,"first")
sys.timerStop(publicTimerCbFnc,"first")
```

---

## sys.timerStopAll(fnc)

关闭sys.timerStart和sys.timerLoopStart创建的某个回调函数的所有定时器

* 参数

|名称|传入值类型|释义|
|-|-|-|
|fnc|function|定时器回调函数|

* 返回值

nil

* 例子

```lua
-- 关闭回调函数为publicTimerCbFnc的所有定时器
local function publicTimerCbFnc(tag)
log.info("publicTimerCbFnc",tag)
end
sys.timerStart(publicTimerCbFnc,8000,"first")
sys.timerStart(publicTimerCbFnc,8000,"second")
sys.timerStart(publicTimerCbFnc,8000,"third")
sys.timerStopAll(publicTimerCbFnc)
```

---

## sys.timerStart(fnc, ms, ...)

创建并且启动一个单次定时器

有两种方式可以唯一标识一个定时器：<br>1、定时器ID<br>2、定时器回调函数和可变参数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|fnc|param|定时器回调函数，必须存在，不允许为nil<br>当定时器超时时间到达时，回调函数的调用形式为fnc(...)，其中...为回调参数|
|ms|number|定时器超时时间，单位毫秒，最小1，最大0x7FFFFFFF<br>实际上支持的最小超时时间是5毫秒，小于5毫秒的时间都会被转化为5毫秒|
|...|param|可变参数，回调函数fnc的回调参数|

* 返回值

number timerId，创建成功返回定时器ID；创建失败返回nil

* 例子

```lua
-- 创建一个5秒的单次定时器，回调函数打印"timerCb"，没有可变参数：
sys.timerStart(function() log.info("timerCb") end, 5000)
-- 创建一个5秒的单次定时器，回调函数打印"timerCb"和"test"，可变参数为"test"：
sys.timerStart(function(tag) log.info("timerCb",tag) end, 5000, "test")
```

---

## sys.timerLoopStart(fnc, ms, ...)

创建并且启动一个循环定时器

有两种方式可以唯一标识一个定时器：<br>1、定时器ID<br>2、定时器回调函数和可变参数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|fnc|param|定时器回调函数，必须存在，不允许为nil<br>当定时器超时时间到达时，回调函数的调用形式为fnc(...)，其中...为回调参数|
|ms|number|定时器超时时间，单位毫秒，最小1，最大0x7FFFFFFF<br>实际上支持的最小超时时间是5毫秒，小于5毫秒的时间都会被转化为5毫秒|
|...|param|可变参数，回调函数fnc的回调参数|

* 返回值

number timerId，创建成功返回定时器ID；创建失败返回nil

* 例子

```lua
-- 创建一个5秒的循环定时器，回调函数打印"timerCb"，没有可变参数：
sys.timerLoopStart(function() log.info("timerCb") end, 5000)
-- 创建一个5秒的循环定时器，回调函数打印"timerCb"和"test"，可变参数为"test"：
sys.timerLoopStart(function(tag) log.info("timerCb",tag) end, 5000, "test")
```

---

## sys.timerIsActive(val, ...)

判断“通过timerStart或者timerLoopStart创建的定时器”是否处于激活状态

* 参数

|名称|传入值类型|释义|
|-|-|-|
|val|param|定时器标识，有两种表示形式<br>1、number类型，通过timerStart或者timerLoopStart创建定时器时返回的定时器ID，此情况下，不需要传入回调参数...就能唯一标识一个定时器<br>2、function类型，通过timerStart或者timerLoopStart创建定时器时的回调函数，此情况下，如果存在回调参数，需要传入回调参数...才能唯一标识一个定时器|
|...|param|回调参数，和“通过timerStart或者timerLoopStart创建定时器”的回调参数保持一致|

* 返回值

status，定时器激活状态；根据val的表示形式，有不同的返回值：<br>1、val为number类型时：如果处于激活状态，则返回function类型的定时器回调函数；否则返回nil<br>2、val为function类型时：如果处于激活状态，则返回bool类型的true；否则返回nil

* 例子

```lua
-- 定时器ID形式标识定时器的使用参考：
local timerId1 = sys.timerStart(function() end,5000)
sys.taskInit(function()
sys.wait(3000)
log.info("after 3 senonds, timerId1 isActive?",sys.timerIsActive(timerId1))
sys.wait(3000)
log.info("after 6 senonds, timerId1 isActive?",sys.timerIsActive(timerId1))
end)
-- 回调函数和回调参数标识定时器的使用参考：
local function timerCbFnc2(tag)
log.info("timerCbFnc2",tag)
end
sys.timerStart(timerCbFnc2,5000,"test")
sys.taskInit(function()
sys.wait(3000)
log.info("after 3 senonds, timerCbFnc2 test isActive?",sys.timerIsActive(timerCbFnc2,"test"))
sys.wait(3000)
log.info("after 6 senonds, timerCbFnc2 test isActive?",sys.timerIsActive(timerCbFnc2,"test"))
end)
```

---

## sys.subscribe(id, callback)

订阅消息

* 参数

|名称|传入值类型|释义|
|-|-|-|
|id|param|消息id|
|callback|param|消息回调处理|

* 返回值

无

* 例子

```lua
subscribe("NET_STATUS_IND", callback)
```

---

## sys.unsubscribe(id, callback)

取消订阅消息

* 参数

|名称|传入值类型|释义|
|-|-|-|
|id|param|消息id|
|callback|param|消息回调处理|

* 返回值

无

* 例子

```lua
unsubscribe("NET_STATUS_IND", callback)
```

---

## sys.publish(...)

发布内部消息，存储在内部消息队列中

* 参数

|名称|传入值类型|释义|
|-|-|-|
|...|param|可变参数，用户自定义|

* 返回值

无

* 例子

```lua
publish("NET_STATUS_IND")
```

---

## rtos.on (id, handler)

注册rtos消息回调处理函数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|id|number|消息类型id|
|handler|param|消息处理函数|

* 返回值

无

* 例子

```lua
rtos.on(rtos.MSG_KEYPAD, function(param) handle keypad message end)
```

---

## sys.run()

run()从底层获取core消息并及时处理相关消息，查询定时器并调度各注册成功的任务线程运行和挂起

* 参数

无

* 返回值

无

* 例子

```lua
sys.run()
```

---
