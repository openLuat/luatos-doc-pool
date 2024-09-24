# 硬件资料

## 一、产品介绍

**Air201资产定位模组**设计背景，由于当前通过销售接触、软件技术在对客户的线上支持，发现目前市场需求已经有了一些定型。现阶段合宙对客户的支持是 提供给客户选型模块，和开放的软件开发资料和demo，由客户自己按照产品方案设计业务逻辑，由于提供给客户的都是小功能的例子，只能做一些简单的数据传输，还没有达到一个产品 所能使用的业务逻辑，所以不管是在设计硬件还是开发软件，客户可能会面临各种各样的问题。

那么如果我们自己有一款设计好的硬件产品，并且有相对成熟的产品方案，也有配套完善的软件项目，对客户来说开发成本降低，产品硬件拿到手里，只要烧录对应配套的软件，就可以直接做测试，如需求没问题、测试通过，即可出整机产品，缩短量产所需的开发时间。

**Air201的核心特色：**

- 能够快速测试市场
- 减少企业客户研发投入，让客户的时间花费在值钱的业务逻辑上
- 选用最好的器件，造就最好的服务
- 提供全套服务（后台，小程序，PCBA，嵌入式软件，外壳）

## 二、模块及芯片

| **模块/芯片型号**    | **特性和功能**                                               |
| -------------------- | ------------------------------------------------------------ |
| 4G模块（780EPS）     | 长连接5分钟心跳保活: 390ua休眠功耗：2.89ua首次开机上网时间：3S外部中断/定时器唤醒上网时间：1.5S从开机到发送数据(100字节)耗能：0.12mw支持海外大多数国家（欧洲，亚洲，澳洲，北美 , 日本等） |
| GNSS                 | 捕获：18mw     追踪:  10mw单点定位精度 <1.5m灵敏度：-149dbm支持双频，北斗，RTK（选配） |
| 音频解码芯片(ES8311) | 支持VOLTE 语音支持录音放音输出 ：最大支持3W                  |
| 加速度传感器(DA267)  | 支持计步支持震动检测                                         |
| 充电芯片             | 可编程充电电流从10mA到500mA集成充电路径管理高精度充电放电电流监控可用于电量计的库仑积分STACMD单线通信，可配置充电参数和监控状态3.4V 输入UVLO，内部集成100nA的shipping模式支持漏电流及各种工作模式电流测试支持Bypass直充模式集成完善的内部保护：输入电流OCP，系统短路保护，放电保护，电池OVP，过热保护等 |

## 三、支持频段

| **模块型号** | **LTE频段**                                   | **适用地区** |
| ------------ | --------------------------------------------- | ------------ |
| 780EPS       | FDD:B1/B3/B5/B8 TDD:B34/B38/B39/B40/B41       | 中国大陆     |
| 780EPSN      | FDD：B2/B4/B5/B12/B13/B66/B71TDD: B38/B40/B41 | 北美         |
| 780EPSU      | FDD:B1/B3/B5/B7/B8/B20/B28TDD: B38/B40/B41    | 欧洲&亚洲    |

## 四、产品特性

| **参数**      | **描述**                                                     |
| ------------- | ------------------------------------------------------------ |
| 供电          | VBAT供电电压范围： 3.1V ~ 4.8V典型供电电压：3.7V默认带有3.7V锂电池 |
| LTE 特性      | 最大支持non-CA CAT1 支持1.4~20MHz射频带宽 LTE-FDD：最大上行速率 5Mbps，最大下行速率10Mbps LTE-TDD：上下行配置1 最大上行速率 4Mbps，最大下行速率 6Mbps LTE-TDD：上下行配置2 最大上行速率 2Mbps，最大下行速率 8Mbps |
| 发射功率      | LTE-FDD：Class3(23dBm+-2dB) LTE-TDD：Class3(23dBm+1/-3dB)    |
| CPU           | Cortex M3 @ 306MHz*216KB ICache                              |
| FLASH         | Nor Flash 4MB                                                |
| RAM           | 4M（2sram+2psram）                                           |
| 支持网络协议  | 支持TCP/UDP/SSL/HTTP/NTP/HTTPS/MQTT/MQTTS/FTP                |
| GNSS 特性     | 支持星系频点BDS: B1I、B1C(*)GPS: L1C/A、L1CGLONASS: L1Galileo: E1B/CQZSS: L1C/ASBAS: L1灵敏度：冷启动 -149dBm，跟踪 -165dBm，重捕捉 -159dBm定位精度：定位精度(RMS)<1.0m 速率精度：0.1m/s    授时精度（1PPS）：20ns数据格式：NMEA-0183，ICOE协议 |
| 短消息（SMS） | 文本与 PDU 模式、点对点短信收发                              |
| (U)SIM 接口   | 支持USIM/SIM卡：1.8V和3V支持贴片卡和插拔卡                   |
| 音频特性      | 支持 1 路数字音频接口：连接ES8311 codec芯片LTE：AMR/AMR-WB 支持回音消除和噪声抑制最大支持8Ω 1.2W功率喇叭 或者 4Ω 2.4W（最高支持3W）功率喇叭 |
| USB 接口      | 支持 USB 2.0 High speed（只支持从模式），数据传输速率最大到 480Mbps用于AT指令、数据传输、软件调试、软件升级 USB 虚拟串口驱动：支持Windows 7/8.1/10/11，Linux 2.6.x/3.x/4.1， Android 4.x/5.x/6.x/7.x 等操作系统下的 USB 驱动 |
| 串口          | UART1： 通用串口，可用于接外设UART2： 通用串口，可用于接外设UART3： 通用串口，可用于接外设UART0： DBG_UART串口，用于输出调试信息（默认6M波特率） |
| BTB连接器     | 支持480*320 LCD显示屏支持Camera摄像头（30W）支持按键矩阵（2*5）共计21个可用IO |
| SPI接口       | 1路 SPI接口                                                  |
| I2C接口       | 1路 I2C接口                                                  |
| 温度范围      | 正常工作温度：-35°C～+70°C极限工作温度：-40°C～+85°C         |
| 天线          | 1个 主LTE射频天线1个 GPS天线弹片和IPEX4接口天线二选一        |
| 指示灯        | 2个 4G模块控制1个 GNSS芯片（1PPS）控制                       |
| 看门狗        | 软件看门狗                                                   |

## 五、硬件说明

Air201板子设计精致小巧，整板大小只有33mm×16.5mm，厚度0.8mm，这块板子上承载了4G通讯模块、GPS芯片、同轴连接器、预留电池焊盘、4G天线、GPS天线、音频解码芯片、喇叭焊盘、按钮、加速度传感器、自弹式SIM卡座、TYPE-C接口，还有BTB 24PIN连接器，可用于再扩展连接LCD、Camera、Uart、I2C等通讯外设。

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=MTFiMmYwMTljOTQwNWEwYTcwMjc1OWEwYTFhYjQ4OWVfS2swaFRjNDF2ajl5ZkpmSkNGb3FJd3FwcVRpbVdkbDVfVG9rZW46UG1zcmJUN3NSb0RjVGF4a3RpQWNzQlIybk9iXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=YjQwZjMyZDk3ODlmMDg2MDBlMmQ2MGJjNTUyNjMxYTBfTWw2V0o1bGtxT25wS09FMWc5NWRmRUN0MXR0TWZpdXZfVG9rZW46S09xSmJUQ2Q5b2FjU3R4Yng4NWNwUXRzbmhiXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

### GPIO 复用表格

[GPIO复用表格.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240415144933952_Air780EP&Air780EPV_GPIO_table_20240415.pdf)

### 板子主要接口分布图

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=Mzc1MmU1NDhmZjliZjU5MDVhNzBkNGFiZTJmYmQ1MjNfR2YzTTNQS3A1Z1BUQXpPOUpKa2dhT0Framh3YTI4dW1fVG9rZW46RDROQ2JjcHJrb05Sd1p4eHlEdGNIN0JKbllmXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=YTgwODVlMDVhNjkzOTdlOGM0MzYyYmM0MmM0NjllNzlfRVhUdUQ5WE41OXBKNHA4RGRCcnljTXVhV2Vhb3pwTktfVG9rZW46Wml3eWIydUo5b2xCQXF4TkdkcmNlRTF0bmdlXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

### 5.1 USB Boot烧录

Air201进入boot下载模式，烧录固件和程序，需要将预留的测试点（Air201板子 B面图） 的boot 上拉到vdd_ext（A面USB旁边），之后上电开机，即可进入下载模式，下载完程序后将boot脚悬空。

### 5.2 BTB扩展接口

 通过BTB连接器，可以扩展使用 pwrkey引脚控制开关机，一路UART1串口接口连接外设，4路模拟IO口，2路带唤醒功能的wakeup引脚，一路I2C接口。同时CAM_SCK、CAM_XCLK、I2C1_SCL、I2C1_SDA于模组的SPI接口复用，支持Flash等SPI外设，另外引出2路电压一路电池电压、一路USB电压。

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=OGEyY2ZlNDRiNDBkNmNkODMwMjk3N2YxZTFiNzEzMTFfMllEcVNsRmd2Umhxa25JNEtxbHg4T2RNTkdYOXlnekhfVG9rZW46RnltMGJXNDZGb2tDcW94WGpQNmNGRGxUbktlXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

#### BTB扩展板

为方便用户更快上手，进行软件开发和调试，最新制作了搭配Air201_BTB接口的扩展板，上面已把所有扩展的io接了出来，并且挂载了flash，预留出lcd、camera的接口。

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=YjRjMTNkMjg0ZDU4MTQ1OTNiYmE4NTc1NDk4NzMwNTlfcXl2dk9lTUMzV0NIT1IzOGppVG4zaFBINUl5MjloVHlfVG9rZW46T1ZFUGJsZXNYb3dPdDl4SDd5SmNQTDZabmhkXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=Yzc0ZmIwY2Y2NDdiYTExMmYyZjk1Y2I5ZjdkODQ0ZWFfRXlDY0pkMkhOU1NYZTZkdjBMd2FSbUhvRXVoZEo1WEZfVG9rZW46T0lGT2IyOHdnbzhjT1N4eDdUbWN4Uzl3bmVlXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=YmU4ZTI0Y2RhNjUwNzk2NmJhNzUwYjU5M2Y1NDQ1OGVfajJZME1BY2ZlenpXRWhBcVR5Q0Q5a09TSGY1Smlmc1dfVG9rZW46Sm5SRmJMYVlCb3M1UTZ4UXJZcmM4djJrbmZlXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

**装配图：**

[Air201_BTB扩展板_装配图v1.0.pdf](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/all/Trdub8xPiox72mxTVPEcOJrunui/?mount_node_token=ARtkdVNBvogt3WxnNe5cDye0nXf&mount_point=docx_file)

**原理图：**

[Air201_BTB扩展板_原理图v1.0.pdf](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/all/TZagbBxRGoTIm2xn8P4cVQOIn5b/?mount_node_token=DduCdoZLyoyoegxtAT4cjZRsnJg&mount_point=docx_file)

#### 5.2.1 LCD 扩展

 扩展接口支持一路LCD专用SPI接口，用于驱动SPI LCD屏幕，不能作为通用SPI使用 **特性：**

1. 最大支持480*320分辨率，30帧
2. 仅支持SPI接口 LCD屏幕

**管脚定义****（"/"后面的管脚号是指模块对应的****PIN脚****）****：**

| **管脚名** | **管脚** | **I/O** | **管脚描述**          | **默认状态**         |
| ---------- | -------- | ------- | --------------------- | -------------------- |
| LCD_RST    | 2/49     | GPIO36  | SPI LCD 复位信号      | 上电状态默认下拉输入 |
| LCD_DOUT   | 4/50     | GPIO37  | SPI LCD 数字输出信号  | 上电状态默认下拉输入 |
| LCD_RS     | 6/51     | GPIO38  | SPI LCD 命令/数据标志 | 上电状态默认下拉输入 |
| LCD_CS     | 8/52     | GPIO35  | SPI LCD 片选          | 上电状态默认下拉输入 |
| LCD_CLK    | 10/53    | GPIO34  | SPI LCD 时钟信号      | 上电状态默认下拉输入 |

可用的供电脚：BTB扩展接口引出的 AGPIO8和AGPIO5 可用于供电1.8V，+4V位置可供3.7V。

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=Zjk2MzIxZmU5YTFhYTEzNGI4NTY0MzEyZmFiMTdmNzRfaDA4YzlpY1N2QmowWWhPVU5MSU9NTnVueXc5cmhiSjJfVG9rZW46VEZ1OGI2bkx0bzZPckR4ZzVnbmNjSGUxbjNmXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=ZmU3YjUxZGI0MzMzNDE4YTA4MWFlZmRjYjM3ZmNmYWVfQWJwWktpdFEyVFVBbmREM2JnR2dpdTVoZ3ZqYkpKM3VfVG9rZW46WFh3MGJ5U1htb3ZTaXF4cEc2TWNGUzhrbmNnXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

Air201_LCD接口.pdf

#### 5.2.2 Camera 扩展

可支持一路摄像头接口。可以用于扫码，拍照应用。

**特性：**

1. 仅支持SPI接口的摄像头
2. 最高支持30W像素

**管脚定义****（"/"后面的管脚号是指模块对应的****PIN脚****）****：**

| **管脚名** | **管脚** | **复用**          | **I/O** | **管脚描述**        | **默认状态**         |
| ---------- | -------- | ----------------- | ------- | ------------------- | -------------------- |
| CAM_SCK    | 12/80    | SPI0_SCLKI2C1_SDA | GPIO4   | SPI Camera 时钟输入 | 上电状态默认下拉输入 |
| CAM_XCLK   | 14/54    | SPI0_MISO         | GPIO3   | Camera 基准时钟     | 上电状态默认下拉输入 |
| CAM_SI0    | 16/55    | UART2_RX          | GPIO6   | SPI Camera数据输入0 | 上电状态默认下拉输入 |
| CAM_SI1    | 18/56    | UART2_TX          | GPIO7   | SPI Camera数据输入1 | 上电状态默认下拉输入 |
| CAM_ISCL   | 20/57    | I2C0_SCL          | GPIO15  | Camera I2C 时钟信号 | 上电状态默认下拉输入 |
| CAM_ISDA   | 22/58    | I2C0_SDA          | GPIO14  | Camera I2C 数据信号 | 上电状态默认下拉输入 |
| CAM_PDN    | 24/81    | I2C1_SCL          | GPIO5   | 关闭Camera          | 上电状态默认下拉输入 |

可用的供电脚：BTB扩展接口引出的 AGPIO8和AGPIO5 可用于供电1.8V，+4V位置可供3.7V。

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=ODQ1MjRkNzA5NzgxMWEyYjE5NWEwMjA3M2MwZWQ5ODdfNlFKS1FHVjdBallOdHhjN3RmMEU0U2laQ2RrdnZxUTJfVG9rZW46WUhuZGJtUmVCb2ZDN0Z4aXY2WWNvb3BrbmZjXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=YzAzMjNmYzhhZGExN2U0MTg4MTAwYTFiNzBjYTdmM2FfbmFRNzhpUkI2akdka3BXbHRkWHFzVFFkM2piSm9JODJfVG9rZW46WWJnUmJGc1JOb25US1p4M05yS2NjbFJWbnRwXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

Air201_摄像头接口.pdf

#### 5.2.3 Uart

Air201一共最多支持4路UART，UART0（DBG_UART）和UART1（MAIN_UART）板子上预留有测试点，如果需要使用UART2和UART3，要通过其他功能管脚复用。

##### UART0（DBG_UART）

DBG_TX、DBG_RX 默认功能为系统底层日志口。 

如果将此引脚复用为其他功能，则无法从 DBG_TX 和 DBG_RX 抓取系统日志。 

在某些场景下，如果模块出现异常，无法抓到问题日志，只能引出 DBG_TX、 DBG_RX，抓取日志再进行分析。 包括但不限于以下两种场景： 

1、低功耗场景： 在低功耗场景下，USB 无法使用，只能通过 DBG_TX、DBG_RX 来抓取日志。 

2、非低功耗场景： 模块接入 USB 时，工作正常，未接入 USB 时，工作异常的情况，只能通过 DBG_TX、DBG_RX 来抓取 日志。 

**管脚定义：**

| **管脚名**   | **管脚** | **复用** | **I/O** | **管脚描述**           |
| ------------ | -------- | -------- | ------- | ---------------------- |
| DBG_UART_TXD | 39       | I2C0_SCL | GPIO17  | 调试串口，输出AP log   |
| DBG_UART_RXD | 38       | I2C0_SDA | GPIO16  | 调试串口，接收调试指令 |

UART0在Air201板子上可直接连接测试点（下图蓝色标记）。由于底层日志输出对速率要求很高，所以该串口默认以6M波特率输出模块底层日志，需要配合EPAT工具+高速串口线（能支持6M波特率，例如ch343、ft4232），来抓取日志。[抓取日志教程](https://doc.openluat.com/wiki/61?wiki_page_id=5243)

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=YjVjNzIwYThmMDU1MTdmNmY0NGU2ZTIzZGUxOWNiNGFfNlptMFFKSGpGYTQ2RjhaNnlwYnVucklOb1NtQzFrZnRfVG9rZW46UEM5SWJzdm40b25aa2F4VkJSa2M3UHdtbkJlXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

#### UART1（MAIN_UART）

对于二次开发方式，UART1可通过串口配置的API接口，对波特率、数据位、校验位、停止位按需设置。

**管脚定义****（"/"后面的管脚号是指模块对应的****PIN脚****）****：**

| **管脚名**    | **管脚** | **I/O** | **管脚描述** |
| ------------- | -------- | ------- | ------------ |
| MAIN_UART_TXD | 7/18     | GPIO19  | 发送数据     |
| MAIN_UART_RXD | 9/17     | GPIO18  | 接收数据     |

UART1管脚预留位置在BTB扩展接口上面，详细位置看下图（蓝色标记）

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=NDk0MDE4OTY3MTQ0YzQzMjgyZjA0N2RhM2IyYzlhYmRfcnViMHRtdUtWeWZsaFRseXB4VHFVWUJSaDZROFRNUm5fVG9rZW46TUtQb2JJZElYb0hFOE54d1pna2N0RE1wbllkXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

##### 485串口扩展

RS485 是一种工业控制环境中常用的通讯协议，其中RS 是 Recommended Standard 的缩写。

RS485 可以进行 半双工异步 串行通信。可使用BTB接口板中的UART1扩展、

**特点：**

1. 支持多节点：一般最大支持 32 个节点。
2. 传输距离远：最远通讯距离可达1200米。
3. 抗干扰能力强：差分信号传输。
4. 连接简单：只需要两根信号线（A+和B-）就可以进行正常的通信。

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=NjZhNWZhMDI2NjViMGYwMzcxYTRlNGVlM2EwYWMyZmFfR3pIQlRRNlJnOGQ1cFBwTDdVaUlTc3I5NEJnRnJrTmpfVG9rZW46SUxXVWJyY2d6b2l0UFd4cUltdGN1OEFEbnc2XzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

Air201_rs485接口.pdf

##### 低功耗蓝牙（BLE）扩展

BLE通常适用于低功耗、轻量级的应用，例如穿戴设备、传感器网络等。而SPP适用于需要大容量数据传输的应用，例如音频设备、文件传输等。在Air201核心板上，也可以通过BTB接口实现外扩蓝牙功能，以下是参考的设计原理图。

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=NTExY2ZjMjAwNmExMjI1ZjIxN2U1NzNmNmIyZWIyNzBfN0tuS2lkbTd3MlVVUVFEV0k3V0hMZGlyYkVhYkdYd1ZfVG9rZW46UExoaGJ6Rlk4b01XZ1R4c3NJbGNkZnljbjJmXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

Air201_蓝牙模块接口板.pdf

#### 5.2.4 SPI

SPI接口可以通过CAM_SCK、CAM_XCLK、I2C1_SCL、I2C1_SDA 四个引脚的功能复用为SPI0来使用。其中 CAM_SCK 和 CAM_XCLK 需要通过0欧姆的电阻进行切换，I2C1_SCL 和 I2C1_SDA需要软件复用为alt func0来作为SPI0的功能。

**管脚定义（"/"后面的管脚号是指模块对应的****PIN脚****）：**

| **管脚名** | **管脚** | **复用**  | **I/O** | **复用SPI管脚描述** |
| ---------- | -------- | --------- | ------- | ------------------- |
| CAM_XCLK   | 14/54    | SPI0_MISO | GPIO3   | SPI 接收数据        |
| CAM_SCK    | 12/80    | SPI0_SCLK | GPIO4   | SPI 时钟同步线      |
| I2C1_SCL   | 17/85    | SPI0_MOSI | GPIO9   | SPI 发送数据        |
| I2C1_SDA   | 19/83    | SPI0_CS   | GPIO8   | SPI 片选引脚        |

#### 5.2.5 IIC（I2C）

**管脚定义（"/"后面的管脚号是指模块对应的****PIN脚****）：**

| **管脚名** | **管脚** | **复用**  | **I/O** | **管脚描述** |
| ---------- | -------- | --------- | ------- | ------------ |
| I2C1_SCL   | 19/85    | SPI0_MOSI | GPIO9   | I2C 时钟线   |
| I2C1_SDA   | 17/83    | SPI0_CS   | GPIO8   | I2C 数据线   |

I2C管脚预留位置在BTB扩展接口上面，详细位置看下图（蓝色标记）

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=N2Q1NTY0YWE3ZmE2ODk4NWUxOTYzOWEyMWM1MWM2NjZfSUhBWlY3ck9lQnJmRG5Oc3FZRzNVeUMybjdwT29oT0ZfVG9rZW46WU9ZY2JxTE91b3dWOUh4WEFhY2NTSTVablh0XzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

#### 5.2.6 按键

**管脚定义（"/"后面的管脚号是指模块对应的****PIN脚****）：**

| **管脚名** | **管脚** | **管脚描述**           |
| ---------- | -------- | ---------------------- |
| PWRKEY     | 3/7      | 控制模块电源，开机关机 |

上图该按键连接的管脚是PWRKEY，电源开关机的功能。在BTB扩展接口处也有预留PWRKEY的管脚（下图蓝色标记），客户可按照业务需求设计按键位置。

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=YmJiNTgyZmViNGExOWM3ZTBjZWY5ZjVlODAzZGQxYjFfWllkS293S01GenFRNmxzS1lHczN1SklDYmt1dm9EekhfVG9rZW46VzRzamIzeHRZb0l3R2F4dDBMd2NVWEpmbnloXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

#### 5.2.7 休眠中可保持电平的GPIO

**管脚定义（"/"后面的管脚号是指模块对应的****PIN脚****）：**

| **管脚名** | **管脚** | **I/O** | **管脚描述**           |
| ---------- | -------- | ------- | ---------------------- |
| AGPIO5     | 13/106   | GPIO25  | 休眠电平保持，普通GPIO |
| AGPIO8     | 5/78     | GPIO28  | 休眠电平保持，普通GPIO |

- AGPIO虽然在休眠下不掉电，但是无法触发中断

#### 5.2.8 休眠唤醒管脚

**管脚定义（"/"后面的管脚号是指模块对应的****PIN脚****）：**

| **管脚名** | **管脚** | **I/O** | **管脚描述**                          |
| ---------- | -------- | ------- | ------------------------------------- |
| AGPIOWU1   | 11/107   | GPIO20  | 休眠电平保持，可作为唤醒脚（WAKEUP3） |
| AGPIOWU2   | 15/19    | GPIO21  | 休眠电平保持，可作为唤醒脚（WAKEUP4） |

- AGPIO虽然在休眠下不掉电，但是无法触发中断，系统休眠后外部只能通过WAKEUP管脚或者LPUART串口唤醒。

#### 5.2.9 注意事项

1. #### AGPIO5管脚目前被内部音频占用

### 5.3 休眠

工作模式

- 待机模式（IDLE）：正常工作模式
- LIGHT（SLEEP1） 轻度睡眠模式：
  - CPU 停止
  - RAM保持供电
  - GPIO保持电平
  - 可通过定时器/网络下行数据/GPIO & WAKEUP引脚中断唤醒
  - 唤醒后程序继续运行
- DEEP（SLEEP2） 深度睡眠模式：
  - CPU 停止
  - 核心RAM掉电, 保留RAM维持供电
  - 只有AGPIO可保持休眠前的电平
  - 可定时器唤醒/WAKEUP引脚中断唤醒
  - 唤醒后程序从头运行,休眠前的运行时数据会丢失，不保存
- HIB 休眠模式：
  - CPU 停止
  - RAM掉电, 保留RAM也掉电
  - 只有AGPIO可保持休眠前的电平
  - 可定时器唤醒/WAKEUP引脚中断唤醒
  - 唤醒后程序从头运行,休眠前的运行时数据会丢失，不保存

#### 5.3.1 功耗数据

| **测试用例**                                            | **USB功能** | **飞行模式** | **LED灯管** | **GNSS**     | **ES8311** | **Gsensor**  | **音频PA** | **平均功耗** |
| ------------------------------------------------------- | ----------- | ------------ | ----------- | ------------ | ---------- | ------------ | ---------- | ------------ |
| SLEEP1模式下最低功耗                                    | 关闭        | 开启         | 关闭        | 关闭         | 关闭       | 关闭         | 关闭       | 84μA         |
| HIB 模式下最低功耗                                      | 开启        | 开启         | 关闭        | 关闭         | 关闭       | 关闭         | 关闭       | 17μA         |
| IDLE 待机功耗                                           | 关闭        | 开启         | 关闭        | 关闭         | 关闭       | 关闭         | 关闭       | 3.54mA       |
| GNSS工作功耗（不含模块和其他部件电流）                  | 关闭        | 开启         | 关闭        | 开启         | 关闭       | 关闭         | 关闭       | 12.07mA      |
| GNSS和Gsensor打开备电（不含模块和其他部件电流）         | 关闭        | 开启         | 关闭        | 只打开GPIO24 | 关闭       | 只打开GPIO24 | 关闭       | 220μA        |
| ES8311供电开启但未工作时 功耗（不含模块和其他部件电流） | 关闭        | 开启         | 关闭        | 关闭         | 开启       | 关闭         | 关闭       | 220μA        |
| 音频PA 功耗（不含模块和其他部件电流）                   | 关闭        | 开启         | 关闭        | 关闭         | 关闭       | 关闭         | 开启       | 2.71mA       |

### 5.4 4G天线调试

建议一般直接找天线厂家帮忙挑选和适配天线。

#### 频率范围：

确定天线的支持频率范围，首先确认模块支持的频段有哪些，不同的频段对应不同的频率，目前我们4G模块所支持的频率范围大致800Mhz-2700Mhz，所以满足合宙CAT 1模块的4G天线的频率需要覆盖到800Mhz-2700Mhz；

#### 增益：

在输入功率相等的条件下，实际天线与理想的辐射单元在空间同一点处所产生的信号的功率密度之比。

一般选择5dbi的增益就能够用，设备环境较差的时候可以选择更高增益的天线；

#### 驻波比：

全称为电压驻波比，又名VSWR和SWR，指驻波波腹电压与波谷电压幅度之比，又称为驻波系数、驻波比。驻波比等于1时，表示馈线和天线的阻抗完全匹配，此时高频能量全部被天线辐射出去，没有能量的反射损耗；驻波比为无穷大时，表示全反射，能量完全没有辐射出去。

驻波比的值为1~∞，4G天线一般选用驻波比≤1.5的最好，理想的驻波比值为1，目前还没有能够达到驻波比为1的情况；

#### 辐射模式：

有全向和定向之分；

全向天线：水平方向图上表现为360°都均匀辐射，也就是平常所说的无方向性；

定向天线：在水平方向图上表现为一定角度范围辐射，也就是平常所说的有方向性；

目前大多数区域的基站覆盖都是比较密集的，所以选择全向天线比较多，在基站比较少，且可以确定基站方位的时候，可以推荐选择定向天线；

#### 天线的极化方式：

天线辐射时形成的电场强度方向；

目前4G基站的天线大多数采取的是双极化的方式，所以UE端多采用线极化的方式；

原因为：一比较好实现，二线极化好匹配；

#### 常见天线形式：

目前天线的形式有多种样式： 棒状天线、船桨天线、吸盘天线、FPC天线，可根据产品的使用场景和其本身的大小进行选择；

#### 馈线长度的问题：

这个根据产品的情况，选择合适的长短，不易过长，尽量减少损耗。

#### 阻抗控制：

模块的ANT PAD输出端的阻抗是50Ω，所以选择同样的50Ω阻抗的天线，利于输入输出达到匹配状态。

### 5.5 GNSS天线调试

建议一般直接找天线厂家帮忙挑选和适配天线。目前Air201板子上只能使用无源天线。

天线作为GPS设备中最重要的接收器件，它起到的作用就像是人的“耳朵”，是将卫星发送下来的电磁波能量变换成电子器件可解析的电流。因此天线的性能好坏将直接关系到GPS整机的产品性能。

GPS天线的种类：从安装方式上分为外置天线和内置天线；供电方式上分为有源天线和无源天线;从极化方式上分为垂直极化和圆极化.

#### 无源天线在我们产品上的使用建议

- 我们的GPS模块上均内置18dBm增益的GPS LNA，可以直接将陶瓷介质的无源天线焊接在模块GPS_ANT PIN脚处使用。 产品布局的时候，GPS陶瓷天线朝上摆放；模块可以放到PCB的另一面。这样就可以做到GPS_ANT PIN到天线焊盘走线尽可能短。
- 匹配电路；如果天线焊盘离模块的GPS_ANT PIN脚很近，那么可以不预留匹配电路。如果由于结构等其他原因造成GPS天线远离模块GPS_ANT PIN，那么建议预留pi型匹配电路。模块 GPS_ANT PIN到GPS天线焊盘之间走线必须做50欧姆特性阻抗控制；如果是多层板，建议阻抗线走L1层，L2层镂空参考L3的地。2层板走线线宽可以参考GSM天线部分走线线宽。
- 天线下方不要走线并做漏铜处理做天线的反射面；
- 天线周边不要有干扰源，特别是DCDC等器件；另外周边也不要有比GPS天线高的金属器件：如下图：

#### GPS天线选型建议

1. 在终端结构空间容许，能够统一保证GPS天线面朝上的安装使用状态；并且周边没有大的金属物件遮挡的情况下，建议使用GPS陶瓷天线，在空间容许的情况下尽量选择大尺寸的陶瓷天线。
2. 在不能保证终端使用状态，且空间受限：比如手机，带定位功能的胸牌；建议使用FPC天线
3. 在明确终端安装环境恶劣，并且对GPS性能有较高要求的；建议使用GPS有源天线
4. 在不能保证产品安装使用状态，但是空间不受限制，也可以选择类似于GSM的外置棒状天线。

#### 对天线厂家的要求

1. VSWR：GPS天线电压驻波比一般要求调到1.5左右.
2. Efficiency：效率一般要求在40%左右
3. Average Gain：平均增益要求在-0.5dB
4. OTA：一般天线厂大多不具备GPS 天线OTA测试环境，天线调试好后可以以实际测试数据做标准来衡量；一般我们GPS实测时要求是：可用于定位卫星颗数大于6颗以上，最强的信号在45 dB/Hz左右，要有3颗卫星信号大于40 dB/Hz。

#### GPS天线厂家选择

国内能自行生产GPS陶瓷天线的厂家主要是艾福电子通讯有限公司、嘉兴佳利电子、佳邦电子、嘉康电子等厂家。但是多数天线厂都是可以完成GPS天线的调试的，只是生产时会外包给其他具有独立陶瓷粉末配方和烧制工艺的厂家。

我们合作过的GPS天线厂家有：

苏州迅合德通讯 联系人：常爱进13913050523

浙江嘉兴佳利电子 联系人：钟雪文15618568209

### 5.6 设计音频注意事项

- 清晰度：确保音频的清晰度，避免出现杂音，回声等影响听感的因素
- 还原度：尽量还原原始声音的细节和质感，使听众能够更好的理解和感受内容
- 音量：保持音量适中，避免过大或者过小，确保听众能够舒适的收听
- 动态范围：合理的控制音频的动态范围，突出重点内容，是听众容易抓住关键信息
- 语速和节奏感：保持适当的节奏感，使音频听起来有节奏感，根据内容需要，适当调整语速，更好的表达情感和强调重点

### 5.7 调试音频方法

- 扬声器调试：播放不同频率的测试音频，并调整扬声器的音量和均衡器，确保音色平衡，避免过度增强某个频段
- 混音器调试：调整不同音轨的音量平衡和混响效果，改善整体音质
- 噪声测试：关闭所有音源，并提高音量到最大，检查是否存在噪声干扰
- 反馈测试：逐步提高麦克风音量，确保没有产生噪音或者断裂的音频信号
- 听觉测试：播放不同类型音频，包括音乐和人声，测试音频的清晰度、音量均衡和混响效果
