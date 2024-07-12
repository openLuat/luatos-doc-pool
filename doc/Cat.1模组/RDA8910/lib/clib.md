
@[TOC]

# clib

模块功能：完善luat的c库接口

## uart.on (id, event, callback)

注册串口事件的处理函数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|id|number|串口ID，1表示串口1，2表示串口2，uart.ATC表示虚拟AT口|
|event|string|串口事件:<br>"recieve"表示串口收到数据，注意：使用uart.setup配置串口时，第6个参数设置为nil或者0，收到数据时，才会产生"receive"事件<br>"sent"表示串口数据发送完成，注意：使用uart.setup配置串口时，第7个参数设置为1，调用uart.write接口发送数据之后，才会产生"sent"事件|
|callback|function|**可选参数，默认为`nil`** 串口事件的处理函数|

* 返回值

nil

* 例子

```lua
uart.on(1,"receive",rcvFnc)
uart.on(1,"sent",sentFnc)
```

---
