## 1. 自己添加的JSON字符串解析失败
>搜索JSON解析网页，先把这段JSON字符串放进网页里看JSON格式是否正确。如果正确，在看看自己代码里的转义字符有没有加对加全。

## 2. json.encode（）这个api生成的json顺序是随机的吗？
>是的，是随机的。

## 3. Air724为什么HTTP POST JSON格式的数据会出现失败
>检查一下是否忘记设置了"Content-Type: application/json"请求头。
>参考http的demo，在head参数中传入{[“Content-Type”]=“application/json”}。
