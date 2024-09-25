## 打开CSQ主动上报：AT\*CSQ

上报的URC（CSQ indicators）如下所列：

 

**`+CSQ:<rssi>,<ber>`**

**`+CESQ:<rxlev>,<ber>,<rscp>,<ecno>,<rsrq>,<rsrp>`**

**`*CESQ: <rxlev>,<ber>,<rscp>,<ecno>,<rsrq>,<rsrp>,<sinr>`**

 

语法规则：

| 命令类型 | 语法         | 返回                                      |
| -------- | ------------ | ----------------------------------------- |
| 设置命令 | `AT*CSQ=<n>` | OK                                        |
| 查询命令 | AT*CSQ?      | `*CSQ:<n>`<br> OK                         |
| 测试命令 | AT*CSQ=?     | `*CSQ =  (list of supported <n>s)` <br>OK |

 

参数定义:

| 参数                                  | 定义                         | 取值 | 对取值的说明 |
| ------------------------------------- | ---------------------------- | ---- | ------------ |
| `<n>`                                 |                              | 0    | 关闭主动上报 |
|                                       |                              | 1    | 打开主动上报 |
| `<rssi>,<ber>`                        | 请参阅 AT+CSQ                |      |              |
| `<rxlev>,<rscp>,<ecno>,<rsrq>,<rsrp>` | 请参阅 AT+CESQ               |      |              |
| `<sinr>`                              | 信号与干扰加噪声比（信噪比） |      |              |
