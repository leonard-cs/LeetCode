# Data Structures

## Table of Contents
- [Arrays](#arrays)
- [List](#list)
  - [Java List → Array](#java-list--array)
    - [Primitive Array (`int[]`)](#primitive-array-int)
    - [To Typed Array](#to-typed-array)
- Map
  - [HashMap](#hashmap)
- Set
  - [HashSet](#hashset)

## Arrays
### Initializing
```java
int[] arr = new int[5];          // Array of 5 integers (default value 0)
int[] arr2 = {1, 2, 3, 4, 5};    // Array with specific values
```
### Printing
```java
// Prints each row
for (int i = 0; i < arr.length; i++) {
    System.out.println(Arrays.toString(arr[i]));
}

// Prints the entire 2D array in one line
System.out.println(Arrays.deepToString(arr));
```

## List
### Initializing
```java
List<Type> list = new ArrayList<>();
List<Type> list = new LinkedList<>();

List<String> fruits = new ArrayList<>(Arrays.asList("Apple", "Banana", "Cherry"));
```

### Common Operations
```java
list.add(element);  // Add at the end
list.add(index, element);  // Add at specific index

list.get(index);  // Retrieve element by index

list.set(index, newElement);  // Replace element at index

list.remove(index);  // Remove by index
list.remove(element);  // Remove first occurrence of element

list.size();  // Get list size
list.contains(element);  // Check if contains element
list.isEmpty();  // Check if list is empty

Collections.sort(list);  // Sort in ascending order

list.clear();  // Remove all elements

Object[] array = list.toArray();
```
### Printing
```java
System.out.println(list);  // Prints list in [1, 2] format
```
### Java List → Array
#### Primitive Array (`int[]`)
```java
int[] arr = list.stream()
                .mapToInt(Integer::intValue)
                .toArray();
```
#### To Typed Array
```java
Integer[] arr = list.toArray(new Integer[0]);
```

### List Implementations
Java provides several types of lists. Here are a few examples:
- `ArrayList` (dynamic array, fast access, slower insertions/removals)
- `LinkedList` (linked list, slower access, fast insertions/removals)
- `Vector` (synchronized, slower than `ArrayList`)
- `Stack` (extends `Vector`, follows LIFO - Last In, First Out)
- `CopyOnWriteArrayList` (thread-safe, often used in multithreading)

## Map
### HashMap
#### Initializing
```java
Map<String, Integer> map = new HashMap<>();
map.put("one", 1);         // Add key-value pair
map.put("two", 2);
```

## Set
### HashSet
#### Initializing
```java
Set<Integer> set = new HashSet<>();
set.add(1);
set.add(2);
set.add(3);
```

## Deque
### ArrayDeque
#### Initializing
```java
import java.util.Deque;
import java.util.ArrayDeque;
Deque<Integer> dq = new ArrayDeque<>();
```

#### Common Operations
```java
dq.addFirst(10);   // throws exception if fails
dq.offerFirst(10); // returns false if fails
dq.addLast(20);
dq.offerLast(20);
dq.push(30); // same as addFirst()
dq.add(x);   // addLast(x)
dq.offer(x);  // offerLast(x)

dq.removeFirst(); // throws exception
dq.pollFirst();   // returns null if empty
dq.pop(); // same as removeFirst()
dq.remove();  // removeFirst()
dq.poll();    // pollFirst()
dq.removeLast();
dq.pollLast();
```
Peek (No Removal)
```java
dq.getFirst();  // throws exception
dq.peekFirst(); // returns null if empty
dq.peek();    // peekFirst()
dq.getLast();
dq.peekLast();
```
Check / Utility
```java
dq.isEmpty();
dq.size();
dq.contains(10);
dq.clear();
```

## StringBuilder
### Initializing
```java
StringBuilder sb = new StringBuilder("Hello");
sb.append(" World!");  // Append to StringBuilder
```
### Printing
```java
String str = sb.toString();  // Convert to String
```
