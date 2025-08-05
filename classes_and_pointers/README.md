# 📘 Python Basics: Classes, Pointers, and Memory in Leetcode Context

This guide explains essential Python concepts used frequently when solving data structure and algorithm problems in Leetcode: **classes**, **pointers**, and **memory behavior**, including **immutability**, **copy vs deepcopy**, and **garbage collection**.

---

## 📦 CLASSES

In Python, everything is an object, and objects are created using **classes**. A class can be thought of as a **blueprint** or a **cookie cutter**. You use it to create (instantiate) multiple similar objects.

### 🔹 Example: Cookie Class

```python
class Cookie:
    def __init__(self, color):
        self.color = color
```

- `__init__` is called a **constructor** – it's a special method that gets called when a new object is created.
- `self` refers to the **current object** being created. It must always be the first parameter in instance methods.

### ✅ Creating an Object

```python
cookie_one = Cookie('green')
```

This creates a new `Cookie` object with the color `'green'`.

### 🔹 Getter and Setter Methods

We can access and modify attributes using class methods:

```python
class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color
```

### ✅ Usage Example

```python
cookie = Cookie('blue')
print(cookie.get_color())  # Output: blue

cookie.set_color('red')
print(cookie.get_color())  # Output: red
```

---

## 🧠 POINTERS AND MEMORY IN PYTHON

Python uses **references** (pointers) under the hood. When you do:

```python
a = b
```

You're not copying values; you're pointing `a` to the same object in memory as `b`.

### 🔹 Example with Integers (Immutable)

```python
num1 = 10
num2 = num1
print(id(num1), id(num2))  # Same ID

num2 = 22
print(id(num1), id(num2))  # Different IDs
```

Why? Because integers are **immutable**.

---

## ❗ Immutability Explained

- **Immutable types**: `int`, `float`, `str`, `tuple`
- **Mutable types**: `list`, `dict`, `set`, `bytearray`

If an object is **immutable**, any change to it creates a **new object** in memory.  
If it's **mutable**, changes are done **in-place**.

---

## 🧪 Mutable Example: Dictionaries and Lists

```python
dict1 = {"value": 1}
dict2 = dict1
dict2["value"] = 22

print(dict1["value"])  # Output: 22 – both point to the same dictionary
```

Same with lists:

```python
list1 = [1, 2]
list2 = list1
list2.append(3)

print(list1)  # Output: [1, 2, 3]
```

---

## 📋 `copy()` vs `deepcopy()`

Sometimes you want to create a **real copy** instead of a pointer reference.

### 🔹 `copy.copy()` – Shallow Copy

```python
import copy

original = {"data": [1, 2]}
shallow = copy.copy(original)
shallow["data"].append(3)

print(original)  # {'data': [1, 2, 3]} – still affected!
```

### 🔹 `copy.deepcopy()` – Deep Copy

```python
import copy

original = {"data": [1, 2]}
deep = copy.deepcopy(original)
deep["data"].append(3)

print(original)  # {'data': [1, 2]} – unaffected!
```

✅ Use `deepcopy()` when copying nested or mutable structures that shouldn't be shared.

---

## 🗑️ Garbage Collection and Lost References

What happens here?

```python
dict1 = {"val": 1}
dict2 = dict1
dict3 = {"val": 2}

dict2 = dict3
dict1 = dict2
```

The original dictionary `{"val": 1}` is no longer referenced by any variable.  
Python will automatically remove this unreferenced object using **garbage collection**.

---

## ✅ Summary Table

| Concept                  | Behavior                                                                 |
|--------------------------|--------------------------------------------------------------------------|
| `a = b`                  | `a` points to the same object as `b`                                     |
| Changing `b` (immutable) | `a` still points to the old value                                        |
| Changing `b` (mutable)   | Affects both `a` and `b`                                                 |
| `copy.copy()`            | Shallow copy: outer object is copied, inner is shared                   |
| `copy.deepcopy()`        | Full deep clone: nothing shared                                         |
| Lost references          | Cleaned up automatically by Python’s garbage collector                  |

---

## 🔁 Leetcode Relevance & Tips

- Use `class` to define custom data structures (e.g., `TreeNode`, `ListNode`, `TrieNode`).
- Understand pointer behavior to avoid side effects in recursive/backtracking problems.
- Use `deepcopy()` carefully when needed to isolate recursive state.

---
