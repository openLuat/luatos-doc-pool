## 通过UART口设置睡眠唤醒：AT+CSCLK

通过串口使模块进入睡眠的先决条件是：不接USB口。

语法规则：

| 命令类型 | 语法           | 返回和说明                                |
| -------- | -------------- | ----------------------------------------- |
| 设置命令 | `AT+CSCLK=<n>` | OK                                        |
| 查询命令 | AT+CSCLK?      | `+CSCLK: <n>` <br>OK                      |
| 测试命令 | AT+CSCLK=?     | `+CSCLK: (list of supported <n>s)`<br> OK |

 

参数定义：

| 参数  | 定义     | 取值 | 对取值的说明                                                 |
| ----- | -------- | ---- | ------------------------------------------------------------ |
| `<n>` | 睡眠设置 | 0    | 关闭模块睡眠功能。模块无法进入睡眠状态。缺省值。             |
|       |          | 1    | 睡眠模式1。由模块MAIN_DTR脚控制是否进入睡眠。<br>当MAIN_DTR拉高（缺省为高，因为有内部上拉），设置AT+CSCLK=1，没有其他中断产生（GPIO、来电、来短信等），模块将自动进入睡眠模式1。在这种模式下，模块仍能接收来自网络的呼叫和短消息。<br>当模块处于睡眠模式1时，可以通过以下的几种方法唤醒模块。<br>模块接收到外部中断信号；<br>模块接收到语音或数据呼叫；<br>模块接收到短消息（SMS）；<br>串口接收到AT命令；<br>拉低AP_WAKEUP_MODULE引脚大概50ms<br>注意：模块收到语音、数据呼叫或短消息后会有URC上报 |
|       |          | 2    | 睡眠模式2。设置AT+CSCLK=2后，模块会连续监测串口数据，如果模块的串口上没有数据输入，并且没有其他中断产生（GPIO，来电，来短信，来数据等），缺省5秒后模块会自动进入睡眠模式2（**注：睡眠模式2情况下，AP_WAKEUP_MODULE电平对模块睡眠唤醒功能无影响，这个是跟休眠模式1最主要的区别**）。在这种模式下，模块仍能接收来自网络的呼叫和短消息。 <br>当模块处于睡眠模式2时，可以通过以下的几种方法唤醒模块。<br>模块接收到外部中断信号；<br>模块接收到语音或数据呼叫；<br>模块接收到短消息（SMS）；<br>串口接收到AT命令。 |
|       |          | 3    | 睡眠模式3(***\*超低功耗\****)。<br>设置AT+CSCLK=3后，模块会连续监测串口数据，如果模块的串口上没有数据输入，并且没有其他中断产生（GPIO，来电，来短信，来数据等），缺省5秒后模块会自动进入睡眠模式3（**注：睡眠模式3情况下，AP_WAKEUP_MODULE电平对模块睡眠唤醒功能无影响，这个是跟休眠模式1最主要的区别**）。在这种模式下，模块仍能接收来自网络的呼叫和短消息。 <br>当模块处于睡眠模式3时，可以通过以下的几种方法唤醒模块。<br>模块接收到外部中断信号；<br>模块接收到语音或数据呼叫；<br>模块接收到短消息（SMS）；<br>串口接收到AT命令。 <br>**注EC618平台系列模块（Air780E系列）软件版本>=V1026支持。** |

 

举例：

| 命令（→）/  返回（←）                                | 实例          | 解释和说明                                                   |
| ---------------------------------------------------- | ------------- | ------------------------------------------------------------ |
| **睡眠唤醒应用实例1**                                |               |                                                              |
| →                                                    | AT+CSCLK=2    | 设置为睡眠模式2。在这种睡眠模式下，以下情况同时满足时，模块进入睡眠。 <br >模块在AT口无输入<br>没有URC上报（包括没有来电，没有短信，没有收到服务器发来的数据等）<br>无GPIO中断 |
| ←                                                    | OK            |                                                              |
| →                                                    | AT+WAKETIM?   | 查询进入睡眠的时间                                           |
| ←                                                    | +WAKETIM:1 OK | 查询结果为1秒钟。1秒钟是CSCLK设置睡眠后缺省进入睡眠的时间    |
| →                                                    | AT+WAKETIM=8  | 如果需要修改进入睡眠的时间，可以通过WAKETIM来设置，例如改为8（一般情况下不需要设置） |
| ←                                                    | OK            |                                                              |
|                                                      |               | 模块唤醒方式有以下几种:<br>1) 串口输入几个AT命令（一个往往唤不醒，需要多输几个）<br>2) 任意URC上报（包括来电，来短信，收到服务器发的数据等）<br>3) GPIO中断 |
| →                                                    | AT+CSCLK=0    |                                                              |
| ←                                                    | OK            | 0，设置为不允许模块睡眠                                      |
| **睡眠唤醒应用实例2**                                |               |                                                              |
| →                                                    | AT+CSCLK=1    | 设置为睡眠模式1。在这种睡眠模式下，以下情况同时满足时，模块进入睡眠。 <br>模块在AT口无输入<br>没有URC上报（包括没有来电，没有短信，没有收到服务器发来的数据等）<br>模块AP_WAKEUP_MODULE为高（AP_WAKEUP_MODULE高，是允许模块睡眠；AP_WAKEUP_MODULE低，是唤醒模块）<br>无GPIO中断 |
| ←                                                    | OK            |                                                              |
| →                                                    | AT+WAKETIM?   | 查询进入睡眠的时间                                           |
| ←                                                    | +WAKETIM:1 OK | 查询结果为1秒钟。1秒钟是CSCLK设置睡眠后缺省进入睡眠的时间    |
| →                                                    | AT+WAKETIM=8  | 如果需要修改进入睡眠的时间，可以通过WAKETIM来设置，例如改为8（一般情况下不需要设置） |
| ←                                                    | OK            |                                                              |
|                                                      |               | 模块唤醒方式有以下几种:<br>串口输入几个AT命令（一两个AT就可以了）<br>任意URC上报（包括来电，来短信，收到服务器发的数据等）GPIO中断<br>AP_WAKEUP_MODULE唤醒（AP_WAKEUP_MODULE低，唤醒；AP_WAKEUP_MODULE高，允许睡眠） |
| →                                                    | AT+CSCLK=0    |                                                              |
| ←                                                    | OK            | 0，设置为不允许模块睡眠                                      |
| **超低功耗应用实例（**用于大多数的数传业务场景**）** |               |                                                              |
| →                                                    | AT+CSCLK=3    | 设置为睡眠模式3(**超低功耗**)。在这种睡眠模式下，以下情况同时满足时，模块进入睡眠。 <br>模块在AT口无输入<br>没有URC上报（包括没有来电，没有短信，没有收到服务器发来的数据等）<br>无GPIO中断 |
| ←                                                    | OK            |                                                              |
| →                                                    | AT+WAKETIM=1  | 设置在IDL状态下等待1秒进入休眠状态                           |
| ←                                                    | OK            |                                                              |
| →                                                    | AT*RTIME=2    | 设置在数传模式下，等待2秒进入休眠状态                        |
| ←                                                    | OK            |                                                              |
|                                                      |               | 模块唤醒方式有以下几种:<br>4) 串口输入几个AT命令（一个往往唤不醒，需要多输几个）<br>5) 任意URC上报（包括来电，来短信，收到服务器发的数据等）<br>6) GPIO中断 |
| →                                                    | AT+CSCLK=0    |                                                              |
| ←                                                    | OK            | 0，设置为不允许模块睡眠                                      |
