## 修改来电URC上报格式：AT+CRC

此设置命令可以修改来电时“RING”的URC上报格式

语法规则：

| 命令类型 | 语法          | 返回                                         |
| -------- | ------------- | -------------------------------------------- |
| 设置命令 | AT+CRC=<mode> | OK <br>其他错误，返回：<br>+CME ERROR: <err> |
| 查询指令 | AT+CRC?       | +CRC: <mode> <br>OK                          |
| 测试指令 | AT+CRC=?      | +CRC: (0,1) <br>OK                           |

注：该指令设置参数不会掉电保存

 

参数定义：

| 参数   | 定义         | 取值 | 对取值的说明                             |
| ------ | ------------ | ---- | ---------------------------------------- |
| <mode> | 来电上报格式 | 0    | 不启用扩展格式，来电URC为（RING）        |
|        |              | 1    | 启用扩展格式，来电URC为（+CRING: VOICE） |
