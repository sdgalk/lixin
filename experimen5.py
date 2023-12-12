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