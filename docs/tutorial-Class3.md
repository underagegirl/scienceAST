# HTTP协议

## HTTP URL

格式为:**http://host[:port][abs_path]**

* http 表示通过HTTP协议来定位网络资源
* host 表示主机域名或IP地址
* port 表示端口号，默认端口为80
* abs_path 指定请求资源的URI
> 若abs_path 为空，则必须给出'/'，在日常使用过程中，该步骤由浏览器完成

### Question

以下HTTP URL在浏览器中均可打开百度首页，但哪些是符合HTTP协议规范的？
1. www.baidu.com
1. http://www.baidu.com/
1. http://www.baidu.com:80
1. http://www.baidu.com:80/

## HTTP 请求

HTTP请求由三部分组成，分别为：请求行、报文头、请求正文
![HTTP请求](./img/Class3-1.png)

* 请求行

    请求行以请求方法开头，后面跟请求的URI和协议的版本，中间以空格隔开

    格式参见截图第一行

    > Method Request-URI HTTP-Version CRLF

    >常用的Method有：
    >1. GET
    >1. POST
    >1. PUT
    >1. DELETE

* 报文头

    简单的说，服务器可以根据报文头中的数据来返回不同响应。具体的参数的用处将会在反爬虫中介绍。

* 请求正文

    包含了在请求响应时所需的额外数据。(部分请求不包含请求正文)

### Question
