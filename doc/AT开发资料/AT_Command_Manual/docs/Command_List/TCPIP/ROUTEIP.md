## 修改RNDIS网卡网关IP地址：AT+ROUTEIP

**注：本命令EC618平台系列模块（Air780E系列）软件版本>=V1140版本支持**

语法规则：

| 命令类型 | 语法              | 返回          |
| -------- | ----------------- | ------------- |
| 设置命令 | `AT+ROUTEIP=<ip>` | OK            |
| 查询命令 | AT+ROUTEIP?       | `<ip> `<br>OK |
| 测试命令 | AT+ROUTEIP=?      | OK            |

 

参数定义：

| 参数   | 定义                      | 取值 | 对取值的说明                                |
| ------ | ------------------------- | ---- | ------------------------------------------- |
| `<ip>` | 当前的RNDIS网卡网关IP地址 |      | IP地址，双引号可加可不加，只支持192.168.X.2 |
