
@[TOC]

# pm

模块功能：休眠管理

## pm.wake(tag)

某个Lua应用唤醒系统

* 参数

|名称|传入值类型|释义|
|-|-|-|
|tag|param|一般string类型，某个Lua应用的唤醒标记，用户自定义|

* 返回值

无

* 例子

```lua
pm.wake(tag)
```

---

## pm.sleep(tag)

某个Lua应用休眠系统

* 参数

|名称|传入值类型|释义|
|-|-|-|
|tag|param|一般string类型，某个Lua应用的唤醒标记，用户自定义，跟wake中的标记保持一致|

* 返回值

无

* 例子

```lua
pm.sleep(tag)
```

---

## pm.isSleep(tag)

pm.isSleep([tag]) 读取某个Lua应用或者全局的休眠状态

* 参数

|名称|传入值类型|释义|
|-|-|-|
|tag|param|可选参数，如果查询某个tag的休眠状态，则跟wake中的tag保持一致；如果查询全局休眠状态，则不需要这个参数|

* 返回值

true休眠，其余没休眠

* 例子

```lua
pm.isSleep() -- 查询全局休眠状态
pm.isSleep('lcd') -- 查询lcd的休眠状态
```

---
