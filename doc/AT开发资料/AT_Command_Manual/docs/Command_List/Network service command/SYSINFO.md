## 查询当前的系统信息：AT^SYSINFO

本命令查询当前的系统信息，例如：服务状态，业务域，漫游状态等。

语法规则：

| 命令类型 | 语法       | 返回                                                         |
| -------- | ---------- | ------------------------------------------------------------ |
| 执行命名 | AT^SYSINFO | ^SYSINFO:<srv_status>,<srv_domain>,<roam_status>,<sys_mode>,<sim_state>,<sys_submode><br> OK |

 

参数定义：

| 参数          | 定义       | 取值 | 对取值的说明            |
| ------------- | ---------- | ---- | ----------------------- |
| <srv_status>  | 服务状态   | 0    | no service              |
|               |            | 1    | restricted service      |
|               |            | 2    | valid service           |
|               |            | 3    | restricted area service |
|               |            | 4    | power service           |
| <srv_domain>  | 业务域     | 0    | no service              |
|               |            | 1    | CS only                 |
|               |            | 2    | PS only                 |
|               |            | 3    | CS and PS               |
| <roam_status> | 漫游状态   | 0    | no roaming              |
|               |            | 1    | roaming                 |
| <sys_mode>    | 网络模式   | 0    | no service              |
|               |            | 1    | reserved                |
|               |            | 2    | reserved                |
|               |            | 3    | GSM/GPRS                |
|               |            | 4    | WCDMA                   |
|               |            | 5    | TD_SCDMA                |
|               |            | 17   | LTE                     |
| <sim_state>   | SIM卡状态  | 0    | sim卡无效               |
|               |            | 1    | sim卡有效               |
|               |            | 255  | SIM未插入或PIN码未解锁  |
| <sys_submode> | 网络子模式 | 0    | GSM                     |
|               |            | 1    | GSM Compact             |
|               |            | 2    | UTRAN                   |
|               |            | 3    | GSM w/EGPRS             |
|               |            | 4    | UTRAN w/HSDPA           |
|               |            | 5    | UTRAN w/HSUPA           |
|               |            | 6    | UTRAN w/HSDPA and HSUPA |
|               |            | 7    | E-UTRAN                 |
