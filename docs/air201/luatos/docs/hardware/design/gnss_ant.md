# GNSS天线调试

建议一般直接找天线厂家帮忙挑选和适配天线。目前Air201板子上只能使用无源天线。

天线作为GPS设备中最重要的接收器件，它起到的作用就像是人的“耳朵”，是将卫星发送下来的电磁波能量变换成电子器件可解析的电流。因此天线的性能好坏将直接关系到GPS整机的产品性能。

GPS天线的种类：从安装方式上分为外置天线和内置天线；供电方式上分为有源天线和无源天线;从极化方式上分为垂直极化和圆极化.

## 无源天线在我们产品上的使用建议

- 我们的GPS模块上均内置18dBm增益的GPS LNA，可以直接将陶瓷介质的无源天线焊接在模块GPS_ANT PIN脚处使用。 产品布局的时候，GPS陶瓷天线朝上摆放；模块可以放到PCB的另一面。这样就可以做到GPS_ANT PIN到天线焊盘走线尽可能短。
- 匹配电路；如果天线焊盘离模块的GPS_ANT PIN脚很近，那么可以不预留匹配电路。如果由于结构等其他原因造成GPS天线远离模块GPS_ANT PIN，那么建议预留pi型匹配电路。模块 GPS_ANT PIN到GPS天线焊盘之间走线必须做50欧姆特性阻抗控制；如果是多层板，建议阻抗线走L1层，L2层镂空参考L3的地。2层板走线线宽可以参考GSM天线部分走线线宽。
- 天线下方不要走线并做漏铜处理做天线的反射面；
- 天线周边不要有干扰源，特别是DCDC等器件；另外周边也不要有比GPS天线高的金属器件：如下图：

## GPS天线选型建议

1. 在终端结构空间容许，能够统一保证GPS天线面朝上的安装使用状态；并且周边没有大的金属物件遮挡的情况下，建议使用GPS陶瓷天线，在空间容许的情况下尽量选择大尺寸的陶瓷天线。
2. 在不能保证终端使用状态，且空间受限：比如手机，带定位功能的胸牌；建议使用FPC天线
3. 在明确终端安装环境恶劣，并且对GPS性能有较高要求的；建议使用GPS有源天线
4. 在不能保证产品安装使用状态，但是空间不受限制，也可以选择类似于GSM的外置棒状天线。

## 对天线厂家的要求

1. VSWR：GPS天线电压驻波比一般要求调到1.5左右.
2. Efficiency：效率一般要求在40%左右
3. Average Gain：平均增益要求在-0.5dB
4. OTA：一般天线厂大多不具备GPS 天线OTA测试环境，天线调试好后可以以实际测试数据做标准来衡量；一般我们GPS实测时要求是：可用于定位卫星颗数大于6颗以上，最强的信号在45 dB/Hz左右，要有3颗卫星信号大于40 dB/Hz。

## GPS天线厂家选择

国内能自行生产GPS陶瓷天线的厂家主要是艾福电子通讯有限公司、嘉兴佳利电子、佳邦电子、嘉康电子等厂家。但是多数天线厂都是可以完成GPS天线的调试的，只是生产时会外包给其他具有独立陶瓷粉末配方和烧制工艺的厂家。

我们合作过的GPS天线厂家有：

苏州迅合德通讯 联系人：常爱进13913050523

浙江嘉兴佳利电子 联系人：钟雪文15618568209