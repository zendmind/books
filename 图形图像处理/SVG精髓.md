# SVG精髓

## 第一章 入门指南

### 1.1 图形系统

计算机中描述图形信息的两大系统是栅格图形(raster graphics)和矢量图形(vector graphics)。

#### 1.1.1 栅格图形

在栅格图形系统中，图形被表示为图片元素或者像素的长方形数组。

#### 1.1.2 矢量图形

在矢量图形系统中，图形被描述为一系列集合形状。矢量图形阅读器接受在指定坐标集上绘制形状的指令。

#### 1.1.3 栅格图形的用途

栅格图形最适合用来表示照片，因为照片很少由明显的线条和曲线组成。

#### 1.1.4 矢量图形的用途

矢量图形用于以下领域：

- 计算机辅助绘图程序
- 设计用于高分辨率打印图像的程序，例如Adobe Illustrator
- Adobe PostScript打印和成像语言
- 基于矢量图形的Macromedia Flash系统，用来设计动画、演示和网站

### 1.2 可缩放

矢量图形可以缩放而不损失图像质量。

### 1.3 SVG的作用

SVG是一个XML应用，能与其他XML处理程序结合使用。

### 1.4 创建一个SVG图像

#### 1.4.1 文档结构

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg width="140" height="170" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <title>Cat</title>
    <desc>Stick Figure of a Cat</desc>
    <circle cx="70" cy="95" r="50" style="stroke: black; fill: none;"  />
    <circle cx="55" cy="80" r="5" stroke="black" fill="#339933" />
    <circle cx="85" cy="80" r="5" stroke="black" fill="#339933" />
  	<!-- 图形对象分组 -->
    <g id="whiskers">
      <line x1="75" x2="135" y1="95" y2="85" stroke="black" />
      <line x1="75" x2="135" y1="95" y2="105" stroke="black" />
    </g>
    <use xlink:href="#whiskers" transform="scale(-1 1) translate(-140 0)" />
    <!-- 耳朵 -->
    <polyline points="108 62, 90 10, 70 45, 50 10, 32 62" stroke="black" fill="none" />
    <!-- 嘴 -->
    <polyline points="35 110, 45 120, 95 120, 105 110" stroke="black" fill="none" />
    <!-- 鼻子 -->
    <path d="M 75 90 L 65 90 A 5 10 0 0 0 75 90" style="stroke:black; fill: #ffcccc" />

    <text x="60" y="165" style="font-family: sans-serif; font-size: 14pt; stroke: none; fill: black;">Cat</text>
</svg>
```



## 第二章 在网页中使用SVG

### 2.1 将SVG作为图像

#### 2.1.1 在\<img\>元素内包含SVG

对于栅格图像来说，它固有尺寸就是它的像素尺寸，对于SVG来说，则更为复杂。如果文件中的根元素\<svg\>带有明确的height和width属性，则它们会被用作文件的固有尺寸。如果只指定height或者width而不是两个都指定，并且\<svg\>带有viewBox属性，那么将用viewBox计算高宽比，图像也会被缩放以匹配指定的尺寸。如果\<svg\>带有viewBox属性而没有尺寸，则viewBox的height和width将被视为像素长度。

#### 2.1.2 在CSS中包含SVG

### 2.2 将SVG作为应用程序

嵌入的SVG可以包含外部文件，同时脚本可以在该对象和父页面之间进行通信。

### 2.3 混合文档中的SVG标记

