# Python Notes

## Table of Contents
- [Sorting](#sorting)
- [Functional Tools](#functional-tools)

## Sorting
### `sort()` vs `sorted()`
| Feature           | `sort()`   | `sorted()`      |
| ----------------- | ---------- | --------------- |
| Works on          | Lists only | Any iterable    |
| Modifies original | Yes        | No              |
| Returns           | None       | New sorted list |

- `sort()`:
    ```python
    data = [(1, 3), (4, 1), (2, 2)]
    data.sort(key=lambda x: x[1], reverse=True)
    ```

- `sorted()`:
    ```python
    data = [(1, 3), (4, 1), (2, 2)]
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
    ```

## Functional Tools
### `map()`
```python
nums = [1, 2, 3, 4]

squares = map(lambda x: x**2, nums)
print(list(squares))

def square(x):
    return x * x
print(list(map(square, [1, 2, 3])))
```

### `filter()`
```python
nums = [1, 2, 3, 4, 5, 6]

evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))
```
