## 保存FTP应用上下文：AT+FTPSCONT

语法规则：

| 命令类型 | 语法         | 返回                                                         | 说明                                                      |
| -------- | ------------ | ------------------------------------------------------------ | --------------------------------------------------------- |
| 查询命令 | AT+FTPSCONT? | +FTPSCONT: <value><br>+FTPSERV: <value><br>+FTPPORT: <value><br>+FTPUN: <value><br>+FTPPW: <value><br>+FTPCID: <value><br>+FTPMODE: <value><br>+FTPTYPE: <value><br>+FTPPUTOPT: <value><br>+FTPREST: <value><br>+FTPGETNAME: <value><br>+FTPGETPATH: <value><br>+FTPPUTNAME: <value><br>+FTPPUTPATH: <value><br>+FTPTIMEOUT: <value> <br>OK |                                                           |
| 执行命令 | AT+FTPSCONT  | OK                                                           | 将FTP上下文保存，等模块重启后，将自动载入上下文参数并生效 |
