## 设置指令行终止符：ATS3

设置指令，可设置用于AT指令行终止符，该字符能被TA识别。

语法规则：

| 命令类型 | 语法       | 返回         |
| -------- | ---------- | ------------ |
| 设置命令 | `ATS3=<n>` | OK           |
| 查询命令 | ATS3?      | `<n>` <br>OK |

 

参数定义：

| 参数  | 定义                  | 取值 | 对取值的说明                                              |
| ----- | --------------------- | ---- | --------------------------------------------------------- |
| `<n>` | 指令行终止符的ASCII值 | 13   | 缺省值：13，对应 ASCII字符为<CR>(回车符) 注：仅支持这个值 |
