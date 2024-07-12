@[TOC]

# pio
模块管脚操作
## pio.pin.close(pin1,pin2,...pinn)

关闭引脚

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|pin1|number|第一个管脚|   |
|pin2(可选)|number|第二个管脚|  |
|pinn(可选)|number|第n个管脚|  |

**返回值**

无

**例子**

```lua
  pio.pin.close(1)

```

---



## pio.pin.plus(pin,high_us, low_us, count, idle)

通过gpio设置方波(阻塞)

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|pin|number|管脚号|   |
|high_us|number|高电平持续时间(单位us)|   |
|low_us|number|低电平持续时间(单位us)|  |
|count|number|高电平个数|   |
|idle|number|输出完成后管脚状态|   |

**返回值**

无

**例子**

```lua
  --gpio13 idle为低电平，输出15个高脉冲，高电平持续10us，低电平持续20us
  pio.pin.plus(13,10,20,15,0)

```

---



## pio.pin.pwm(pin,high_us, low_us, count)

通过gpio模拟pwm(非阻塞)

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|pin|number|管脚号|  |
|high_us|number|高电平持续时间(单位us）|   |
|low_us|number|低电平持续时间(单位us）|   |
|count|number|电平个数 -1:一直发|   |

**返回值**

无

**例子**

```lua
  --[[通过gpio端口持续发送一个高电平与一个低电平，且所有高电平时间相同，所有低电平时间相同。维持高电平与低电平的时间，就可以形成周期时间。占空比 = 高电平时间/周期时间
  如果我们改变高低电平的持续时间，就可以完成占空比的调节，从而模拟出pwm波。]]
  --gpio13 持续输出，高电平持续100us，低电平持续200us
  pio.pin.pwm(13,100,200,-1)
  --gpio13 关闭模拟的pwm
  pio.pin.pwm(13,0,0,-1)

```

---



## pio.pin.setdir( direction,pin1,pin2,...,pinn,pin_op)

设置管脚的方向

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.07.28|脉冲检测模式|>3101| |

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|direction|number|管脚方向,(可选)|pio.INPUT,pio.OUTPUT,pio.INT|
|pin1|number|第一个管脚|   |
|pin2|number|第2个管脚(可选)|   |
|pin3|number|第3个管脚(可选)|   |
|pinn|number|第n个管脚(可选)|  |
|pin_op|number|引脚功能,(可选)|pio.FIFO为脉冲检测模式,pio.CONT为统计脉冲个数(频率超过1.5kHz会有漏检和误差过大的情况)|

**返回值**

无

---



## pio.pin.setpull(method,pin)

配置IO口默认状态

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|method|number|pio.PULLUP：上拉模式 。pio.PULLDOWN：下拉模式。pio.NOPULL：高阻态|   |
|pin|number|配置管脚|   |

**返回值**

无

**例子**

```lua
  pio.pin.setpull(pio.PULLUP,pio.P0_5)  --配置为上拉
--pio.pin.setpull(pio.PULLDOWN,pio.P0_5)  --配置为下拉
--pio.pin.setpull(pio.NOPULL,pio.P0_5)  --不配置上下拉

```

---



## pio.pin.setdebounce(ms)

配置IO口防抖时间

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|ms|number|防抖时间，0为关闭消抖功能，开机后默认为20ms|   |

**返回值**

无

**例子**

```lua
  pio.pin.setdebounce(20)  --延时消抖设置为20ms
  pio.pin.setdebounce(5)  --延时消抖设置为5ms
  pio.pin.setdebounce(0)  --关闭延时消抖功能

```

---



## pio.pin.setval( direction,pin1,pin2,...,pinn)

设置管脚的输出状态

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|direction|number|管脚状态，可选0或1|   |
|pin1|number|第一个管脚|   |
|pin2|number|第2个管脚(可选)|   |
|pin3|number|第3个管脚(可选)|   |
|pinn|number|第n个管脚(可选)|       |

**返回值**

无

---



## pio.pin.sethigh(pin1,pin2,...,pinn)

设置管脚为高电平(1)

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|pin1|number|第一个管脚|   |
|pin2|number|第2个管脚(可选)|   |
|pin3|number|第3个管脚(可选)|   |
|pinn|number|第n个管脚(可选)|       |

**返回值**

无

---



## pio.pin.setlow(pin1,pin2,...,pinn)

设置管脚为低电平(0)

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|pin1|number|第一个管脚|   |
|pin2|number|第2个管脚(可选)|   |
|pin3|number|第3个管脚(可选)|   |
|pinn|number|第n个管脚(可选)|       |

**返回值**

无

---



## pio.pin.getval(pin1,pin2,...,pinn)

读取管脚的状态

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.07.28|脉冲检测功能|>3101| |

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|pin1|number|第一个管脚|   |
|pin2|number|第2个管脚(可选)|   |
|pin3|number|第3个管脚(可选)|   |
|pinn|number|第n个管脚(可选)|  |

**返回值**

 **返回值**
 |                                        | 类型   | 释义         | 取值                     |
 | -------------------------------------- | ------ | ------------ | ------------------------ |
 | 当pio.pin.setdir()不传pin_op时      | number | 管脚状态     | 0表示低电平，1表示高电平 |
 | 当pio.pin.setdir()中参数pin_op传pio.FIFO时 | table  | 脉冲检测模式 |                         |
 | 当pio.pin.setdir()中参数pin_op传pio.CONT时 | table  | 统计脉冲个数 |           

**例子**

```lua
 **例子**

  **当pio.pin.setdir()不传pin_op时**

 ```
 pin1, pin2, ..., pinn = pio.pin.getval( pin1, pin2, ..., pinn )
 ```

 **当pio.pin.setdir()中参数pin_op传pio.FIFO时**

 ```
 table = pio.pin.getval( pin1, pin2, ..., pinn )
 表的格式为
 {
  {
    edge = 0, -- 下降沿
    delta = 10, -- 离上次变化的事件（单位us）
  },
  {
    edege = 1, -- 上升沿
    delta = 20, -- 离上次变化的事件（单位us）
  },
  ...
 }
 ```

 **当pio.pin.setdir()中参数pin_op传pio.CONT时**

 ```
 table = pio.pin.getval( pin1, pin2, ..., pinn )
 表的格式为
 {
  low = 10, -- 低电平个数
   high = 10, -- 高电平个数
  duration = 2000000, -- 距上次读取的时间（单位us）
 }
 ```

```

---

## pio.pin.setIoMux(pins[,fc])  （注：该接口目前仅支持Air795）
IO复用
**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|pins|number|pins文件下宏|例如：pins.IOMUX_GPIO10  |
|fc|number|多种复用选择|0，1，0默认通道|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|ret|boole|状态|复用成功返回true，失败返回false|

---

