## URC)系统模式：^MODE

显示系统模式有改变。

 

语法规则：

| URC                           |
| ----------------------------- |
| ^MODE:<SysMainMode>,<SysMode> |

 

参数定义：

| 参数                    | 取值   | 解释                                      |
| ----------------------- | ------ | ----------------------------------------- |
| <SysMainMode>,<SysMode> | 17,17  | TD LTE capabilities  （4G）               |
|                         | 5/15,8 | 3G only  (3G)                             |
|                         | 5/15,7 | 3G, HSDPA, and HSDPA capabilities  (3G)   |
|                         | 5/15,6 | 3G and HSUPA capabilities  (3G)           |
|                         | 5/15,5 | 3G and HSDPA capabilities  (3G)           |
|                         | 3,3    | GSM, GPRS, and EGPRS capabilities  （2G） |
|                         | 3,2    | GSM and GPRS capabilities  (2G)           |
|                         | 3,1    | GSM only  (2G)                            |
|                         | 0,0    | 无服务                                    |
