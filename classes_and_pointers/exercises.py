import copy


# ===================================================
# 🧪 Exercise 1: Class and Instance Methods
# ===================================================
# Create a class Dog that stores a name and age.
# Add methods to get and update both values.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"

    def set_age(self, new_age):
        self.age = new_age


# ✅ Test
dog = Dog("Rex", 5)
print(dog.get_info())  # Rex is 5 years old
dog.set_age(6)
print(dog.get_info())  # Rex is 6 years old

# 🧠 Explanation:
# self is the instance. Each dog has its own name and age.
# When we change the age, it only affects that instance.

# ===================================================
# 🧪 Exercise 2: Pointer Behavior with Lists
# ===================================================
# Demonstrate how list pointers work in Python.

a = [1, 2, 3]
b = a
b.append(4)

print(a)  # [1, 2, 3, 4]

# 🧠 Explanation:
# a and b both point to the same list object in memory.
# Changes in b affect a too.

# ===================================================
# 🧪 Exercise 3: Copy vs Deepcopy
# ===================================================

original = {"info": [1, 2]}
shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow["info"].append(3)
deep["info"].append(4)

print("Original:", original)  # {'info': [1, 2, 3]}
print("Shallow:", shallow)  # {'info': [1, 2, 3]}
print("Deep:", deep)  # {'info': [1, 2, 4]}

# 🧠 Explanation:
# shallow points to the same inner list as original.
# deep has a fully separated copy of the nested list.

# ===================================================
# 🧪 Exercise 4: Garbage Collection
# ===================================================
# What happens when we overwrite references?

d1 = {"val": 1}
d2 = d1
d3 = {"val": 2}

d2 = d3
d1 = d2

# 🧠 At this point, {"val": 1} is no longer referenced.
# Python’s garbage collector will eventually delete it.

# We can’t access {"val": 1} anymore.

# ===================================================
# 🧪 Exercise 5: Immutable vs Mutable
# ===================================================
# Try changing an integer and a list

x = 5
y = x
y = 10

print(x)  # 5 – integers are immutable

list1 = [1, 2]
list2 = list1
list2.append(3)

print(list1)  # [1, 2, 3] – lists are mutable

# 🧠 Explanation:
# x and y point to different integers after reassignment
# list1 and list2 still point to the same object
