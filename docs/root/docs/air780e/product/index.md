## Air780E几句话介绍
1. 在阅读本页面资料之前，强烈建议您先阅读一遍合宙产品选型手册， Docs.openluat.com 首页打开即是；
2. 合宙4G Cat.1模组主推型号有十余款，每一款都各有特点，每一款都有各自更适合的场景，Air780E是其中一款；
3. Air780E是一款面向国内的全网通模组，支持移动、电信、联通三大运营商；
4. Air780E封装尺寸是16*18*2.3mm，仅比合宙Air700ECQ/Air700EAQ/Air700EMQ相对大一些；
5. Air780E软件上既支持传统的AT指令，也支持合宙基于Lua脚本开发的嵌入操作系统LuatOS；
6. Air780E硬件上支持丰富的外设管脚，比如USB、UART、SPI、I2C、PWM、GPIO等；
7. Air780E支持丰富的网络协议，比如TCP/UDP、TCP-SSL/TCP-TLS、MQTT、HTTP、WEBSOCKET、NTP等；
8. Air780E不支持TTS语音播放，也不支持VoLTE语音通话，需要支持这两个功能的应用推荐选择合宙Air724UG；
9. Air780E功耗表现在合宙现有模组中排名中等，低功耗模式下低于0.5mA，低功耗表现最好的模组型号是合宙Air780EPS；


# Air780E产品手册

| 模块名称 | 适用区域         | 频段                                           | 封装尺寸          |
| -------- | ---------------- | ---------------------------------------------- | ----------------- |
| Air780E  | 中国/印度/东南亚 | TDD：B34/B38/B39/B40/B41<br />FDD：B1/B3/B5/B8 | 17.7\*15.8\*2.3mm |

## 模块硬件资料

| 资料简介           | 相关链接                                                     |
| ------------------ | ------------------------------------------------------------ |
| 低功耗             | [Air780E低功耗特性相关数据](http://docs.openluat.com/airpower/) <br /> |
| 规格书             | [Air780E_模块产品规格书_V1.0.5.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240814171731789_Air780E_模块产品规格书_V1.0.5.pdf)<br />[Air780E_Product_Specification_Sheet_V1.0.3.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240814171748402_Air780E_Product_Specification_Sheet_V1.0.3.pdf) |
| 硬件手册   | [Air780E_硬件设计手册_V1.3.5.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20241024151610963_Air780E_硬件设计手册_V1.3.5.pdf)<br />[Air780E_Hardware_Design_Manual_V1.2.4.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240819170438346_Air780E_Hardware_Design_Manual_V1.2.4.pdf)<br />[Air780E开机GPIO引脚电平变化](https://doc.openluat.com/article/4996)<br />[Air780E_GPIO_table_20240812.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240813172012124_Air780E&Air780EG&Air780EX&Air700E_GPIO_table_20240812.pdf)<br />[Air780E&amp;Air780ET&amp;Air780EP的管脚对照表.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240701144747559_Air780E&Air780ET&Air780EP的管脚对照表.pdf) |
| 原理图及PCB封装    | [Air780E_AT_PADS_Decal_V20241026](file/Air780E_AT_PADS_Decal_V20241026.zip){:target="_blank"} <br />[Air780E_LuaOS_PADS_Decal_V20241026](file/Air780E_LuaOS_PADS_Decal_V20241026.zip){:target="_blank"} |
| 参考设计原理图     | [Air780E用于AT使用方式时的参考设计V20241025(PADS)](file/Air780E用于AT使用方式时的参考设计V20241025.sch){:target="_blank"}<br />[Air780E用于AT使用方式时的参考设计V20241025(PDF)](file/Air780E用于AT使用方式时的参考设计V20241025.pdf){:target="_blank"}<br />[Air780E用于LuatOS使用方式时的参考设计V20241025(PADS)](file/Air780E用于LuatOS使用方式时的参考设计V20241025.sch){:target="_blank"}<br />[Air780E用于LuatOS使用方式时的参考设计V20241025(PDF)](file/Air780E用于LuatOS使用方式时的参考设计V20241025.pdf){:target="_blank"} |
| 开发板相关资料     | [开发板Core_Air780E使用说明V1.0.5.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240419155721583_开发板Core_Air780E使用说明V1.0.5.pdf)<br />[Air780E开发板原理图和PCB(立创EDA)](https://oshwhub.com/luat/evb_air780x_v1-6 "780X开发板原理图和PCB(立创EDA)")<br />[EVB_Air780X_V1.5_SCH.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20230705082334351_EVB_Air780X_V1.5_SCH.pdf)<br />[EVB_Air780X_V1.5.zip](https://cdn.openluat-luatcommunity.openluat.com/attachment/20230705082416943_EVB_Air780X_V1.5.zip)<br />[EVB_Air780X_V1.6.zip](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240513100446379_EVB_Air780X_V1.6.zip)<br />[EVB_Air780X_V1.8.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20231222160117780_EVB_Air780X_V1.8.pdf)<br />[EVB_Air780X_V1.8.zip](https://cdn.openluat-luatcommunity.openluat.com/attachment/20230329163731051_EVB_Air780X_V1.8.zip)（兼容780EX，780EG,780E模块） |
| 低功耗全功能开发板 | [Air780E_IO_V2.1.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240913104512513_Air780E_IO_V2.1.pdf)<br />[开发板EVB-Air780E-IO使用说明V1.2.0.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20231009103600243_开发板EVB-Air780E-IO使用说明V1.2.0.pdf)<br />[Air780F_IO_V2.1_设计文件_20240521.rar](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240913104648422_Air780F_IO_V2.1_设计文件_20240521.rar) |

## 模块外形

| 正面                                                                                                          | 反面                                                                                                            |
| ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| ![undefined](https://cdn.openluat-luatcommunity.openluat.com/images/20230509102332246_Air780E面图.PNG "undefined") | ![undefined](https://cdn.openluat-luatcommunity.openluat.com/images/20230509102406420_Air780E背面图.PNG "undefined") |

## 模块固件版本

[AT固件版本](https://docs.openluat.com/air780e/at/firmware/)

[LuatOS二次开发sdk和demo](https://docs.openluat.com/air780e/luatos/firmware/)

## 认证证书

### CCC 证书

- [Air780E_CCC中文证书(2023).pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20230601135402627_Air780E_CCC中文证书(2023).pdf)
- [Air780E_CCC英文证书(2023).pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20230601135417547_Air780E_CCC英文证书(2023).pdf)

### 入网许可证

- [Air780E入网许可证-2023.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20231222165428617_Air780E入网许可证-2023.pdf)

### SRRC 证书

- [Air780E型号核准证.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20230221104159741_Air780E%E5%9E%8B%E5%8F%B7%E6%A0%B8%E5%87%86%E8%AF%81.pdf)

### ROHS 证书

- [Air780E-ROHS证书.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20230313092434185_Air780E-ROHS%E8%AF%81%E4%B9%A6.pdf)
