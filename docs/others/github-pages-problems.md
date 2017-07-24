---
title: Github Pages
description: Github Pages使用过程中的一些小问题
---

**本文仅讨论关于如何使用Github Pages提供的markdown渲染。**

**使用本地渲染后托管HTML代码的方式，不在本文讨论范围。**

# 修改默认模板
在Github pages服务中，我们不仅仅可以选择主题(虽然真的好少/(ㄒoㄒ)/~~)，还可以对所对应主题所提供的默认模板进行修改。

步骤很简单，这里以`jekyll-cayman-theme`为例:

1. 找到对应的[项目](https://github.com/pages-themes/cayman)。
1. 找到`_layouts/`文件夹下的`default.html`文件并下载。
1. 在我们的pages页面根目录下新建一个`_layouts`文件夹，并将`default.html`放进去。
1. 自此我们本地的`default.html`将会覆盖Github Pages提供的默认模板，如要修改模板的话，直接在本地的`default.html`修改即可。

# 添加代码高亮
因为Github Pages服务的渲染限制，其jekyllrb不支持使用插件。

所以，在此我采用的解决方案是使用基于js的`highlight.js`。

为了使用简单(其实是懒)，我这里直接使用官网所提供的cdn链接。

步骤也很简单:

1. 在模板文件的`<head>`中添加三行代码。
    ``` html
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/default.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/highlight.min.js"></script>
    <script>hljs.initHighlightingOnLoad();</script>
    ```
1. 然后提交，等Github Pages重新生成后刷新即可。

# 添加二维码
为了方便移动端阅读，我在每个页面中都添加了二维码。

添加二维码最粗暴的途径就是先生成二维码图片，然后添加图片链接。

但显然这种方式太麻烦了，为了简化文件结构，我这里使用了js来生成当前页面的二维码。

因为也是直接调用第三方库的，所以步骤一如既往的简单:

1. 在你想要添加二维码的位置，添加以下代码:
    ``` html
    <script src="https://cdn.bootcss.com/jquery/1.8.2/jquery.min.js"></script>
    <script src="https://cdn.bootcss.com/jquery.qrcode/1.0/jquery.qrcode.min.js"></script>
    <div id="qrcode">
        <script>
        $('#qrcode').qrcode({
                width:256,
                height:256,
                render: "canvas",
                correctLevel: 0,
                foreground: "#50abab",
                text: document.URL
        });
    ```
1. 其中，`width`和`height`根据你所需要的尺寸来设置,`foreground`为二维码所显示的颜色(这么简单的代码，当然只是单色二维码咯,,ԾㅂԾ,,)，`correctLevel`的话，对于不添加任何修饰的二维码而言，设置最低就行了。
1. 但是，以这种形式添加二维码的话，有两个弊病：
    1. 不能显示中文URL。
    1. 对于较低版本的IE浏览器来说，不支持以`canvas`方式进行绘制。
    >解决方法可以参考[余斗的博客](http://www.yudouyudou.com/jiaochengheji/wangzhanjianshe/426.html)