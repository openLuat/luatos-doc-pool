# 780EP开发板驱动Camera示例

> - 本文档内容适用于780EP开发板
>
> - 关联文档和使用工具：
>
>   - [LuatOS-SoC固件获取](https://gitee.com/openLuat/LuatOS/releases) （页面Ctrl+F搜索780EP即可找到对应的固件）
>
>   - [camera Demo](https://gitee.com/openLuat/LuatOS/tree/master/demo/camera/spi_cam)
>
>   - [Luatools下载调试工具](../doc/%E5%BC%80%E5%8F%91%E5%B7%A5%E5%85%B7%E5%8F%8A%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E/Luatools%E4%B8%8B%E8%BD%BD%E8%B0%83%E8%AF%95%E5%B7%A5%E5%85%B7.md)

## 1、环境准备

1. 780EP开发板一套

 ![开发板图片](image/%E5%9B%BE%E7%89%871.png)

2. 摄像头一个，目前demo适配了三款摄像头（**bf30a2、gc032a、gc0310**），这里使用了gc032a作为演示

3. 串口助手，这里使用了sscom5.13

4. 固件版本： [LuatOS-SoC_V1001_EC718P](https://gitee.com/openLuat/LuatOS/releases) 或者更高版本

5. LuatOS-demo路径：[LuatOS\demo\camera\spi_cam](https://gitee.com/openLuat/LuatOS/tree/master/demo/camera/spi_cam)
---

## 2、修改部分参数

 ![demo](image/%E5%9B%BE%E7%89%873.png)

local uartid = 1 -- 根据实际设备选取不同的uartid

 ![demo](image/%E5%9B%BE%E7%89%874.png)

camera_id = gc032aInit(cspiId,i2cId,24000000,SCAN_MODE,SCAN_MODE)

---

## 3、固件及软件下载

打开luatools项目管理新建项目并下载固件

 ![luatools项目管理下载固件](image/%E5%9B%BE%E7%89%875.png)
---

## 4、效果展示

1. 下载固件后开机会加载以下打印

 ![luatools日志界面](image/%E5%9B%BE%E7%89%876.png)

2. 按下boot按键拍照，并将串口数据发送至串口1

 ![sscom界面](image/%E5%9B%BE%E7%89%877.png)

3. 查看保存的图片文件

 ![sscom安装目录下查找读取的文件](image/%E5%9B%BE%E7%89%878.png)
 ![sscom安装目录下查找读取的文件](image/%E5%9B%BE%E7%89%879.png)


----


![选型手册简洁版01](image/1.jpg)
![选型手册简洁版02](image/2.jpg)

