## 在工程模式下查询GSM/UMTS/LTE信息：AT+EEMGINFO

语法规则：

| 命令类型 | 语法         | 返回                                                         |
| -------- | ------------ | ------------------------------------------------------------ |
| 查询命令 | AT+EEMGINFO? | ``+EEMGINFO:<state>,<nw_type> `<br>OK <br>`+EEMLTESVC:<info>`<br>`+EEMLTEINTRA:<info>`<br>`+EEMLTEINTER:<info>` |

 

参数定义:

| 参数      | 定义         | 取值 | 解释           |
| --------- | ------------ | ---- | -------------- |
| `<state>` | MT state     | 0    | Idle状态       |
|           |              | 1    | Dedicated 状态 |
|           |              | 2    | PS PTM 状态    |
|           |              | 3    | 有效状态       |
| <nw_type> | network type | 0    | GSM            |
|           |              | 1    | UMTS           |
|           |              | 2    | LTE            |
