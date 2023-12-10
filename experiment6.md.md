# 实验六 Python函数

班级： 21计科2

学号： B20210302212

姓名： 李欣

Github地址：<https://github.com/sdgalk/lixin>

CodeWars地址：<https://www.codewars.com/users/lx666>

---

## 实验目的

1. 学习Python函数的基本用法
2. 学习lambda函数和高阶函数的使用
3. 掌握函数式编程的概念和实践

## 实验环境

1. Git
2. Python 3.10
3. VSCode
4. VSCode插件

## 实验内容和步骤

### 第一部分

Python函数

完成教材《Python编程从入门到实践》下列章节的练习：

- 第8章 函数

---

### 第二部分

在[Codewars网站](https://www.codewars.com)注册账号，完成下列Kata挑战：

---

#### 第一题：编码聚会1

难度： 7kyu

你将得到一个字典数组，代表关于首次报名参加你所组织的编码聚会的开发者的数据。
你的任务是返回来自欧洲的JavaScript开发者的数量。
例如，给定以下列表：

```python
lst1 = [
  { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
  { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
  { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
  { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
]
```

你的函数应该返回数字1。
如果，没有来自欧洲的JavaScript开发人员，那么你的函数应该返回0。

注意：
字符串的格式将总是"Europe"和"JavaScript"。
所有的数据将始终是有效的和统一的，如上面的例子。

这个卡塔是Coding Meetup系列的一部分，其中包括一些简短易行的卡塔，这些卡塔是为了让人们掌握高阶函数的使用。在Python中，这些方法包括：`filter`, `map`, `reduce`。当然也可以采用其他方法来解决这些卡塔。

代码提交地址：
<https://www.codewars.com/kata/coding-meetup-number-1-higher-order-functions-series-count-the-number-of-javascript-developers-coming-from-europe>

---

#### 第二题： 使用函数进行计算

难度：5kyu

这次我们想用函数来写计算，并得到结果。让我们看一下一些例子：

```python
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
```

要求：

- 从0（"零"）到9（"九"）的每个数字都必须有一个函数。
- 必须有一个函数用于以下数学运算：加、减、乘、除。
- 每个计算都由一个操作和两个数字组成。
- 最外面的函数代表左边的操作数，最里面的函数代表右边的操作数。
- 除法应该是整数除法。

例如，下面的计算应该返回2，而不是2.666666...。

```python
eight(divided_by(three()))
```

代码提交地址：
<https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39>

---

#### 第三题： 缩短数值的过滤器(Number Shortening Filter)

难度：6kyu

在这个kata中，我们将创建一个函数，它返回另一个缩短长数字的函数。给定一个初始值数组替换给定基数的 X 次方。如果返回函数的输入不是数字字符串，则应将输入本身作为字符串返回。

例子：

```python
filter1 = shorten_number(['','k','m'],1000)
filter1('234324') == '234k'
filter1('98234324') == '98m'
filter1([1,2,3]) == '[1,2,3]'
filter2 = shorten_number(['B','KB','MB','GB'],1024)
filter2('32') == '32B'
filter2('2100') == '2KB';
filter2('pippi') == 'pippi'
```

代码提交地址：
<https://www.codewars.com/kata/56b4af8ac6167012ec00006f>

---

#### 第四题： 编码聚会7

难度： 6kyu

您将获得一个对象序列，表示已注册参加您组织的下一个编程聚会的开发人员的数据。

您的任务是返回一个序列，其中包括最年长的开发人员。如果有多个开发人员年龄相同，则将他们按照在原始输入数组中出现的顺序列出。

例如，给定以下输入数组：
```python
list1 = [
  { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
  { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
  { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
  { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
]
```

您的程序应该返回如下结果：

```python
[
  { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
  { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
]
```

注意：

- 输入的列表永远都包含像示例中一样有效的正确格式的数据，而且永远不会为空。

代码提交地址：
<https://www.codewars.com/kata/582887f7d04efdaae3000090>

---

#### 第五题： Currying versus partial application

难度： 4kyu

[Currying versus partial application](https://2ality.com/2011/09/currying-vs-part-eval.html)是将一个函数转换为具有更小arity(参数更少)的另一个函数的两种方法。虽然它们经常被混淆，但它们的工作方式是不同的。目标是学会区分它们。

Currying

是一种将接受多个参数的函数转换为以每个参数都只接受一个参数的一系列函数链的技术。

Currying接受一个函数：

```python
f：X × Y → R
```

并将其转换为一个函数：

```python
f'：X → (Y → R)
```

我们不再使用两个参数调用f，而是使用第一个参数调用f'。结果是一个函数，然后我们使用第二个参数调用该函数来产生结果。因此，如果非curried f被调用为：

```python
f(3, 5)
```

那么curried f'被调用为：

```python
f'(3)(5)
```

示例
给定以下函数：

```python
def add(x, y, z):
  return x + y + z
```

我们可以以普通方式调用：

```python
add(1, 2, 3) # => 6
```

但我们可以创建一个curried版本的add(a, b, c)函数：

```python
curriedAdd = lambda a: (lambda b: (lambda c: add(a,b,c)))
curriedAdd(1)(2)(3) # => 6
```

Partial application
是将一定数量的参数固定到函数中，从而产生另一个更小arity(参数更少)的函数的过程。

部分应用接受一个函数：

```python
f：X × Y → R
```

和一个固定值x作为第一个参数，以产生一个新的函数

```python
f'：Y → R
```

f'与f执行的操作相同，但只需要填写第二个参数，这就是其arity比f的arity少一个的原因。可以说第一个参数绑定到x。

示例:

```python
partialAdd = lambda a: (lambda *args: add(a,*args))
partialAdd(1)(2, 3) # => 6
```

你的任务是实现一个名为curryPartial()的通用函数，可以进行currying或部分应用。

例如：

```python
curriedAdd = curryPartial(add)
curriedAdd(1)(2)(3) # => 6

partialAdd = curryPartial(add, 1)
partialAdd(2, 3) # => 6
```

我们希望函数保持灵活性。

所有下面这些例子都应该产生相同的结果：

```python
curryPartial(add)(1)(2)(3) # =>6 
curryPartial(add, 1)(2)(3) # =>6 
curryPartial(add, 1)(2, 3) # =>6 
curryPartial(add, 1, 2)(3) # =>6 
curryPartial(add, 1, 2, 3) # =>6 
curryPartial(add)(1, 2, 3) # =>6 
curryPartial(add)(1, 2)(3) # =>6 
curryPartial(add)()(1, 2, 3) # =>6 
curryPartial(add)()(1)()()(2)(3) # =>6 

curryPartial(add)()(1)()()(2)(3, 4, 5, 6) # =>6 
curryPartial(add, 1)(2, 3, 4, 5) # =>6 

curryPartial(curryPartial(curryPartial(add, 1), 2), 3) # =>6
curryPartial(curryPartial(add, 1, 2), 3) # =>6
curryPartial(curryPartial(add, 1), 2, 3) # =>6
curryPartial(curryPartial(add, 1), 2)(3) # =>6
curryPartial(curryPartial(add, 1)(2), 3) # =>6
curryPartial(curryPartial(curryPartial(add, 1)), 2, 3) # =>6
```

代码提交地址：
<https://www.codewars.com/kata/53cf7e37e9876c35a60002c9>

---

### 第三部分

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

- [第一部分 Python函数](#第一部分)
- [第二部分 Codewars Kata挑战](#第二部分)

第一题
```bash
def count_developers(lst):
    count = 0
    for developer in lst:
        if developer['continent'] == 'Europe' and developer['language'] == 'JavaScript':
            count += 1
    return count
```
第二题
```bash
def zero(operation=None):
    if operation:
        return operation(0)
    return 0

def one(operation=None):
    if operation:
        return operation(1)
    return 1

def two(operation=None):
    if operation:
        return operation(2)
    return 2

def three(operation=None):
    if operation:
        return operation(3)
    return 3

def four(operation=None):
    if operation:
        return operation(4)
    return 4

def five(operation=None):
    if operation:
        return operation(5)
    return 5
def six(operation=None):
    if operation:
        return operation(6)
    return 6

def seven(operation=None):
    if operation:
        return operation(7)
    return 7

def eight(operation=None):
    if operation:
        return operation(8)
    return 8

def nine(operation=None):
    if operation:
        return operation(9)
    return 9
def plus(num):
    return lambda x: x + num

def minus(num):
    return lambda x: x - num

def times(num):
    return lambda x: x * num

def divided_by(num):
    return lambda x: x // num  # 整数除法
```
第三题
```bash
def shorten_number(base):
    def inner(num):
        try:
            num = float(num)
            for unit in ['', 'K', 'M', 'B', 'T']:
                if abs(num) < 1000.0:
                    return f"{num:3.1f}{unit}"
                num /= 1000.0
            return f"{num:.1f}Q"
        except ValueError:
            return str(num)
    return inner
```

第四题
```bash
def find_senior(lst): 
    max_age = max([dev['age'] for dev in lst])
    return [dev for dev in lst if dev['age'] == max_age]
```
- [第三部分 使用Mermaid绘制程序流程图](#第三部分)

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

1. 什么是函数式编程范式？
   
   函数式编程是一种编程范式，它将计算机运算看作是数学中函数的计算，并且避免了状态以及变量的概念在函数式编程中，函数是一等公民，意味着函数可以被作为数据来处理，可以作为参数传递，也可以作为返回值。函数式编程的主要优点包括提高了代码的可预测性、可测试性和复用性，同时也支持并发和分布式计算函数式编程被广泛应用于各种领域，包括科学计算、数据分析、并发和分布式系统、Web开发等。
2. 什么是lambda函数？请举例说明。
   
   Lambda函数是一种匿名函数，它可以在一行代码中定义并调用。Lambda函数通常用于需要一个简单函数作为参数的场景，或者在需要一个临时函数的地方。Lambda函数由以下几个要素组成：
lambda关键字：lambda是Python中用于定义lambda函数的保留关键字。
参数：参数是lambda函数的输入值。
冒号：冒号用于分隔参数和函数体。
函数体：函数体是lambda函数的输出值。
以下是一个简单的lambda函数示例：
f = lambda x: x**2
print(f(3))
3. 什么是高阶函数？常用的高阶函数有哪些？这些高阶函数如何工作？使用简单的代码示例说明。
   
   高阶函数是一种函数，它接受一个或多个函数作为参数，并/或返回一个函数。高阶函数可以用于简化代码、提高代码的可读性和可维护性，以及实现更高级别的抽象。
以下是一些常用的高阶函数：
map()：将一个函数应用于一个序列中的每个元素，并返回一个新的序列，其中包含应用函数后的结果。例如，以下代码将列表中的每个元素加倍：
lst = [1, 2, 3, 4, 5]
new_lst = list(map(lambda x: x * 2, lst))
print(new_lst)  # Output: [2, 4, 6, 8, 10]
filter()：根据指定的条件过滤序列中的元素，并返回一个新的序列，其中包含符合条件的元素。例如，以下代码将列表中的所有偶数过滤出来：
lst = [1, 2, 3, 4, 5]
new_lst = list(filter(lambda x: x % 2 == 0, lst))
print(new_lst)  # Output: [2, 4]
reduce()：将一个函数应用于序列中的所有元素，并返回一个单一的值。例如，以下代码将列表中的所有元素相加：
from functools import reduce
lst = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, lst)
print(total)  # Output: 15
sorted()：根据指定的条件对序列中的元素进行排序，并返回一个新的序列。例如，以下代码将列表中的元素按照从小到大的顺序排序：
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
new_lst = sorted(lst)
print(new_lst)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
zip()：将两个或多个序列中的元素配对，并返回一个新的序列，其中包含元素对。例如，以下代码将两个列表中的元素配对：
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
new_lst = list(zip(lst1, lst2))
print(new_lst)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
## 实验总结

总结一下这次实验你学习和使用到的知识，例如：编程工具的使用、数据结构、程序语言的语法、算法、编程技巧、编程思想。

Lambda函数和高阶函数都是Python中的重要概念。Lambda函数是一种匿名函数，可以在需要时定义并传递给其他函数。高阶函数是参数或返回值包含函数的函数。Lambda函数通常作为高阶函数的参数使用。Python具备函数式编程的许多核心特征，因此可以借鉴其他函数式语言的设计模式和编程技术，编写出简洁优雅的代码。函数式编程的一般概念及特点包括迭代器、生成器表达式、内置函数、常用高阶函数、递归与归约、实用模块和装饰器的用法，以及避开Python严格求值顺序的变通方法、Web服务设计方法和一些优化技巧。
