@[TOC]

# uart
uart支持
## uart.on (id, event, callback)

uart 与虚拟 AT 交互接口

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|串口号|1表示串口1，2表示串口2，uart.ATC表示虚拟AT口|
|event|string|串口事件|"receive"表示串口收到数据，注意：使用uart.setup配置串口时，第6个参数设置为nil或者0，收到数据时，才会产生"receive"事件"sent"表示串口数据发送完成，注意：使用uart.setup配置串口时，第7个参数设置为1，调用uart.write接口发送数据之后，才会产生"sent"事件|
|function|number|可选参数，默认为nil，callback 串口事件的处理函数||

**返回值**

无

**例子**

```lua
  uart.on(1,"receive",rcvFnc)
  uart.on(1,"sent",sentFnc)

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1935 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2201 "示例")

---



## uart.setup( id, baud, databits, parity, stopbits,[msgmode],[txDoneReport],[flowcontrol],[priority])

uart初始化配置

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|串口号|1(UART1),2(UART2),3(UART3),0x81(USB)|
|baud|number|波特率|可选1200，2400，4800，9600，10400，14400，19200，28800，38400，57600，115200，230400，460800，921600|
|databits|number|数据位|只有一个取值8|
|parity|number|校验位|取值uart.PAR_EVEN, uart.PAR_ODD或uart.PAR_NONE|
|stopbits|number|停止位|取值uart.STOP_1，uart.STOP_2|
|msgmode|number|0 或者默认 - 消息通知，1 - 无消息上报需要用户主动轮询|0/1|
|txDoneReport|number|txdone消息上报开关|0：关闭，1：打开|
|flowcontrol|number|硬流控功能|0：关闭(默认)，1：打开|
|priority|number|uart rx优先级|0：慢(默认)，1：快|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number| 串口的真实波特率||

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1935 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2201 "示例")

---



## uart.set_rs485_oe(id, io[, level] [, timeUs] [, mode])

485转向控制

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|串口号|1(UART1),2(UART2),3(UART3),0x81(USB)|
|io|number|GPIO值|pio.Pxx|
|level|number|输出使能电平有效值，默认1，配置为1时表示高电平发送，配置为0时表示低电平发送| 1/0|
|timeUs|number|485 oe转向延迟时间,单位US，缺省时为0延迟5个当前波特率的时钟时间||
|mode|number|485 oe转向模式选择，默认0。 配置为1时表示使用定时器控制，可以使转向时间小于100us(timeUs最小值为1)| 1/0|

**返回值**

无

**例子**

```lua
--[[
uart.setup(UART_ID,115200,8,uart.PAR_NONE,uart.STOP_1,nil,1) --必须先使用setup，并且最后一个参数是1（打开发送完成后的通知功能）
uart.set_rs485_oe(UART_ID, pio.P2_0) --仅4G 0013版本之后支持
当mode=1时
uart.set_rs485_oe(UART_ID, pio.P2_0,1,1,1)
使用定时器进行转向控制，所以timeUs最小值为1。由于误差的存在，所以设置timeUs范围在（1--20），才能保证转向时间小于100us。
]]

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1935 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2201 "示例")

---



## uart.close(id)

关闭uart串口

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|串口号|1(UART1),2(UART2),3(UART3),0x81(USB)|

**返回值**

无
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1935 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2201 "示例")

---



## uart.write( id, data1, [data2], ...[datan] )

向串口写字符串或者整型数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|串口号|1(UART1),2(UART2),3(UART3),0x81(USB)|
|data1|number/string|第一个字符串或8位整型数据||
|data2|number/string|第二个字符串或8位整型数据||
|datan|number/string|第n个字符串或8位整型数据||

**返回值**

无
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1935 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2201 "示例")

---



## uart.read( id, format)

从串口读取字符串

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|串口号|1(UART1),2(UART2),3(UART3),0x81(USB)|
|format|number/char|*l：读取到结束字符\n或者阻塞发送*n：读取整型数据*s：读取到空格字符数字，number类型：只读取number长度的数据||

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|string/string|串口读出到的数据||

**例子**

```lua
[[
-- number类型的数字：表示读取指定长度字节的数据
--     如果缓冲区中没有数据，则返回空字符串，返回值为string类型
--     如果缓冲区中的数据长度小于等于要读取的数据长度，则返回缓冲区中的所有数据，返回值为string类型
--     如果缓冲区中的数据长度大于要读取的数据长度，则返回要读取的长度的数据，返回值为string类型
-- string类型的*l：  表示读取到换行符\n
--     如果缓冲区中没有数据，则返回空字符串，返回值为string类型
--     如果缓冲区中的数据没有\n，则返回缓冲区中的所有数据，返回值为string类型
--     如果缓冲区中的数据有\n，则返回到\n结束的所有数据（包括\n），返回值为string类型
-- string类型的*n：  表示读取整型数据
--     如果缓冲区中没有数据，则返回0，返回值为number类型
--     如果缓冲区中的第一个字节的数据不是+、-、数字，则返回0，返回值为number类型
--     如果缓冲区中的前几个字节满足整型数据格式[+-]%d+，则按照最长匹配返回数据，返回值为number类型
-- string类型的*s：  表示读取到空格字符
--     如果缓冲区中没有数据，则返回空字符串，返回值为string类型
--     如果缓冲区中的数据没有空格，则返回缓冲区中的所有数据，返回值为string类型
--     如果缓冲区中的数据有空格，则返回到空格结束的所有数据（不包括空格），返回值为string类型
]]

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1935 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2201 "示例")

---

## uart.getchar()

从串口读取单字符

- 语法

  `str = uart.getchar( id )`

- 参数

  | 参数        | 释义                      |取值范围|
  | ----------- | ------------------------- | ----|
  | id          | 串口号|1-3,0x81(USB)    |

- 返回值

  串口读出来的字符

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1935 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2201 "示例")

------



