## 1.Air724模块摄像头Camera接口特点
>只支持SPI接口
>最高像素30W像素@15fps
>支持数据格式YUV422, Y420, RAW8, RAW10

## 2.为什么显示白屏，黑屏，扫码不成功？
>查看下，屏是否插好，引脚是否接对，core,是否选对。

## 3.Air724模块为什么图像左移
>把预览缩小2倍试试。
>disp.camerapreviewzoom(zoom)-----–zoom： 放缩设置, 正数放大负数缩小，最大4倍，0不放缩
>disp.camerapreviewzoom(-2)---–缩小2倍

## 4.Air724模块摄像头拍照的时候，按键没法触发
>默认拍照和保存照片为阻塞模式，新增可选参数nonblock可以设置为阻塞和非阻塞模块，1非阻塞，0阻塞（固件版本>=V3032）。

## 5.使用camera的demo，将拍照的图片转发给串口，如何将串口工具接收到的字符串转成可见的照片格式?
>使用sscom，接收到一整张完整的图片后，点击保存数据,进入sscom根目录，会看见一个.DAT文件，将该文件后缀名改为.jpg即可

## 6.Air72XUG/Air82XUG支持什么摄像头?
>内部配置的gc0310 camera;
>外部配置gc6153 camera SDR;
>外部配置gc0310 camera SDR;
>外部配置gc0310 camera DDR 640*480;
>外部配置gc0310 camera DDR;
>外部配置bf302A camera SDR;

## 7.Air724模块AT扫码功能介绍
>目前AT指令只支持扫码功能，且只能支持CG0310摄像头。
>扫码支持QR,Code 49,Code 128格式。
>内部集成Zbar解码库
>AT+CCAM=0 打开cam
>AT+CCAM=1 关闭cam
>AT+CCAM=2 打开扫码
>AT+CCAM=3 关闭扫码
>扫码成功有+CCAM上报<br>
>注意：版本号大于470的固件才能支持摄像头功能
