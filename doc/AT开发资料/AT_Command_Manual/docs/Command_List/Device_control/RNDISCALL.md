## RNDIS/ECM功能开关：AT+RNDISCALL

**注：本命EC618平台系列模块（Air780E系列）软件版本>=V1140版本支持**

语法规则：

| 命令类型 | 语法                  | 返回                                   |
| -------- | --------------------- | -------------------------------------- |
| 设置命令 | `AT+RNDISCALL=<mode>` | OK                                     |
| 读取命令 | AT+RNDISCALL?         | `+RNDISCALL:<mode>`<br> OK             |
| 测试命令 | AT+RNDISCALL=?        | +RNDISCALL:(0-disable;1-enable)<br> OK |

 

参数定义：

| 参数     | 定义     | 取值 | 对取值的说明                |
| -------- | -------- | ---- | --------------------------- |
| `<mode>` | 工作模式 | 0    | 关闭RNDIS/ECM网卡，重启生效 |
|          |          | 1    | 打开RNDIS/ECM网卡，重启生效 |
