# 一、讨论的边界

   本文讨论的功耗的场景边界是：

   模组绝大多数时间深度休眠状态， 几个小时醒过来一次，
   
   向服务器端发送报文，然后继续深度休眠。

   由于不存在TCP链接， 所以服务器端无法主动向终端发送消息。

   服务器只能等待终端主动通信， 再通过回复消息，对终端做控制和参数配置。

   所以无法实现对终端的实时控制。

   对于实时在线的场景， 不在本文描述；

   对于大数据量长时间连续通信的场景，也不在本文描述。


# 二、测试条件

    - 1， 供电电压：      3.8V；
    - 2， IO电平设置：   1.8V；
    - 3， 固件版本： 截止到2024年9月30日的最新LuatOS固件；
    - 4， 测试服务器：    airtest.openluat.com, "2901"，回环测试；
    - 5， 每次终端醒来通信的内容：  
         10字节字符串： "0123456789"，    循环10次，一共 100字节；
    - 6，  驻网频段与驻网小区ID：   B3频段，小区id：  153708387；
        其他频段的功耗，会略有差异，但是对于小数据量的传输场景来说，差异不会特别的大。
    - 7，  UART1串口波特率：         9600；
    - 8，  信号强度：         实网环境， RSRP[-86，-88]之间；
    - 9， 测试硬件：    合宙Air780E/Air780EQ/Air780EP/Air780EPS/Air700ECQ，通用全IO开发板，2.1版本。
          删除了可能产生耗电的外设，比如 LED状态灯。
 

# 三、影响实网功耗的主要网络因素

在非实时在线，深度休眠，定时醒来通信的通信场景下，影响功耗的因素，按照影响力从大到小排序， 分别是：

## 1，  定时醒来的间隔时间

    深度休眠的功耗非常低，只有几个微安。

    醒来通信的功耗相比深度休眠，功耗高了至少百倍。

    所以，醒过来的频次越低，总体功耗就越低。

    醒来的频次越高， 总体功耗就越高。


## 2， 实网信号强度
    终端的4G信号强度越好， 说明跟基站通信越容易。
    
    因此终端就不需要用特别大的功率和基站通信，因此功耗就会比较低。

    信号强度越差， 终端就需要用比较大的功率和基站通信，发射的功耗就会上升很多。

    本文的测试数据， 是基于信号强度良好的情况下测试出来的，
    
    这符合中国的4G信号的普遍情况。

    如果你的设备是在地下室，偏远地区这些信号比较弱的场景， 
    
    那么实际的设备的功耗，会上升一些。

    定时醒来的越频繁， 信号强度对功耗的影响越大；

    如果一天只醒来一次， 功耗的消耗主要是休眠的功耗消耗，信号强度对功耗的影响就没那么大了。


# 四、各个模组的深度休眠定时醒来通信的功耗数据

    以下的数据，醒来发送数据的时间间隔按照 1小时，4小时，12小时的测试数据来呈现。

## 1， 780EPS
    34 微安，  26 微安，7.5微安 毫安；
 转换成毫瓦为：
    0.13 毫瓦，  0.1毫瓦，  0.29毫瓦；

## 2，780EP
    待测试；

## 3，780E和780EX
    待测试；

## 4,  780EQ，700ECQ，700EAQ，700EMQ，780EEN，700EEU
    待测试；




