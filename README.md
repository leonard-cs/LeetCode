# LeetCode Notes

## Table of Contents
- [Python Data Structures](#python-data-structures)
    - [Lists](#lists)
    - [Dictionaries (Hash Maps)](#dictionaries-hash-maps)
- [Python Sorted Data Structures](#python-sorted-data-structures)
    - [Heap (Heap Queue)](#heap-heap-queue)
    - [Priority Queue](#priority-queue)
    - [Sorted List](#sorted-list-via-bisect-or-sortedcontainers)
    - [`SortedDict` and `SortedSet`](#sorteddict-and-sortedset-from-sortedcontainers)
    - [Binary Search Trees / AVL / Red-Black Trees](#binary-search-trees--avl--red-black-trees)
- [Python Tips](#python-tips)
    - [Sorting](#sorting)
    - [Counter](#counter)
    - [Bit Manipulation](#bit-manipulation)

## Python Data Structures
### Lists
#### Reverse a List
```python
my_list.reverse()              # in-place
reversed_list = my_list[::-1]  # creates a new list
reversed_list = list(reversed(my_list))
```

### Linked Lists
### Stacks
#### 1. Using Python List (Built-in Stack)
#### 2. Using `collections.deque` for a More Efficient Stack

### Queues
#### 1. 2. Using `collections.deque` (Efficient)
#### 2. Using `queue.Queue` for Thread-Safe Queues

### Double-ended Queue `deque`
```python
from collections import deque

# Create an empty deque
d = deque()
```
- `append(item)`: Adds an item to the right end of the deque.
- `appendleft(item)`: Adds an item to the left end of the deque.
- `pop()`: Removes and returns the item from the right end.
- `popleft()`: Removes and returns the item from the left end.
- `extend(iterable)`: Adds all items from the iterable to the right end.
- `extendleft(iterable)`: Adds all items from the iterable to the left end (note: it adds items in reverse order).
- `rotate(n)`: Rotates the deque by n steps. Positive n rotates right, negative n rotates left.

### Dictionaries (Hash Maps)
#### 1. Creating a Dictionary
```python
empty_dict = {}

my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

from collections import defaultdict
count = defaultdict(int)  # int → default 0; list → default []
```
#### 2. Accessing Dictionary Values
```python
print(my_dict['name'])  # Output: Alice
print(my_dict.get('age'))  # Output: 25

# Using get() avoids errors if the key doesn't exist
print(my_dict.get('gender', 'Not available'))  # Output: Not available
```
#### 3. Adding or Modifying Items
```python
# Adding a new key-value pair
my_dict['gender'] = 'Female'

# Modifying an existing key-value pair
my_dict['age'] = 26
```
#### 4. Removing Items
```python
# Removing a specific key-value pair using del
del my_dict['city']

# Removing a key-value pair using pop()
removed_value = my_dict.pop('age')  # It returns the value removed
print(removed_value)  # Output: 26

# Removing and returning the last key-value pair using popitem()
last_item = my_dict.popitem()
print(last_item)  # Output: ('gender', 'Female')
```
#### Dictionary Methods
- `.keys()` — Returns a view of all keys.
- `.values()` — Returns a view of all values.
- `.items()` — Returns a view of all key-value pairs.
- `.clear()` — Removes all items in the dictionary.
#### Merging Dictionaries
```python
# Using update() to merge dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Using the `|` operator (Python 3.9+)
merged = dict1 | dict2
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}
```
#### Sorting Dictionaries
```python
my_dict = {'banana': 3, 'apple': 2, 'orange': 1}

# Sorting by value and converting back to dictionary
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
```

### Sets
### Trees
### Graphs

## Python Sorted Data Structures
### Heap (Heap Queue)
```python
import heapq

numbers = [5, 3, 8, 1, 2]
heapq.heapify(numbers)     # converts list into a heap
print(numbers)             # [1, 2, 8, 3, 5] (heap order, not sorted order)

heapq.heappush(numbers, 0)
print(numbers)             # [0, 1, 8, 3, 5, 2]

smallest = heapq.heappop(numbers)
print(smallest)            # 0
```
**Key functions:**
- `heapify(list)` – turn list into a heap.
- `heappush(heap, item)` – push new item.
- `heappop(heap)` – pop smallest item.
- `nlargest(n, heap)` / `nsmallest(n, heap)` – get top n elements.
### Priority Queue
A priority queue can be implemented using `heapq` or `queue.PriorityQueue`.
```python
import heapq

tasks = []
heapq.heappush(tasks, (2, "write code"))
heapq.heappush(tasks, (1, "fix bugs"))
heapq.heappush(tasks, (3, "test program"))

while tasks:
    priority, task = heapq.heappop(tasks)
    print(priority, task)
```

### Sorted List (via `bisect` or `sortedcontainers`)
#### `bisect` module — standard library
```python
import bisect

nums = [1, 3, 5, 7]
bisect.insort(nums, 4)   # insert while keeping order
print(nums)              # [1, 3, 4, 5, 7]
```
#### `sortedcontainers` library — third-party (very efficient)
```bash
pip install sortedcontainers
```
```python
from sortedcontainers import SortedList

slist = SortedList(["apple", "kiwi", "banana"], key=len)
slist.add("fig")
slist.remove("banana")
print(slist)
# → SortedList(['fig', 'kiwi', 'apple'], key=<built-in function len>)
```
**Common Operations:**
| Operation                                | Description                                              | Time Complexity                                                   | Example                      |
| ---------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------- |
| **`add(x)`**                             | Insert an element in sorted order                        | **O(log n)**                                                      | `slist.add(10)`              |
| **`remove(x)`**                          | Remove a single element (raises `ValueError` if missing) | **O(log n)** (search) + **O(n)** (shifting) = **O(n)** worst-case | `slist.remove(10)`           |
| **`discard(x)`**                         | Same as remove, but no error if not found                | **O(n)** worst-case                                               | `slist.discard(10)`          |
| **`pop(i=-1)`**                          | Remove and return element at index `i`                   | **O(log n)** (to find block) + **O(1)** (within block)            | `slist.pop()`                |
| **`__getitem__(i)`**                     | Get element by index                                     | **O(log n)**                                                      | `x = slist[2]`               |
| **`__setitem__`**                        | Not supported (immutable order)                          | –                                                                 | –                            |
| **`__delitem__(i)`**                     | Delete element at index                                  | **O(log n)** (to find) + **O(1)** (to delete)                     | `del slist[0]`               |
| **`__contains__(x)`**                    | Membership test (binary search)                          | **O(log n)**                                                      | `if x in slist:`             |
| **`index(x)`**                           | Find index of element                                    | **O(log n)**                                                      | `pos = slist.index(10)`      |
| **`bisect_left(x)` / `bisect_right(x)`** | Find insertion point                                     | **O(log n)**                                                      | `pos = slist.bisect_left(5)` |
| **`count(x)`**                           | Count occurrences                                        | **O(log n)**                                                      | `slist.count(5)`             |
| **`update(iterable)`**                   | Add multiple elements                                    | **O(k log n)** where k = len(iterable)                            | `slist.update([1, 3, 2])`    |
| **`clear()`**                            | Remove all elements                                      | **O(1)**                                                          | `slist.clear()`              |
| **`__len__()`**                          | Get number of elements                                   | **O(1)**                                                          | `len(slist)`                 |
| **`__iter__()`**                         | Iterate over elements                                    | **O(n)**                                                          | `for x in slist:`            |
| **`copy()`**                             | Shallow copy                                             | **O(n)**                                                          | `slist.copy()`               |


### `SortedDict` and `SortedSet` (from `sortedcontainers`)
```python
from sortedcontainers import SortedDict, SortedSet

sset = SortedSet([5, 3, 1])
print(sset)             # SortedSet([1, 3, 5])

sdict = SortedDict({"b": 2, "a": 1})
print(sdict)            # SortedDict({'a': 1, 'b': 2})
```
### Binary Search Trees / AVL / Red-Black Trees
- `bintrees` (`pip install bintrees`)
- `binarytree` (for visualization)

## Python Tips
### Sorting 
```python
# Sort by age (ascending), then by salary (descending)
sorted_people_reverse = sorted(people, key=lambda p: (p.age, -p.salary))
```

### `Counter`
#### 1. Creating a Counter
```python
from collections import Counter

# Example 1: Count frequencies of elements in a list
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
counter = Counter(my_list)
```
#### Accessing Elements in a Counter
```python
print(counter['l'])  # Output: 3
print(counter['z'])  # Output: 0 (If the element does not exist, it returns 0)
```
#### Common Methods of Counter
```python
# Example: Get the 2 most common elements
most_common = counter.most_common(2)
# Example: Delete an element (key) from the Counter
del counter['apple']
# Example: Get all elements in the Counter
elements = list(counter.elements())
# Example: Update the counter with new data
counter.update(['apple', 'orange', 'grape'])
# Example: Subtract counts from the Counter
counter.subtract(['apple', 'banana'])
# Example: Clear the Counter
counter.clear()
```
#### Mathematical Operations with Counter
You can add (+), subtract (-), intersect (&), or unionize (|) Counter objects.
```python
result = counter1 + counter2
```

### Bit Manipulation
You can perform bitwise operations in Python using `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), and `>>` (right shift) on integers.
#### Printing in Binary
- `bin(n)`: Returns the binary representation with a "0b" prefix.
- `bin(n)[2:]`: Removes the "0b" prefix.
- `format(n, 'b')`: Provides a binary representation without the "0b" prefix.
- `format(n, '08b')`: Pads the binary representation to a fixed width (e.g., 8 bits).
- `f-string (f"{n:b}")`: A convenient way to get the binary representation in Python 3.6 and later.