# 合宙资料中心

本资料中心包含合宙模组的所有资料

- [产品手册](./product_manual/index.md)
- [问答中心](https://chat.openluat.com/)
- [合宙官网](https://www.openluat.com/)

<script>
var tmp = window.location.pathname.split("/").filter(part => part.length > 0);
console.log(tmp)
var redirectUrl = 'product_manual/';
if (tmp.length == 0 || (tmp.length == 2 && window.location.pathname.endsWith("/"))) {
    // 如果符合，跳转到指定URL
    window.location.href = window.location.pathname + redirectUrl;
}
// 检查当前页面是否是首页
var path = window.location.pathname
</script>
