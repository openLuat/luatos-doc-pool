## 读取基站定位（LBS）信息和时间：AT+CIPGSMLOC

语法规则：

| 命令类型 | 语法                      | 返回                                                         |
| -------- | ------------------------- | ------------------------------------------------------------ |
| 设置命令 | AT+CIPGSMLOC=<type>,<cid> | **If <type>=1:** <br>+CIPGSMLOC:<locationcode>[,<latitude>,<longitude>,<date>,<time>]  <br>OK<br> **If <type>=2:** <br>+CIPGSMLOC: <locationcode>[,<date>,<time>]  <br>OK  <br>**If error is related to ME functionality:** <br>+CME ERROR: <err> |
| 测试命令 | AT+CIPGSMLOC=?            | +CIPGSMLOC:(list of supported <type>s),(range of <cid>) <br>OK |

 

参数定义：

| 参数           | 定义                       | 取值  | 对取值的说明          |
| -------------- | -------------------------- | ----- | --------------------- |
| <type >        | 操作类型                   | 1     | 查看精度、维度和时间  |
|                |                            | 2     | 只查看时间            |
| <cid>          | as <cid> defined in +SAPBR | 1-3   |                       |
| <longitude>    | 当前经度(以度为单位)       |       | 经度(小数点后保留7位) |
| <latitude>     | 当前纬度，以度表示         |       | 纬度(小数点后保留7位) |
| <date>         | 格式为 yy/mm/dd            |       | 例如2023/11/08        |
| <time>         | 格式为 hh/mm/ss            |       | 例如15:47:26          |
| <locationcode> |                            | 0     | 成功                  |
|                |                            | 1     | 未找到数据            |
|                |                            | 6     | 参数错误              |
|                |                            | 7     | 未知错误              |
|                |                            | 404   | 未找到                |
|                |                            | 408   | 请求超时              |
|                |                            | 601   | 网络错误              |
|                |                            | 602   | 内存不足              |
|                |                            | 603   | DNS错误               |
|                |                            | 604   | 堆栈忙                |
|                |                            | 65535 | 其它错误              |

 

举例:

| 命令（→）/返回（←） | 实例                                                         | 解释和说明                                                   |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| →                   | AT+SAPBR=3,1,"CONTYPE","GPRS"                                | 设置承载类型为GPRS                                           |
| ←                   | OK                                                           |                                                              |
| →                   | AT+SAPBR=3,1,"APN",""                                        | 设置PDP承载之APN参数 模块注册网络后会从网络自动获取<apn>并激活一个PDP上下文，用于RNDIS上网使用（此<apn>可以通过AT+CGDCONT?来查询），所以输入AT+SAPBR=3,<cid>,"APN","" 即可，模块内部会按照自动获取的<apn>来设置APN |
| ←                   | OK                                                           |                                                              |
| →                   | AT+SAPBR=1,1                                                 | 激活GPRS PDP上下文                                           |
| ←                   | OK                                                           |                                                              |
| →                   | AT+SAPBR=2,1                                                 | 查询是否激活                                                 |
| ←                   | +SAPBR: 1,1,010.169.179.213 <br>OK                           | 返回中有IP地址表明激活成功                                   |
| →                   | AT+CIPGSMLOC=1,1                                             | 查询位置和时间（超时时间30S）                                |
| ←                   | +CIPGSMLOC: 0,034.7983328,114.3214505,2023/06/05,14:38:50 <br>OK |                                                              |
| →                   | AT+CIPGSMLOC=2,1                                             | 只查询时间                                                   |
| ←                   | +CIPGSMLOC: 0,2023/06/05,14:38:55<br>OK                      |                                                              |
| →                   | AT+SAPBR=0,1                                                 | 去激活PDP上下文                                              |
| ←                   | OK                                                           |                                                              |
