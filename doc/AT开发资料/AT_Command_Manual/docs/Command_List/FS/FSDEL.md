## 删除文件：AT+FSDEL

语法规则：

| 命令类型 | 语法                  | 返回              |
| -------- | --------------------- | ----------------- |
| 设置命令 | `AT+FSDEL=<filename>` | OK<br>或<br>ERROR |
| 查询命令 | AT+FSDEL=?            | OK<br>或<br>ERROR |

 

参数定义：

| 参数         | 定义   | 取值 | 对取值的说明                           |
| ------------ | ------ | ---- | -------------------------------------- |
| `<filename>` | 文件名 |      | 字符串型，不用加双引号，不超过64个字节 |
