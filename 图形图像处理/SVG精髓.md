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
   
</svg>
```

