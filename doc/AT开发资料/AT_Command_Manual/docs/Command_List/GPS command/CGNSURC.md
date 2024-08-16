## 打开GNSS URC上报：AT+CGNSURC

语法规则：

| 命令类型 | 语法                                                         | 返回                           |
| -------- | ------------------------------------------------------------ | ------------------------------ |
| 设置命令 | AT+CGNSURC=<period_time> <br>OK                              | OK                             |
|          |                                                              | +CME ERROR:<err>               |
| 查询命令 | AT+CGNSURC?                                                  | +CGNSURC: <period_time> <br>OK |
| 测试命令 | AT+CGNSURC=?                                                 | +CGNSURC: (0-255)  <br>OK      |
| URC      | 与AT+CGNSINF的返回格式相同：<br>+CGNSINF: <GNSS run status>,<Fix status>, <UTC date & Time>,<Latitude>,<Longitude>, <MSL Altitude>,<Speed Over Ground>, <Course Over Ground>, <Fix Mode>,<Reserved1>,<HDOP>,<PDOP>, <VDOP>,<Reserved2>,<GNSS Satellites in View>, <GNSS Satellites Used>,<GLONASS Satellites Used>,<Reserved3>,<C/N0 max>,<HPA>,<VPA> |                                |

 

参数定义：

| 参数          | 定义 | 取值  | 对取值的说明                          |
| ------------- | ---- | ----- | ------------------------------------- |
| <period_time> |      | 0     | 关闭导航数据URC上报                   |
|               |      | 1~255 | 开启导航数据URC周期上报并设置周期时间 |
