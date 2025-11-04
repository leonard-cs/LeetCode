# LeetCode

## Python Data Structures
### Arrays / Lists
### Linked Lists
### Stacks
### Queues
### Heaps

### Hash Maps (Dictionaries)
#### 1. Creating a Dictionary
```python
empty_dict = {}

my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}
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
### Priority Queues (using Heaps)

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