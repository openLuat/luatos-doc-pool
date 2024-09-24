## SIM实体卡，虚拟卡切换：AT+ECSIMCFG

**注：本命令EC618平台系列模块（Air780E系列）软件版本LSVS软件版本支持**

 

语法规则：

| 命令类型 | 语法                                                         | 返回                                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 设置命令 | `AT+ECSIMCFG="SoftSim",<mode>`                               | OK                                                           |
| 查询命令 | AT+ECSIMCFG?                                                 | `+ECSIMCFG: "SimPowerSave",<mode>`<br>`+ECSIMCFG: "SimPowerSave",<mode>`<br>`+ECSIMCFG: "SimPresenceDetect",<mode>`<br>`+ECSIMCFG: "SimSlot",<mode>`<br>`+ECSIMCFG: "SoftSim",<mode>`<br>OK |
| 测试命令 | AT+ECSIMCFG=?                                                | +ECSIMCFG: (list of supported) <br>OK                        |
| 注意事项 | 需要进飞行模式下进行卡切换（进入飞行模式（AT+CFUN=0），切换卡，退出飞行模式AT+CFUN=1） |                                                              |

 

参数定义:

| 参数              | 定义             | 取值 | 对取值的说明 |
| ----------------- | ---------------- | ---- | ------------ |
| `<mode>(SoftSim)` | 是否切换为虚拟卡 | 0    | 切换为实体卡 |
|                   |                  | 1    | 切换为虚拟卡 |

 

举例：

| 命令（→）/返回（←） | 实例                    | 解释和说明     |
| ------------------- | ----------------------- | -------------- |
| →                   | AT+CFUN=0               | 切换为飞行模式 |
| ←                   | OK                      |                |
| →                   | AT+ECSIMCFG="SoftSim",1 | 切换为虚拟卡   |
| ←                   | OK                      |                |
| →                   | AT+CFUN=1               | 退出飞行模式   |
| ←                   | OK                      |                |

