@[TOC](目录名称)

## 基站/WIFI定位原理
模块正常联网后，搜索附近的小区信息，上报给后台；后台查询小区经纬度，并结合信号强度等因素进行计算，最后返回计算出来的经纬度给模块。
WIFI定位的原理和基站定位原理类似，搜索附近WIFI的MAC地址信息，上报给后台。后台查询MAC地址经纬度，并结合信号强度等因素进行计算，最后返回计算出来的经纬度给模块。

## 免费和收费服务区别
目前合宙的4G模块都支持基站定位，此服务免费。但免费的服务器承受不了高并发压力，为了提供更好的服务，后期会提供收费服务。
### 免费服务
1. 免费服务仅支持单基站定位,无wifi定位, 同一IMEI的请求间隔需大于15秒。
2. 超过频次的定位请求均会返回定位失败。返回错误码，不包含位置信息。

### 收费服务
1. 收费服务支持多基站定位和wifi定位, 同一IMEI的请求间隔需大于5秒。

## 各固件的配置方式
### 免费服务
  沿用现有的接入参数和流程, 但要控制访问频次
  1. AT固件, 现有固件均支持
  2. Lua固件, 无需修改
  3. CSDK固件, 无需修改

### 收费服务
    计费方式: 联系销售按IMEI数量购买, 由销售导入IMEI列表，或使用项目key的方式批量购买

## 使用方法
### LuatOS使用方法
demo见[demo/lbsLoc/main.lua](https://gitee.com/openLuat/LuatOS/blob/v0007.ec618.v1106/demo/lbsLoc/main.lua"demo/lbsLoc")

#### 免费
脚本逻辑是调用lbsLoc.request(getLocCb)，在getLocCb回调函数里就会有查询到的经纬度。
#### 收费
脚本逻辑是设置正确的项目key（XXX），在getLocCb回调函数里就会有查询到的经纬度。

 WIFI定位，需要通过wlan.scan()获取对应WIFI地址，然后在调用lbsLoc.request()，在getLocCb回调函数里就会有查询到的经纬度。
```lua
-- 以下为基站+wifi混合定位
 sys.subscribe("WLAN_SCAN_DONE", function ()
    local results = wlan.scanResult()
     log.info("scan", "results", #results)
    if #results > 0 then
         local reqWifi = {}
        for k,v in pairs(results) do
             log.info("scan", v["ssid"], v["rssi"], v["bssid"]:toHex())
             local bssid = v["bssid"]:toHex()
             bssid = string.format ("%s:%s:%s:%s:%s:%s", bssid:sub(1,2), bssid:sub(3,4), bssid:sub(5,6), bssid:sub(7,8), bssid:sub(9,10), bssid:sub(11,12))
            reqWifi[bssid]=v["rssi"]
         end
         lbsLoc.request(getLocCb,nil,nil,"XXX",nil,nil,nil,reqWifi)
     else
         lbsLoc.request(getLocCb) -- 没有wifi数据,进行普通定位
     end
 end)

 sys.taskInit(function()
     sys.waitUntil("IP_READY", 30000)
     wlan.init()
     while 1 do
         wlan.scan()
         sys.wait(60000)
    end
 end)
```

### AT使用方法
AT使用方法见：[Luat4G模块EC618系列AT命令手册](https://doc.openluat.com/wiki/37?wiki_page_id=4460 "Luat4G模块EC618系列AT命令手册")
#### 免费
参考如下章节说明
5.17 读取基站定位（LBS）信息和时间：AT+CIPGSMLOC
#### 收费
1. 多基站定位>V1148以上版本支持
2. 发AT+WIFILOC=1,1,1这个定位需要WIFI扫描，要选择WIFI优先，不然模块处于连接态时WIFI扫不到

### CSDK使用方法
CSDK使用方法见demo：[git\luatos-soc-2022\project\example_lbsLoc](https://gitee.com/openLuat/luatos-soc-2022 "git\luatos-soc-2022\project\example_lbsLoc") 
#### 免费
直接用上面的DEMO就可以
#### 收费
修改KEY值
```c
static uint8_t *productKey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
```
WIFI定位，打开下面的宏定义
```c
#define WIFI_LOC 1 // 是否开启wifi 定位
```


## 常见问题
### 基站定位精度如何？
搜索到的小区越多，定位的精度越高；一般来说，城市中心定位精度比郊区和农村定位精度高，城市中心的定位精度在几十米到几百米不等，郊区和农村的定位精度更低，可能会有几千米甚至更多的误差。
通过多小区定位，将实时搜索到的所有小区同时上报给后台参与定位，基站定位的误差都比较大，如果需要准确定位，请使用支持GPS的模块，例如Air780EG、Air510U。

### wifi定位精度？
根据设备获取的WiFi的信息进行定位，WIFI定位精度一般不受使用环境影响，主要和单一WIFI辐射半径、WIFI覆盖密度有关。一般来说，WIFI精度在3米－200米左右。

### 为什么基站定位失败？
1、 main.lua中的PRODUCT_KEY和此设备在iot.openluat.com中所属项目的ProductKey必须一致，请去检查。<br>
2、 后台基站数据库查询不到所有小区的位置信息；在trace中向上搜索mcc,mnc,lac,ci，然后在电脑浏览器中打开[定位查询](http://bs.openluat.com/ "定位查询")，手动查找mcc,mnc,lac,ci后的所有小区位置；如果手动可以查到位置，则服务器存在BUG，直接向技术支持人员反映问题；如果手动无法查到位置，则基站数据库还没有收录当前设备的小区位置信息，向技术支持人员反馈，我们会尽快收录。
3、达到了总的qps限制数量。

###  合宙官方的基站/WIFI定位能在国外使用吗？
不能，没有国外的基站数据库。

### 基站/WIFI定位获取的经纬度是什么格式的？
基站定位获取的经纬度为WGS-84格式。
各种坐标系说明以及转换方法参考：http://old.openluat.com/GPS-Offset.html

### 当同时使用基站定位和wifi定位怎么判断是基站定位成功了还是wifi定位成功了？
根据返回的locType判断，为0表示基站定位成功，返回255表示WIFI定位成功。