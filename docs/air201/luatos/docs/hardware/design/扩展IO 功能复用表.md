

| 管脚序列 | 管脚名    | Pad Name | paddr [7:2] | 上电默认状态   | Alt Func0 | Alt Func1 | Alt Func2 | Alt Func3  | Alt Func4   | Alt Func5 | Alt Func6 | 说明                             |
| -------- | --------- | -------- | ----------- | -------------- | --------- | --------- | --------- | ---------- | ----------- | --------- | --------- | -------------------------------- |
| 2        | LCD_RST   | GPIO36   | 42          |                | GPIO36    | USP2_DIN  | I2C1_SCL  |            |             |           |           |                                  |
| 4        | LCD_DOUT  | GPIO37   | 43          | 非输入，非上拉 | GPIO37    | USP2_DOUT | I2C1_SDA  |            |             |           |           | LSP_SDA                          |
| 6        | LCD_RS    | GPIO38   | 44          | 非输入，非上拉 | GPIO38    | USP2_MCLK | USP2_WRX  |            |             |           |           | LSP_WRX                          |
| 8        | LCD_CS    | GPIO35   | 41          | 非输入，非上拉 | GPIO35    | USP2_LRCK |           | UART3_TXD  |             |           |           | LSPI_CSX                         |
| 10       | LCD_CLK   | GPIO34   | 40          | 非输入，非上拉 | GPIO34    | USP2_BCLK |           | UART3_RXD  |             |           |           | LSPI_DCX (CLK)                   |
| 12       | CAM_SCK   | GPIO3    | 18          | 非输入，非上拉 | GPIO3     | USP1_MCLK | USP1_WRX  |            | ONEW        | PWM2      | KPC_C4    | CSPI_MCLK                        |
| 14       | CAM_XCLK  | GPIO4    | 19          | 非输入，非上拉 | GPIO4     | USP1_BCLK | I2C1_SDA  | UART1_RTSn | USIM1_URSTn |           | KPC_R1    | CSPI_BCLK                        |
| 16       | CAM_SI0   | GPIO6    | 21          | 非输入，非上拉 | GPIO6     | USP1_DIN  |           | UART1_RTSn | USIM1_UIO   |           | KPC_C3    | CSPI_RX0                         |
| 18       | CAM_SL1   | GPIO7    | 22          | 非输入，非上拉 | GPIO7     | USP1_DOUT |           | UART1_CTSn | ONEW        |           | KPC_C2    | CSPI_RX1                         |
| 20       | CAM_ISCL  | GPIO15   | 30          | 非输入，非上拉 | GPIO15    | SPI1_SCLK |           | UART3_TXD  | USP2_MCLK   | PWM1      | KPC_C2    | Camera                           |
| 22       | CAM_ISDA  | GPIO14   | 29          | 非输入，非上拉 | GPIO14    | SPI1_MISO |           | UART3_RXD  | USIM1_UCLK  | PWM0      | KPC_C3    | Camera                           |
| 24       | CAM_PDN   | GPIO5    | 20          | 非输入，非上拉 | GPIO5     | USP1_LRCK | I2C1_SCL  | UART1_CTSn | USIM1_UCLK  |           | KPC_R0    | CAM-PD                           |
|          |           |          |             |                |           |           |           |            |             |           |           |                                  |
| 3        | PWRKEY    | PWRKEY   |             |                | PWRKEY    |           |           |            |             |           |           | 开机键,中断可唤醒                |
| 5        | AGPIO8    | AGPIO8   | 53          | 非输入，非上拉 | GPIO28    |           |           | PWM4n      | ONEW        |           |           | 休眠可保持输出                   |
| 7        | UART1_RXD | GPIO18   | 33          | 非输入，非上拉 | GPIO18    | UART1_RXD |           |            |             |           |           | 主串口，可在休眠时候UART数据唤醒 |
| 9        | UART1_TXD | GPIO19   | 34          | 非输入，非上拉 | GPIO19    | UART1_TXD |           |            |             |           |           | 主串口，可在休眠时候UART数据唤醒 |
| 11       | AGPIOWU1  | AGPIOWU1 | 46          | 非输入，非上拉 | GPIO21    |           |           |            | FEM6        | PWM4      | KPC_C3    | 中断可唤醒，休眠可保持IO输出     |
| 13       | 空        |          |             |                |           |           |           |            |             |           |           |                                  |
| 15       | AGPIOWU2  | AGPIOWU2 | 47          | 非输入，非上拉 | GPIO22    |           |           | PWM4n      | FEM5        |           | KPC_C4    | 中断可唤醒，休眠可保持IO输出     |
| 17       | I2C1_SDA  | SWDIO1   | 14          | 输入上拉       | SWDIOC    |           |           | I2C1_SDA   | GPIO19      | PWM1      | KPC_C4    | I2C 数据线                       |
| 19       | I2C1_SCL  | SWCLK1   | 13          | 输入上拉       | SWCLKC    |           |           | I2C1_SCL   | GPIO18      | PWM0      | KPC_R4    | I2C 时钟线                       |
| 21       | VCC(+4v)  | VCC(+4v) |             |                |           |           |           |            |             |           |           | 引自电池，可对外供电             |
| 23       | VBUS      | WAKEUP1  |             | 输入           | WAKEUP1   |           |           |            |             |           |           | 中断可唤醒                       |

注意事项：											
1	休眠情况下，中断可唤醒的IO 有4个，另外还支持UART 数据唤醒										
2	休眠情况下，可对外输出的IO口总计3个										
3	AONGPIO(5,11,15)管脚休眠模式下可保持，保持高或低。										
4	WAKEUP(11,15,23)管脚固定电平1.8V，由于内部分压，内部上拉电平测量在1.1V左右										
5	WAKEUP(11,15,23)管脚内部上下拉非常弱，驱动能力<30uA.										
6	系统休眠后外部只能通过WAKEUP(11,15,23)管脚或者LPUART(7,9)串口唤醒，AONGPIO(5,11,15)虽然在休眠下不掉电，但是无法触发中断。										
7	普通GPIO在休眠后均会处于高阻状态。										
8	"板载的DBG_TX、DBG_RX默认功能为系统底层日志口，进行模块硬件设计时，在剩余功能引脚充足的前提下，避免使用DBG_TX和DBG_RX。
如果将此引脚复用为其他功能，则无法从DBG_TX和DBG_RX抓取系统日志。
在某些场景下，如果模块出现异常，无法抓到问题日志，只能通过硬件改版，引出DBG_TX、DBG_RX，抓取日志再进行分析。
包括但不限于以下两种场景：
1、低功耗场景：
在低功耗场景下，USB无法使用，只能通过DBG_TX、DBG_RX来抓取日志。
2、非低功耗场景：
模块接入USB时，工作正常，未接入USB时，工作异常的情况，只能通过DBG_TX、DBG_RX来抓取日志。"										
9	"所有GPIO和wakeuppad都支持双边沿中断；
可以复用为wakeup的io，休眠以及唤醒状态下都能使用；
其余io唤醒状态下可用，休眠状态下不能使用；
wakeup io可以唤醒休眠，其余GPIO都不可以。"										