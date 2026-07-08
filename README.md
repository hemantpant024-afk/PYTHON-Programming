# Python Class

## What is a Class?

A **class** is a blueprint or template used to create objects in Python. It defines the data (attributes) and behavior (methods) that objects of the class will have.

## Syntax

```python
class ClassName:
    pass
```

## Example

```python
class Student:
    pass
```

## Class with Attributes

```python
class Student:
    name = "Hemant"
    course = "Python"
```

## Accessing Class Attributes

```python
print(Student.name)
print(Student.course)
```

**Output**

```
Hemant
Python
```

## Advantages of Classes

- Organizes code
- Makes code reusable
- Represents real-world objects
- Supports Object-Oriented Programming (OOP)


---

# Python Functions

## What is a Function?

A function is a block of code that performs a specific task. It helps reduce code repetition and makes programs easier to read and maintain.

---

## Syntax

```python
def function_name():
    # Code
    pass
```

---

## Example

```python
def greet():
    print("Welcome to Python!")

greet()
```

---

## Output

```
Welcome to Python!
```

---

## Function with Parameters

```python
def add(a, b):
    print("Sum =", a + b)

add(10, 20)
```

---

## Output

```
Sum = 30
```

---

## Advantages of Functions

- Reusable code
- Reduces code duplication
- Improves readability
- Easy to debug
- Easy to maintain

---

## Types of Functions

1. Built-in Functions (`print()`, `input()`, `len()`)
2. User-defined Functions


---

# _LIST_
List is the colluction of data.Witch is ordered and channgeable.   

```python
 list = [2,3,4,hemant,true,10]
 print(list[0]) # index
 print(list[-2])# negative index
 ```
 # Python List Methods

| S.No. | Method      | Description                                                      |
| ----: | ----------- | ---------------------------------------------------------------- |
|     1 | `append()`  | Adds an element at the end of the list.                          |
|     2 | `clear()`   | Removes all the elements from the list.                          |
|     3 | `copy()`    | Returns a copy of the list.                                      |
|     4 | `count()`   | Returns the number of elements with the specified value.         |
|     5 | `extend()`  | Adds the elements of a list to the end of the current list.      |
|     6 | `index()`   | Returns the index of the first element with the specified value. |
|     7 | `insert()`  | Adds an element at the specified position.                       |
|     8 | `pop()`     | Removes the element at the specified position.                   |
|     9 | `remove()`  | Removes the item with the specified value.                       |
|    10 | `reverse()` | Reverses the order of the list.                                  |
|    11 | `sort()`    | Sorts the list.                                                  |


---

# TUPLE

Tuple is an immmutable list.Once a Tuple is created, no changes can be made to it. Tuple is also defind like list. in instead of square breacket [], parenthesis () is used only for the element.


Tuple and it's Method

* It is not possible to add element in Tuple. No append or extend method work in Tuple. 
* Similarly, it is also not possible to remove an element in a Tuple. Tuple dose not have any remove or pop method. 
* Support Boolean Expression like 'IN' like 'LIST' Tuple. 

---

# SET

SET is unauthored collection of item, in witch each element is unique, there is no duplicate element and is immutable, that is, it cannot be changed. 


---

# Introduction

A **Dictionary** is a built-in data type in Python that stores data as **key-value pairs**. Each key in a dictionary is **unique** and is used to access its corresponding value. Dictionaries are **mutable**, meaning their contents can be added, updated, or removed after creation. They are widely used to store structured data such as student records, employee details, product information, and configuration settings because they provide fast and efficient data retrieval.

---
# Dictionary Methods

| Method         | Syntax                        | Description                                                                                | Example                               |
| -------------- | ----------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------- |
| `clear()`      | `dict.clear()`                | Removes all items from the dictionary.                                                     | `student.clear()`                     |
| `copy()`       | `dict.copy()`                 | Returns a shallow copy of the dictionary.                                                  | `new_dict = student.copy()`           |
| `fromkeys()`   | `dict.fromkeys(keys, value)`  | Creates a new dictionary with specified keys and a common value.                           | `dict.fromkeys(["a","b"], 0)`         |
| `get()`        | `dict.get(key)`               | Returns the value of the given key.                                                        | `student.get("name")`                 |
| `items()`      | `dict.items()`                | Returns all key-value pairs.                                                               | `student.items()`                     |
| `keys()`       | `dict.keys()`                 | Returns all keys in the dictionary.                                                        | `student.keys()`                      |
| `pop()`        | `dict.pop(key)`               | Removes and returns the value of the specified key.                                        | `student.pop("age")`                  |
| `popitem()`    | `dict.popitem()`              | Removes and returns the last inserted key-value pair.                                      | `student.popitem()`                   |
| `setdefault()` | `dict.setdefault(key, value)` | Returns the value of the key. If the key doesn't exist, inserts it with the default value. | `student.setdefault("city", "Delhi")` |
| `update()`     | `dict.update(other_dict)`     | Updates the dictionary with key-value pairs from another dictionary.                       | `student.update({"age": 20})`         |
| `values()`     | `dict.values()`               | Returns all values in the dictionary.                                                      | `student.values()`                    |

---
