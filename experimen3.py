第一题  
  ```
  def solution(number):
    if number < 0:
        return 0
        sum = 0
        for i in range(1,number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
            return sum
  ```  
    第二题  
  ```
  def duplicate_encode(word):
    word = word.lower()
    s = ''
    for ch in word:
        if word.count(ch) > 1:
            s += ')'
        else :
            s += '('
    return s
  ```  
  第三题

    ```
  def valid_braces(string):
    s = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in string:
        if char in mapping:
            if not s or s.pop() != mapping[char]:
                return False
        else:
            s.append(char)
    return len(s) == 0
  ```  


  第五题  
  ```
  def disemvowel(string_):
    
    s = "aeiouAEIOU"
    res = ""
    
    for char in string_:
        if char not in s:
            res += char
    
    return res
  ```