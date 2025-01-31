## SIM卡切换：AT+SIMCROSS

单卡状态：

​	如果只有SIM0接口上插入SIM卡时，模块会去读取SIM0接口的卡信息去注册网络；

​	如果只有SIM1接口上插入SIM卡时，需要通过手动输入AT+SIMCROSS这个指令将位置切换为SIM1后，模块才	能读取到SIM1接口的卡信息然后去注册网络；

双卡状态：

​	如果SIM0接口和SIM1接口如果同时插入了SIM卡，默认会使用SIM0接口上的SIM卡，此时可通过AT+SIMCROSS这个指令切换为SIM1接口上的SIM卡；

无卡状态：

​	如果SIM0接口和SIM1接口上都没有插入SIM卡时，则会报错:未插入SIM卡；

 

语法规则：

| 命令类型 | 语法                                                         | 返回                              |
| -------- | ------------------------------------------------------------ | --------------------------------- |
| 设置命令 | `AT+SIMCROSS=<id>`                                           | OK                                |
| 查询命令 | AT+SIMCROSS?                                                 | `+SIMCROSS:<id>`<br> OK           |
| 测试命令 | AT+SIMCROSS=?                                                | `+SIMCROSS:(<id>取值范围)` <br>OK |
| 注意事项 | 本命令关机保存，但是需重启生效<br>EC618需要进飞行模式下进行卡切换（进入飞行模式（AT+CFUN=0），切换卡，退出飞行模式AT+CFUN=1） |                                   |

 

参数定义:

| 参数   | 定义    | 取值 | 对取值的说明       |
| ------ | ------- | ---- | ------------------ |
| `<id>` | SIM No. | 0    | SIM卡0             |
|        |         | 1    | SIM卡1或内置贴片卡 |

 

举例：

| 命令（→）/返回（←） | 实例               | 解释和说明               |
| ------------------- | ------------------ | ------------------------ |
| →                   | AT+SIMCROSS?       |                          |
| ←                   | +SIMCROSS:0 <br>OK | SIM卡位置为0             |
| →                   | AT+SIMCROSS=1      | 切换成内置贴片卡或SIM卡1 |
| ←                   | OK                 |                          |

