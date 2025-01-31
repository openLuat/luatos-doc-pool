# 4G天线调试

建议一般直接找天线厂家帮忙挑选和适配天线。

## 频率范围：

确定天线的支持频率范围，首先确认模块支持的频段有哪些，不同的频段对应不同的频率，目前我们4G模块所支持的频率范围大致800Mhz-2700Mhz，所以满足合宙CAT 1模块的4G天线的频率需要覆盖到800Mhz-2700Mhz；

## 增益：

在输入功率相等的条件下，实际天线与理想的辐射单元在空间同一点处所产生的信号的功率密度之比。

一般选择5dbi的增益就能够用，设备环境较差的时候可以选择更高增益的天线；

## 驻波比：

全称为电压驻波比，又名VSWR和SWR，指驻波波腹电压与波谷电压幅度之比，又称为驻波系数、驻波比。驻波比等于1时，表示馈线和天线的阻抗完全匹配，此时高频能量全部被天线辐射出去，没有能量的反射损耗；驻波比为无穷大时，表示全反射，能量完全没有辐射出去。

驻波比的值为1~∞，4G天线一般选用驻波比≤1.5的最好，理想的驻波比值为1，目前还没有能够达到驻波比为1的情况；

## 辐射模式：

有全向和定向之分；

全向天线：水平方向图上表现为360°都均匀辐射，也就是平常所说的无方向性；

定向天线：在水平方向图上表现为一定角度范围辐射，也就是平常所说的有方向性；

目前大多数区域的基站覆盖都是比较密集的，所以选择全向天线比较多，在基站比较少，且可以确定基站方位的时候，可以推荐选择定向天线；

## 天线的极化方式：

天线辐射时形成的电场强度方向；

目前4G基站的天线大多数采取的是双极化的方式，所以UE端多采用线极化的方式；

原因为：一比较好实现，二线极化好匹配；

## 常见天线形式：

目前天线的形式有多种样式： 棒状天线、船桨天线、吸盘天线、FPC天线，可根据产品的使用场景和其本身的大小进行选择；

## 馈线长度的问题：

这个根据产品的情况，选择合适的长短，不易过长，尽量减少损耗。

## 阻抗控制：

模块的ANT PAD输出端的阻抗是50Ω，所以选择同样的50Ω阻抗的天线，利于输入输出达到匹配状态。