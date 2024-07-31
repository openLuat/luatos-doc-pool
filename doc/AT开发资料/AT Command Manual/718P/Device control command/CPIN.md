## 输入PIN码：AT+CPIN

语法规则：

| 命令类型 | 语法                     | 返回和说明                                                   |
| -------- | ------------------------ | ------------------------------------------------------------ |
| 设置命令 | AT+CPIN=<pin>[,<newpin>] | OK<br> 说明：如果需要的PIN 是SIM PUK 或者SIM PUK2, 则需要第二个pin。<new  pin>用来取代 SIM 卡中的原有的pin。 |
| 查询命令 | AT+CPIN?                 | +CPIN: <code><br> OK                                         |
| 测试命令 | AT+CPIN=?                | OK                                                           |
| URC      | +CPIN:<code>             |                                                              |

 

参数定义：

| 参数     | 定义   | 取值        | 对取值的说明            |
| -------- | ------ | ----------- | ----------------------- |
| <pin>    | 密码   | -           | 字符串型                |
| <newpin> | 新密码 | -           | 字符串型                |
| <code>   |        | READY       | ME不再需要提供密码      |
|          |        | SIM PIN     | ME等待提供SIM卡的PIN码  |
|          |        | SIM PUK     | ME等待提供SIM卡的PUK码  |
|          |        | SIM PIN2    | ME等待提供SIM卡的PIN2码 |
|          |        | SIM PUK2    | ME等待提供SIM卡的PUK2码 |
|          |        | SIM REMOVED | SIM卡未检出             |

 

举例：

| 命令（→）/  返回（←） | 实例                  | 解释和说明                                                   |
| --------------------- | --------------------- | ------------------------------------------------------------ |
| →                     | AT+CPIN?              | 查询PIN码锁状态                                              |
| ←                     | +CPIN: READY <br>OK   | 表示PIN码锁并未开启                                          |
| →                     | AT+CLCK="SC",1,"1234" | 开启开机PIN码锁，1234是PIN码，SC表示是SIM卡                  |
| ←                     | OK                    | 返回OK后，重启模块                                           |
| ←                     | +CPIN: SIM PIN        | 重新开机后，模块会自动上报PIN码状态，SIM PIN表示开机PIN码为ON的状态（即开机需要输入PIN码） |
| →                     | AT+CPIN="1234"        | 此时需要输入PIN码                                            |
| ←                     | +CPIN: READY <br>OK   | 表示密码正确，PIN码锁解锁                                    |
| →                     | AT+CLCK="SC",2        | 查询当前的开机PIN码是否仍然开启                              |
| ←                     | +CLCK: 1 OK           | 1表示仍然有开机PIN码提示                                     |
| →                     | AT+CLCK="SC",0,"1234" | 关闭开机PIN码提示                                            |
| ←                     | OK                    | 返回OK后重新开机                                             |
| ←                     | +CPIN: READY          | 重新开机后，模块会自动上报PIN码状态，READY表示开机PIN码：OFF |
