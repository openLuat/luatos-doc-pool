# 合宙Air700ECQ模组资料中心

- [合宙Air700ECQ模组产品手册](https://docs.openluat.com/air700ecq/product/)
- [合宙Air700ECQ模组LuatOS资料中心](https://docs.openluat.com/air700ecq/luatos/)
- [合宙Air700ECQ模组AT资料中心](https://docs.openluat.com/air700ecq/at/)


## 选型Air700ECQ/EAQ/EMQ时，我应该注意什么?

### 这篇文档的目的是什么

1. 从用户的角度，解答大家对Air700ECQ/EAQ/EMQ这三款模组最关心的问题；
2. 本篇文档内容不深入探究技术细节，更多从选型、应用等非技术维度展开；
3. 阅读本篇文档之前，建议先详细阅读一遍"合宙产品选型手册"，有助于理解；
4. 接下来的内容，我们仅以移动版本Air700ECQ为例做说明，电信版本Air700EAQ、联通版本Air700EMQ，软件和硬件与Air700ECQ完全兼容，大家可以根据自己产品选用的SIM卡运营商来灵活选择具体型号；

### Air700ECQ核心信息描述

照片

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=OTViODdmZDE3MWI0YTA2Nzg2OTdhZjFiYzY1Y2EzMzBfMHhXbjFHRXRyUXIxUTFzZVdJVUZBcDBNTjczNUlrbUJfVG9rZW46TEtKdWJwT0ZTbzFjUXh4VXdUYmN2c1drbjJnXzE3MjgyOTA1NDg6MTcyODI5NDE0OF9WNA)

管脚透视图

![](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NGI1NDZmYmY1MThmNmQzNjRmODljYTMzZGY2ZTJlNDVfR2luZTdoOVYwWmtja2JPNUdFV2JjTG5MMHc2UHdBUE5fVG9rZW46RHNxd2J6ZVkyb3RQV1l4bE1pSGM2RUV5bnhnXzE3MjgyOTA1NDg6MTcyODI5NDE0OF9WNA)

1. Air700ECQ的主打卖点超小超薄，大小仅为10\*13\*1.7mm，不仅小，而且薄，尺寸受限的产品可以选择；
2. Air700ECQ因为设计取向为尺寸超小，所以无法在硬件上同时支持移动、电信和联通，三大运营商要分三个不同的版本，其中，Air700ECQ为移动版本，Air700EAQ为电信版本，Air700EMQ为联通版本；
3. Air700ECQ/Air700EAQ/Air700EMQ的区别只有所支持的运营商不同(本质是不同运营商所需要支持的射频频段不同)，除此之外，软硬件上都可以完全兼容，可以根据客户所需灵活选择不同运营商版本即可；
4. Air700ECQ软件上既支持传统的AT指令，也支持合宙基于Lua脚本开发的嵌入操作系统LuatOS；
5. Air700ECQ硬件上支持丰富的外设管脚，比如USB、UART、SPI、I2C、PWM、GPIO等，相对Air780EQ较多，相对Air780E/Air780EP/Air780EPS则较少一些；
6. Air700ECQ支持丰富的网络协议，比如TCP/UDP、TCP-SSL/TCP-TLS、MQTT、HTTP、WEBSOCKET、NTP等；
7. Air700ECQ不支持TTS语音播放，也不支持VoLTE语音通话，需要支持这两个功能的应用推荐选择合宙Air724UG；
8. Air700ECQ功耗表现在合宙现有模组中排名中等，低功耗模式下0.5mA，低功耗表现最好的模组型号是合宙Air780EPS；

### Air700ECQ实网功耗数据

| Air700ECQ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 常规模式                    | 低功耗模式                                   | PSM+模式                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4G在线状态                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 在线，长连接                | 在线，长连接                                 | 离线，飞行模式                                            |
| 定时器唤醒                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 支持                        | 支持                                         | 支持                                                      |
| 中断唤醒                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 支持                        | 支持                                         | 支持                                                      |
| 串口唤醒                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 支持                        | 支持，唤醒时波特率需先设置为9600bps          | 支持，唤醒时波特率需先设置为9600bps                       |
| 服务器4G唤醒                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 支持，1秒内``        | 支持，1秒内                                  | 不支持                                                    |
| 上行发送                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1秒内响应                   | 1秒内响应                                    | 1.5秒内响应                                               |
| VEXT电源输出状态                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 保持输出                    | 不能保持输出，也不能保持关闭，间歇性输出状态 | 不能保持输出，也不能保持关闭，间歇性输出状态              |
| 所有GPIO管脚是否可以控制输出电平                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 可以                        | 不可以                                       | 不可以                                                    |
| 常规GPIO管脚是否可以保持电平                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 可以                        | 不可以                                       | 不可以                                                    |
| 特殊AGPIO管脚是否可以保持电平                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 可以                        | 可以                                         | 可以                                                      |
| RAM供电及唤醒后软件运行状态                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | RAM供电，正常工作，满血状态 | RAM供电，唤醒后保持原状态运行                | RAM掉电，唤醒后程序从初始状态运行(PSM+状态前运行数据丢失) |
| 典型功耗表现                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 较低(7mA)                   | 均衡(0.5mA)                                  | 极低(3uA)                                                 |


**测试环境：**

1)Air700ECQ，供电电压3.8V，移动网络，频段B3，RSRP值-88附近，DRX 2.56秒，心跳间隔5分钟，心跳数据100Byte，TCP协议，合宙服务器，回环测试；

2)Air700ECQ，同等环境下，低功耗模式，DRX 1.28秒时，平均电流0.9mA，DRX 0.64秒时，平均电流1mA；

3)Air700ECQ，同等环境下，常规模式，DRX 1.28秒时，平均电流7.2mA，DRX 0.64秒时，平均电流7.6mA；

4)DRX，Discontinuous Reception，非连续接收，可简单理解为模块与基站之间保持心跳的间隔，一般为0.64秒/1.28秒/2.56秒，需要注意的是，DRX由基站根据网络实际情况而定，模组无法自行控制；

5)Air700ECQ功耗表现在合宙现有模组中排名中等，低功耗模式下平均电流0.5mA，低功耗表现最好的模组型号是合宙Air780EPS，请根据需要灵活选择； 

### Air700ECQ之AT指令

|    功能点    | Air700ECQ<br />Air700EAQ<br />Air700EMQ <br />Air780EQ | Air780ER | Air780EP | Air780E<br />Air780EX | Air780EPS | Air724UG | Air780EEN<br />Air780EEU<br />Air780EEJ | Air780EG | 备注说明                                                                 |
| :-----------: | :----------------------------------------------------: | :------: | :------: | :-------------------: | :-------: | :------: | :-------------------------------------: | :------: | ------------------------------------------------------------------------ |
|   基础指令   |                           Y                           |    Y    |    Y    |           Y           |     Y     |    Y    |                    Y                    |    Y    |                                                                          |
|    TCP/UDP    |                           Y                           |    Y    |    Y    |           Y           |     Y     |    Y    |                    Y                    |    Y    |                                                                          |
|     HTTP     |                           Y                           |          |    Y    |           Y           |     Y     |    Y    |                    Y                    |    Y    |                                                                          |
|     MQTT     |                           Y                           |          |    Y    |           Y           |     Y     |    Y    |                    Y                    |    Y    |                                                                          |
|      FTP      |                           Y                           |          |    Y    |           Y           |     Y     |    Y    |                    Y                    |    Y    |                                                                          |
|      NTP      |                           Y                           |    Y    |    Y    |           Y           |     Y     |    Y    |                    Y                    |    Y    | NetworkTimeProtocol,网络时间协议                                         |
|      SSL      |                           Y                           |    Y    |    Y    |           Y           |     Y     |    Y    |                    Y                    |    Y    | TLS/SSL配置                                                              |
|      FS      |                           Y                           |          |    Y    |           Y           |     Y     |    Y    |                    Y                    |    Y    | 建立文件,枚举文件,传输TLS/SSL证书                                        |
|      SMS      |                           Y                           |          |    Y    |           Y           |     Y     |    Y    |                    Y                    |    Y    | 短信功能，Air724UG支持移动联通电信，``其余型号仅支持移动联通，电信不支持 |
|   WiFiScan   |                           Y                           |          |    Y    |           Y           |     Y     |    Y    |                    Y                    |    Y    | WiFi扫描,用于定位                                                        |
|      LBS      |                           Y                           |          |    Y    |           Y           |     Y     |    Y    |                    Y                    |    Y    | 基站定位                                                                 |
|      GPS      |                                                        |          |          |                      |          |          |                                        |    Y    | 定位功能                                                                 |
|      TTS      |                                                        |          |          |                      |          |    Y    |                                        |          | Text To Speech                                                           |
|     VoTLE     |                                                        |          |          |                      |          |    Y    |                                        |          | 语音通话                                                                 |
|      PPP      |                                                        |    Y    |          |           Y           |          |    N    |                    Y                    |    Y    | PPP拨号上网                                                              |
| USB_RNDIS_ECM |                                                        |    Y    |          |           Y           |          |    N    |                    Y                    |    Y    | USB网络驱动                                                              |

### Air700ECQ之LuatOS

|                   功能点                   |   Air780EQ   | Air700ECQ<br />Air700EAQ<br />Air700EMQ |    Air780E    |   Air780EX   |   Air780EG   |       Air780EP       |      Air780EPS      |  Air724UG  | 备注                        |
| :-----------------------------------------: | :-----------: | :-------------------------------------: | :-----------: | :-----------: | :-----------: | :------------------: | :------------------: | :--------: | --------------------------- |
|                   总Flash                   |      4M      |                   4M                   |      5MB      |      5MB      |      5MB      |         4MB         |         8MB         |     8M     |                             |
| 用户代码可用Flash<br />（含脚本和脚本FOTA） |     1.4M     |                  1.4M                  |    >1.6MB    |    >1.6MB    |    >1.6MB    |        <1.6MB        |         <5MB         |    >4M    |                             |
|                    总RAM                    |      1M      |                   1M                   |   2MB(SRAM)   |   2MB(SRAM)   |   2MB(SRAM)   | 2MB(SRAM)+2MB(PSRAM) | 2MB(SRAM)+2MB(PSRAM) | 16M(PSRAM) |                             |
|                   TCP/UDP                   |      2路      |                   2路                   |      6路      |      6路      |      6路      |         6路         |         6路         |    8路    |                             |
|               TCP-SSL/TCP-TLS               |      1路      |                   1路                   |      2路      |      2路      |      2路      |         2路         |         2路         |    4路    |                             |
|                    MQTT                    |       Y       |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | mqtt通信                    |
|                    HTTP                    |       Y       |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | http通信                    |
|                     FTP                     |       Y       |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | ftp通信                     |
|                  WEBSOCKET                  |       Y       |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | websocket通信               |
|                 NTP网络对时                 |       Y       |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | 时钟,必带                   |
|                    JSON                    |       Y       |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | json                        |
|                   SMS短信                   | Y(不支持电信) |              Y(不支持电信)              | Y(不支持电信) | Y(不支持电信) | Y(不支持电信) |    Y(不支持电信)    |    Y(不支持电信)    |     Y     | 短信功能                    |
|         阿里云/腾讯云/百度云/华为云         |       Y       |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | 各种云平台的密钥计算        |
|               REPL控制台repl               |              |                                        |              |              |              |                      |                      |     Y     | 控制台repl                  |
|                  PROTOBUF                  |              |                                        |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | 谷歌PB编解码                |
|                   RSA加密                   |              |                                        |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | RSA加密                     |
|                  XXTEA加密                  |              |                                        |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | XXTEA加密                   |
|                  国密算法                  |              |                                        |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | 国密加密                    |
|            加密解密md5/sha1/aes            |       Y       |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | 加密/解密,md5/sha1之类      |
|                64位数据处理                |       Y       |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     N     | 64位数据的处理库            |
|               ICONV字符集转换               |       Y       |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | 字符编码转换                |
|              ZBUFF(C内存数组)              |       Y       |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     N     | c风格内存数组, tcp/udp需要  |
|               PACK数据编解码               |       Y       |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | 数据打包解包                |
|                  zlib解压                  |       Y       |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | zlib压缩                    |
|                 内部WDT硬狗                 |       Y       |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | 硬狗,必带                   |
|                 PM功耗管理                 |       Y       |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | 功耗管理                    |
|                 低功耗模式                 |       Y       |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |            | 长连接低功耗模式            |
|                   接口类                   |              |                                        |              |              |              |                      |                      |            |                             |
|                    GPIO                    | Y(仅AONGPIO) |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | 复用较多,数量见具体硬件手册 |
|                    UART                    |    Y(2个)    |                 Y(2个)                 |    Y(2个)    |    Y(2个)    |    Y(1个)    |        Y(3个)        |        Y(3个)        |   Y(3个)   | 串口通信/485/少量传感器     |
|                     I2C                     |              |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | 传感器居多                  |
|                     SPI                     |              |                    Y                    |       Y       |              |       Y       |          Y          |          Y          |     Y     | 传感器/各种外设/SPI屏幕     |
|                     ADC                     |              |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | 测外部电压/供电电压/CPU温度 |
|                     PWM                     |              |                    Y                    |       Y       |       Y       |       Y       |          Y          |          Y          |     Y     | 输出方波,驱动马达           |
|                   GPS定位                   |              |                                        |              |              |       Y       |                      |                      |            | GPS定位功能                 |
|                  WIFISCAN                  |  Y(共用天线)  |               Y(共用天线)               |  Y(共用天线)  |  Y(共用天线)  |  Y(共用天线)  |     Y(共用天线)     |     Y(共用天线)     |     Y     | WiFi扫描,用于WiFi定位       |
|                   音频类                   |              |                                        |              |              |              |                      |                      |            |                             |
|                音频播放(MP3)                |              |                                        |              |              |              |                      |                      |     Y     | 播放AMR/MP3                 |
|                    录音                    |              |                                        |              |              |              |                      |                      |     Y     | 录音                        |
|                     TTS                     |              |                                        |              |              |              |                      |                      |     Y     | TTS                         |
|                    VOLTE                    |              |                                        |              |              |              |                      |                      |     Y     | VoLTE                       |
|                    UI类                    |              |                                        |              |              |              |                      |                      |            |                             |
|                  SPI串口屏                  |              |                                        |              |              |              |                      |                      |     Y     | SPI屏幕                     |
|                   墨水屏                   |              |                                        |              |              |              |                      |                      |     Y     | 墨水屏驱动                  |
|                 OLED单色屏                 |              |                                        |              |              |              |                      |                      |     Y     | OLED驱动                    |
|                  中文字体                  |              |                                        |              |              |              |                      |                      |     Y     | 字体管理                    |
|                    LVGL                    |              |                                        |              |              |              |                      |                      |     Y     | LVGL                        |
|                   摄像头                   |              |                                        |              |              |              |                      |                      |     Y     | 摄像头功能                  |
|                    扫码                    |              |                                        |              |              |              |                      |                      |     Y     |                             |

### Air700ECQ常见咨询

1. **Air700ECQ支持C-SDK开发吗？**

   Air700ECQ不支持C-SDK开发，推荐您使用LuatOS开发方式；

   LuatOS基于Lua脚本语言开发，Demo功能库齐全，文档丰富，用户只需定义好业务逻辑便可快速开发；

   LuatOS专用调试工具Luatools，具备项目代码维护、软件下载、查看运行Trace，快速定位问题等功能；

2. **Air700ECQ支持FOTA功能吗？**

   Air700ECQ支持FOTA功能；

   [合宙IoT平台](https://iot.openluat.com)可以对个人账号下的每一片模组进行FOTA管理；

   Air700ECQ支持差分升级，无论AT软件，还是LuatOS软件，都可以通过合宙IoT后台进行FOTA升级；

3. **Air700ECQ支持数据透传吗？**

   Air700ECQ支持数据透传功能；

   无论AT指令，还是LuatOS，Air700ECQ都可以方便的实现数据透传功能；

   如果您想更快速的实现设备上网功能，可以使用合宙的DTU模组或整机，详见[合宙dtu管理平台](https://dtu.openluat.com)；

4. **Air700ECQ与Air780EQ什么关系？**

   Air700ECQ与Air780EQ共有四点不同：

   封装不同，Air700ECQ更小，Air780EQ稍大；

   管脚不同，Air780EQ因为封装较大，管脚也较多；

   支持的运营商不同，Air780EQ支持国内三大运营商，而Air700ECQ支持移动，Air700EAQ支持电信，Air700EMQ支持联通；

   LuatOS支持的功能不同，Air780EQ支持所有通信协议、UART和AGPIO，Air700ECQ在此基础上又增加了I2C、SPI、ADC、PWM等硬件接口的支持；

   就AT指令所支持的功能来讲，Air700ECQ和Air780EQ完全相同；

5. **Air700ECQ可以支持海外市场吗？**

   Air700ECQ不支持海外市场；

   Air700ECQ支持 FDD:B3/8;TDD:B34/38/39/40/41 ，支持中国移动运营商；

   Air700EAQ支持 FDD:B1/3/5 ，支持中国电信运营商；

   Air700EMQ支持 FDD:B1/3/8 ，支持中国联通运营商；

   如果您需要支持海外市场的模组，可推荐如下三款型号：

   Air780EEN/Air780EEU/Air780EEJ可以支持海外不同的国家和区域；

   Air780EEN，频段支持FDD:B2/4/5/12/13/66/71;TDD:B40/41，主要面向北美区域；

   Air780EEU，频段支持FDD:B1/3/5/7/8/20/28;TDD:B40/41，主要面向欧洲亚洲区域；

   Air780EEJ，频段支持FDD:B1/3/8/18/19/26/28;TDD:B40/41，主要面向日本；

### 合宙模组更多资料

官网 [www.openluat.com](www.openluat.com)

资料 [docs.openluat.com](https://docs.openluat.com)

样品 [luat.taobao.com](luat.taobao.com)

公众号 HelloLuatOS
