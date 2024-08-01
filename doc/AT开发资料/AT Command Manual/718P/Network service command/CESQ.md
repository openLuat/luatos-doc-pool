## 查询信号质量（扩展）：AT+CESQ

执行命令返回接收信号的各个参数。如果当前的服务小区不是一个GERAN小区，<rxlev>和<rxqual >设置为99；如果当前服务小区不是一个UTRA FDD或UTRA TDD小区，<rscp>设置为255；如果当前服务小区不是一个UTRA FDD小区，<ecno>设置为255；如果当前服务小区不是一个E-UTRA小区，<rsrq>和<rsrp>设置为255。

语法规则：

| 命令类型 | 语法    | 返回                                                        |
| -------- | ------- | ----------------------------------------------------------- |
| 执行命令 | AT+CESQ | +CESQ: <rxlev>,<rxqual >,<rscp>,<ecno>,<rsrq>,<rsrp><br> OK |

 

参数定义:

| 参数      | 定义                                                         | 取值 | 对取值的说明                                 |
| --------- | ------------------------------------------------------------ | ---- | -------------------------------------------- |
| <rxlev>   | 接收信号强度(received signal strength level ; 3GPP TS 45.008 subclause 8.1.4)；整数型 | 0    | rssi < -110 dBm                              |
|           |                                                              | 1    | -110 dBm £ rssi < -109 dBm                   |
|           |                                                              | 2    | -109 dBm £ rssi < -108 dBm                   |
|           |                                                              | …    | …                                            |
|           |                                                              | 61   | -50 dBm £ rssi < -49 dBm                     |
|           |                                                              | 62   | -49 dBm £ rssi < -48 dBm                     |
|           |                                                              | 63   | -48 dBm £ rssi                               |
|           |                                                              | …    | …                                            |
|           |                                                              | 99   | 未知或不可测                                 |
| <rxqual > | 接收信号质量（请参考3GPP TS 45.008 subclause 8.2.4中表格R中XQUAL值）；整数型 | 0    | BER	<0.2 %	Assumed value =	0.14 %   |
|           |                                                              | 1    | 0.2 %<BER<0.4 %Assumed value =	0.28 %     |
|           |                                                              | 2    | 0.4 %<BER<0.8 %	Assumed value =	0.57 % |
|           |                                                              | 3    | 0.8 %<BER<1.6 %	Assumed value =	1.13 % |
|           |                                                              | 4    | 1.6 %<BER<3.2 %	Assumed value =	2.26 % |
|           |                                                              | 5    | 3.2 %<BER<6.4 %	Assumed value =	4.53 % |
|           |                                                              | 6    | 6.4 %<BER<12.8 %Assumed value =	9.05 %    |
|           |                                                              | 7    | 12.8 %<BER	Assumed value =	18.10 %     |
|           |                                                              | 99   | 未知或不可测                                 |
| <rscp>    | received signal code power(请参考3GPP TS 25.133subclause 9.1.1.3 和 3GPP TS 25.123subclause 9.1.1.1.3) ；整数型 | 0    | rscp < -120 dBm                              |
|           |                                                              | 1    | -120 dBm £ rscp < -119 dBm                   |
|           |                                                              | 2    | -119 dBm £ rscp < -118 dBm                   |
|           |                                                              | …    | …                                            |
|           |                                                              | 94   | -27 dBm £ rscp < -26 dBm                     |
|           |                                                              | 95   | -26 dBm £ rscp < -25 dBm                     |
|           |                                                              | 96   | -25 dBm £ rscp                               |
|           |                                                              | 255  | 未知或不可测                                 |
| <ecno>    | ratio of the received energy per PN chip to the total received power spectral density (see 3GPP TS 25.133 )；整数型 | 0    | Ec/Io < -24 dB                               |
|           |                                                              | 1    | -24 dB £ Ec/Io < -23.5 dB                    |
|           |                                                              | 2    | -23.5 dB £ Ec/Io < -23 dB                    |
|           |                                                              | …    | …                                            |
|           |                                                              | 47   | -1 dB £ Ec/Io < -0.5 dB                      |
|           |                                                              | 48   | -0.5 dB £ Ec/Io < 0 dB                       |
|           |                                                              | 49   | 0 dB £ Ec/Io                                 |
|           |                                                              | 255  | 未知或不可测                                 |
| <rsrq>    | reference signal received quality (请参考3GPP TS 36.133 subclause 9.1.7) ；整数型 | 0    | rsrq < -19.5 dB                              |
|           |                                                              | 1    | -19.5 dB £ rsrq < -19 dB                     |
|           |                                                              | 2    | -19 dB £ rsrq < -18.5 dB                     |
|           |                                                              | …    | …                                            |
|           |                                                              | 32   | -4 dB £ rsrq < -3.5 dB                       |
|           |                                                              | 33   | -3.5 dB £ rsrq < -3 dB                       |
|           |                                                              | 34   | -3 dB £ rsrq                                 |
|           |                                                              | 255  | 未知或不可测                                 |
| <rsrp>    | reference signal received power (请参考3GPP TS 36.133 subclause 9.1.4) ；整数型 | 0    | rsrp < -140 dBm                              |
|           |                                                              | 1    | -140 dBm £ rsrp < -139 dBm                   |
|           |                                                              | 2    | -139 dBm £ rsrp < -138 dBm                   |
|           |                                                              | …    | …                                            |
|           |                                                              | 95   | -46 dBm £ rsrp < -45 dBm                     |
|           |                                                              | 96   | -45 dBm £ rsrp < -44 dBm                     |
|           |                                                              | 97   | -44 dBm £ rsrp                               |
|           |                                                              | 255  | 未知或不可测                                 |
