nginx学习笔记
=

# 1.1 Nginx简介
## 1.1.1 web服务器
### 1. Apache
>Apache(Apache HTTP Server)是目前广泛流行的 Web 服务器软件，具有开放源代码、 跨平台、安全稳定等特点。但由于 Apache 在设计之初 对性能和资源的消耗没有过多的关注，导致在应对高并发的业务场景时，被一些轻量级的高性能Web服务器赶超。
### 2. Tomcat
>Tomcat(Apache Tomcat)主要用于Java Web环境，是一个运行Servlet 和 JSP 的容器。在静态资源和高并发方面的性能较弱，因此经常和Apache等软件搭配，实现动静态请求分离。
### 3. Lighttpd
>由德国人发起的轻量级开源Web服务器软件Lighttpd，不仅实现了Apache的常用功能，同时还保持了轻量级的优势，具有低内存开销、低CPU占用率、性能高以及模块丰富等特点 。 
### 4. Nginx
>Nginx(读作 engine x)是一个轻量级开源Web服务器软件，可以作为反向代理、负载均衡与缓存服务器使用。Nginx和Lighttpd都是为高并发网站的应用场景而设计的。
### 5. Microsoft IIS
>IIS(Internet Information Services ，互联网信息服务)是Microsoft(微软)公司的Web服务器产品，运行在Windows Server平台，具有图形界面管理工具。

## 1.1.2 Nginx概述
>- Nginx 是俄罗斯人Igor Sysoev开发的一个开源的高性能Web服务器软件，起初是为Rambler. ru(俄罗斯访问量第二的大型门户网站和搜索引擎)使用的，具有轻量级和高并发的特点，第一个公开版本0.1.0发布于2004年10月。目前，Nginx通过BSD-like开源软件许可协议发行，可以在UNIX、Linux、macOS、Solaris以及Windows等操作系统中运行。
>- Nginx可以提供HTTP服务，包括处理静态文件，支持SSL(提供HTTPS访问)、GZIP(网页压缩)、虚拟主机、URL重写等功能，可以搭配FastCGI程序(如 PHP)处理动态请求。除此之外，Nginx还可以用于代理、反向代理、负载均衡、缓存等服务器功能，在集群环境中解决网络负载、提高可用性等。





