## 远程服务器上创建文件目录：AT+FTPMKD

语法规则：

| 命令类型 | 语法                                          | 返回                        | 说明           |
| -------- | --------------------------------------------- | --------------------------- | -------------- |
| 执行命令 | AT+FTPMKD                                     | OK <br>+FTPMKD: 1,0         | 创建成功       |
|          |                                               | OK <br>`+FTPMKD: 1,<error>` | 创建失败       |
|          |                                               | `+CME ERROR: <err>`         | 如果是命令错误 |
| 测试命令 | AT+FTPMKD=?                                   | OK                          |                |
| 注意事项 | 执行命令创建的文件目录由命令AT+FTPGETPATH定义 |                             |                |

 

参数定义：

| 参数      | 定义   | 取值 | 对取值的说明                       |
| --------- | ------ | ---- | ---------------------------------- |
| `<error>` | 错误码 |      | 与AT+FTPGET命令的`<error>`定义相同 |
