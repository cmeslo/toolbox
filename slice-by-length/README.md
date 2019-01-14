# Slice string by length

source:
```
122333444455555666666
```

config:
```
n = [1, 2, 3, 4, 5, 6]
```

result:
```
1-22-333-4444-55555-666666
```

## Code
```python
from itertools import islice

s = '122333444455555666666'
n = [1, 2, 3, 4, 5, 6]

it = iter(s)
s = '-'.join(''.join(islice(it, 0, x)) for x in n)
print(s)

```
