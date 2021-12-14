## 第一章 作用域是什么

### 1.1 编译原理

传统编译语言的编译步骤：

- 分词/词法分析(Tokenizing/Lexing)

  > 分词(tokenizing)和词法分析(Lexing)之间的区别是非常微妙、晦涩的， 主要差异在于词法单元的识别是通过有状态还是无状态的方式进行的。简 单来说，如果词法单元生成器在判断 a 是一个独立的词法单元还是其他词法 单元的一部分时，调用的是有状态的解析规则，那么这个过程就被称为词法 分析。

- 解析/语法分析(Parsing)

  > 这个过程是将词法单元流(数组)转换成一个由元素逐级嵌套所组成的代表了程序语法 结构的树。这个树被称为“抽象语法树”(Abstract Syntax Tree，AST)。

- 代码生成

  > 将 AST 转换为可执行代码的过程称被称为代码生成。这个过程与语言、目标平台等息 息相关。

比起那些编译过程只有三个步骤的语言的编译器，JavaScript 引擎要复杂得多:

- 首先，JavaScript 引擎不会有大量的(像其他语言编译器那么多的)时间用来进行优化，因 为与其他语言不同，JavaScript 的编译过程不是发生在构建之前的。
- 对于 JavaScript 来说，大部分情况下编译发生在代码执行前的几微秒(甚至更短!)的时 间内。在我们所要讨论的作用域背后，JavaScript 引擎用尽了各种办法(比如 JIT，可以延 迟编译甚至实施重编译)来保证性能最佳。
- 简单地说，任何 JavaScript 代码片段在执行前都要进行编译(通常就在执行前)。

作用域是一套规则，用于确定在何处以及如何查找变量(标识符)。如果查找的目的是对变量进行赋值，那么就会使用 LHS 查询;如果目的是获取变量的值，就会使用 RHS 查询。

JavaScript引擎首先会在代码执行前对其进行编译，在这个过程中，像var a = 2这样的声 明会被分解成两个独立的步骤:

1. 首先，var a 在其作用域中声明新变量。这会在最开始的阶段，也就是代码执行前进行。
2. 接下来，a = 2 会查询(LHS 查询)变量 a 并对其进行赋值。

LHS 和 RHS 查询都会在当前执行作用域中开始，如果有需要(也就是说它们没有找到所 需的标识符)，就会向上级作用域继续查找目标标识符，这样每次上升一级作用域(一层 楼)，最后抵达全局作用域(顶层)，无论找到或没找到都将停止。

不成功的 RHS 引用会导致抛出 ReferenceError 异常。不成功的 LHS 引用会导致自动隐式 地创建一个全局变量(非严格模式下)，该变量使用 LHS 引用的目标作为标识符，或者抛 出 ReferenceError 异常(严格模式下)。



## 第二章 词法作用域

### 2.1 词法阶段

简单地说，词法作用域就是定义在词法阶段的作用域。换句话说，词法作用域是由你在写 代码时将变量和块作用域写在哪里来决定的，因此当词法分析器处理代码时会保持作用域 不变(大部分情况下是这样的)

作用域气泡由其对应的作用域块代码写在哪里决定，它们是逐级包含的。

#### 查找

**作用域查找会在找到第一个匹配的标识符时停止。**在多层的嵌套作用域中可以定义同名的 标识符，这叫作“遮蔽效应”(内部的标识符“遮蔽”了外部的标识符)。抛开遮蔽效应， 作用域查找始终从运行时所处的最内部作用域开始，逐级向外或者说向上进行，直到遇见 第一个匹配的标识符为止。

> 全局变量会自动成为全局对象(比如浏览器中的 window 对象)的属性，因此 可以不直接通过全局对象的词法名称，而是间接地通过对全局对象属性的引 用来对其进行访问。
>
> window.a
>
> 通过这种技术可以访问那些被同名变量所遮蔽的全局变量。但非全局的变量 如果被遮蔽了，无论如何都无法被访问到。

### 2.2 欺骗词法

#### 2.2.1 eval

```javascript

function foo(str, a) {
	eval( str ); // 欺骗! console.log( a, b );
}
var b = 2;
foo( "var b = 3;", 1 ); // 1, 3
```

在严格模式的程序中，eval(..) 在运行时有其自己的词法作用域，意味着其 中的声明无法修改所在的作用域。

```javascript
function foo(str) {
  "use strict";
	eval( str );
  console.log( a ); // ReferenceError: a is not defined
}
foo( "var a = 2" );
```

#### 2.2.2 with

```javascript
function foo(obj) { 
  with (obj) {
	a = 2; 
  }
}
var o1 = { 
  a: 3
};
var o2 = { 
  b: 3
};
foo( o1 );
console.log( o1.a ); // 2
foo( o2 );
console.log( o2.a ); // undefined
console.log( a ); // 2 —— 不好，a 被泄漏到全局作用域上了!
```

eval(..) 函数如果接受了含有一个或多个声明的代码，就会修改其所处的词法作用域，而 with 声明实际上是根据你传递给它的对象凭空创建了一个全新的词法作用域。

可以这样理解，当我们传递 o1 给 with 时，with 所声明的作用域是 o1，而这个作用域中含 有一个同 o1.a 属性相符的标识符。但当我们将 o2 作为作用域时，其中并没有 a 标识符， 因此进行了正常的 LHS 标识符查找(查看第 1 章)。

o2 的作用域、foo(..) 的作用域和全局作用域中都没有找到标识符 a，因此当 a=2 执行 时，自动创建了一个全局变量(因为是非严格模式)。

#### 2.2.3 性能

如果引擎在代码中发现了 eval(..) 或 with，它只能简单地假设关于标识符位置的判断 都是无效的，因为无法在词法分析阶段明确知道 eval(..) 会接收到什么代码，这些代码会 如何对作用域进行修改，也无法知道传递给 with 用来创建新词法作用域的对象的内容到底 是什么。

最悲观的情况是如果出现了 eval(..) 或 with，所有的优化可能都是无意义的，因此最简 单的做法就是完全不做任何优化。

如果代码中大量使用 eval(..) 或 with，那么运行起来一定会变得非常慢。无论引擎多聪 明，试图将这些悲观情况的副作用限制在最小范围内，也无法避免如果没有这些优化，代 码会运行得更慢这个事实。



## 第三章 函数作用域和块作用域

### 3.1 函数中的作用域

函数作用域的含义是指，属于这个函数的全部变量都可以在整个函数的范围内使用及复 用(事实上在嵌套的作用域中也可以使用)。这种设计方案是非常有用的，能充分利用 JavaScript 变量可以根据需要改变值类型的“动态”特性。

### 3.2 隐藏内部实现

为什么“隐藏”变量和函数是一个有用的技术?

有很多原因促成了这种基于作用域的隐藏方法。它们大都是从最小特权原则中引申出来 的，也叫最小授权或最小暴露原则。这个原则是指在软件设计中，应该最小限度地暴露必 要内容，而将其他内容都“隐藏”起来，比如某个模块或对象的 API 设计。

#### 规避冲突

“隐藏”作用域中的变量和函数所带来的另一个好处，是可以避免同名标识符之间的冲突， 两个标识符可能具有相同的名字但用途却不一样，无意间可能造成命名冲突。冲突会导致 变量的值被意外覆盖。

1. 全局命名空间

   变量冲突的一个典型例子存在于全局作用域中。当程序中加载了多个第三方库时，如果它 们没有妥善地将内部私有的函数或变量隐藏起来，就会很容易引发冲突。

   这些库通常会在全局作用域中声明一个名字足够独特的变量，通常是一个对象。这个对象 被用作库的命名空间，所有需要暴露给外界的功能都会成为这个对象(命名空间)的属 性，而不是将自己的标识符暴漏在顶级的词法作用域中。

2. 模块管理

   另外一种避免冲突的办法和现代的模块机制很接近，就是从众多模块管理器中挑选一个来 使用。使用这些工具，任何库都无需将标识符加入到全局作用域中，而是通过依赖管理器 的机制将库的标识符显式地导入到另外一个特定的作用域中。

### 3.3 函数作用域

```javascript
var a = 2;
(function foo(){ // <-- 添加这一行
	var a = 3;
	console.log( a ); // 3 
})(); // <-- 以及这一行
console.log( a ); // 2
```



区分函数声明和表达式最简单的方法是看 function 关键字出现在声明中的位 置(不仅仅是一行代码，而是整个声明中的位置)。如果 function 是声明中 的第一个词，那么就是一个函数声明，否则就是一个函数表达式。

#### 3.3.1 匿名和具名

1. 匿名函数在栈追踪中不会显示出有意义的函数名，使得调试很困难。
2. 如果没有函数名，当函数需要引用自身时只能使用已经过期的arguments.callee引用， 比如在递归中。另一个函数需要引用自身的例子，是在事件触发后事件监听器需要解绑自身。
3. 匿名函数省略了对于代码可读性/可理解性很重要的函数名。一个描述性的名称可以让 代码不言自明。

#### 3.3.2 立即执行函数表达式

```javascript
var a = 2;
(function IIFE( global ) {
	var a = 3;
	console.log( a ); // 3 
  console.log( global.a ); // 2
})( window );
console.log( a ); // 2
```

IIFE 还有一种变化的用途是倒置代码的运行顺序，将需要运行的函数放在第二位，在 IIFE 执行之后当作参数传递进去。这种模式在 UMD(Universal Module Definition)项目中被广 泛使用。尽管这种模式略显冗长，但有些人认为它更易理解。

```
var a = 2;
(function IIFE( def ) { 
	def( window );
})(function def( global ) {
  var a = 3;
  console.log( a ); // 3
  console.log( global.a ); // 2
});
```

### 3.4 块作用域

```javascript
for (var i=0; i<10; i++) {
	console.log( i );
}
```

我们在 for 循环的头部直接定义了变量 i，通常是因为只想在 for 循环内部的上下文中使用 i，而忽略了 i 会被绑定在外部作用域(函数或全局)中的事实。

#### 3.4.1 with

用 with 从对象中创建出的作用域仅在 with 声明中而非外 部作用域中有效。

#### 3.4.2 try/catch

```javascript

try {
	undefined(); // 执行一个非法操作来强制制造一个异常
}
catch (err) {
	console.log( err ); // 能够正常执行!
}
console.log( err ); // ReferenceError: err not found
```

#### 3.4.3 let

let 关键字可以将变量绑定到所在的任意作用域中(通常是 { ... } 内部)。

```javascript
var foo = true;
if (foo) {
	let bar = foo * 2;
	bar = something( bar ); 
	console.log( bar );
}
console.log( bar ); // ReferenceError
```

1.垃圾收集

```javascript
function process(data) {
// 在这里做点有趣的事情
}
var someReallyBigData = { .. };
process( someReallyBigData );
var btn = document.getElementById( "my_button" );
btn.addEventListener( "click", function click(evt) {
  console.log("button clicked");
}, /*capturingPhase=*/false );
```

click 函数的点击回调并不需要 someReallyBigData 变量。理论上这意味着当 process(..) 执 行后，在内存中占用大量空间的数据结构就可以被垃圾回收了。但是，由于 click 函数形成 了一个覆盖整个作用域的闭包，JavaScript 引擎极有可能依然保存着这个结构(取决于具体 实现)。

```javascript

function process(data) {
// 在这里做点有趣的事情
}
// 在这个块中定义的内容可以销毁了! 
{
  let someReallyBigData = { .. }; 
  process( someReallyBigData );
}
var btn = document.getElementById( "my_button" );
btn.addEventListener( "click", function click(evt){
	console.log("button clicked");
}, /*capturingPhase=*/false );
```

2.let循环

```javascript

for (let i=0; i<10; i++) {
	console.log( i );
}
console.log( i ); // ReferenceError
```

for 循环头部的 let 不仅将 i 绑定到了 for 循环的块中，事实上它将其重新绑定到了循环的每一个迭代中，确保使用上一个循环迭代结束时的值重新进行赋值。

```javascript
{
let j;
for (j=0; j<10; j++) {
	let i = j; // 每个迭代重新绑定!
  console.log( i );
  }
}

```

#### 3.4.4 const

除了 let 以外，ES6 还引入了 const，同样可以用来创建块作用域变量，但其值是固定的 (常量)。之后任何试图修改值的操作都会引起错误。



## 第四章

### 4.1 先有鸡还是先有蛋

```javascript
a = 2;
var a; 
console.log( a ); // 2
```

```javascript
console.log( a ); 
var a = 2; // undefined
```

### 4.2 编译器再度来袭

只有声明本身会被提升，而赋值或其他运行逻辑会留在原地。如果提升改变了代码执行的顺序，会造成非常严重的破坏。

### 4.3 函数优先

函数声明和变量声明都会被提升。但是一个值得注意的细节(这个细节可以出现在有多个“重复”声明的代码中)是函数会首先被提升，然后才是变量。

```javascript
foo(); // 1
var foo;
function foo() {
	console.log( 1 );
}
foo = function() {
	console.log( 2 );
};
```

```javascript
foo(); // 3
function foo() {
	console.log( 1 );
}
var foo = function() {
	console.log( 2 );
};
function foo() {
	console.log( 3 );
}

```











