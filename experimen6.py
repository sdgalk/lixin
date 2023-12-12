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