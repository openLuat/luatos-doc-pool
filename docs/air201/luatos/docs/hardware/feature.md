# 产品特性

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