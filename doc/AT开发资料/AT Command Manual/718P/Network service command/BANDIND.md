## 查询当前工作频段：AT*BANDIND

设置命令可以打开频段自动上报。

查询命令返回当前的工作频段。

 

语法规则：

| 命令类型 | 语法                                                         | 返回                                |
| -------- | ------------------------------------------------------------ | ----------------------------------- |
| 设置命令 | AT*BANDIND[=<n>]                                             | OK                                  |
| 查询命令 | AT*BANDIND?                                                  | *BANDIND: <n>[,<band>,<AcT>] <br>OK |
| 测试命令 | AT*BANDIND=?                                                 | *BANDIND: (0,1) <br>OK              |
| URC      | <n>=1而且频段改变时，自动上报 URC: ***BANDIND: <band>, <Act>** |                                     |

 

参数定义：

| 参数   | 定义                                                  | 取值 | 对取值的说明  |                   |
| ------ | ----------------------------------------------------- | ---- | ------------- | ----------------- |
| <n>    | <n>=1而且频段改变时，自动上报 *BANDIND: <band>, <Act> | 0    | disable       |                   |
|        |                                                       | 1    | enable        |                   |
| <act>  | Access Technology，接入机制                           | 0    | GSM           |                   |
|        |                                                       | 1    | GSM Compact   |                   |
|        |                                                       | 2    | UTRAN         |                   |
|        |                                                       | 3    | GSM w/EGPRS   |                   |
|        |                                                       | 4    | UTRAN w/HSDPA |                   |
|        |                                                       | 5    | UTRAN w/HSUPA |                   |
|        |                                                       | 6    | UTRAN w/HSPA  |                   |
|        |                                                       | 7    | E-UTRAN       |                   |
|        |                                                       | 8    | UTRAN HSPA+   |                   |
| <band> | 频段                                                  | 0    | PGSM 900      | 当<act>=0/1/3     |
|        |                                                       | 1    | DCS GSM 1800  |                   |
|        |                                                       | 2    | PCS GSM 1900  |                   |
|        |                                                       | 3    | EGSM 900      |                   |
|        |                                                       | 4    | GSM 450       |                   |
|        |                                                       | 5    | GSM 480       |                   |
|        |                                                       | 6    | GSM 850       |                   |
|        |                                                       | 0    | UMTS BAND1    | 当<act>=2/4/5/6/8 |
|        |                                                       | 1    | UMTS BAND2    |                   |
|        |                                                       | 2    | UMTS BAND3    |                   |
|        |                                                       | 3    | UMTS BAND4    |                   |
|        |                                                       | 4    | UMTS BAND5    |                   |
|        |                                                       | 5    | UMTS BAND6    |                   |
|        |                                                       | 6    | UMTS BAND7    |                   |
|        |                                                       | 7    | UMTS BAND8    |                   |
|        |                                                       | 8    | UMTS BAND9    |                   |
|        |                                                       | 9    | UMTS BAND10   |                   |
|        |                                                       | 10   | UMTS BAND11   |                   |
|        |                                                       | 11   | UMTS BAND12   |                   |
|        |                                                       | 12   | UMTS BAND13   |                   |
|        |                                                       | 13   | UMTS BAND14   |                   |
|        |                                                       | 14   | UMTS BAND15   |                   |
|        |                                                       | 15   | UMTS BAND16   |                   |
|        |                                                       | 16   | UMTS BAND17   |                   |
|        |                                                       | 17   | UMTS BAND18   |                   |
|        |                                                       | 18   | UMTS BAND19   |                   |
|        |                                                       | 1    | LTE BAND 1    | 当<act>=7         |
|        |                                                       | 2    | LTE BAND 2    |                   |
|        |                                                       | 3    | LTE BAND 3    |                   |
|        |                                                       | 4    | LTE BAND 4    |                   |
|        |                                                       | 5    | LTE BAND 5    |                   |
|        |                                                       | 6    | LTE BAND 6    |                   |
|        |                                                       | 7    | LTE BAND 7    |                   |
|        |                                                       | 8    | LTE BAND 8    |                   |
|        |                                                       | 9    | LTE BAND 9    |                   |
|        |                                                       | 10   | LTE BAND 10   |                   |
|        |                                                       | 11   | LTE BAND 11   |                   |
|        |                                                       | 12   | LTE BAND 12   |                   |
|        |                                                       | 13   | LTE BAND 13   |                   |
|        |                                                       | 14   | LTE BAND 14   |                   |
|        |                                                       | 15   | LTE BAND 15   |                   |
|        |                                                       | 16   | LTE BAND 16   |                   |
|        |                                                       | 17   | LTE BAND 17   |                   |
|        |                                                       | 18   | LTE BAND 18   |                   |
|        |                                                       | 19   | LTE BAND 19   |                   |
|        |                                                       | 20   | LTE BAND 20   |                   |
|        |                                                       | 21   | LTE BAND 21   |                   |
|        |                                                       | 22   | LTE BAND 22   |                   |
|        |                                                       | 23   | LTE BAND 23   |                   |
|        |                                                       | 24   | LTE BAND 24   |                   |
|        |                                                       | 25   | LTE BAND 25   |                   |
|        |                                                       | 26   | LTE BAND 26   |                   |
|        |                                                       | 27   | LTE BAND 27   |                   |
|        |                                                       | 28   | LTE BAND 28   |                   |
|        |                                                       | 29   | LTE BAND 29   |                   |
|        |                                                       | 30   | LTE BAND 30   |                   |
|        |                                                       | 31   | LTE BAND 31   |                   |
|        |                                                       | 32   | LTE BAND 32   |                   |
|        |                                                       | 33   | LTE BAND 33   |                   |
|        |                                                       | 34   | LTE BAND 34   |                   |
|        |                                                       | 35   | LTE BAND 35   |                   |
|        |                                                       | 36   | LTE BAND 36   |                   |
|        |                                                       | 37   | LTE BAND 37   |                   |
|        |                                                       | 38   | LTE BAND 38   |                   |
|        |                                                       | 39   | LTE BAND 39   |                   |
|        |                                                       | 40   | LTE BAND 40   |                   |
|        |                                                       | 41   | LTE BAND 41   |                   |
