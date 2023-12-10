# 实验二 Python变量、简单数据类型

班级： 21计科2班

学号：B20210302212

姓名： 李欣

Github地址：<https://github.com/sdgalk/lixin>

CodeWars地址：<https://www.codewars.com/users/lx666>

---

## 实验目的

1. 使用VSCode编写和运行Python程序
2. 学习Python变量和简单数据类型

## 实验环境

1. Git
2. Python 3.10
3. VSCode
4. VSCode插件

## 实验内容和步骤

### 第一部分

实验环境的安装

1. 安装Python，从Python官网下载Python 3.10安装包，下载后直接点击可以安装：[Python官网地址](https://www.python.org/downloads/)
2. 为了在VSCode集成环境下编写和运行Python程序，安装下列VScode插件
   - Python
   - Python Environment Manager
   - Python Indent
   - Python Extended
   - Python Docstring Generator
   - Jupyter
   - indent-rainbow
   - Jinja

---

### 第二部分

Python变量、简单数据类型和列表简介

完成教材《Python编程从入门到实践》下列章节的练习：

- 第2章 变量和简单数据类型

---

### 第三部分

在[Codewars网站](https://www.codewars.com)注册账号，完成下列Kata挑战：

---

#### 第1题：求离整数n最近的平方数（Find Nearest square number）

难度：8kyu

你的任务是找到一个正整数n的最近的平方数
例如，如果n=111，那么nearest_sq(n)（nearestSq(n)）等于121，因为111比100（10的平方）更接近121（11的平方）。
如果n已经是完全平方（例如n=144，n=81，等等），你需要直接返回n。
代码提交地址
<https://www.codewars.com/kata/5a805d8cafa10f8b930005ba>

---

#### 第2题：弹跳的球（Bouncing Balls）

难度：6kyu

一个孩子在一栋高楼的第N层玩球。这层楼离地面的高度h是已知的。他把球从窗口扔出去。球弹了起来,  例如:弹到其高度的三分之二（弹力为0.66）。他的母亲从离地面w米的窗户向外看,母亲会看到球在她的窗前经过多少次（包括球下落和反弹的时候）？

一个有效的实验必须满足三个条件：

- 参数 "h"（米）必须大于0
- 参数 "bounce "必须大于0且小于1
- 参数 “window "必须小于h。

如果以上三个条件都满足，返回一个正整数，否则返回-1。
**注意:只有当反弹球的高度严格大于窗口参数时，才能看到球。**
代码提交地址
<https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python>

---

#### 第3题： 元音统计(Vowel Count)

难度： 7kyu

返回给定字符串中元音的数量（计数）。对于这个Kata，我们将考虑a、e、i、o、u作为元音（但不包括y）。输入的字符串将只由小写字母和/或空格组成。

代码提交地址：
<https://www.codewars.com/kata/54ff3102c1bad923760001f3>

---

#### 第4题：偶数或者奇数（Even or Odd）

难度：8kyu

创建一个函数接收一个整数作为参数，当整数为偶数时返回”Even”当整数位奇数时返回”Odd”。
代码提交地址：
<https://www.codewars.com/kata/53da3dbb4a5168369a0000fe>

### 第四部分

使用Mermaid绘制程序流程图

安装Mermaid的VSCode插件：

- Markdown Preview Mermaid Support
- Mermaid Markdown Syntax Highlighting

使用Markdown语法绘制你的程序绘制程序流程图（至少一个），Markdown代码如下：

![程序流程图](/Experiments/img/2023-08-05-22-00-00.png)

显示效果如下：

```mermaid
flowchart LR
    A[Start] --> B{Is it?}
    B -->|Yes| C[OK]
    C --> D[Rethink]
    D --> B
    B ---->|No| E[End]
```

查看Mermaid流程图语法-->[点击这里](https://mermaid.js.org/syntax/flowchart.html)

使用Markdown编辑器（例如VScode）编写本次实验的实验报告，包括[实验过程与结果](#实验过程与结果)、[实验考查](#实验考查)和[实验总结](#实验总结)，并将其导出为 **PDF格式** 来提交。

## 实验过程与结果

请将实验过程与结果放在这里，包括：

- [第二部分 Python变量、简单数据类型和列表简介](#第二部分)
- [第三部分 Codewars Kata挑战](#第三部分)


第一题：

```bash
def nearest_sq(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return n
    else:
        i = 1
        while i * i <= n:
            i += 1
        return (i - 1) ** 2 if (n - (i - 1) ** 2) < (i ** 2 - n) else i ** 2
```
第二题：
```bash
def bouncing_ball(h, bounce, window):
    if h<=0 or bounce<=0 or bounce>=1 or window>=h:
       return -1

    count = 1
    
    while h * bounce >window:
        count += 2
        h= h* bounce
        
    return count  

  
```
第三题：
```bash
def get_count(sentence):
    s = ['a','e','i','o','u']
    count = 0
    for ch in sentence:   
        if ch=='a' or ch=='e' or ch == 'i' or ch== 'o' or ch== 'u':
            count +=1
    return count
    
    
```

第四题：
```bash
def even_or_odd(number):
    if number%2 == 0:
        return "Even"
    else :
        return "Odd"

  
```
- [第四部分 使用Mermaid绘制程序流程图](#第四部分)

第一题：
```bash
flowchart LR
   A[Start]  --> B{sqrt_n**2==n}
   B  -->|Yes| C[return n]
   C  -->D[end]
   B  -->|no| E[lower_sq=sqrt_n**2, uower_sq=++sqrt_n**2] 
   E  -->F{n - lower_sq < upper_sq - n}
   F  -->|yes| G[return lower_sq]
   G  -->D
   F  -->|no| H[return upper_sq]
   H  -->D
```
第二题：
```bash
flowchart LR
   A[Start]  --> B{h<=0 or bounce<=0 or bounce>=1 or window>=h}
   B  -->|Yes| C[return -1]
   C  -->D[end]
   B  -->|no| E[count = 1] 
   E  -->F{h * bounce >window}
   F  -->|yes| G[count += 2
        h= h* bounce]
   G  -->F
   F  -->|no| H[return count]
   H  -->D
```
第三题：
```bash
flowchart LR
   A[Start]  --> B[s ='a','e','i','o','u', count = 0, for ch in sentence]
   B  --> C{ch=='a' or ch=='e'
   or ch == 'i' or ch== 'o'
   or ch== 'u'}
   C  -->|no| D[return count] 
   C  -->|yes| E[count +=1]
   E  -->C
   D  -->F[end]
```
第四题：
```bash
flowchart LR
   A[Start]  --> B{number%2 == 0}
   B  -->|Yes| C[return Even]
   B -->|No| D[return Odd]
   C -->E[end]
   D -->E
```
注意代码需要使用markdown的代码块格式化，例如Git命令行语句应该使用下面的格式：

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

## 实验考查

请使用自己的语言并使用尽量简短代码示例回答下面的问题，这些问题将在实验检查时用于提问和答辩以及实际的操作。

1. Python中的简单数据类型有那些？我们可以对这些数据类型做哪些操作？
   
  答： Python中常用的简单数据类型有6种：数字 (Number)、字符串 (String)、列表 (List)、元组 (Tuple)、字典 (Dictionary)、集合 (Set)。其中数字类型包括整数、浮点数、布尔值和复数。字符串类型是由字符组成的序列，可以进行索引、切片、分割和长度等操作。列表和元组都是有序的数据集合，可以进行索引、切片、循环、长度和包含等操作。字典是无序的键值对集合，可以进行增加、删除和查询等操作。集合是无序的不重复数据集合，可以进行增加、删除和交集等操作。

2. 为什么说Python中的变量都是标签？
   
  答： Python中的变量是标签，而不是盒子。这意味着变量不是存储数据的容器，而是指向存储数据的内存地址的标签。当我们创建一个变量时，Python会在内存中分配一些空间来存储该变量的值，并将该空间的地址分配给该变量。因此，当我们使用变量时，实际上是在引用该内存地址中存储的值。这种方式使得Python中的变量非常灵活，可以指向任何类型的对象，并且可以随时更改指向的对象。

3. 有哪些方法可以提高Python代码的可读性？
   
   答：Python中的代码可读性是非常重要的，因为它可以帮助其他人更好地理解和维护你的代码。以下是一些提高Python代码可读性的方法：
1.遵循PEP8规范：PEP8是Python编码规范指南，它提供了一些关于代码布局、命名规范、注释等方面的建议，遵循这些规范可以使你的代码更加整洁、易读。
2.使用有意义的变量名：使用有意义的变量名可以使你的代码更加易读。变量名应该简洁明了，能够准确地描述变量所代表的含义。
3.编写清晰的注释：注释可以帮助其他人更好地理解你的代码。注释应该清晰明了，能够准确地描述代码所实现的功能。
4.使用空格和缩进：使用空格和缩进可以使你的代码更加易读。在Python中，使用4个空格作为一个缩进级别是一个很好的习惯。
5.减少代码行数：减少代码行数可以使你的代码更加简洁、易读。你可以通过使用列表推导式、生成器表达式等方式来减少代码行数。
6.使用函数和类：使用函数和类可以使你的代码更加模块化、易读。函数和类可以将复杂的逻辑封装起来，使得代码更加易于理解和维护。
7.避免使用魔法数字：魔法数字是指在代码中出现的没有明确含义的数字。应该将这些数字定义为常量，并使用常量来代替魔法数字。

## 实验总结

总结一下这次实验你学习和使用到的知识，例如：编程工具的使用、数据结构、程序语言的语法、算法、编程技巧、编程思想。

通过这个实验，我学习了Python中的变量和简单数据类型。我还学习了如何使用Mermaid绘制程序流程图。在实验中，我发现Python的变量是标签而不是盒子，这意味着变量不是存储数据的容器，而是指向存储数据的内存地址的标签。
为了提高Python代码的可读性，我们可以遵循PEP8规范、使用有意义的变量名、编写清晰的注释、使用空格和缩进、减少代码行数、使用函数和类以及避免使用魔法数字等方法。并且通过这次实验我更好的理解了Python编程语言。·
