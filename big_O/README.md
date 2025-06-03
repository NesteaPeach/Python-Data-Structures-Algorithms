# Big O Notation – Summary and Key Concepts

This document provides a beginner-friendly explanation of **Big O notation**, **time complexity**, and **space complexity**, with simple examples to build your intuition for technical interviews.

---

## 📐 What is Big O?

**Big O notation** is a mathematical way to describe the efficiency of code — specifically, how the runtime or space requirements grow as the input size increases. It is used to compare different algorithms that solve the same problem and determine which one is more efficient.

Big O focuses on the **upper bound** of performance — the worst-case scenario — which helps in predicting scalability.

In coding interviews, you will often be asked to analyze the **Big O** of your solutions to evaluate how well your code will perform as input sizes grow.

---

## ⏱️ Time Complexity

**Time complexity** describes how the number of **operations** an algorithm performs grows relative to the input size `n`.

> Example:
>
> Code A runs in 15 seconds, and Code B runs in 60 seconds for the same task.  
> While runtime in seconds can vary due to machine/environment, **Big O** gives a machine-independent way to compare them based on **growth rate**.

### 📌 How is it calculated?

Time complexity is typically estimated by:
- Counting the number of fundamental operations.
- Focusing on the **dominant term** as `n` grows.
- Ignoring constants and lower-order terms.

---

## 💾 Space Complexity

**Space complexity** measures how much additional **memory** an algorithm uses as the input size grows.

> Example:
>
> - Code A is fast but uses a lot of memory.
> - Code B is slower but uses very little memory.
> 
> If minimizing memory usage is your goal, you'd prefer **Code B**.

Space complexity is calculated similarly to time complexity, by:
- Counting variables and data structures that grow with input size.
- Ignoring constant space usage.

---

## 🧠 Notation Types

### Ω (Omega) – Best Case

- Describes the **best-case scenario** for an algorithm.
- Example: Searching for `1` in `[1, 2, 3]` – it's the first element.
- **Ω(1)** in this case — just one operation.

### Θ (Theta) – Average Case

- Describes the **average-case** scenario.
- Example: Looking for `2` in `[1, 2, 3]` – it's in the middle.
- **Θ(n)** means an algorithm consistently takes *n* operations on average.

### O (Omicron / Big O) – Worst Case

- Describes the **worst-case scenario**, most commonly used in analysis.
- Example: Searching for `3` in `[1, 2, 3]` – you must check all elements.
- **O(n)** – linear time.

---

## 🧮 Common Big O Complexities

| Big O        | Name             | Example Scenario                                                        |
|--------------|------------------|-------------------------------------------------------------------------|
| **O(1)**     | Constant Time    | Accessing an element by index in an array: `arr[0]`                     |
| **O(log n)** | Logarithmic Time | Binary search in a sorted array                                         |
| **O(n)**     | Linear Time      | Looping once through an array                                           |
| **O(n²)**    | Quadratic Time   | Nested loops (e.g., bubble sort)                                        |
| **O(2ⁿ)**    | Exponential Time | Recursive Fibonacci without memoization: `fib(n) = fib(n-1) + fib(n-2)` |

