# **Camera使用说明**

> - 本文档暂时适用于780EP/780EPV开发板，但是测试DEMO适用于618/718p/718pv模块
>
> - 关联文档和使用工具：
>
>   - [从Ramdump里分析内存泄漏问题](ramDump.md)
>
>   - [LuatOS-SoC固件获取](https://gitee.com/openLuat/LuatOS/releases)
>
>   - [camera Demo](https://gitee.com/openLuat/LuatOS/tree/master/demo/camera/spi_cam)
>
>   - [Luatools下载调试工具](../../%E5%BC%80%E5%8F%91%E5%B7%A5%E5%85%B7%E5%8F%8A%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E/Luatools%E4%B8%8B%E8%BD%BD%E8%B0%83%E8%AF%95%E5%B7%A5%E5%85%B7.md)

## 1、环境准备

1. 780ep(v)开发板一套

![开发板图片](../../../image/LuatOS%E5%BC%80%E5%8F%91%E8%B5%84%E6%96%99/%E7%A4%BA%E4%BE%8B/Camera/%E5%9B%BE%E7%89%871.png)

2. 摄像头一个，目前demo适配了三款摄像头，这里使用了gc032a

3. 串口助手，这里使用了sscom5.13

![串口助手](../../../image/LuatOS%E5%BC%80%E5%8F%91%E8%B5%84%E6%96%99/%E7%A4%BA%E4%BE%8B/Camera/%E5%9B%BE%E7%89%872.png)

4. 固件版本： [LuatOS-SoC_V1001_EC718P](https://gitee.com/openLuat/LuatOS/releases) 或者更高版本

5. LuatOS-demo路径：[LuatOS\demo\camera\spi_cam](https://gitee.com/openLuat/LuatOS/tree/master/demo/camera/spi_cam)
---

## 2、修改部分参数

![demo](../../../image/LuatOS%E5%BC%80%E5%8F%91%E8%B5%84%E6%96%99/%E7%A4%BA%E4%BE%8B/Camera/%E5%9B%BE%E7%89%873.png)

local uartid = 1 -- 根据实际设备选取不同的uartid

![demo](../../../image/LuatOS%E5%BC%80%E5%8F%91%E8%B5%84%E6%96%99/%E7%A4%BA%E4%BE%8B/Camera/%E5%9B%BE%E7%89%874.png)

camera\_id = gc032aInit(cspiId,i2cId,24000000,SCAN\_MODE,SCAN\_MODE)
---

## 3、固件及软件下载

打开luatools项目管理新建项目并下载固件

![luatools项目管理下载固件](../../../image/LuatOS%E5%BC%80%E5%8F%91%E8%B5%84%E6%96%99/%E7%A4%BA%E4%BE%8B/Camera/%E5%9B%BE%E7%89%875.png)
---

## 4、效果展示

1. 下载固件后开机会加载以下打印

![luatools日志界面](../../../image/LuatOS%E5%BC%80%E5%8F%91%E8%B5%84%E6%96%99/%E7%A4%BA%E4%BE%8B/Camera/%E5%9B%BE%E7%89%876.png)

2. 按下boot按键拍照，并将串口数据发送至串口1

![sscom界面](../../../image/LuatOS%E5%BC%80%E5%8F%91%E8%B5%84%E6%96%99/%E7%A4%BA%E4%BE%8B/Camera/%E5%9B%BE%E7%89%877.png)

3. 查看保存的文件

![sscom安装目录下查找读取的文件](../../../image/LuatOS%E5%BC%80%E5%8F%91%E8%B5%84%E6%96%99/%E7%A4%BA%E4%BE%8B/Camera/%E5%9B%BE%E7%89%878.png)
![sscom安装目录下查找读取的文件](../../../image/LuatOS%E5%BC%80%E5%8F%91%E8%B5%84%E6%96%99/%E7%A4%BA%E4%BE%8B/Camera/%E5%9B%BE%E7%89%879.png)
