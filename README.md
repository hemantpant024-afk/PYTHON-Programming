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