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