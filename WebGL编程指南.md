# 第1章 WebGL概述

WebGL是一项用来在网页上绘制和渲染复杂三维图形，并允许用户与之进行交互的技术。

## WebGL的优势

WebGL是内嵌在浏览器中的，允许javascript在网页上显示和操作三维图形，而且编写和发布的流程相对简单。

# 第2章	WebGL入门

## Canvas是什么？

\<canvas\>标签定义了网页上的绘图区域，\<canvas\>提供一些简单的绘图函数，用来绘制点、线、矩形、圆等，可以使用javascript动态的绘制图形。

由于\<cavans\>元素可以灵活地同时支持二维图形和三维图形，它不直接提供绘图方法，而是提供了一种叫上下文(context)的机制来进行绘图。canvas.getContext()方法的参数指定了上下文的类型(二维或三维)。
```javascript
// WebGL清空绘图区
function main() {
  var canvas = document.getElementById("webgl");

  var gl = getWebGLContext(canvas);

  if (!gl) {
    console.error("Failed to get the rendering context for WebGL");
    return;
  }
  // 指定绘图区域的背景色
  gl.clearColor(1.0, 0.0, 0.0, 1.0);
  // 清空颜色缓冲区，将导致WebGL清空页面上的<cavas>区域
  gl.clear(gl.COLOR_BUFFER_BIT);
}
```

### 着色器是什么？

在代码中，着色器程序是以字符串的形式嵌入在javascript文件中的，WebGL需要两种着色器。

- 顶点着色器(Vertex shader)：顶点着色器是用来描述顶点特性(如位置，颜色等)的程序。顶点(Vertex)是指二维或三维空间中的一个点。
- 片元着色器(Fragment shader)：进行逐片元处理过程如光照的程序。片元(fragment)是一个WebGL术语，可以将其理解为像素。

>  齐次坐标：齐次坐标使用如下的符号描述：$(x,y,z,w)$。齐次坐标等价于三维坐标$(x/w,y/w,z/w)$。所以如果齐次坐标的第4个分量是1，你就可以将它当做三维坐标来使用。$w$的值必须是大于等于0的。如果$w$趋近于0，那么它所表示的点将趋近无穷远。三维图形系统在计算过程中，通常使用齐次坐标来表示顶点的三维坐标。

```javascript
// 顶点着色器程序 （GLSL ES）语言
var VSHADER_SOURCE = 
`
  // 运行在WebGL系统中
  void main() {
    // 指定点的位置
    // 类型：vec4
    // 齐次坐标
    gl_Position = vec4(0.0, 0.0, 0.0, 1.0);
    // 指定点的尺寸
    // 类型：float
    gl_PointSize = 10.0;
  }
`;

// 片元着色器程序 （GLSL ES）语言
var FSHADER_SOURCE =
`
  // 运行在WebGL系统中
  void main() {
    // 指定点的颜色
    // gl_FragColor是片元着色器唯一的内置变量
    gl_FragColor = vec4(1.0, 0.0, 0.0, 1);
  } 
`;

// 主程序
function main() {
  var canvas = document.getElementById("webgl");

  var gl = getWebGLContext(canvas);

  if (!gl) {
    console.error("Failed to get the rendering context for WebGL");
    return;
  }
  // 初始化着色器
  if (!initShaders(gl, VSHADER_SOURCE, FSHADER_SOURCE)) {
    console.error("Failed to initialize shaders.");
  }

   // 指定绘图区域的背景色
   gl.clearColor(0.0, 0.0, 0.0, 1.0);

   // 清空颜色缓冲区，将导致WebGL清空页面上的<cavas>区域
   gl.clear(gl.COLOR_BUFFER_BIT);

   // 绘制一个点
   gl.drawArrays(gl.POINTS, 0, 1);
}
```

### WebGL坐标系统

默认情况下，WebGL使用右手坐标系。

![image-20210306123236327](WebGL编程指南.assets/image-20210306123236327.png)

### 使用attribute变量

