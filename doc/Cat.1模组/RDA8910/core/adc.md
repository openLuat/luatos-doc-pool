@[TOC]

# adc
adc数模转换模块
## adc.open(id,scale)	

打开ADC通道

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|需要打开的adc的通道id|0:ADC0依次类推|
|scale|number|设置adc检测的范围|adc.SCALE_1V250<br>adc.SCALE_2V444<br>adc.SCALE_3V233<br>adc.SCALE_5V000|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|返回ADC打开的结果|0打开失败1打开成功|

**例子**

```lua
-- 打开ADC通道2
local id=2  
local result=adc.open(id)  
if result==1 then  
    log.info("adc",id,"打开成功！");  
end

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1934 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2160 "示例")

---



## adc.read(id)

读取ADC

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|需要读取的adc的通道id|0:ADC0,依次类推|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|adcval|number|adc的原始值，实际电压值/3|当读取失败则返回0xFFFF|
|voltval|number|转换后的电压值,单位为毫伏|当读取失败则返回0xFFFF|

**例子**

```lua
-- 读取ADC通道2
local id=2  
local adcval, voltval=adc.read(id)  
if adcval~=0xffff then  
    log.info("ADC的原始测量数据和电压值:", adcval, voltval)  
end  

```

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1934 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2160 "示例")

---



## adc.close(Id) 


关闭ADC通道

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|Id|number|需要读取的adc的通道id|0:ADC0,依次类推|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|返回ADC关闭的结果|0打开失败1打开成功|

**例子**

```lua
-- 关闭ADC通道2
local id=2  
local result=adc.close(id)  
if result==1 then  
    log.info("adc",id,"关闭成功！");  
end  

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1934 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2160 "示例")

---



