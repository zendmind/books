Mastering PostCSS for Web Design
=

翻译自: [Mastering PostCSS for Web Design](http://git.wangxutech.com/web/frontend/notes/books/blob/master/pdf/Mastering%20PostCSS%20for%20Web%20Design.pdf)

# PostCSS简介

## 该部分讨论的主要内容
>- 创建预处理器的好处
>- 介绍PostCSS并探索其功能
>- 搭建开发环境
>- 使用PostCSS的一个小例子
>- 探索PostCSS的工作方式及其架构

SASS, Stylus, Haml 和 Less 都是近年来出现的编译器，使用这些编译器，能让我们更好的组织代码结构、复用代码，让样式代码的可维护性更高，但是他们都有以下一些缺点：
>- 或多或少都有依赖库，比如SASS就依赖于Ruby
>- 项目中可能只使用了少量的预处理代码，但是却被迫依赖整个大型库，比如SASS
>- 编译时间比较长，单次编译可能会感受不到，但是多次编译会累积成巨大的等待时间

## PostCSS介绍
PostCSS包含两部分，一部分是核心工具，另一部分是其插件生态系统。核心工具能完成的功能不多，但是其插件生态系统里的各式各样的插件能帮助我们完成各种各样的任务，具体来说有以下功能或者说是优势：
>- 它的模块化架构使我们能挑选使用其中的部分模块功能，减少整体库的大小
>- 现有的处理系统倾向于从预处理和后处理二者选其一，而PostCSS允许我们在同一个处理过程中同时进行两种处理
>- PostCSS可以无缝嵌入到各种任务管理工具，比如gulp，grunt等
>- 编译过程没有其他依赖，只要安装了Node.js就可以运行
>- 无需学习其他语言，只要懂Javascript就可以配置开发
>- 可以自由配置修改现有的各种插件
>- 编写修改插件的门槛很低
>- 相比于其他处理系统，速度更快

## 搭建开发环境
1. 下载并安装Node.js
2. 



