## 获取Sim类型：AT\*EUICC

获知SIM卡类型。

 

语法规则：

| 命令类型 | 语法      | 返回                 |
| -------- | --------- | -------------------- |
| 查询命令 | AT*EUICC? | `*EUICC: <n> `<br>OK |

 

参数定义:

| 参数  | 定义          | 取值 | 对取值的说明 |
| ----- | ------------- | ---- | ------------ |
| `<n>` | SIM card type | 0    | SIM          |
|       |               | 1    | USIM         |
