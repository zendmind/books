# Pro Git学习笔记

## 起步

### 关于版本控制

版本控制是一种记录一个或若干个文件内容变化，以便将来查阅特定版本修订情况的系统。

### 版本控制系统分为三种类型： 本地版本控制系统，集中化的版本控制系统和分布式版本控制系统
>1. 本地版本控制系统：采用简单的数据库来记录文件的历次更新差异，所有记录保存在本地。
>2. 集中化的版本控制系统：为了解决不同系统上的开发者协同工作问题，集中化的版本控制系统应运而生，由一个单一的服务器集中管理所有文件的修订版本。缺点是中央服务器的单点故障，如果中央服务器出现问题，所有人无法提交更新，如果中心数据库所在磁盘发生损坏，有没有恰当备份，整个项目的变更历史都将丢失。
>3. 分布式版本管理系统：客户端并不只提取最新版本的文件快照，而是把代码仓库完整地镜像 下来。 这么一来，任何一处协同工作用的服务器发生故障，事后都可以用任何一个镜像出来的本地仓库恢复。 因为每一次的克隆操作，实际上都是一次对代码仓库的完整备份。


## git基础
### Git在保存和对待各种信息的时候与其它版本控制系统有很大差异，尽管操作起来的命令形式非常相近，理解这些差异将有助于防止你使用中的困惑。

>### 直接记录快照，而非差异比较  
>Git 和其它版本控制系统(包括 Subversion 和近似工具)的主要差别在于 Git 对待数据的方法。 概念上来区分，其它大部分系统以文件变更列表的方式存储信息。 这类系统(CVS、Subversion、Perforce、Bazaar 等 等)将它们保存的信息看作是一组基本文件和每个文件随时间逐步累积的差异。  
>![git-pro-1](http://git.wangxutech.com/web/frontend/notes/books/raw/master/images/git-pro-1.jpg)  

>反之，Git 更像是把数据看作是对小型文件系统的一组快照。 每次你提交 更新，或在 Git 中保存项目状态时，它主要对当时的全部文件制作一个快照并保存这个快照的索引。 为了高效， 如果文件没有修改，Git 不再重新存储该文件，而是只保留一个链接指向之前存储的文件。 Git 对待数据更像是 一个 快照流。  
>![git-pro-1](http://git.wangxutech.com/web/frontend/notes/books/raw/master/images/git-pro-1.jpg)  

>### 近乎所有操作都是本地执行
>在 Git 中的绝大多数操作都只需要访问本地文件和资源，一般不需要来自网络上其它计算机的信息.包括提交和浏览项目历史，git都不需要连接服务器，你几乎可以在本地进行任何操作，等到有网络了再进行上传。  
>### Git保证完整性
>Git 中所有数据在存储前都计算校验和，然后以校验和来引用,校验机制是SHA-1散列，git数据中保存的信息都是以文件内容的哈希值来索引，而不是文件名。
>### Git一般只添加数据
>你执行的 Git 操作，几乎只往 Git 数据库中增加数据。 很难让 Git 执行任何不可逆操作，或者让它以任何方式清 除数据。
### 三种状态
>Git有三种状态，你的文件可能处于其中之一：已提交(committed)、已修改(modified)和已暂存(staged)。 已提交表示数据已经安全的 保存在本地数据库中。 已修改表示修改了文件，但还没保存到数据库中。 已暂存表示对一个已修改文件的当前 版本做了标记，使之包含在下次提交的快照中。
>![git-pro-3](http://git.wangxutech.com/web/frontend/notes/books/raw/master/images/git-pro-3.jpg)    

- Git 仓库目录是 Git 用来保存项目的元数据和对象数据库的地方。 这是 Git 中最重要的部分，从其它计算机克隆仓库时，拷贝的就是这里的数据。  
- 工作目录是对项目的某个版本独立提取出来的内容。 这些从 Git 仓库的压缩数据库中提取出来的文件，放在磁盘上供你使用或修改。  
- 暂存区域是一个文件，保存了下次将提交的文件列表信息，一般在 Git 仓库目录中。 有时候也被称作`‘索引’'，不过一般说法还是叫暂存区域。  
  
### 基本工作流程
1. 在工作目录中修改文件。
2. 暂存文件，将文件的快照放入暂存区域。
3. 提交更新，找到暂存区域的文件，将快照永久性存储到 Git 仓库目录。


## 初次运行配置
### git的配置变量存储在三个不同的位置
>1. /etc/config: 系统通用配置，使用 --system选项的git config时，会从此文件读写配置变量。
>2. !/.gitconfig 或 ~/.config/git/config: 系统当前用户的配置，使用 --global时，会从此文件读取配置变量。
>3. 当前使用仓库的 Git 目录中的 config 文件(就是 .git/config):针对该仓库。
每一个级别会覆盖上一个级别的配置。

### 配置用户信息
```
$ git config --global user.name "John Doe"  
$ git config --global user.email johndoe@example.com  
```

### 检查配置信息
```
$ git config --list
user.name=John Doe
user.email=johndoe@example.com
color.status=auto
color.branch=auto
color.interactive=auto
color.diff=auto
```

### 获取帮助
```
$ git help <verb>
$ git <verb> --help
$ man git-<verb>
```

## Git基础操作

### 获取Git仓库
1. 在现有目录中初始化仓库
```
$ git init
```
>该命令将创建一个名为 .git 的子目录，这个子目录含有你初始化的 Git 仓库中所有的必须文件，这些文件是 Git 仓库的骨干。 但是，在这个时候，我们仅仅是做了一个初始化的操作，你的项目里的文件还没有被跟踪。  
2. 克隆现有的仓库
```
$ git clone https://github.com/libgit2/libgit2 mylibgit
```
>该命令会克隆远程仓库并将本地创建的仓库名字变更为mlibgit

### git文件的生命周期
>![git-pro-4](http://git.wangxutech.com/web/frontend/notes/books/raw/master/images/git-pro-4.jpg)  

### 检查当前文件状态
```
$ git status
```

### 跟踪新文件
```
$ git add README
```

### 暂存已修改文件
```
$ git add CONTRIBUTING.md
```
>git add是个多功能命令:可以用它开始跟踪新文件，或者把已跟踪的文件放到暂存区，还能用于合并时把有冲突的文件标记为已解决状态等。 将这个命令理解为“添加内容到下一次提交中”而不是“将一个文件添加到项目中”要更加合适。

### 状态简览
```
$ git status -s
// or
$ git status --short
M README
MM Rakefile
A  lib/git.rb
M  lib/simplegit.rb
?? LICENSE.txt
```
>新添加的未跟踪文件前面有 ??标记，新添加到暂存区中的文件前面有A标记，修改过的文件前面有M标记。你可能注意到了M有两个可以出现的位置，出现在右边的M表示该文件被修改了但是还没放入暂存区，出现在靠左边的M表示该文件被修改了并放入了暂存区。 例如，上面的状态报告显示: README文件在工作区被修改了但是还没有将修改后的文件放入暂存区,lib/simplegit.rb文件被修改了并将修改后的文件放入了暂存区。而Rakefile在工作区被修改并提交到暂存区后又在工作区中被修改了，所以在暂存区和工作区都有该文件被修改了的记录。

### 忽略文件
>git使用.gitignore来指定git需要忽略的文件或者文件夹
>文件 .gitignore 的格式规范如下:  
>- 所有空行或者以 # 开头的行都会被 Git 忽略。
>- 可以使用标准的 glob 模式匹配。
>- 匹配模式可以以(/)开头防止递归。
>- 匹配模式可以以(/)结尾指定目录。
>- 要忽略指定模式以外的文件或目录，可以在模式前加上惊叹号(!)取反。

### git diff
```
$ git diff
```
>此命令比较的是工作目录中当前文件和暂存区域快照之间的差异，也就是修改之后还没有暂存起来的变化内容。
>若要查看已暂存的将要添加到下次提交里的内容，可以用git diff --cached 命令。


### 提交更新
```
$ git commit -m "提交信息"
```
>提交时记录的时存放在暂存区域的快照。

### 跳过使用暂存区域
```
$ git commit -a -m 'added new benchmarks'
```
>Git会自动把所有已经跟踪过的文件暂存起来一并提交，从而跳过git add步骤。