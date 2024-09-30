# 基本用法

本文通过demo演示来说明本章节内容的基本用法。

## 文档和工具

- gpio接口文档：[gpio](https://wiki.luatos.com/api/gpio.html)

- 780E模块使用固件：[LuatOS固件](https://gitee.com/openLuat/LuatOS/releases)，本demo使用的固件版本是：LuatOS-SoC_V1112_EC618_FULL.soc

- 本教程使用的demo：[780E_LuatOS_Gpio_Demo](https://gitee.com/openLuat/LuatOS/blob/master/demo/gpio/gpio/main.lua)

- 将固件和脚本烧录到模块中：[烧录教程](https://doc.openluat.com/wiki/21?wiki_page_id=6024)

## GPIO简介

1、认识模块的GPIO管脚：780E模块的gpio与其他MCU类的芯片一样，也可以配置为输入/输出/上拉/下拉/中断等状态，只有在硬件设计手册上注明带GPIO功能的管脚才能作为GPIO使用。

普通GPIO输出驱动能力单管脚<=10mA, 但是所有普通驱动电流总和不能超过200m

### 本demo使用api介绍

#### gpio.setup(pin, mode, pull, irq, alt)

设置管脚功能

**参数**

| 传入值类型 | 解释 |
|:----:|:----:|
| int        | pin gpio编号,必须是数值|
| any        | mode 输入输出模式： 数字0/1代表输出模式 nil代表输入模式 function代表中断模式，如果填gpio.count，则为中断计数功能，中断时不回调 |
| int        | pull 上拉下拉模式, 可以是上拉模式 gpio.PULLUP 或下拉模式 gpio.PULLDOWN, 或者开漏模式 0. 需要根据实际硬件选用 |
| int        | irq 中断触发模式,默认gpio.BOTH。中断触发模式 上升沿gpio.RISING 下降沿gpio.FALLING 上升和下降都触发gpio.BOTH |
| int        | alt 复用选项，目前只有EC618平台需要这个参数，有些GPIO可以复用到不同引脚上，可以选择复用选项（0或者4）从而复用到对应的引脚上 |

**返回值**

| 返回值类型 | 解释 |
|:----:|:----:|
| any        | 输出模式返回设置电平的闭包, 输入模式和中断模式返回获取电平的闭包 |

**例子**

```lua
-- 设置gpio17为输入
gpio.setup(17, nil)

-- 设置gpio17为输出,且初始化电平为低,使用硬件默认上下拉配置
gpio.setup(17, 0)

-- 设置gpio17为输出,且初始化电平为高,且启用内部上拉
gpio.setup(17, 1, gpio.PULLUP)

-- 设置gpio27为中断, 默认双向触发
gpio.setup(27, function(val)
    print("IRQ_27",val) -- 提醒, val并不代表触发方向, 仅代表中断后某个时间点的电平
end, gpio.PULLUP)

-- 设置gpio27为中断, 仅上升沿触发
gpio.setup(27, function(val)
    print("IRQ_27",val) -- 提醒, val并不代表触发方向, 仅代表中断后某个时间点的电平
end, gpio.PULLUP, gpio.RISING)

-- 中断计数 于2024.5.8新增
-- 设置gpio7为中断计数，详细demo见gpio/gpio_irq_count
gpio.setup(7, gpio.count)

-- alt_func 于2023.7.2新增
-- 本功能仅对部分平台有效, 且仅用于调整GPIO复用,其他复用方式请使用muc.iomux函数
-- 以下示例代码, 将I2S_DOUT复用成gpio18
-- AIR780E的PIN33(模块管脚序号), 对应paddr 38, 默认功能是I2S_DOUT, 复用成gpio18
-- 方向输出,且初始化电平为低,使用硬件默认上下拉配置
-- Air780E(EC618系列的GPIO复用请查阅 https://air780e.cn 首页硬件资料表格中的Air780E&Air780EG&Air780EX&Air700E_GPIO_table_20231227.pdf)
-- Air780EP(EC718P系列的GPIO复用请查阅 https://air780ep.cn 首页硬件资料表格中的Air780E&Air780EG&Air780EX&Air700E_GPIO_table_20231227.pdf)
gpio.setup(18, 0, nil, nil, 4)

-- 提醒: 
-- 当管脚为输入模式或中断,才能通过gpio.get()获取到电平
-- 当管脚为输出模式,才能通过gpio.set()设置电平
-- 当管脚为输出模式,通过gpio.get()总会得到0
-- 中断回调的val参数不代表触发方向, 仅代表中断后某个时间点的电平
-- 对Cat.1模块,EC618系列只有AONGPIO才能双向触发，其他系列所有GPIO都能双向触发，具体看硬件手册
-- 默认设置下,中断是没有防抖时间的,可以通过gpio.set_debounce(pin, 50)来设置防抖时间

-- pull参数的额外说明, 上拉/下拉配置
-- 对于部分的BSP来说, 只支持 gpio.PULLUP 或 gpio.PULLDOWN, 但有部分BSP支持开漏模式
-- 对于支持开漏的bsp, pull参数要传 0 才能开启开漏模式, 不是传nil
-- 例如:
-- EC618系列(Air780E/Air780EG/Air780EX/Air700E等)
```
