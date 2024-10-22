# 简介

本章节将介绍如何使用Air780E模块更快，更简单的上手UART、ADC、GPIO相关的功能实现，方便缩短您学习、开发所需的周期时间。

## UART

Air780E模块物理uart有3个(0/1/2)

1. uart0是日志口(DBG_TX/DBG_RX),不推荐使用,启动时也有输出,LuatOS固件默认不允许用户使用uart0
2. uart1是主串口(MAIN_TX/MAIN_RX), 推荐使用
3. uart2是次串口(AUX_TX/AUX_RX)
4. [云编译](https://wiki.luatos.com/develop/compile/Cloud_compilation.html)支持释放uart0, 虽然不推荐这样做.
5. 下列映射是默认值, 通过 mcu.iomux 可配置

| 功能    | 对应的PIN脚 | 对应的GPIO | 对应的PAD |
| ------- | -------- | ---------- | --------- |
| DBG_RX  |    38    | -          | 29        |
| DBG_TX  |    39    | -          | 30        |
| MAIN_RX |    17    | GPIO18     | 33        |
| MAIN_TX |    18    | GPIO19     | 34        |
| AUX_RX  |    28    | GPIO10     | 25        |
| AUX_TX  |    29    | GPIO11     | 26        |

## ADC

ADC（模数转换器）用于将模拟信号转换为数字信号。在Air780E模块中，有2个ADC接口。

| 功能    | 对应的PIN脚 |
| ------- | --------  |
| ADC0    |    9      |
| ADC1    |    96     |

## GPIO

GPIO（通用输入/输出）接口用于控制和读取外部设备。在Air780E模块中，有32个GPIO接口。
[Air780E_GPIO_table_20240812.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240813172012124_Air780E&Air780EG&Air780EX&Air700E_GPIO_table_20240812.pdf)，从此文件可以查看可用的gpio脚位置和可复用功能。
