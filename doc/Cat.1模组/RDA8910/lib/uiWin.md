
@[TOC]

# uiWin

模块功能：UI窗口管理

## uiWin.add(wnd)

新增一个窗口

* 参数

|名称|传入值类型|释义|
|-|-|-|
|wnd|table|窗口的元素以及消息处理函数表|

* 返回值

number，窗口ID

* 例子

```lua
uiWin.add({onUpdate = refresh})
```

---

## uiWin.remove(winId)

移除一个窗口

* 参数

|名称|传入值类型|释义|
|-|-|-|
|winId|number|窗口ID|

* 返回值

nil

* 例子

```lua
uiWin.remove(winId)
```

---

## uiWin.isActive(winId)

判断一个窗口是否处于最前显示

* 参数

|名称|传入值类型|释义|
|-|-|-|
|winId|number|窗口ID|

* 返回值

bool，true表示最前显示，其余表示非最前显示

* 例子

```lua
uiWin.isActive(winId)
```

---
