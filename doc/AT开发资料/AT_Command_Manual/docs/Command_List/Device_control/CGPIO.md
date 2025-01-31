## GPIO口控制：AT+CGPIO

**注：本命令仅适用于合宙4G CAT1模块（EC618系列）>=V1115版本**

语法规则：

| 命令类型 | 语法                                                         | 返回                                         |
| -------- | ------------------------------------------------------------ | -------------------------------------------- |
| 设置命令 | `AT+CGPIO=<mode>,<gpio_id>,<set_mode>`                       | `+CGPIO: <mode>,<gpio_id>,<set_mode>` <br>OK |
| 注意事项 | 设计上不考虑gpio复用情况，部分gpio复用设置不生效是正常现象，另外输入默认状态原厂限制无法更改，也是正常现象。 |                                              |

 

参数定义：

| 参数         | 定义           | 取值  | 对取值的说明                                       |
| ------------ | -------------- | ----- | -------------------------------------------------- |
| `<mode>`     | 状态           | 0     | 输入                                               |
|              |                | 1     | 输出                                               |
| `<gpio_id>`  | 具体GPIO 号    |       | 参考对应硬件手册                                   |
| `<set_mode>` | 输出高低电平   | 0,1   | 如果是输出的话，就是： 1：输出高电平 0：输出低电平 |
|              | 输入上下拉状态 | 0,1,2 | 如果是输入的话,就是： 0：下拉 1: 上拉 2：悬空      |
