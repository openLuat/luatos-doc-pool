## 小区信息查询：AT+CCED

本命令可以查询本小区和最多6个临小区的信息。

语法规则：

| 命令类型 | 语法                            | 返回                                                         |
| -------- | ------------------------------- | ------------------------------------------------------------ |
| 设置命令 | AT+CCED=<mode>,<requested dump> | OK                                                           |
| 测试命令 | AT+CCED=?                       | +CCED: (list of <mode>s ),(list of <requested dump>s) <br>OK |

 

参数定义：

| 参数             | 定义     | 取值 | 对取值的说明                                                 |
| ---------------- | -------- | ---- | ------------------------------------------------------------ |
| <mode>           | 工作模式 | 0    | 一次上报                                                     |
|                  |          | 1    | 周期性上报                                                   |
|                  |          | 2    | 关闭上报                                                     |
| <requested dump> | 消息类型 | 1    | 主小区，即服务小区信息                                       |
|                  |          | 2    | 邻小区信息如果是LTE邻小区，则上报：MCC,MNC,frequency,cellid,rsrp,rsrq,tac,SrxLev,pcid如果是GSM邻小区，则上报：MCC,MNC,lac,cellid,bsic,rxlev |
|                  |          | 8    | 主小区的RSSI 指示，即Rxlev（0~31）                           |

 

举例：

|                                                              |
| ------------------------------------------------------------ |
| **<requested dump>=1，上报主小区或服务小区的信息：**<br>如果当前是LTE模式，则上报：<br>+CCED:LTE current cell:MCC,MNC,imsi,roamingFlag,bandInfo,bandwidth,dlEarfcn,cellid,rsrp,rsrq,tac,SrxLev,pcid<br>如果当前是GSM模式，则上报：<br>+CCED:GSM current cell info:MCC,MNC,lac,cellid,bsic,rxlev,RxLevSub,Arfcn <br><br>**举例：<br>一次性查询当前小区(LTE模式)**：<br>AT+CCED=0,1 <br>+CCED:LTE current cell:460,00,460045926307603,0,40,n100,39148,140542123,51,29,6334,34,351<br> OK<br><br>**一次性查询当前小区(GSM模式)：**<br>AT+CCED=0,1 <br>+CCED:GSM current cell info:460,00,18be,5045,13,63,63,6 <br>OK<br><br>**当前小区信息周期性上报（LTE模式）：**<br>AT+CCED=1,1 <br>+CCED:LTE current cell:460,00,460045926307603,0,40,n100,39148,140542123,61,31,6334,44,351 <br>OK <br><br>+CCED:LTE current cell:460,00,460045926307603,0,40,n100,39148,140542123,61,31,6334,44,351<br>+CCED:LTE current cell:460,00,460045926307603,0,40,n100,39148,140542123,61,31,6334,44,351<br>+CCED:LTE current cell:460,00,460045926307603,0,40,n100,39148,140542123,61,35,6334,44,351 <br><br>**当前小区信息周期性上报（GSM模式）：**<br>AT+CCED=1,1 <br>+CCED:GSM current cell info:460,00,18be,5045,13,61,61,6 <br>OK<br><br> +CCED:GSM current cell info:460,00,18be,5045,13,63,63,6<br>+CCED:GSM current cell info:460,00,18be,5045,13,63,63,6<br>+CCED:GSM current cell info:460,00,18be,5045,13,63,63,6<br>+CCED:GSM current cell info:460,00,18be,5045,13,63,63,6<br> |
| **<requested dump>=2，上报邻接小区的信息：<br>**如果当前是LTE模式，则上报：<br>+CCED:LTE neighbor cell: MCC,MNC,frequency,cellid,rsrp,rsrq,tac,SrxLev,pcid <br><br>如果当前是GSM模式，则上报：<br>+CCED:GSM neighbor cell info: MCC,MNC,lac,cellid,bsic,rxlev <br><br>**举例：<br>一次性查询邻接小区(LTE模式)：**<br>AT+CCED=0,2<br> +CCED:LTE neighbor cell:460,00,38950,140541985,57,24,6334,36,351<br>+CCED:LTE neighbor cell:460,00,1300,26224401,48,24,6334,27,37<br>+CCED:LTE neighbor cell:460,00,1300,26224402,43,15,6334,22,38<br>+CCED:LTE neighbor cell:460,00,38400,26224397,42,23,6334,21,191<br>+CCED:LTE neighbor cell:460,00,40936,12793923,34,15,6334,13,191<br>+CCED:LTE neighbor cell:460,00,3590,26224415,44,9,6334,27,318<br>+CCED:LTE neighbor cell:460,00,3590,26224416,47,19,6334,30,319 <br>OK<br><br>**一次性查询邻接小区(GSM模式)：**<br>AT+CCED=0,2 <br>+CCED:GSM neighbor cell info:460,00,6334,20522,31,75<br>+CCED:GSM neighbor cell info:460,00,6334,0,21,80<br>+CCED:GSM neighbor cell info:460,00,6334,20521,30,91 <br>OK<br><br> **邻接小区信息周期性上报（LTE模式）：**<br>AT+CCED=1,2 <br>+CCED:LTE neighbor cell:460,00,38950,140541985,57,24,6334,36,351<br>+CCED:LTE neighbor cell:460,00,1300,26224401,48,24,6334,27,37<br>+CCED:LTE neighbor cell:460,00,1300,26224402,43,15,6334,22,38<br>+CCED:LTE neighbor cell:460,00,38400,26224397,42,23,6334,21,191<br>+CCED:LTE neighbor cell:460,00,40936,12793923,34,15,6334,13,191<br>+CCED:LTE neighbor cell:460,00,3590,26224415,44,9,6334,27,318<br>+CCED:LTE neighbor cell:460,00,3590,26224416,47,19,6334,30,319 <br>OK <br><br>+CCED:LTE neighbor cell:460,00,38950,140541985,57,24,6334,36,351<br>+CCED:LTE neighbor cell:460,00,1300,26224401,48,24,6334,27,37<br>+CCED:LTE neighbor cell:460,00,1300,26224402,43,15,6334,22,38<br>+CCED:LTE neighbor cell:460,00,38400,26224397,42,23,6334,21,191<br>+CCED:LTE neighbor cell:460,00,40936,12793923,34,15,6334,13,191<br>+CCED:LTE neighbor cell:460,00,3590,26224415,44,9,6334,27,318<br>+CCED:LTE neighbor cell:460,00,3590,26224416,47,19,6334,30,319 <br><br>**邻接小区信息周期性上报（GSM模式）：**<br>AT+CCED=1,2<br> +CCED:GSM neighbor cell info:460,00,6334,20522,31,76<br>+CCED:GSM neighbor cell info:460,00,6334,0,21,80<br>+CCED:GSM neighbor cell info:460,00,6334,20521,30,94 <br>OK <br><br>+CCED:GSM neighbor cell info:460,00,6334,20522,31,85<br>+CCED:GSM neighbor cell info:460,00,6334,0,21,78<br>+CCED:GSM neighbor cell info:460,00,6334,20521,30,83 |
