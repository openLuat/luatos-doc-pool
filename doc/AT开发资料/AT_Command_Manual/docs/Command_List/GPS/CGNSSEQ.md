## 定义NMEA解析 ：AT+\*******\*CGNSSEQ

语法规则：

| 命令类型 | 语法                  | 返回                               |
| -------- | --------------------- | ---------------------------------- |
| 设置命令 | AT+CGNSSEQ=＂ｓｔｒ＂ | OK                                 |
|          |                       | `+CME ERROR:<err>`                 |
| 查询命令 | AT+CGNSSEQ?           | +CGNSSEQ: %s <br>OK                |
| 测试命令 | AT+CGNSSEQ=?          | +CGNSSEQ: (GGA,GSA,RMC,GSV) <br>OK |

参数定义：

| 参数   | 定义   | 取值 | 对取值的说明 |
| ------ | ------ | ---- | ------------ |
| ｓｔｒ | 字符串 |      | 字符串类型   |
