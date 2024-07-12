@[TOC](目录名称)
### MSG


| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| rtos.WAIT_MSG_TIMEOUT| 无 |等待消息超时 |

### timer

| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| rtos.MSG_TIMER| time_id：定时器ID值|定时器 |

### UART

| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| rtos.MSG_UART_RXDATA| uart_id：串口ID值 |UART接收数据 |
| rtos.MSG_UART_TX_DONE| uart_id：串口ID值 |UART发送数据 |

### keypad

| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| rtos.MSG_KEYPAD| 1、pressed:按键状态<br> 2、key_matrix_row:  键盘行坐标<br> 3、key_matrix_col: 键盘列坐标 |按键状态相关参数 |

### gpio中断

| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| rtos.MSG_INT|1、int_id：中断id <br>2、int_resnum： |gpio中断状态 |

### PMD

| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| rtos.MSG_PMD| 1、present：电池状态 <br>2、voltage：电池电压值 <br>3、level：电池电量状态 <br>4、charger：充电状态 <br>5、state：充电器状态 | pmd状态上报 |

### AUDIO

| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| rtos.MSG_AUDIO| 播放状态<br>play_end_ind：播放结束<br>play_error_ind：播放错误 |audio播放状态消息上报 |
| rtos.MSG_RECORD| 录音状态<br>record_end_ind：录音结束<br>record_error_ind：录音错误  |audio录音状态消息上报 |
| rtos.MSG_STREAM_RECORD| wait_read_len：流录音长度 |audio流录音长度消息上报 |
| rtos.MSG_HEADSET| 1、type：耳机类型 <br>2、param：耳机参数  |耳机状态消息上报 |

### RTMP

| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| rtos.MSG_RTMP| 1、result：rtmp状态 <br>2、result_code：rtmp状态码|RTMP播放结果消息上报 |

### ALARM

| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| rtos.MSG_ALARM| 无 |闹钟消息上报 |

### TTS

| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
|rtos.MSG_TTSPLY_STATUS| ttsply_status_ind：tts状态 |tts状态上报 |
| rtos.MSG_TTSPLY_ERROR| ttsply_error_ind：tts错误 |tts错误上报 |

### socket

| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| rtos.MSG_SOCK_CONN_CNF| 1、socket_index：socket id值<br>2、result：socket连接状态码 |socket连接结果 |
|rtos.MSG_SOCK_SEND_CNF| 1、socket_index：socket id值<br>2、result：发送数据状态码<br>3、send_len： 发送数据长度 |数据发送结果 |
|rtos.MSG_SOCK_RECV_IND|  1、socket_index：socket id值<br>2、result：接收数据状态码<br>3、recv_len： 接收数据长度  |接收到数据 |
|rtos.MSG_SOCK_CLOSE_CNF| 1、socket_index：socket id值<br>2、result：关闭socket回复状态码  |主动断开连接 |
|rtos.MSG_SOCK_CLOSE_IND| 1、socket_index：socket id值<br>2、result：主动关闭socket状态码  |被动断开连接 |

### zbar

| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| rtos.MSG_ZBAR| 1、result：zbar状态码<br>2、type：zbar类型<br>3、data：接收zbar数据 | zbar数据上报 |


### WIFI

| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| rtos.MSG_WIFI| 1、cnt：扫描wifi个数<br>2、info：扫描到的wifi信息 | 扫描到的wifi数据上报 |

### BLUETOOTH

| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| rtos.MSG_BLUETOOTH| msg：蓝牙状态 | 蓝牙状态上报 |


