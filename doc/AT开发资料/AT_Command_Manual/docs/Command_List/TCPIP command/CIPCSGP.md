## 设置为CSD或GPRS连接模式：AT+CIPCSGP

语法规则：

| 命令类型 | 语法                                   | 返回和说明                                                   |
| -------- | -------------------------------------- | ------------------------------------------------------------ |
| 设置命令 | AT+CIPCSGP=<mode>,[<apn>,<user>,<pwd>] | OK                                                           |
| 查询命令 | AT+CIPCSGP?                            | +CIPCSGP: <mode>, <apn>, <user>, <pwd> <br>OK                |
| 测试命令 | AT+CIPCSGP=?                           | +CIPCSGP: 0-CSD,DIAL NUMBER,USER NAME,PASSWORD,RATE(0-3)<br>+CIPCSGP: 1-GPRS,APN,USER NAME,PASSWORD <br>OK |

 

参数定义：

 

| 参数                 | 定义            | 取值 | 对取值的说明                 |
| -------------------- | --------------- | ---- | ---------------------------- |
| <mode>               | 无线连接模式    | 1    | GPRS连接                     |
|                      |                 | 2    | CSD连接                      |
| GPRS下要设置的参数： |                 |      |                              |
| <apn>                | GPRS 接入点名称 | -    | 字符串参数(字符串需要加引号) |
| <username>           | GPRS 用户名     | -    | 字符串参数(字符串需要加引号) |
| <password>           | GPRS 密码       | -    | 字符串参数(字符串需要加引号) |
