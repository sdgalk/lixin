# 实验五 Python数据结构与数据模型

班级： 21计科2

学号： B20210302212

姓名： 李欣

Github地址：<https://github.com/sdgalk/lixin>

CodeWars地址：<https://www.codewars.com/users/lx666>

---

## 实验目的

1. 学习Python数据结构的高级用法
2. 学习Python的数据模型

## 实验环境

1. Git
2. Python 3.10
3. VSCode
4. VSCode插件

## 实验内容和步骤

### 第一部分

在[Codewars网站](https://www.codewars.com)注册账号，完成下列Kata挑战：

---

#### 第一题：停止逆转我的单词

难度： 6kyu

编写一个函数，接收一个或多个单词的字符串，并返回相同的字符串，但所有5个或更多的字母单词都是相反的（就像这个Kata的名字一样）。传入的字符串将只由字母和空格组成。只有当出现一个以上的单词时，才会包括空格。
例如：

```python
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
```

代码提交地址：
<https://www.codewars.com/kata/5264d2b162488dc400000001>

提示：

- 利用str的split方法可以将字符串分为单词列表
例如：

```python
words = "hey fellow warrior".split()
# words should be ['hey', 'fellow', 'warrior']
```

- 利用列表推导将长度大于等于5的单词反转(利用切片word[::-1])
- 最后使用str的join方法连结列表中的单词。

---

#### 第二题： 发现离群的数(Find The Parity Outlier)

难度：6kyu

给你一个包含整数的数组（其长度至少为3，但可能非常大）。该数组要么完全由奇数组成，要么完全由偶数组成，除了一个整数N。请写一个方法，以该数组为参数，返回这个 "离群 "的N。

例如：

```python
[2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)
```

代码提交地址：
<https://www.codewars.com/kata/5526fc09a1bbd946250002dc>

---

#### 第三题： 检测Pangram

难度：6kyu

pangram是一个至少包含每个字母一次的句子。例如，"The quick brown fox jumps over the lazy dog "这个句子就是一个pangram，因为它至少使用了一次字母A-Z（大小写不相关）。

给定一个字符串，检测它是否是一个pangram。如果是则返回`True`，如果不是则返回`False`。忽略数字和标点符号。
代码提交地址：
<https://www.codewars.com/kata/545cedaa9943f7fe7b000048>

---

#### 第四题： 数独解决方案验证

难度：6kyu

数独背景

数独是一种在 9x9 网格上进行的游戏。游戏的目标是用 1 到 9 的数字填充网格的所有单元格，以便每一列、每一行和九个 3x3 子网格（也称为块）中的都包含数字 1 到 9。更多信息请访问：<http://en.wikipedia.org/wiki/Sudoku>

编写一个函数接受一个代表数独板的二维数组，如果它是一个有效的解决方案则返回 true，否则返回 false。数独板的单元格也可能包含 0，这将代表空单元格。包含一个或多个零的棋盘被认为是无效的解决方案。棋盘总是 9 x 9 格，每个格只包含 0 到 9 之间的整数。

代码提交地址：
<https://www.codewars.com/kata/63d1bac72de941033dbf87ae>

---

#### 第五题： 疯狂的彩色三角形

难度： 2kyu

一个彩色的三角形是由一排颜色组成的，每一排都是红色、绿色或蓝色。连续的几行，每一行都比上一行少一种颜色，是通过考虑前一行中的两个相接触的颜色而产生的。如果这些颜色是相同的，那么新的一行就使用相同的颜色。如果它们不同，则在新的一行中使用缺失的颜色。这个过程一直持续到最后一行，只有一种颜色被生成。

例如：
```python
Colour here:            G G        B G        R G        B R
Becomes colour here:     G          R          B          G
```


一个更大的三角形例子：

```python
R R G B R G B B
 R B R G B R B
  G G B R G G
   G R G B G
    B B R R
     B G R
      R B
       G
```

你将得到三角形的第一行字符串，你的工作是返回最后的颜色，这将出现在最下面一行的字符串。在上面的例子中，你将得到 "RRGBRGBB"，你应该返回 "G"。
限制条件： 1 <= length(row) <= 10 ** 5
输入的字符串将只包含大写字母'B'、'G'或'R'。

例如：

```python
triangle('B') == 'B'
triangle('GB') == 'R'
triangle('RRR') == 'R'
triangle('RGBG') == 'B'
triangle('RBRGBRB') == 'G'
triangle('RBRGBRBGGRRRBGBBBGG') == 'G'
```

代码提交地址：
<https://www.codewars.com/kata/5a331ea7ee1aae8f24000175>

提示：请参考下面的链接，利用三进制的特点来进行计算。
<https://stackoverflow.com/questions/53585022/three-colors-triangles>

---

### 第二部分

使用Mermaid绘制程序流程图

安装VSCode插件：

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

- [第一部分 Codewars Kata挑战](#第一部分)
  
第一题
```bash
def spin_words(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]
    return ' '.join(words)

```
 第二题
```bash
def find_outlier(integers):
    odds = [x for x in integers if x % 2 != 0]
    evens = [x for x in integers if x % 2 == 0]
    return odds[0] if len(odds) == 1 else evens[0]

```
第三题
```bash
def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return set(sentence.lower()) >= alphabet

```
第四题
```bash


```
- [第二部分 使用Mermaid绘制程序流程图](#第二部分)
  
 第一题流程图
```mermaid
graph LR
A[开始] --> B{拆分字符串}
B -- 是 --> C[判断单词长度是否大于等于5]
B -- 否 --> D[将原单词添加到结果列表]
C -- 是 --> E[翻转单词并添加到结果列表]
C -- 否 --> D
E --> F{遍历下一个单词}
F -- 是 --> C
F -- 否 --> G[连接结果列表中的单词并返回]
G --> H[结束]
```

第二题流程图
```mermaid
graph LR
A[开始] --> B{遍历整数列表}
B -- 偶数 --> C[将偶数添加到偶数列表]
B -- 奇数 --> D[将奇数添加到奇数列表]
C -- 有两个及以上偶数且只有一个奇数 --> E[返回奇数]
C -- 否则 --> B
D -- 有两个及以上奇数且只有一个偶数 --> F[返回偶数]
D -- 否则 --> B
B -- 结束 --> G[返回None]
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

**注意：不要使用截图，因为Markdown文档转换为Pdf格式后，截图会无法显示。**

## 实验考查

请使用自己的语言并使用尽量简短代码示例回答下面的问题，这些问题将在实验检查时用于提问和答辩以及实际的操作。

1. 集合（set）类型有什么特点？它和列表（list）类型有什么区别？
   
答：集合（set）类型是 Python 中的一种数据结构，它具有以下特点：
无序性：集合中的元素没有固定的顺序。
唯一性：集合中的元素是唯一的，不会包含重复的值。
可变性：集合是可变的，可以添加、删除和修改元素。
与集合相比，列表（list）类型有以下区别：
有序性：列表中的元素按照插入的顺序有序排列。
允许重复元素：列表中的元素允许重复。
可变性：列表是可变的，可以修改元素的值，添加和删除元素。
2. 集合（set）类型主要有那些操作？
   
   答：1.s.add(x)：向集合 s 中添加元素 x。
2.s.update(iterable)：向集合 s 中添加可迭代对象 iterable 中的所有元素。
3.S.remove(x)：从集合 s 中删除元素 x，如果元素不存在则会抛出 KeyError 异常。
4.s.discard(x)：从集合 s 中删除元素 x，如果元素不存在不会抛出异常。
5.s.pop()：随机删除集合 s 中的一个元素，并返回该元素。
6.s.clear()：清空集合 s 中的所有元素。
7.s.copy()：复制集合 s 生成一个新的集合。
8.len(s)：返回集合 s 中元素的个数。
9.x in s：判断元素 x 是否在集合 s 中。
10.s.isdisjoint(other)：判断集合 s 和集合 other 是否不相交。
11.s.issubset(other) 或者 s <= other：判断集合 s 是否是集合 other 的子集。
12.s.issuperset(other) 或者 s >= other：判断集合 s 是否是集合 other 的超集。
13.s.union(other) 或者 s | other：返回集合 s 和集合 other 的并集。
14.s.intersection(other) 或者 s & other：返回集合 s 和集合 other 的交集。
15.s.difference(other) 或者 s - other：返回集合 s 相对于集合 other 的差集。
16.s.symmetric_difference(other) 或者 s ^ other：返回集合 s 和集合 other 的对称差集。
3. 使用`*`操作符作用到列表上会产生什么效果？为什么不能使用`*`操作符作用到嵌套的列表上？使用简单的代码示例说明。
   
   答：
   在Python中，使用`*`操作符作用到列表上会将列表中的元素复制指定的次数。例如，如果我们有一个列表[1, 2, 3]，并且我们想将其复制3次，我们可以使用以下代码：
my_list = [1, 2, 3]
new_list = my_list * 3
print(new_list)
这将输出[1, 2, 3, 1, 2, 3, 1, 2, 3]，其中列表中的元素被复制了3次。
但是，不能使用`*`操作符作用于嵌套的列表上，因为它会导致意外的结果。例如，如果我们有一个嵌套的列表[[1, 2], [3, 4]]，并且我们想将其复制2次，我们可能会尝试使用以下代码：
my_list = [[1, 2], [3, 4]]
new_list = my_list * 2
print(new_list)
这将输出[[1, 2], [3, 4], [1, 2], [3, 4]]，其中我们得到了两个相同的子列表，而不是我们期望的4个单独的列表。这是因为*操作符只是复制了原始列表的引用，而不是复制其内容
4. 总结列表,集合，字典的解析（comprehension）的使用方法。使用简单的代码示例说明。
   
   答：列表解析
new_list = [expression for item in iterable if condition]
其中，expression 是一个表达式，item 是可迭代的对象或值，iterable 是一个列表、集合、元组、字典或生成器，condition 是一个可选的条件语句。
以下是一个简单的例子，它生成一个包含 0 到 4 这 5 个数字的列表：
my_list = [a for a in range(5)]
print(my_list)  # [0, 1, 2, 3, 4]
如果想对 0 到 4 的数字乘以 2，可以这样写：
my_list = [a * 2 for a in range(5)]
print(my_list)  # [0, 2, 4, 6, 8]
如果想对可迭代对象进行过滤，可以加上一个条件语句，比如：
my_list = [a * 2 for a in range(5) if a > 0]
print(my_list)  # [2, 4, 6, 8]
集合解析
集合解析的语法与列表解析类似，只不过它生成的是一个集合。以下是一个简单的例子，它生成一个包含 0 到 4 的数字的集合：
my_set = {a for a in range(5)}
print(my_set)  # {0, 1, 2, 3, 4}
字典解析
字典解析的语法如下：
new_dict = {key_expression: value_expression for item in iterable if condition}
其中，key_expression 和 value_expression 是表达式，item 是可迭代的对象或值，iterable 是一个列表、集合、元组、字典或生成器，condition 是一个可选的条件语句。
以下是一个简单的例子，它生成一个包含 0 到 4 的数字的字典：
my_dict = {a: a * 2 for a in range(5)}
print(my_dict)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
## 实验总结

总结一下这次实验你学习和使用到的知识，例如：编程工具的使用、数据结构、程序语言的语法、算法、编程技巧、编程思想。

答：python数据模型是python中对象的属性。 数据模型其实是对python框架的描述，它规范了这门语言自身构建模块的接口，这些模块包括但不限于序列、迭代器、函数、类和上下文管理器。
