
@[TOC]

# syspuls

模块功能：Luat协程调度框架

## sysplus.taskInitEx(fun, taskName, cbFun, ...)

创建一个任务线程,在模块最末行调用该函数并注册模块中的任务函数，main.lua导入该模块即可

* 参数

|名称|传入值类型|释义|
|-|-|-|
|fun|param|任务函数名，用于resume唤醒时调用|
|taskName|param|任务名称，用于唤醒任务的id|
|cbFun|param|接收到非目标消息时的回调函数|
|...|param|任务函数fun的可变参数|

* 返回值

co  返回该任务的线程号

* 例子

```lua
sysplus.taskInitEx(task1,'a',callback)
```

---

## sysplus.taskDel(taskName)

删除由taskInitEx创建的任务线程

* 参数

|名称|传入值类型|释义|
|-|-|-|
|taskName|param|任务名称，用于唤醒任务的id|

* 返回值

无

* 例子

```lua
sysplus.taskDel('a')
```

---

## sysplus.waitMsg(taskName, target, ms)

等待接收一个目标消息

* 参数

|名称|传入值类型|释义|
|-|-|-|
|taskName|param|任务名称，用于唤醒任务的id|
|target|param|目标消息，如果为nil，则表示接收到任意消息都会退出|
|ms|param|超时时间，如果为nil，则表示无超时，永远等待|

* 返回值

msg or false 成功返回table型的msg，超时返回false

* 例子

```lua
sysplus.waitMsg('a', 'b', 1000)
```

---

## sysplus.sendMsg(taskName, param1, param2, param3, param4)

向目标任务发送一个消息

* 参数

|名称|传入值类型|释义|
|-|-|-|
|taskName|param|任务名称，用于唤醒任务的id|
|param1|param|消息中的参数1，同时也是waitMsg里的target|
|param2|param|消息中的参数2|
|param3|param|消息中的参数3|
|param4|param|消息中的参数4|

* 返回值

true or false 成功返回true

* 例子

```lua
sysplus.sendMsg('a', 'b')
```

---
