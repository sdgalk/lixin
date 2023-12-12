# 实验一 Git和Markdown基础

班级： 21计科2

学号： B20210302212

姓名： 李欣

Github地址：<https://github.com/sdgalk/lixin>

---

## 实验目的

1. Git基础，使用Git进行版本控制
2. Markdown基础，使用Markdown进行文档编辑

## 实验环境

1. Git
2. VSCode
3. VSCode插件

## 实验内容和步骤

### 第一部分 实验环境的安装

1. 安装git，从git官网下载后直接点击可以安装：[git官网地址](https://git-scm.com/)
2. 从Github克隆课程的仓库：[课程的仓库地址](https://github.com/zhoujing204/python_course)，运行git bash应用（该应用包含在git安装包内），在命令行输入下面的命令（命令运行成功后，课程仓库会默认存放在Windows的用户文件夹下）

```bash
git clone https://github.com/zhoujing204/python_course.git
```

如果你在使用`git clone`命令时遇到SSL错误，请运行下面的git命令(这里假设你的Git使用了默认安装目录)：

```bash
git config --global http.sslCAInfo "C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt"
```

或者运行下面的命令:

```bash
git config --global http.sslVerify false
```

如果遇到错误：`error setting certificate file` 或者 `warning: http.sslcaInfo has multiple values`，请运行下面的命令重新指定git的安全证书：

```bash
git config --global --unset-all http.sslCAInfo
git config --global http.sslCAInfo "C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt"
```

或者使用下面的命令编辑git配置文件，打开编辑器手动输入编辑配置信息

```bash
git config --global --edit
```

该仓库的课程材料后续会有更新，如果需要更新课程材料，可以在本地课程仓库的目录下运行下面的命令：

```bash
git pull
```

在本地的仓库内容有更新后，可以运行下面的命令，将本地仓库的内容和远程仓库的内容同步：

```bash
git push origin main
```

3. 注册Github账号或者Gitee帐号，创建一个新的仓库，例如：<https://gitee.com/zj204/python_task.git>，使用下面的命令将新建的仓库clone到本地：

```bash
git clone https://gitee.com/zj204/python_task.git
```

如果已经关联了远程仓库，显示结果如下：

```bash
origin  https://github.com/zhoujing204/python_course.git (fetch)
origin  https://github.com/zhoujing204/python_course.git (push)
```

如果还没有关联远程仓库，可以使用你创建的远程仓库的地址和下面的命令，添加你要关联的远程仓库：

```bash
git remote add gitee https://gitee.com/zj204/python_task.git
```

接下来准备好你的远程仓库账号的邮箱地址和密码，使用下面的命令下载远程仓库的内容更新本地仓库：

```bash
git pull gitee main
```

运行下面的命令，将本地仓库的内容同步到远程仓库：

```bash
git push gitee main
```

4. 安装VScode，下载地址：[Visual Studio Code](https://code.visualstudio.com/)
5. 安装下列VScode插件
   - GitLens
   - Git Graph
   - Git History
   - Markdown All in One
   - Markdown Preview Enhanced
   - Markdown PDF
   - Auto-Open Markdown Preview
   - Paste Image
   - markdownlint

### 第二部分 Git基础

教材《Python编程从入门到实践》P440附录D：使用Git进行版本控制，按照教材的步骤，完成Git基础的学习。

### 第三部分 learngitbranching.js.org

访问[learngitbranching.js.org](https://learngitbranching.js.org)，如下图所示完成Main部分的Introduction Sequence和Ramping Up两个小节的学习。

![Learngitbranching.js.org](/Experiments/img/2023-07-28-21-07-40.png)

上面你学习到的git命令基本上可以应付百分之九十以上的日常使用，如果你想继续深入学习git，可以：

- 继续学习[learngitbranching.js.org](https://learngitbranching.js.org)后面的几个小节（包括Main和Remote）
- 在日常的开发中使用git来管理你的代码和文档，用得越多，记得越牢
- 在git使用过程中，如果遇到任何问题，例如：错误删除了某个分支、从错误的分支拉取了内容等等，请查询[git-flight-rules](https://github.com/k88hudson/git-flight-rules)

### 第四部分 Markdown基础

查看[Markdown cheat-sheet](http://www.markdownguide.org/cheat-sheet)，学习Markdown的基础语法

使用Markdown编辑器（例如VScode）编写本次实验的实验报告，包括[实验过程与结果](#实验过程与结果)、[实验考查](#实验考查)和[实验总结](#实验总结)，并将其导出为 **PDF格式** 来提交。

如何将markdown文件转换为pdf格式的文件？

- 安装vscode插件Markdown PDF，安装后重启vscode，打开markdown文件，按下`Ctrl+Shift+P`，输入`Markdown PDF: Export (pdf)`，回车即可导出pdf文件。
- 使用Google Chrome浏览器，在Github网站或者Gitee网站打开你的仓库，浏览你的markdown文件，按下`Ctrl+P`，选择`打印`，选择`目标打印机`为`另存为PDF`，点击`保存`即可导出pdf文件。

## 实验过程与结果

请将实验过程中编写的代码和运行结果放在这里，注意代码需要使用markdown的代码块格式化，例如Git命令行语句应该使用下面的格式：

![Git命令](/Experiments/img/2023-07-26-22-48.png)

显示效果如下：

```bash
git init
git add .
git status
git commit -m "first commit"
```

如果是Python代码，应该使用下面代码块格式，例如：

![Python代码](/Experiments/img/2023-07-26-22-52-20.png)

显示效果如下：

```python
def add_binary(a,b):
    return bin(a+b)[2:]
```

代码运行结果的文本可以直接粘贴在这里。

**注意：不要使用截图，Markdown文档转换为Pdf格式后，截图可能会无法显示。**

1.[git commit]
```bash
 git commit
 git commit
```
2.[git branch]
```bash
git branch bugFix
git checkout bugFix
```
3.[git merge]
```bash
git branch bugFix
git checkout bugFix
git commit
git checkout main
git commit
git merge bugFix
```
4.[git rebase]
```bash
git branch bugFix
git checkout bugFix
git commit
git checkout main
git commit
git checkout bugFix
git rebase main
```
5.分离HEAD
```bash
git checkout bugFix
```
6.[相对引用（^）]
```bash
git checkout bugFix^
```
7.[相对引用2（~）]
```bash
git branch -f main c6
git checkout c1
git branch -f bugFix c0
```

## 实验考查

请使用自己的语言回答下面的问题，这些问题将在实验检查时用于提问和答辩，并要求进行实际的操作。

1. 什么是版本控制？使用Git作为版本控制软件有什么优点？
   
   答： 版本控制是一种用于管理和跟踪软件项目中文件和代码变化的系统。它允许开发团队记录、跟踪
和协调不同版本的文件和代码，并提供了协同工作、版本追踪、回滚和合并等功能。
Git是一个流行的分布式版本控制系统，有以下优点：
1.分布式系统：Git是一种分布式版本控制系统，每个开发者都可以在本地完整地保存代码仓库的副
本，并且可以在没有网络连接的情况下工作。这使得开发者可以更加灵活地管理代码和进行版本控制。
2.高效性能：Git的设计目标之一是快速和高效地处理大型项目。Git使用了一种称为快照的概念来存
储文件的状态，而不是存储文件的差异。这种设计使得Git在处理大量文件和提交时更加高效。
3.强大的分支管理：Git的分支管理非常灵活和强大。开发者可以轻松地创建、合并和删除分支，这使
得并行开发和特性分支的管理变得更加简单和可靠。
4.版本追踪和回滚：Git可以跟踪每个提交的变化，包括文件内容的修改、添加和删除等。这使得开发
者可以轻松地查看项目的历史记录，并回滚到之前的版本。
5.社区支持和广泛应用：Git是一个开源软件，拥有庞大的用户社区和广泛的应用。这意味着可以找到
大量的文档、教程和支持资源，方便开发者学习和解决问题。

2. 如何使用Git撤销还没有Commit的修改？如何使用Git检出（Checkout）已经以前的Commit？（实际操作）
   要撤销还没有 Commit 的修改，可以使用以下 Git 命令：
1.如果只是想撤销对某个文件的修改，可以使用以下命令：
git checkout -- <文件路径>
这将会丢弃对该文件的修改，恢复为最近一次 Commit 时的状态。
如果想撤销所有还没有添加到暂存区的修改，可以使用以下命令：
git checkout .
这将会丢弃所有尚未添加到暂存区的修改，恢复为最近一次 Commit 时的状态。
2.要检出已经过去的某个 Commit，可以使用以下 Git 命令：
首先，可以使用以下命令查看项目的提交历史：
git log
这将显示所有的提交记录，包括 Commit 的哈希值和提交信息。
找到想要检出的特定 Commit 的哈希值（通常是 Commit 哈希的前几个字符），然后使用以下命令进
行检出：
git checkout <Commit哈希>
例如，如果要检出哈希为 “abc123” 的 Commit，就可以使用：
git checkout abc123
这将会将代码库切换到指定 Commit 的状态，你可以查看和修改文件，在此状态下进行操作。
3. Git中的HEAD是什么？如何让HEAD处于detached HEAD状态？（实际操作）
   在Git中，HEAD是一个指针，它指向当前被检出的分支或者特定的提交（Commit）。它可以看作是当
前工作树的快照，用于确定你正在操作的位置。
让HEAD处于detached HEAD状态意味着将HEAD指向一个具体的提交，而不是指向一个分支。这种状态
下，你不能够进行分支操作，而是可以直接在这个提交上进行工作或查看。
以下是让HEAD进入detached HEAD状态的操作步骤：
1.首先，可以使用以下命令查看当前的提交状态以及分支情况：
git log --oneline --decorate
2.找到你想要让HEAD指向的特定提交的哈希值（通常是哈希的前几个字符），然后使用以下命令进入
detached HEAD状态：
git checkout <Commit哈希>
4. 什么是分支（Branch）？如何创建分支？如何切换分支？（实际操作）
   分支是Git中的一个重要概念，它可以让你在不影响主分支的情况下进行代码的修改和提交。创建分支
可以让你在不同的分支上进行不同的开发工作，而切换分支则可以让你在不同的分支之间进行切换。
以下是创建和切换分支的步骤：
创建分支：执行 git branch <branch-name> 命令，其中 <branch-name> 是你想要创建的分支名
称。例如，如果你想要创建一个名为 dev 的新分支，则可以执行 git branch dev 命令。
切换分支：执行 git checkout <branch-name> 命令，其中 <branch-name> 是你想要切换到的分
支名称。例如，如果你想要切换到名为 dev 的分支，则可以执行 git checkout dev 命令。
5. 如何合并分支？git merge和git rebase的区别在哪里？（实际操作）
   要合并分支，你可以使用 git merge 命令。该命令将指定的分支合并到当前所在的分支中。例如，如
果你想要将名为 dev 的分支合并到当前所在的分支中，则可以执行 git merge dev 命令。
git merge 和 git rebase 都是用于合并分支的命令，但它们之间有一些区别。主要区别在于它们如
何将更改应用于目标分支。
1.git merge：将指定分支的更改合并到当前所在的分支中。它会创建一个新的提交来表示合并操作，
并保留所有原始提交的历史记录。这意味着你可以轻松地查看所有更改的来源，并跟踪它们是如何被合
并到目标分支中的。
2.git rebase：将当前所在分支上的更改应用于指定分支。它会将当前所在分支上的所有提交复制到
指定分支上，并创建一个新的提交来表示这些更改。这意味着你可以获得一个更干净、更线性的提交历
史记录，但也可能会丢失一些原始提交的上下文信息。
6. 如何在Markdown格式的文本中使用标题、数字列表、无序列表和超链接？（实际操作）
Markdown是一种轻量级标记语言，它可以让你使用简单的文本格式来创建富文本内容。以下是如何在
Markdown格式的文本中使用标题、数字列表、无序列表和超链接的步骤：
（1）标题：要创建标题，请在标题文字前添加井号 。井号的个数即表示是几级标题，最低可到六级标
题。例如，要创建一级标题，请在标题文字前添加一个井号。
（2）数字列表：要创建数字列表，请在每个列表项前添加数字并紧跟一个英文句点。数字不必按数学
顺序排列，但是列表应当以数字 1 起始。例如，要创建一个数字列表，请在每个列表项前添加数字和
句点，如：


1. 第一项
2. 第二项
3. 第三项
（3）无序列表：要创建无序列表，请在每个列表项前面添加减号 - 或星号 * 或加号 + ，这三种符
号都可以使用，也可以混用，但这样写的话预览效果中行距有所不同，因此不建议混用，符号后需要添
加空格。例如，要创建一个无序列表，请在每个列表项前添加减号和空格，如：
- 第一项
- 第二项
- 第三项
（4）超链接：要创建超链接，请使用方括号 [] 包含链接文本和圆括号 () 包含链接地址。例如，要
创建一个指向 Bing 的超链接，请使用以下语法：
Bing
## 实验总结

总结一下这次实验你学习和使用到的知识，例如：编程工具的使用、数据结构、程序语言的语法、算法、编程技巧、编程思想。
通过这次实验我熟悉了Git基础，学会了使用Git进行版本控制，以及Markdown的基础，使用Markdown
进行文档编辑。学会安装和配置Git工具，并使用命令行界面进行版本控制操作。学习了Markdown的基
本语法、标记和样式，以及如何在Markdown文档中添加标题、列表、链接、图片和代码块等元素。了
解了Git中的核心数据结构，包括Commit、Branch、Head等，以及它们之间的关联关系。熟悉了一些
常用命令的语法和参数，例如git init、git commit、git checkout等。了解了一些基本的算法概
念，如提交对象的哈希值和树对象的构建。学会使用Git提供的一系列工具和命令来管理代码，如状态
查看、分支创建、合并冲突解决等。