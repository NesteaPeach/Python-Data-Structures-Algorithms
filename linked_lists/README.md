
# 📘 Linked List – LeetCode-Oriented Summary

## 🔗 What is a Linked List?
A linked list is a linear data structure where elements (nodes) are not stored in contiguous memory.
Unlike arrays (or Python lists), which are stored next to each other in memory, linked list nodes are
scattered across memory. Each node contains a `value` and a `next` pointer to the following node.
We use two special references: `head` (first node) and `tail` (last node). The last node points to `None`.

## ⚙️ Node Structure Example (Under the Hood)
A node can be represented as:
```python
{"value": 7, "next": {"value": 4, "next": None}}
```

## 🧠 Big O Complexity Summary

| Operation           | Linked List | List     |
|---------------------|-------------|----------|
| Append              | O(1)        | O(1)     |
| Pop                 | O(n)        | O(1)     |
| Prepend             | O(1)        | O(n)     |
| Pop First           | O(1)        | O(n)     |
| Insert              | O(n)        | O(n)     |
| Remove              | O(n)        | O(n)     |
| Lookup by Index     | O(n)        | O(1)     |
| Lookup by Value     | O(n)        | O(n)     |

### Operation Details

- **Append to end (with tail):** O(1) — The last node and tail both point to the new node.
- **Remove last item:** O(n) — Traverse from head to find the new last node and update tail.
- **Prepend (add to front):** O(1) — New node points to the old head, and head is updated.
- **Remove from front:** O(1) — Update head to head.next.
- **Insert in middle:** O(n) — Traverse from head to find insertion point and rewire pointers.
- **Remove from middle:** O(n) — Traverse from head to find and reassign pointers.
- **Lookup:** O(n) — Must traverse from head as nodes are not indexed.

