
@[TOC]

# netLed

模块功能：网络指示灯模块

## netLed.setup(flag, ledPin, ltePin)

配置网络指示灯和LTE指示灯并且立即执行配置后的动作

* 参数

|名称|传入值类型|释义|
|-|-|-|
|flag|bool|是否打开网络指示灯和LTE指示灯功能，true为打开，false为关闭|
|ledPin|number|控制网络指示灯闪烁的GPIO引脚，例如pio.P0_1表示GPIO1|
|ltePin|number|控制LTE指示灯闪烁的GPIO引脚，例如pio.P0_4表示GPIO4|

* 返回值

nil

* 例子

```lua
setup(true,pio.P0_1,pio.P0_4)表示打开网络指示灯和LTE指示灯功能，GPIO1控制网络指示灯，GPIO4控制LTE指示灯
setup(false)表示关闭网络指示灯和LTE指示灯功能
```

---

## netLed.updateBlinkTime(state, on, off)

配置某种工作状态下指示灯点亮和熄灭的时长（如果用户不配置，使用netLed.lua中ledBlinkTime配置的默认值）

* 参数

|名称|传入值类型|释义|
|-|-|-|
|state|string|某种工作状态，仅支持"FLYMODE"、"SIMERR"、"IDLE"、"GSM"、"GPRS"、"SCK"|
|on|number|指示灯点亮时长，单位毫秒，0xFFFF表示常亮，0表示常灭|
|off|number|指示灯熄灭时长，单位毫秒，0xFFFF表示常灭，0表示常亮|

* 返回值

nil

* 例子

```lua
updateBlinkTime("FLYMODE",1000,500)表示飞行模式工作状态下，指示灯闪烁规律为：亮1秒，灭0.5秒
updateBlinkTime("SCK",0xFFFF,0)表示有socket连接上后台的工作状态下，指示灯闪烁规律为：常亮
updateBlinkTime("SIMERR",0,0xFFFF)表示SIM卡异常状态下，指示灯闪烁规律为：常灭
```

---
