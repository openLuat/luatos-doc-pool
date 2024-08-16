## 读取GNSS信息：AT+CGNSINF

语法规则：

| 命令类型 | 语法       | 返回                                                         |
| -------- | ---------- | ------------------------------------------------------------ |
| 执行命令 | AT+CGNSINF | +CGNSINF: <GNSS run status>,<Fix status>, <UTC date & Time>,<Latitude>,<Longitude>, <MSL Altitude>,<Speed Over Ground>, <CourseOver Ground>, <Fix Mode>,<Reserved1>,<HDOP>,<PDOP>, <VDOP>,<Reserved2>,<GNSS Satellites in View>, <GNSS Satellites Used>,<GLONASS Satellites Used>,<Reserved3>,<C/N0 max>,<HPA>,<VPA> <br>OK |

 

参数定义：

| 参数                      | 定义            | 取值           | 对取值的说明                                                 |
| ------------------------- | --------------- | -------------- | ------------------------------------------------------------ |
| <GNSS run status>         | GNSS运行状态    | 0              | GNSS OFF                                                     |
|                           |                 | 1              | GNSS ON                                                      |
| <Fix status>              | 定位状态        | 0              | not fixed position                                           |
|                           |                 | 1              | fixed position                                               |
| <UTC date & Time>         | UTC时间         | yyyyMMddhhmmss | yyyy: [1980,——] MM : [1,12] dd: [1,31] hh: [0,23] mm: [0,59] ss:[0,60] |
| <Latitude>                | 纬度            | ±dd.dddddd     | [-90.000000,90.000000]                                       |
| <Longitude>               | 经度            | ±ddd.dddddd    | [-180.000000,180.000000]                                     |
| <MSL Altitude>            | 海拔高度        |                | 单位：meters                                                 |
| <Speed Over Ground>       | 对地速度        | 0~999.99       | 单位：海里/小时                                              |
| <Course Over Ground>      | 对地航向        | 0~360.00       | 单位：degress                                                |
| <Fix Mode>                | 定位模式        | 1              | 1 为未定位                                                   |
|                           |                 | 2              | 2 为2D定位                                                   |
|                           |                 | 3              | 3 为3D定位                                                   |
| <Reserved1>               | 保留1           |                |                                                              |
| <HDOP>                    | 水平精度因子    | 0~99.9         |                                                              |
| <PDOP>                    | 位置精度因子    | 0~99.9         |                                                              |
| <VDOP>                    | 垂直精度因子    | 0~99.9         |                                                              |
| <Reserved2>               | 保留2           |                |                                                              |
| <GNSS Satellites in View> | 可视GNSS卫星    | 0~99           |                                                              |
| <GNSS Satellites Used>    | 使用GNSS卫星    | 0~99           |                                                              |
| <GLONASS Satellites Used> | 使用GLONASS卫星 | 0~99           |                                                              |
| <Reserved3>               | 保留3           |                |                                                              |
| <C/N0 max>                | 最大信噪比      | 0~55           | 单位：dBHz                                                   |
| <HPA>                     |                 | 0~9999.9       | 单位：meters                                                 |
| <VPA>                     |                 | 0~9999.9       | 单位：meters                                                 |
