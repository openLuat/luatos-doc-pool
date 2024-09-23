## 查询各种信息：AT*I

语法规则：

| 命令类型 | 语法 | 返回                                                         |
| -------- | ---- | ------------------------------------------------------------ |
| 设置命令 | AT*I | `Manufacturer:<manufacturer><br>Model: <model><br>Revision: <revision><bt>HWVer: <hwver><br>Buildtime: <Buildtime><br>IMEI: <imei><br>ICCID:<iccid><br>IMSI:<imsi><br> OK` |

 

参数定义：

| 参数             | Definition                                                   | 取值 | 解释           |
| ---------------- | ------------------------------------------------------------ | ---- | -------------- |
| `<manufacturer>` | +CGMI 命令的返回                                             |      |                |
| `<model>`        | +CGMM命令的返回                                              |      |                |
| `<revision>`     | +CGMR命令的返回                                              |      |                |
| `<hwver>`        | 硬件版本                                                     |      |                |
| `<Buildtime>`    | 版本固件的编译时间                                           |      |                |
| `<imei>`         | 同+CGSN命令的返回值                                          |      |                |
| `<iccid>`        | 同+ICCID命令的返回值                                         |      |                |
| `<imsi>`         | 国际移动台用户识别码（International Mobile Subscriber Identity） |      | 由15位数字组成 |

 

举例：

| 命令（→）/返回（←） | 实例                                                         | 解释和说明 |
| ------------------- | ------------------------------------------------------------ | ---------- |
| →                   | AT*I                                                         |            |
| ←                   | Manufacturer: AirM2M<br>Model: Air780E<br>Revision: AirM2M_780E_V1120_LTE_AT<br>HWver: A12<br>Buildtime: Mar  6 2023 20:04:22<br>IMEI: 864040060365518<br>ICCID: 89860621260002571487<br>IMSI: 460060086257148 <br>OK |            |
