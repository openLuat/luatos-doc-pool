## 发送DTMF音：AT+VTS

DTMF(Double Tone Multiple Frequency，双音多频)，用来在电话建立以后拨打分机号码或自动语音服务。

语法规则：

| 命令类型 | 语法                       | 返回                                                         |
| -------- | -------------------------- | ------------------------------------------------------------ |
| 设置命令 | AT+VTS=<dtmf>[,<duration>] | 通话中发送成功，返回：<br>OK <br>未建立通话时发送，返回：<br>ERROR 其他错误，返回：<br>+CME ERROR: <err> |
| 测试指令 | AT+VTS=?                   | +VTS:(0-9,#,*,A-D),(1-10) <br>OK                             |

 

参数定义：

| 参数       | 定义     | 取值 | 对取值的说明                                                 |
| ---------- | -------- | ---- | ------------------------------------------------------------ |
| <dtmf>     | 单个DTMF |      | 单个 ASCII 字符，不需要双引号""。范围如下0-9, #,*, A,B,C,D。DTMF持续时间定义如下： <br>如果AT+VTS=<dtmf>则持续时间通过命令+VTD 来设置；<br>如果AT+VTS=<dtmf>,<duration>则持续时间通过<duration>定义 |
| <duration> | 持续时间 | 1~10 | tone的持续时间，以1/10秒为单位。                             |

 

举例：

| 命令（→）/返回（←） | 实例                             | 解释和说明                       |
| ------------------- | -------------------------------- | -------------------------------- |
| ->                  | AT+VTS=?                         |                                  |
| <-                  | +VTS:(0-9,#,*,A-D),(1-10) <br>OK |                                  |
| ->                  | ATD10086                         | 电话呼叫号码10086                |
| <-                  | OK                               |                                  |
| ->                  | AT+VTS=1                         | 拨通后 发送选择语音服务中的1服务 |
| <-                  | OK                               |                                  |
