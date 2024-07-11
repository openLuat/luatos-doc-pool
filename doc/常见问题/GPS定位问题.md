## 1. 哪些模块支持GPS定位
>目前：Air820，Air780EG支持
>其余模块例如Air724UG如果要支持GPS，可以采用Air724UG+Air530方案，使用LuatOS-Air二次开发实现。

## 2. GPS天线如何设计
>参考：[LuatOS-Air模块GPS天线设计建议](https://doc.openluat.com/wiki/21?wiki_page_id=2614 "LuatOS-Air模块GPS天线设计建议")

## 3. 如何测试信噪比
> 参考：http://oldask.openluat.com/article/963

## 4. 724模块如何输出原始NMEA数据
>添加如下代码：
>gps.setNmeaMode(2, function(nmeaItem) log.info("nmea", nmeaItem) end)

## 5. GPS无信号、信号弱、定位失败
>1、使用Air820官方开发板+客户固件对比测试：如果Air820官方开发板也存在同样问题，重点检查以下步骤中的环境问题和软件问题；如果Air820没问题，重点检查一下步骤中的硬件问题。<br>
>2、不能在室内测试，必须到室外测试；如果只能在室内测试，可以淘宝搜索“gps信号转发器”，但是不可用于rtk定位测试。为什么不能在室内测试，参考：http://oldask.openluat.com/article/66。<br>
>3、检查gps天线
  1) 必须使用gps天线，普通的gsm、蓝牙、wifi、433等天线不支持gps定位。
  2) gps陶瓷天线，如果大板和陶瓷天线面积都比较小，一定要去正规天线厂调试。如果面积都比较大，实在没条件调试，可以不去调试。
  3) 天线朝上，面向天空，天线上方不能有金属物质，不能有较厚的遮挡物（例如几厘米的塑料盒子肯定不行，几毫米的塑料盒子可以）。
  4) 如果用的是有源天线，测量下供电电压是否正常。<br>
4、gps设备不要放在笔记本键盘等有电磁干扰的设备上。<br>
5、参考：http://oldask.openluat.com/article/963 ，确认下信噪比以及天线是否受到干扰。<br>
6、Air530，Air530Z模块串口的模特率是9600，Air530H模块gps串口的波特率是115200，使用时注意区分，[Air530Z、Air530H 和 Air530的兼容攻略](https://doc.openluat.com/share_article/6UTqAlMKxnfmV "Air530Z、Air530H 和 Air530的兼容攻略")。<br>
7、参考问题4输出原始NMEA数据，如果无数据输出，用示波器测量一下GPS_RXD上是否有数据。
8、天线设计不合规。

## 6. 如何支持秒定位（GPS定位慢）
>LuatOS-Air开发方式：require"agps"即可。
>
>AT开发方式：AT+CGNSPWR=1 打开 gps 就会跑秒定位的流程。

## 7. 什么是GPS的冷启动、温启动、热启动
>参考：http://oldask.openluat.com/article/32

## 8. GPS定位经纬度不准确
>1、使用Air820官方开发板+客户固件对比测试：如果Air820官方开发板也存在同样问题，重点检查以下步骤中的环境问题和软件问题；如果Air820没问题，重点检查一下步骤中的硬件问题。<br>
>2、坐标没有纠偏，参考：http://www.openluat.com/GPS-Offset.html 进行纠偏处理。<br>
>3、周围有比较高的障碍物，会导致定位误差。<br>
>3、在开阔地带，正常情况下定位精度只能做到5米。<br>
>3、不能在室内测试，必须到室外测试；如果只能在室内测试，可以淘宝搜索“gps信号转发器”，但是不可用于rtk定位测试。<br>
>6、信噪比低或者天线受到干扰，参考 http://oldask.openluat.com/article/963 和 [LuatOS-Air模块GPS天线设计建议](https://doc.openluat.com/wiki/21?wiki_page_id=2614 "LuatOS-Air模块GPS天线设计建议") 做硬件优化。<br>

## 9. GPS模块内部有LNA吗
> 有LNA低噪声放大器。

## 10. GPS定位海拔不准确
>卫星距离地球有33000km，所以高程差几十米很正常。几十米相对于33000km，真的不算什么。如果要求精确，一般个人建议：
>1、找基准点。
>2、rtk。
>3、气压传感器/海拔表。
>那么，放在飞机上会更准吗？就方向角、经纬度、速度而言，会；但是，气压不会准，因为舱内有增压装置。但是海拔而言，飞机一般用雷达、声纳，以及皮托管（气压）、或者陀螺仪（惯导）。

## 11. 可视卫星、可用卫星有什么区别
>可视卫星是当前区域，接收条件良好情况下，应该可以收到卫星信号的卫星。
>可用卫星是当前已经收到信号并正在使用参与定位的卫星。

## 12. GGA和RMC应该用哪个
>视具体情况而定，建议用gga，信息相对更全面。

## 12. 如何解读NMEA报文每个字段的含义
>参考：http://www.openluat.com/Product/file/800/NMEA数据格式说明.docx

## 14. 是否支持ntrip协议
>不支持，可以使用LuatOS-Air开发方式自行对接ntrip协议。
>ntrip协议参考：https://blog.csdn.net/hanford/article/details/53025771

## 15. 已知两个经纬度，如何计算间距？
>可以使用如下函数（但是注意，没有考虑到地球曲率，计算结果存在误差。建议使用高德地图等提供的api在服务端计算。
>-[[
>函数名：diffofloc
>功能 ：计算两对经纬度之间的直线距离（近似值）
>参数:
>  latti1：纬度1（度格式，例如"31.12345"度）
> longti1：经度1（度格式）
> latti2：纬度2（度格式）
> longti2：经度2（度格式）
> typ：距离类型
>返回值：typ如果为true，返回的是直线距离(单位米)的平方和；否则返回的是直线距离(单位米)
>]]
```
function diffofloc(latti1, longti1, latti2, longti2,typ) --typ=true:返回a+b ; 否则是平方和

     local I1,I2,R1,R2,diff,d

     I1,R1=smatch(latti1,"(%d+)%.(%d+)")

     I2,R2=smatch(latti2,"(%d+)%.(%d+)")

     if not I1 or not I2 or not R1 or not R2 then

              return 0

     end



     R1 = I1 .. ssub(R1,1,5)

     R2 = I2 .. ssub(R2,1,5)

     d = tonumber(R1)-tonumber(R2)

     d = (d*111-(d*111%100))/100

     if typ == true then

              diff =  (d>0 and d or (-d))

     else

              diff = d * d

     end

             

     I1,R1=smatch(longti1,"(%d+)%.(%d+)")

     I2,R2=smatch(longti2,"(%d+)%.(%d+)")

     if not I1 or not I2 or not R1 or not R2 then

              return 0

     end



     R1 = I1 .. ssub(R1,1,5)

     R2 = I2 .. ssub(R2,1,5)

     d = tonumber(R1)-tonumber(R2)

     if typ == true then

              diff =  diff + (d>0 and d or (-d))

     else

              diff =  diff + d*d

     end

     --diff =  diff + d*d

     print("all diff:", diff)

     return diff
end
```

## 16. 如何解决静态漂移
>通常是因为卫星、接收器、天线等多重因素导致，建议服务端从算法层面去过滤这种漂移；设备端也可以通过振动传感器判断静止状态、wifi判断wifi变化率较低、基站变化率较低等多种手段，较少不必要的GPS位置上报来过滤漂移。

## 17. 做车载定位器，进入隧道没办法定位怎么办
>使用基站定位。

## 18. 能否用于制作人员定位器、定位手表
>可以。

## 19 . 使用LuatOS-Air版本FLOAT底层，能否实现坐标转换（WGS84~GCJ02）加偏/纠偏
>建议在服务器端实现。因为加偏算法是很复杂的浮点运算，模块输出结果可能和实际情况有差；如果需要更高的加偏结果，可以使用百度/高德等地图提供的api。

## 20. 哪些地图使用的是GCJ02坐标系
>高德、腾讯；（百度是GCJ02又转换为BD09，所以不能直接使用GCJ02。

## 21、哪些地图可以直接查看WGS84定位
> bing maps（非bing地图），google maps（非gogole 地图）。

## 22. 车载使用时需要天线引出到车顶上吗
>1、挡风玻璃如果没有贴膜或者贴了不含金属材料的膜，可以放在挡风玻璃下，但是gps信号会有一定衰减，在万不得已的情况下，可以放在挡风玻璃下，最好再实际测试确认一下。
>2、挡风玻璃如果贴了含有金属材料的膜，则不能放在挡风玻璃下，必须将天线到车顶。

## 23. 可视卫星、可用卫星有什么区别
>可视卫星是当前区域，接收条件良好情况下，应该可以收到卫星信号的卫星。
>可用卫星是当前已经收到信号并正在使用参与定位的卫星。
