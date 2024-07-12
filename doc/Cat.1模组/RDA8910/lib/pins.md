
@[TOC]

# pins

模块功能：GPIO 功能配置，包括输入输出IO和上升下降沿中断IO

## pins.setup(pin, val, pull)

配置GPIO模式

* 参数

|名称|传入值类型|释义|
|-|-|-|
|pin|number|GPIO，ID<br>GPIO 0到GPIO 31表示为pio.P0_0到pio.P0_31<br>GPIO 32到GPIO XX表示为pio.P1_0到pio.P1_(XX-32)，例如GPIO33 表示为pio.P1_1<br>GPIO 64到GPIO XX表示为pio.P2_0到pio.P2_(XX-64)，例如GPIO65 表示为pio.P2_1|
|val|param|number、nil或者function类型<br>配置为输出模式时，为number类型，表示默认电平，0是低电平，1是高电平<br>配置为输入模式时，为nil<br>配置为中断模式时，为function类型，表示中断处理函数|
|pull|param|number，pio.PULLUP：上拉模式。pio.PULLDOWN：下拉模式。pio.NOPULL：高阻态<br>如果没有设置此参数，默认的上下拉参考模块的硬件设计说明书|

* 返回值

function<br>配置为输出模式时，返回的函数，可以设置IO的电平<br>配置为输入或者中断模式时，返回的函数，可以实时获取IO的电平

* 例子

```lua
setOutputFnc = pins.setup(pio.P1_1,0)，配置GPIO 33，输出模式，默认输出低电平；
-- 执行setOutputFnc(0)可输出低电平，执行setOutputFnc(1)可输出高电平
getInputFnc = pins.setup(pio.P1_1,intFnc)，配置GPIO33，中断模式
-- 产生中断时自动调用intFnc(msg)函数：上升沿中断时：msg为cpu.INT_GPIO_POSEDGE；下降沿中断时：msg为cpu.INT_GPIO_NEGEDGE
-- 执行getInputFnc()即可获得当前电平；如果是低电平，getInputFnc()返回0；如果是高电平，getInputFnc()返回1
getInputFnc = pins.setup(pio.P1_1),配置GPIO33，输入模式
-- 执行getInputFnc()即可获得当前电平；如果是低电平，getInputFnc()返回0；如果是高电平，getInputFnc()返回1
-- 有些GPIO需要打开对应的ldo电压域之后，才能正常配置工作，电压域和对应的GPIO关系如下
pmd.ldoset(x,pmd.LDO_VSIM1) -- GPIO 29、30、31
pmd.ldoset(x,pmd.LDO_VLCD) -- GPIO 0、1、2、3、4
pmd.ldoset(x,pmd.LDO_VMMC) -- GPIO 24、25、26、27、28
x=0时：关闭LDO
x=1时：LDO输出1.716V
x=2时：LDO输出1.828V
x=3时：LDO输出1.939V
x=4时：LDO输出2.051V
x=5时：LDO输出2.162V
x=6时：LDO输出2.271V
x=7时：LDO输出2.375V
x=8时：LDO输出2.493V
x=9时：LDO输出2.607V
x=10时：LDO输出2.719V
x=11时：LDO输出2.831V
x=12时：LDO输出2.942V
x=13时：LDO输出3.054V
x=14时：LDO输出3.165V
x=15时：LDO输出3.177V
-- 除了上面列举出的GPIO外，其余的GPIO不需要打开特定的电压域，可以直接配置工作
```

---

## pins.close(pin)

关闭GPIO模式 test

* 参数

|名称|传入值类型|释义|
|-|-|-|
|pin|number|GPIO，ID<br><br>GPIO 0到GPIO 31表示为pio.P0_0到pio.P0_31<br><br>GPIO 32到GPIO XX表示为pio.P1_0到pio.P1_(XX-32)，例如GPIO33 表示为pio.P1_1|

* 返回值

无

* 例子

```lua
pins.close(pio.P1_1)，关闭GPIO33
```

---
