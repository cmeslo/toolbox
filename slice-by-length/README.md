# Slice string by different length

Source:
```
122333444455555666666
```

Config:
```
n = [1, 2, 3, 4, 5, 6]
```

Expect (without trail):
```
1-22-333-4444-55555-666666
```

## Code (method 1)
```python
from itertools import islice

s = '122333444455555666666'
n = [1, 2, 3, 4, 5, 6]

it = iter(s)
s = '-'.join(''.join(islice(it, 0, x)) for x in n)
trail = ''.join(it)

print(s + '-' + trail)

```

## Code (method 2)
```python
s = '122333444455555666666'
n = [1, 2, 3, 4, 5, 6]

d = []
start = 0
for x in n:
    d.append(s[start:start+x])
    start += x
d.append(s[start:])
print('-'.join(d))
```
