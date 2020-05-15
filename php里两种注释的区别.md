php代码里 `//` 注释和 `/* */`注释的区别
=

从基本功能来看，`//`是对一行代码的注释说明, `/* */` 是对一块代码的注释说明，从代码注释的功能来看，以下两行注释代码是完全相同的：
```
<?php
  $a = 1; // 我是注释
  $a = 1; /* 我是注释 */
?>
```
但是，如果把这段代码解析成AST，就会发现 `//` 和 `/* */`有很大的区别:
在上面那段代码中，解析出来的AST包含的expressionstatement有两个，也就是两个assign表达式，关键在于两个expressionstatement的'leadingComments'和'trailingComments'部分，第一个expressionstatement是没有leadingComments和trailingComments的，而第二个expressionstatement同时包含了leadingComments和trailingComments,其中 \`// 我是注释 \` 变成了第二个expressionstatement的leadingComments, \` /* 我是注释 */ \` 变成了第二个expressionstatement的trailingComments,也就是说，`//`这种格式的注释会默认算作下一个expressionstatement的leadingComments,这在对php文件作解析的时候非常重要，比如下面的翻译字段：
```
<?php
  'Product Price' => '$%s', // 产品价格
  'Annual Price' => '$%s<span class="unit">/year</span>', // 年度价格
?>
```
如果想要读取翻译字段，value和注释，上面这种写法，就需要进行一些特殊处理，因为在AST里面，\`// 产品价格 \` 是对应到下一行的leadingComments的，需要做一个平移操作才能对应到正确的翻译字段,如果按下面这种写法，就不存在这种问题
```
<?php 

?>
```



