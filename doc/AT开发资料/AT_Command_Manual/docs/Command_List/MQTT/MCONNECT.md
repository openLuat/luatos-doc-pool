## 客户端向服务器请求会话连接：AT+MCONNECT

语法规则：

| 命令类型 | 语法                                                         | 返回                               | 说明                                                         |
| -------- | ------------------------------------------------------------ | ---------------------------------- | ------------------------------------------------------------ |
| 设置命令 | `AT+MCONNECT=<clean_session>,<keepalive>`                    | OK                                 | 设置成功                                                     |
| 测试命令 | AT+MCONNECT=?                                                | `+MCONNECT:(0-1),(1-65535)` <br>OK | 测试命令的返回的是`<clean_session>`和`<keepalive>`的取值范围 |
| URC      | 设置命令设置成功，返回OK后，后续会根据连接情况自动上报URC：<br>如果连接成功则返回：CONNACK OK<br>如果连接失败则返回：ERROR |                                    |                                                              |

 

参数定义：

| 参数              | 定义     | 取值    | 对取值的说明                                                 |
| ----------------- | -------- | ------- | ------------------------------------------------------------ |
| `<clean_session>` |          | 0       | 服务端必须基于当前会话（使用客户端标识符识别） 的状态恢复与客户端的通信。 如果没有与这个客户端标识符关联的会话， 服务端必须创建一个新的会话。在连接断开之后， 当连接断开后， 客户端和服务端必须保存会话信息 [MQTT-3.1.2-4]。当清理会话标志为 0的会话连接断开之后，服务端必须将之后的 QoS 1 和 QoS 2 级别的消息保存为会话状态的一部分， 如果这些消息匹配断开连接时客户端的任何订阅 [MQTT-3.1.2-5]。服务端也可以保存满足相同条件的 QoS 0 级别的消息。 |
|                   |          | 1       | client和server都会抛弃以前的会话，建立一个新的会话。会话持续时间与网络连接持续时间一样长。与此会话相关的会话状态数据在后序的会话中不被采用。 |
| `<keepalive>`     | 保活时间 | 1-65535 | 时间单位：秒<br>设备端在保活时间内至少需要发送一次报文，包括PING请求。<br>如果服务器端在保活时间内未接收到任何报文，会断开连接，设备端需要发起重连。<br>建议取值在300s以上。 |
