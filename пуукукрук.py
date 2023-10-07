from itertools import *
k = 0
for x in product('айокс', repeat=5):
    s = ''.join(x)
    k+=1
    if s.count('о')<=1 and 'сс' not in s:
        print(k,s)