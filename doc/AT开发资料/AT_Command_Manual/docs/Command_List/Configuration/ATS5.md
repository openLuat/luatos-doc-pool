## 设置命令行编辑字符：ATS5

此命令设置删除命令行先前字符的字符。

语法规则：

| 命令类型 | 语法       | 返回         |
| -------- | ---------- | ------------ |
| 设置命令 | `ATS5=<n>` | OK           |
| 查询命令 | ATS5?      | `<n>` <br>OK |

 

参数定义：

| 参数  | 定义                  | 取值 | 对取值的说明                         |
| ----- | --------------------- | ---- | ------------------------------------ |
| `<n>` | 指令行编辑符的ASCII值 | 8    | 缺省值：8(对应ASCII字符`<BS>`后退符) |

 

举例：

| 命令（→） /  返回（←） | 实例     | 解释和说明                           |
| ---------------------- | -------- | ------------------------------------ |
| →                      | ATS5?    | 查询当前指令行编辑字符               |
| ←                      | 8 <br>OK | 当前指令行编辑字符为BackSpace 后退符 |
