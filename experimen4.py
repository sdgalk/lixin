第一题
  ```bash
  def naughty_or_nice(data):
    naughty_count = 0
    nice_count = 0

    for month in data:
        for day in data[month]:
            if data[month][day] == 'Naughty':
                naughty_count += 1
            elif data[month][day] == 'Nice':
                nice_count += 1

    if naughty_count > nice_count:
        return 'Naughty!'
    elif nice_count > naughty_count:
        return 'Nice!'
    else:
        return 'Nice!'
  ```
    第二题
  ```bash
  def get_pins(observed):
    adjacent_digits = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9'],
        '0': ['0', '8']
    }
    result = []
    for digit in observed:
        result.append(adjacent_digits[digit])
    from itertools import product
    return list(map(''.join, product(*result)))
  ```
    第三题
  ```bash
  def protein(rna):
    protein = ''
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon in PROTEIN_DICT:
            amino_acid = PROTEIN_DICT[codon]
            if amino_acid == 'Stop':
                break
            protein += amino_acid
    return protein
  ```
    第四题
  ```bash
    def fillable(stock, merch, n):
    if merch in stock and stock[merch] >= n:
        return True
    else:
        return False
  ```