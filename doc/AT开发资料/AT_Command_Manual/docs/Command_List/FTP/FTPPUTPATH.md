## 设置FTP上传文件路径：AT+FTPPUTPATH

设置将文件上传到服务器后的保存目录。

语法规则：

| 命令类型 | 语法                    | 返回                         | 说明         |
| -------- | ----------------------- | ---------------------------- | ------------ |
| 设置命令 | `AT+FTPPUTPATH=<value>` | OK                           | 正常返回     |
|          |                         | ERROR                        | 输入格式有误 |
| 查询命令 | AT+FTPPUTPATH?          | `+FTPPUTPATH:<value> `<br>OK |              |
| 测试命令 | AT+FTPPUTPATH=?         | OK                           |              |

 

参数定义：

| 参数      | 定义            | 取值 | 对取值的说明                |
| --------- | --------------- | ---- | --------------------------- |
| `<value>` | FTP上传文件路径 |      | 长度不超过99的ASCII字符串。 |
