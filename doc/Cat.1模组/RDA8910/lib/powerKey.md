
@[TOC]

# powerKey

模块功能：开机键功能配置

## powerKey.setup(longPrd, longCb, shortCb)

配置开机键长按弹起和短按弹起的功能.

如何定义长按键和短按键，例如长按键判断时长为3秒：<br>按下大于等于3秒再弹起判定为长按键；<br>按下后，在3秒内弹起，判定为短按键

* 参数

|名称|传入值类型|释义|
|-|-|-|
|longPrd|number|**可选参数，默认为`3000`** 长按键判断时长，单位毫秒|
|longCb|function|**可选参数，默认为`nil`** 长按弹起时的回调函数，如果为nil，使用默认的处理函数，会自动关机|
|shortCb|function|**可选参数，默认为`nil`** 短按弹起时的回调函数|

* 返回值

nil

* 例子

```lua
powerKey.setup(nil,longCb,shortCb)
powerKey.setup(5000,longCb)
powerKey.setup()
```

---
