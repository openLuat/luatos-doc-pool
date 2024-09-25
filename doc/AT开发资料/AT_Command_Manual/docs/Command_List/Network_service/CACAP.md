## 查询接入机制（Access Technology）：AT^CACAP

查询命令返回当前小区的接入机制(Access Technology)。

 

语法规则：

| 命令类型 | 语法       | 返回                   |
| -------- | ---------- | ---------------------- |
| 查询命令 | AT^CACAP?  | `+CACAP: <act>`<br> OK |
| 测试命令 | AT^CACAP=? | +CACAP:(0-7) <br>OK    |

 

参数定义：

| 参数    | 定义 | 取值 | 对取值的说明  |
| ------- | ---- | ---- | ------------- |
| `<act>` |      | 0    | GSM           |
|         |      | 1    | GSM Compact   |
|         |      | 2    | UTRAN         |
|         |      | 3    | GSM w/EGPRS   |
|         |      | 4    | UTRAN w/HSDPA |
|         |      | 5    | UTRAN w/HSUPA |
|         |      | 6    | UTRAN w/HSPA  |
|         |      | 7    | E-UTRAN       |
