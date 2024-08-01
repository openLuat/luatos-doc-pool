## 显示WIFISCAN扫描数量的设置指令：AT+WIFISCANCOUNT

**注：本命令EC618平台系列模块（Air780E系列）软件版本=V1144版本支持**

语法规则：

| 命令类型 | 语法                    | 返回                          | 说明 |
| -------- | ----------------------- | ----------------------------- | ---- |
| 设置命令 | AT+WIFISCANCOUNT=<mode> | OK                            |      |
| 查询命令 | AT+WIFISCANCOUNT?       | +WIFISCANCOUNT: <mode> <br>OK |      |

 

| 参数   | 定义                     | 取值 | 对取值的说明 |
| ------ | ------------------------ | ---- | ------------ |
| <mode> | 是否显示WIFISCAN扫描数量 | 0    | 不显示       |
| 1      | 显示                     |      |              |

 

举例:

| 命令（→）/返回（←） | 实例                                                         | 解释和说明               |
| ------------------- | ------------------------------------------------------------ | ------------------------ |
| →                   | AT+WIFISCANCOUNT=1                                           | 设置显示WIFISCAN扫描数量 |
| ←                   | OK                                                           |                          |
| →                   | AT+WIFISCAN                                                  | 非阻塞方式查询所有信道   |
| ←                   | OK <br>+WIFISCAN COUNT: 10 <br>+WIFISCAN: "22:f2:2c:6f:55:9a",-42,11 <br>+WIFISCAN: "18:f2:2c:6f:55:9a",-42,11 <br>+WIFISCAN: "c8:bf:4c:ce:d4:fe",-53,11 <br>+WIFISCAN: "a6:f9:33:3a:45:e4",-60,1<br> +WIFISCAN: "c0:cc:42:f0:6b:b0",-84,4 <br>+WIFISCAN: "78:13:e0:d2:75:e6",-84,5 <br>+WIFISCAN: "48:7d:2e:5c:66:a4",-84,13<br> +WIFISCAN: "e0:38:3f:dc:17:f0",-85,7 <br>+WIFISCAN: "4c:e9:e4:1c:ba:88",-91,1 <br>+WIFISCAN: "34:f7:16:19:6f:a2",-96,11 |                          |
