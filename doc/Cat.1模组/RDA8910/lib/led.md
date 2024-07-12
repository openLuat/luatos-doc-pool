
@[TOC]

# led

模块功能：LED闪灯模块

## led.blinkPwm(ledPin, light, dark)

闪烁指示灯

* 参数

|名称|传入值类型|释义|
|-|-|-|
|ledPin|function|ledPin(1)用pins.setup注册返回的方法|
|light|number|light-亮灯时间ms|
|dark|number|dark-灭灯时间ms|

* 返回值

nil

* 例子

```lua
led.blinkPwm(lenPin,500,500)
-- 调用函数需要使用任务支持
```

---

## led.levelLed(ledPin, bl, bd, cnt, gap)    

等级指示灯

* 参数

|名称|传入值类型|释义|
|-|-|-|
|ledPin|function|ledPin(1)用pins.setup注册返回的方法|
|bl|number|亮灯时间ms|
|bd|number|灭灯时间ms|
|cnt 重复次数|number|(等级的级别,亮灭1次算数字1)|
|gap 间隔时间|number|(每次循环周期的间隔)|

* 返回值

nil

* 例子

```lua
led.leveled(ledPin,200,200,4,1000)
-- 调用函数需要使用任务支持
```

---

## led.breateLed(ledPin)

呼吸灯

* 参数

|名称|传入值类型|释义|
|-|-|-|
|ledPin|function|呼吸灯的ledPin(1)用pins.setup注册返回的方法|

* 返回值

nil

* 例子

```lua
led.breateLed(ledPin)
-- 调用函数需要使用任务支持
```

---
