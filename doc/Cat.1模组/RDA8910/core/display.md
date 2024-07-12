@[TOC]

# display
显示屏和camera支持
## disp.init(para)

初始化LCD驱动配置

**参数**

param：显示参数，table类型，包含：
| **参数**    | **释义**                                                     | **取值**                                |
| ----------- | ------------------------------------------------------------ | --------------------------------------- |
| width       | 分辨率宽度                                                   | 数值，最大支持QVGA分辨率，不超过320/240 |
| height      | 分辨率高度                                                   | 数值，最大支持QVGA分辨率，不超过320/240 |
| bus      | LCD总线类型   | disp.BUS_SPI4LINE                       |
| xoffset     | x偏移，不设置该域则默认0                                     | 数值类型                                |
| yoffset     | y偏移，不设置该域则默认0                                     | 数值类型                                |
| freq        | spi时钟频率，支持110K到13M（即110000到13000000）之间的整数（包含110000和13000000） | 最小800K，最大200M                      |
| pinrst | 暂不支持                                                       | 0 |
| pinrs | 暂不支持                                            | 0 |
| initcmd     | 初始化指令表                                                 | table类型                               |
| sleepcmd    | LCD进入休眠命令表                                            | table类型                               |
| wakecmd     | LCD退出休眠命令表                                            | table类型                               |
| id_reg      |LCD读ID寄存器（同时配置多了LCD参数时需要填）                                            | table类型                               |
| id_value    | LCD ID （同时配置多了LCD参数时需要填）                                            | table类型                               |
| porch_vs    | porch vs参数,缺省为8 (mipi lcd才会使用,可以缺省，如果lcd屏幕不兼容时才需要修改)                                            |数值类型,缺省为8                           |
| porch_vbp    | porch vbp参数 (mipi lcd才会使用,可以缺省，如果lcd屏幕不兼容时才需要修改)                                            |数值类型,缺省为20                              |
| porch_vfp    | porch vfp参数 (mipi lcd才会使用,可以缺省，如果lcd屏幕不兼容时才需要修改)                                            |数值类型,缺省为20                             |
| porch_hs    | porch hs参数 (mipi lcd才会使用,可以缺省，如果lcd屏幕不兼容时才需要修改)                                            |数值类型,缺省为10                           |
| porch_hbp    | porch hbp参数 (mipi lcd才会使用,可以缺省，如果lcd屏幕不兼容时才需要修改)                                            |数值类型,缺省为20                              |
| porch_hfp    | porch hfp参数 (mipi lcd才会使用,可以缺省，如果lcd屏幕不兼容时才需要修改)                                            |数值类型,缺省为20                             |
| continue_mode    | 配置时钟contunue模式 (mipi lcd才会使用,可以缺省，如果lcd屏幕不兼容时才需要修改)                                            |数值类型,1表示continue模式,0表示non continue时,缺省为0                        |


**返回值**

无

**例子**

```lua

--同时配置多个LCD，需要填写id_reg和id_value字段
--同时配置多个LCD，disp.init具有返回值0：配置成功 -1：配置失败
--如果传入LCD参数只有一个时和配置一个LCD使用方式兼容,且没有返回值
local function init()
    local lcd_1 =
    {
        id_reg = 0x04,
    	id_value = 0x7c89f0,
        ..... --和配置一个LCD参数一样需要填下width、height等参数，这里先省略
    }
    local lcd_2 =
    {
        id_reg = 0x04,
    	id_value = 0x123456,
        ..... --和配置一个LCD参数一样需要填下width、height等参数，这里先省略
    }
    local lcd_3 =
    {
        id_reg = 0x05,
    	id_value = 0x654321,
        ..... --和配置一个LCD参数一样需要填下width、height等参数，这里先省略
    }
    --同时配置3个LCD参数，底层可以通过读ID寄存器然后和id_value进行比较，找到正确的LCD配置
    --找到了返回0 匹配失败返回-1
    --如果只传输一个参数，可以不传入id_reg id_value字段，同时disp.init没有返回值，和之前兼容
    ret = disp.init(lcd_1,lcd_2,lcd_3)
    if ret == 0 then 
    disp.clear()
    disp.update()
    	log.info("disp.init succeed !!!")
	else
    	log.info("disp.init fail !!!")
	end
end

--配置一个LCD
local function init()
    local para =
    {
        width = 128, --分辨率宽度，128像素；用户根据屏的参数自行修改
        height = 160, --分辨率高度，160像素；用户根据屏的参数自行修改
        bpp = 16, --位深度，彩屏仅支持16位
        bus = disp.BUS_SPI4LINE, --LCD专用SPI引脚接口，不可修改
        xoffset = 2, --X轴偏移
        yoffset = 1, --Y轴偏移
        freq = 20000000, --spi时钟频率，最小800K，最大200M
        pinrst = pio.P0_6, --reset，复位引脚
        pinrs = pio.P0_1, --rs，命令/数据选择引脚
        --camera_preview_no_update_screen = 1, --0表示摄像头预览刷屏；1表示摄像头预览不刷屏
        --初始化命令
        --前两个字节表示类型：0001表示延时，0000或者0002表示命令，0003表示数据
        --延时类型：后两个字节表示延时时间（单位毫秒）
        --命令类型：后两个字节命令的值
        --数据类型：后两个字节数据的值
        initcmd =
        {
            0x00020011,
            0x00010078,
            0x000200B1,
            0x00030002,
            0x00030035,
            0x00030036,
            0x000200B2,
            0x00030002,
            0x00030035,
            0x00030036,
            0x000200B3,
            0x00030002,
            0x00030035,
            0x00030036,
            0x00030002,
            0x00030035,
            0x00030036,
            0x000200B4,
            0x00030007,
            0x000200C0,
            0x000300A2,
            0x00030002,
            0x00030084,
            0x000200C1,
            0x000300C5,
            0x000200C2,
            0x0003000A,
            0x00030000,
            0x000200C3,
            0x0003008A,
            0x0003002A,
            0x000200C4,
            0x0003008A,
            0x000300EE,
            0x000200C5,
            0x0003000E,
            0x00020036,
            -- set rotation
            -- 0x000300C0,
            0x00030000,
            0x000200E0,
            0x00030012,
            0x0003001C,
            0x00030010,
            0x00030018,
            0x00030033,
            0x0003002C,
            0x00030025,
            0x00030028,
            0x00030028,
            0x00030027,
            0x0003002F,
            0x0003003C,
            0x00030000,
            0x00030003,
            0x00030003,
            0x00030010,
            0x000200E1,
            0x00030012,
            0x0003001C,
            0x00030010,
            0x00030018,
            0x0003002D,
            0x00030028,
            0x00030023,
            0x00030028,
            0x00030028,
            0x00030026,
            0x0003002F,
            0x0003003B,
            0x00030000,
            0x00030003,
            0x00030003,
            0x00030010,
            0x0002003A,
            0x00030005,
            0x00020029,
        },
        --休眠命令
        sleepcmd = {
            0x00020010,
        },
        --唤醒命令
        wakecmd = {
            0x00020011,
        }
    }
    disp.init(para)
    disp.clear()
	disp.update()
end

--配置一个MIPI lcd
local function init()
    local para =
    {
        width = 480, --分辨率宽度，
        height = 854, --分辨率高度
        bpp = 16, --MIPI LCD直接写16，暂不支持其他配置
        bus = disp.BUS_MIPI, --LCD专用SPI引脚接口，不可修改
        xoffset = 0, --X轴偏移
        yoffset = 0, --Y轴偏移
        freq = 200000000, --mipi时钟最高为500000000
        pinrst = pio.P0_20, --reset，复位引脚,MIPI屏幕必须填写
        pinrs = 0xffff, --mipi不需要rs脚，直接写0xffff

		---- porch_vs porch_vbp porch_vfp porch_hs porch_hbp porch_hfp 这6个参数可以不配置
		---- 软件有默认的配置。一般mipi屏会兼容多套参数。也可以根据厂商提供的参数进行修改
		porch_vs = 2,
		porch_vbp = 15, 
		porch_vfp = 8,
		porch_hs = 10,
		porch_hbp = 30,
		porch_hfp = 30,

		-- continue_mode 可以不配置底层默认为0. 配置后一直处于高速continue 模式
		continue_mode = 1,

        --初始化命令
        --前两个字节表示类型：0001表示延时，0000或者0002表示命令，0003表示数据
        --延时类型：后两个字节表示延时时间（单位毫秒）
        --命令类型：后两个字节命令的值
        --数据类型：后两个字节数据的值
	--现在MIPI LCD 只支持,lane 2线,RGB565格式
		
		initcmd =
        {
			...
			--寄存器配置和spi写法一样
        },
        --休眠命令
        sleepcmd = {
	    	...
			--寄存器配置和spi写法一样
        },
        --唤醒命令
        wakecmd = {
        	...
			--寄存器配置和spi写法一样
        }
    }
    disp.init(para)
    disp.clear()
    disp.update()
end


```

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1963 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2202 "示例")

---

## disp.getlcdinfo()

获取屏信息接口

**参数**
无

|返回值|类型|释义|取值|
|-|-|-|-|
|width|number|返回屏分辨率宽度|取值范围0-调用disp.init()接口设置的width|
|height|number|返回屏分辨率高度|取值范围0-调用disp.init()接口设置的height|
|bpp|number|位深度|彩屏仅支持16位，调用disp.init()接口设置的bpp|

**例子**

```lua
 local WIDTH,HEIGHT = disp.getlcdinfo()
```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1963 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2202 "示例")

---

## disp.close()

关闭显示模块

**参数**

无

**返回值**

无

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1963 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2202 "示例")

---



## disp.clear()

清空显示

**参数**

无

**返回值**

无

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1963 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2202 "示例")

---



## disp.update()

刷新数据到LCD

**参数**

无

**返回值**

无

**例子**

```lua
--[[
    注意：所有要显示的内容，摆放成功后需要调用该接口刷新，这样才能看到显示的内容
]]

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1963 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2202 "示例")

---



## disp.puttext(str,x,y,grade,thickness)

显示文字

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.11.26|支持矢量字体|>=3026|需要字库外设|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|str|string|文字内容|   |
|x|number|显示位置横向坐标|取值范围0-disp.width|
|y|number|显示位置纵向坐标|取值范围0-disp.height|
|grade|number|矢量字体的灰阶（可选）|取值1,2或4|
|thickness|number|矢量字体的粗细（可选）|  |

**返回值**

无

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1963 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2202 "示例")

---



## disp.putimage(img,x,y)

显示图片

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|img|string|图片文件|支持bmp，jpeg，png格式|
|x|number|显示位置，横向坐标|取值范围0-disp.width|
|y|number|显示位置，纵向坐标|取值范围0-disp.height|

**返回值**

无

**例子**

```lua
 --显示图片
 disp.putimage("/lua/logo_color_240X320.png",0,80)
 --将显示的内容刷到LCD
 disp.update()
 end

```

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1963 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2202 "示例")

---



## disp.img.convert(org_file,org_format,dest_file,dest_format)

图片格式转换接口

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|org_file|string|源文件路径|可以是lua资源，文件系统，sd卡|
|org_format|number|源文件格式|暂时只支持disp.IMG_FORMAT_PNG|
|dest_file|string|目标文件路径|如果dest_file!=nil，转换数据直接保存到文件系统，返回值为number 0：成功 -1：失败， 如果dest_file==nil 成功返回：string类型数据 失败：nil|
|dest_format|number|目标文件格式|暂时只支持disp.IMG_FORMAT_RGB565|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|ret|number|当dest_file不为nil时|成功返回0 失败返回-1|
|ret|string|当dest_file为nil时|转换成功返回dest_format格式的数据|
|ret|nil|当dest_file为nil时|转换失败返回nil|

**例子**

```lua
 --png转rgb565 dest_file=nil 返回值ret为string类型的rgb数据，失败返回nil
 ret=disp.img.convert("/lua/logo.png",disp.IMG_FORMAT_PNG, nil, disp.IMG_FORMAT_RGB565)
 print("ret ", type(ret), ret:toHex())
 
 --png转rgb565 dest_file=rgb 将转换的数据保存到/rgb文件中，返回值ret为number类型，成功返回0 失败-1
 imgdata=disp.img.convert("/lua/logo.png",disp.IMG_FORMAT_PNG, "/rgb", disp.IMG_FORMAT_RGB565)
 print("ret  ", type(ret), ret)

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1963 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2202 "示例")

---



## disp.drawrect(left,top,right,bottom,color)

显示矩形框

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|left|number|起始位置-左|0-disp.width|
|top|number|起始位置-上|取值范围0-disp.height|
|right|number|起始位置-右|取值范围0-disp.width|
|bottom|number|起始位置-下|取值范围0-disp.height|
|color|number|颜色|0-65535（具体根据LCD色域来定）|

**返回值**

无

**例子**

```lua
 --disp.drawrect(0,43,128,44,lcd.rgb(222,222,222))
 end

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1963 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2202 "示例")

---



## disp.putqrcode(data,width,displayWidth,x,y)

显示二维码

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|data|string|二维码数据| qrencode.encode()二维码编码，返回的二维码数据  |
|width|number|二维码数据的实际宽度|  qrencode.encode()二维码编码，返回的二维码宽度 |
|displayWidth|number|二维码实际显示宽度| 二维码在当前屏幕上显示的宽度  |
|x|number|二维码显示起始坐标x|取值范围0-disp.width|
|y|number|二维码显示起始坐标y|取值范围0-disp.heith|

**返回值**

无

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2317 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2189 "示例")

---



## disp.setcolor(color)

设置前景色

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|color|number|颜色|0-65535（具体根据LCD色域来定）|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|返回历史背景色|  |

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1963 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2202 "示例")

---



## disp.setbkcolor(color)

设置背景色

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|color|number|颜色|0-65535（具体根据LCD色域来定）|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|返回历史背景色|  |

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1963 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2202 "示例")

---



## disp.loadfont(font)

加载字体文件

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.11.26|支持矢量字体|>=3026|需要字库外设|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|font|string\|number|字体文件\|外设SPI号|  |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|font_id|number|字体对应id|  |

**例子**

```lua
font_id = disp.loadfont("/lua/18x36_0-colon.bin")
font_id = disp.loadfont(spi.SPI_1)


```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1963 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2202 "示例")

---



## disp.setfont(font_id)

设置当前显示字体

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|font_id|number|字体id|取值为disp.loadfont(font)返回值|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|历史字体id|   |

**例子**

```lua
 local oldFont = disp.setfont(font_id)
 

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1963 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2202 "示例")

---



## disp.write(cmd)

向LCD控制器写入命令

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|cmd|number|命令|参考disp.init(para.initcmd)|

**返回值**

无

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1963 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2202 "示例")

---



## disp.sleep(enable)

控制LCD是否进入休眠

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|enable|number|LCD休眠|0：退出休眠，1：进入休眠|

**返回值**

无

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1963 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2202 "示例")

---



## disp.camerapreview(offsetx,offsety,startx,starty,endx,endy)

打开摄像头预览

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|offsetx|number|保留|取值0|
|offsety|number|保留|取值0|
|startx|number|预览起始位置x|  |
|starty|number|预览起始位置y|  |
|endx|number|预览结束位置x|  |
|endy|number|预览结束位置y|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|$bool|true:成功，false:失败|  |

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1940 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2168 "示例")

---



## disp.camerapreviewzoom(0xff)

预览缩放

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|zoom|number|放缩设置|目前仅支持填入0xff自适应屏幕尺寸|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number| 0/1,失败/成功|1/0|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1940 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2168 "示例")

---



## disp.camerapreviewrotation(rotation)

预览旋转

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|rotation|number|旋转|反转角度设置 暂时只支持0和90度|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|0/1|number|失败/成功|0/1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1940 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2168 "示例")

---



## disp.camerawritereg(regTable)

设置camera sensor寄存器

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|regTable|string|寄存器表|  |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/1 失败/成功|0/1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1940 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2168 "示例")

---



## disp.cameraopen(type,zbarscan,mirror,jump)

初始化摄像头

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|type|number|保留|取值1|
|zbarscan|number|扫码功能|1：支持扫码，0：不支持扫码|
|mirror|number|镜像功能|1：开启摄像头镜像，0：关闭摄像头镜像|
|jump|number|预览隔行列输出|  |

**返回值**

无

**例子**

```lua
pm.wake("testTakePhoto")
    --打开摄像头
    disp.cameraopen(1,0,0,1)
    --disp.cameraopen(1,0,0,0)  --因目前core中还有问题没解决，所以不能关闭隔行隔列
    --打开摄像头预览
    --如果有LCD，使用LCD的宽和高
    --如果无LCD，宽度设置为240像素，高度设置为320像素，240*320是Air268F支持的最大分辨率
    disp.camerapreview(0,0,0,0,WIDTH or DEFAULT_WIDTH,HEIGHT or DEFAULT_HEIGHT)
    --设置照片的宽和高像素并且开始拍照
    --此处设置的宽和高和预览时的保持一致
    disp.cameracapture(WIDTH or DEFAULT_WIDTH,HEIGHT or DEFAULT_HEIGHT)
    --设置照片保存路径
    disp.camerasavephoto("/testCamera.jpg")
    log.info("testCamera.takePhotoAndDisplay fileSize",io.fileSize("/testCamera.jpg"))
    --关闭摄像头预览
    disp.camerapreviewclose()
    --关闭摄像头
    disp.cameraclose()
    --允许系统休眠
    pm.sleep("testTakePhoto")
end

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1940 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2168 "示例")

---



## disp.cameraopen_ext(param)

LUA外部配置camera功能

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|param|string|参数表|  |

**返回值**

无

**例子**

```lua
--参数定义如下所示（配置gc6153 8万摄像头）
local gc6153 =
{
    zbar_scan = 1,  --是否支持扫码
    i2c_addr = 0x40,  -- 摄像头i2c访问地址 
    sensor_width = 240,  -- 摄像头的宽 
    sensor_height = 320, -- 摄像头的高 
    id_reg = 0xf1,      --  摄像头ID寄存器 
    id_value = 0x53,    --  摄像头ID值 
    --  摄像头SPI是几线输出 
    --disp.CAMERA_SPI_MODE_LINE1 1线
    --disp.CAMERA_SPI_MODE_LINE2 2线
    --disp.CAMERA_SPI_MODE_LINE4 4线
    spi_mode = disp.CAMERA_SPI_MODE_LINE1, 
    --  摄像头采集速率 
    --disp.CAMERA_SPEED_SDR  单片采集
    --disp.CAMERA_SPEED_DDR  双边采集
    spi_speed = disp.CAMERA_SPEED_SDR,  
     --  摄像头输出YUV的格式 
    spi_yuv_out = disp.CAMERA_SPI_OUT_U0_Y1_V0_Y0,
   --disp.CAMERA_SPI_OUT_Y0_U0_Y1_V0
   --disp.CAMERA_SPI_OUT_Y0_V0_Y1_U0
   --disp.CAMERA_SPI_OUT_U0_Y0_V0_Y1
   --disp.CAMERA_SPI_OUT_U0_Y1_V0_Y0
   --disp.CAMERA_SPI_OUT_V0_Y0_U0_Y1
   --disp.CAMERA_SPI_OUT_Y1_V0_Y0_U0
   --disp.CAMERA_SPI_OUT_Y1_U0_Y0_V0
    cmd = --摄像头初始化寄存器
    {
         0xfe, 0xa0  ,
         0xfe, 0xa0  ,
         0xfe, 0xa0  ,
         0xf6, 0x00  ,
         0xfa, 0x11  ,
         0xfc, 0x12  ,
         0xfe, 0x00  ,     
         0xfe, 0x00  ,
         0x01, 0x41  , 
         0x02, 0x12  , 
         0x0d, 0x40  , 
         0x14, 0x7E  , 
         0x16, 0x05 , 
         0x17, 0x18  , 
         0x1c, 0x31  , 
         0x1d, 0xbb  , 
         0x1f, 0x3f  , 
         0x73, 0x20  , 
         0x74, 0x71  , 
         0x77, 0x22  , 
         0x7a, 0x08  , 
         0x11, 0x18  , 
         0x13, 0x48  , 
         0x12, 0xc8  , 
         0x70, 0xc8  , 
         0x7b, 0x18  , 
         0x7d, 0x30  , 
         0x7e, 0x02  , 
         0xfe, 0x10  , 
         0xfe, 0x00  ,
         0xfe, 0x00  ,
         0xfe, 0x00  ,
         0xfe, 0x00  ,
         0xfe, 0x00  ,
         0xfe, 0x10  ,
         0xfe, 0x00  ,
         0x49, 0x61  ,  
         0x4a, 0x40  ,  
         0x4b, 0x58  ,  
         0xfe, 0x00  ,
         0x39, 0x02  , 
         0x3a, 0x80  , 
         0x20, 0x7e  , 
         0x26, 0x87  , 
         0x33, 0x10  , 
         0x37, 0x06  , 
         0x2a, 0x21  , 
         0x3f, 0x16  ,
         0x52, 0xa6  ,
         0x53, 0x81  ,
         0x54, 0x43  ,
         0x56, 0x78  ,
         0x57, 0xaa  ,
         0x58, 0xff  , 
         0x5b, 0x60  , 
         0x5c, 0x50  , 
         0xab, 0x2a  , 
         0xac, 0xb5  ,
         0x5e, 0x06  , 
         0x5f, 0x06  ,
         0x60, 0x44  ,
         0x61, 0xff  ,
         0x62, 0x69  , 
         0x63, 0x13  ,
         0x65, 0x13  , 
         0x66, 0x26  ,
         0x67, 0x07  ,
         0x68, 0xf5  , 
         0x69, 0xea  ,
         0x6a, 0x21  ,
         0x6b, 0x21  , 
         0x6c, 0xe4  ,
         0x6d, 0xfb  ,
         0x81, 0x3b  , 
         0x82, 0x3b  , 
         0x83, 0x4b  ,
         0x84, 0x90  ,
         0x86, 0xf0  ,
         0x87, 0x1d  ,
         0x88, 0x16  ,
         0x8d, 0x74  ,
         0x8e, 0x25  ,
         0x90, 0x36  ,
         0x92, 0x43  ,
         0x9d, 0x32  , 
         0x9e, 0x81  ,
         0x9f, 0xf4  ,
         0xa0, 0xa0  ,
         0xa1, 0x04  ,
         0xa3, 0x2d  ,
         0xa4, 0x01  ,
         0xb0, 0xc2  ,
         0xb1, 0x1e  ,
         0xb2, 0x10  ,
         0xb3, 0x20  ,
         0xb4, 0x2d  ,
         0xb5, 0x1b  , 
         0xb6, 0x2e  ,
         0xb8, 0x13  ,
         0xba, 0x60  ,
         0xbb, 0x62  ,
         0xbd, 0x78  , 
         0xbe, 0x55  ,
         0xbf, 0xa0  , 
         0xc4, 0xe7  ,
         0xc5, 0x15  ,
         0xc6, 0x16  ,
         0xc7, 0xeb  , 
         0xc8, 0xe4  ,
         0xc9, 0x16  ,
         0xca, 0x16  ,
         0xcb, 0xe9  ,
         0x22, 0xf8  ,
         0xfe, 0x02  ,
         0x01, 0x01  , 
         0x02, 0x80  , 
         0x03, 0x20  , 
         0x04, 0x20  ,  
         0x0a, 0x00  , 
         0x13, 0x10  , 
         0x28, 0x03  ,
         0xfe, 0x00  , 
         0x22, 0xf8  , 
         0xf2, 0x03  , 
    },    
}
end

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1940 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2168 "示例")

---



## disp.cameraclose()

关闭摄像头

**参数**

无

**返回值**

无

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1940 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2168 "示例")

---



## disp.camerapreviewclose()

关闭预览

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number| 0/1, 失败/成功|0/1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1940 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2168 "示例")

---



## disp.cameracapture(width,height[,quality])

拍照片

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|width|number|照片宽度|取值取决于摄像头|
|height|number|照片高度|取值取决于摄像头|
|quality|number|照片压缩质量|0-100（值越大，质量越高）|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number| 0/1, 失败/成功|0/1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1940 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2168 "示例")

---



## disp.camerasavephoto(filename[,x][,y][,w][,h][,quality])

保存指定区域的拍摄的照片到文件，默认保存整张

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|filename|string|保存文件路径|  |
|x|number|图片的x起始坐标|  |
|y|number|图片的y起始坐标|  |
|w|number|图片宽度|  |
|h|number|图片高度|  |
|quality|number|照片压缩质量|0-100（值越大，质量越高）|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number| 0/1, 失败/成功|0/1|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1940 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2168 "示例")

---



## disp.scanmode(mode)

设置扫码模式

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|mode|number|扫码模式设置|取值0:正常扫码 1:镜像扫码 2:都可以扫码 注:只有擎亚扫码库才支持|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0:成功，-1:失败||

---



## disp.scantype(value)

设置正反色扫码

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|value|number|扫码正反色设置|取值1:正色扫码 2:反色扫码 3:都可以扫码 注:只有擎亚扫码库才支持|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0:成功，-1:失败||

---



## disp.screenshots(pathname,x1,x2,y1,y2)

截屏接口

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|pathname|number|文件路径名|只支持bmp|
|x1|number|水平初始值|MIPI屏（0-479）/LCD屏（0-239）|
|x2|number|水平结束值|MIPI屏（x1-479）/LCD屏（x1-239）|
|y1|number|垂直初始值|MIPI屏（0-853）/LCD屏（9-320）|
|y2|number|垂直结束值|MIPI屏（y1-853）/LCD屏（y1-320）|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1| 成功/失败|

---



## disp.get_screenrgb(pathname,x1,x2,y1,y2)

获取整屏rgb数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|pathname|number|文件路径名||
|x1|number|水平初始值|MIPI屏(0)/LCD屏(0)|
|x2|number|水平结束值|MIPI屏（479）/LCD屏（239）|
|y1|number|垂直初始值|MIPI屏（0）/LCD屏（9）|
|y2|number|垂直结束值|MIPI屏（853）/LCD屏（320）|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0/-1| 成功/失败|



## disp.common_reset(ret)

复位驱动

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|ret|boole|复位驱动选择|false：mipi大屏老复位驱动<br/>true：mipi大屏新复位驱动<br/>默认false|



**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|1/0| 成功/失败|

---


