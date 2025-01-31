## 读取MAC地址：AT+MIFIMAC

MAC地址也叫物理地址、硬件地址，由网络设备制造商生产时烧录在网卡(Network lnterface Card)的[EPROM](https://baike.baidu.com/item/EPROM/1690813)(一种闪存芯片，通常可以通过程序擦写)。它存储的是传输数据时真正赖以标识发出数据的电脑和接收数据的主机的地址。

语法规则：

| 命令类型  | 语法         | 返回                    |
| --------- | ------------ | ----------------------- |
| 读MAC地址 | AT+MIFIMAC=R | `+MIFIMAC: <mac>`<br>OK |

 

参数定义：

| 参数    | 定义    | 取值 | 对取值的说明 |
| ------- | ------- | ---- | ------------ |
| `<mac>` | MAC地址 |      |              |

 

举例：

| 命令（→）/返回（←） | 实例                               | 解释和说明 |
| ------------------- | ---------------------------------- | ---------- |
| →                   | AT+MIFIMAC=R                       | 读MAC地址  |
| ←                   | +MIFIMAC: 4a:24:83:99:84:34<br> OK |            |
