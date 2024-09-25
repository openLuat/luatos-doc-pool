## 设置网络模式：AT^SYSCONFIG

本命令设置系统模式，GSM/WCDMA接入顺序，漫游和业务域特征。

语法规则：

| 命令类型 | 语法                                               | 返回                                                     |
| -------- | -------------------------------------------------- | -------------------------------------------------------- |
| 设置命令 | `AT^SYSCONFIG=<mode>,<acqorder>,<roam>,<srvdoman>` | OK                                                       |
| 查询命令 | AT^SYSCONFIG?                                      | `^SYSCONFIG:<mode>,<acqorder>,<roam>,<srvdomain>` <br>OK |

 

参数定义：

| 参数          | 定义         | 取值 | 对取值的说明                |
| ------------- | ------------ | ---- | --------------------------- |
| `<mode>`      | 网络模式     | 2    | Automatic selection         |
|               |              | 13   | GSM ONLY                    |
|               |              | 14   | WCDMA ONLY                  |
|               |              | 15   | TD-SCDMA ONLY               |
|               |              | 16   | LTE+UTRAN+GSM               |
| `<acqorder>`  | 网络接入顺序 | 0    | Automatic                   |
|               |              | 1    | GSM first, then UTRAN       |
|               |              | 2    | UTRAN first ,then GSM       |
|               |              | 3    | LTE first,then GSM or UTRAN |
| `<roam>`      | 漫游支持     | 0    | roaming disabled            |
|               |              | 1    | roaming enabled             |
|               |              | 2    | No Change                   |
| `<srvdomain>` | 域设置       | 0    | CS_ONLY                     |
|               |              | 1    | PS_ONLY                     |
|               |              | 2    | CS_PS                       |
|               |              | 3    | ANY                         |
|               |              | 4    | No Change                   |
