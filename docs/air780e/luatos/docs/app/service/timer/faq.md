# 常见问题

1.使用定时器sys.wait()或者sys.waitUntil()，程序出错。

sys.wait()和sys.waitUntil()只能用于task中

2.sys.timerLoopStart定时器的值，可以用变量动态改动吗？

不可以，第一次调用的时候会把值传进去，之后会用第一次传的值，不会随着变量值的变化而改变。
