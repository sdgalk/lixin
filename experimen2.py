第一题：


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

第二题：

def bouncing_ball(h, bounce, window):
    if h<=0 or bounce<=0 or bounce>=1 or window>=h:
       return -1

    count = 1
    
    while h * bounce >window:
        count += 2
        h= h* bounce
        
    return count  

  

第三题：

def get_count(sentence):
    s = ['a','e','i','o','u']
    count = 0
    for ch in sentence:   
        if ch=='a' or ch=='e' or ch == 'i' or ch== 'o' or ch== 'u':
            count +=1
    return count
    
    

第四题：

def even_or_odd(number):
    if number%2 == 0:
        return "Even"
    else :
        return "Odd"



