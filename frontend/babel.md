# Babel为何物？

## Babel是一个JavaScript编译器

Babel 是一个工具链，主要用于将采用 ECMAScript 2015+ 语法编写的代码转换为向后兼容的 JavaScript 语法，以便能够运行在当前和旧版本的浏览器或其他环境中。Babel可以完成以下一些工作：

- 语法转换
- 通过 Polyfill 方式在目标环境中添加缺失的特性（通过第三方 polyfill 模块，例如 [core-js](https://github.com/zloirock/core-js)，实现）
- 源码转换
- 对代码进行各种形式的静态分析(Static analysis )

> Static analysis is the process of analyzing code without executing it. (Analysis of code while executing it is known as dynamic analysis). The purpose of static analysis varies greatly. It can be used for linting, compiling, code highlighting, code transformation, optimization, minification, and much more.

## 核心概念

[参考文档](https://github.com/jamiebuilds/babel-handbook/blob/master/translations/en/plugin-handbook.md#introduction)

### ASTs

@babel/core实际处理的对象是AST( [Abstract Syntax Tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree))，所以需要先把源代码解析成AST，所使用的的解析器修改自 [ESTree](https://github.com/estree/estree)。

如下一段代码：

```javascript
function square(n) {
  return n * n;
}
```

将被解析成如下的抽象语法树：

```
- FunctionDeclaration:
  - id:
    - Identifier:
      - name: square
  - params [1]
    - Identifier
      - name: n
  - body:
    - BlockStatement
      - body [1]
        - ReturnStatement
          - argument
            - BinaryExpression
              - operator: *
              - left
                - Identifier
                  - name: n
              - right
                - Identifier
                  - name: n
```

或者如下的javascript对象：

```javascript
{
  type: "FunctionDeclaration",
  id: {
    type: "Identifier",
    name: "square"
  },
  params: [{
    type: "Identifier",
    name: "n"
  }],
  body: {
    type: "BlockStatement",
    body: [{
      type: "ReturnStatement",
      argument: {
        type: "BinaryExpression",
        operator: "*",
        left: {
          type: "Identifier",
          name: "n"
        },
        right: {
          type: "Identifier",
          name: "n"
        }
      }
    }]
  }
}
```

抽象语法树的每一层有相似的结构：

```javascript
{
  type: "FunctionDeclaration",
  id: {...},
  params: [...],
  body: {...}
}
```

### Babel的工作流程

Babel的三个主要的工作流程按顺序分别是parse,transform,generate。

#### parse

parse阶段会将源码转换成抽象语法树，parse又分为词法分析([**Lexical Analysis**](https://en.wikipedia.org/wiki/Lexical_analysis) )和语法分析([**Syntactic Analysis**](https://en.wikipedia.org/wiki/Parsing))阶段。

##### 词法分析

词法分析是计算机科学中将字符序列转换为标记(token)序列的过程。

```javascript
n * n;
```

以上代码片段将会被转换成下面的标记序列：

```javascript
[
  { type: { ... }, value: "n", start: 0, end: 1, loc: { ... } },
  { type: { ... }, value: "*", start: 2, end: 3, loc: { ... } },
  { type: { ... }, value: "n", start: 4, end: 5, loc: { ... } },
  ...
]
```

其中的type字段会描述当前标记的一些属性：

```javascript
{
  type: {
    label: 'name',
    keyword: undefined,
    beforeExpr: false,
    startsExpr: true,
    rightAssociative: false,
    isLoop: false,
    isAssign: false,
    prefix: false,
    postfix: false,
    binop: null,
    updateContext: null
  },
  ...
}
```

##### 语法分析

语法分析会将标记序列转成抽象语法树，以便做后续处理。

#### Transform

Transform阶段会遍历AST节点，然后对节点做增删改操作，也是babel最重要，最复杂的代码逻辑部分。

#### Generate

代码生成阶段会将处理好的的AST转换成代码字符串，增加source maps。















