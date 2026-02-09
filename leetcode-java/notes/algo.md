# Algorithms

## Table of Contents
- [Sorting](#sorting)
  - [Sorting Arrays](#sorting-arrays)
  - [Sorting a List](#sorting-a-list)
- Tree
  - [Inorder Traversal (BST Rule)](#inorder-traversal-bst-rule)

## Sorting
### Sorting Arrays
```java
// Ascending order
int[] arr = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3};
Arrays.sort(arr); // Default is ascending

// Descending order using a custom comparator
Integer[] arrDesc = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3};
Arrays.sort(arrDesc, Collections.reverseOrder()); // Use Collections.reverseOrder() for descending
```
#### Sorting with `Arrays.sort()` for Custom Object Arrays
```java
Person[] people = {
    new Person("Alice", 30),
    new Person("Bob", 25),
    new Person("Charlie", 35)
};

// Sort by age
Arrays.sort(people, (p1, p2) -> Integer.compare(p1.age, p2.age));
```
#### Sorting a 2D Array
```java
int[][] arr = {
    {3, 1, 4},
    {9, 2, 6},
    {5, 8, 7}
};

// Sort by second column, then by third column
Arrays.sort(arr, new Comparator<int[]>() {
    @Override
    public int compare(int[] row1, int[] row2) {
        // First compare by second column (index 1)
        int cmp = Integer.compare(row1[1], row2[1]);
        if (cmp != 0) {
            return cmp;
        }
        // If second column is equal, compare by third column (index 2)
        return Integer.compare(row1[2], row2[2]);
    }
});
```

### Sorting a List
```java
// Ascending order
List<Integer> list = Arrays.asList(3, 1, 4, 1, 5, 9, 2, 6, 5, 3);
Collections.sort(list); // Default is ascending

// Descending order
List<Integer> listDesc = Arrays.asList(3, 1, 4, 1, 5, 9, 2, 6, 5, 3);
Collections.sort(listDesc, Collections.reverseOrder()); // Descending order
```

#### Sorting a 2D List (List of Lists)
```java
List<List<Integer>> listOfLists = new ArrayList<>();
listOfLists.add(Arrays.asList(3, 1, 4));
listOfLists.add(Arrays.asList(1, 2, 5));
listOfLists.add(Arrays.asList(2, 8, 3));

// Sort by the first element in each inner list
Collections.sort(listOfLists, (a, b) -> Integer.compare(a.get(0), b.get(0)));
```

#### Sorting with Multiple Criteria
Sort first by the first element, and then by the second element if the first elements are equal:
```java
Collections.sort(listOfLists, (a, b) -> {
    int cmp = Integer.compare(a.get(0), b.get(0));
    if (cmp != 0) {
        return cmp;
    }
    return Integer.compare(a.get(1), b.get(1));
});
```

#### Sorting with Custom Comparators
```java
class Person {
    String name;
    int age;
    
    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

List<Person> people = Arrays.asList(
    new Person("Alice", 30),
    new Person("Bob", 25),
    new Person("Charlie", 35)
);

// Sort by age (ascending)
Collections.sort(people, (p1, p2) -> Integer.compare(p1.age, p2.age));

// Sort by name (ascending)
Collections.sort(people, (p1, p2) -> p1.name.compareTo(p2.name));
```

## Tree
### Inorder Traversal (BST Rule)
Recursive
```java
public void inorder(TreeNode root) {
    if (root == null) return;

    inorder(root.left);
    System.out.print(root.val + " ");
    inorder(root.right);
}
```
Iterative (using stack)
```java
public List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> res = new ArrayList<>();
    Stack<TreeNode> stack = new Stack<>();
    TreeNode curr = root;

    while (curr != null || !stack.isEmpty()) {
        while (curr != null) {
            stack.push(curr);
            curr = curr.left;
        }

        curr = stack.pop();
        res.add(curr.val);
        curr = curr.right;
    }

    return res;
}
```
