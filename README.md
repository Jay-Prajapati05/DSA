# 🧠 DSA Practice in Python

A collection of Data Structures & Algorithms solutions in Python, organized topic-wise for fast revision.
Every solution includes the approach, time/space complexity, and notes on mistakes.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-In%20Progress-green)

## 🎯 Goal

- Practice DSA **daily** and build problem-solving consistency
- Maintain a clean, searchable repository for **quick revision**
- Prepare for technical interviews

## 📁 Repository Structure

```
DSA/
├── README.md
├── new.py                      # helper to create a new solution file
├── templates/
│   └── solution_template.py
├── docs/
│   ├── patterns_cheatsheet.md
│   └── revision_list.md
├── 01_arrays/        (easy | medium | hard)
├── 02_strings/
├── 03_hashing/
├── 04_two_pointers/
├── 05_sliding_window/
├── 06_binary_search/
├── 07_linked_list/
├── 08_stack_queue/
├── 09_recursion_backtracking/
├── 10_trees/
├── 11_heap/
├── 12_graphs/
├── 13_dynamic_programming/
├── 14_greedy/
└── 15_misc/
```

Each topic folder is split into `easy/`, `medium/` and `hard/`.

## 📝 Solution Format

Every file starts with a header describing the problem, approach and complexity:

```python
"""
Problem   : Two Sum
Platform  : LeetCode #1
Difficulty: Easy
Pattern   : Hashing (dict)

Approach:
  - Store value -> index in a dict
  - For each number, check if (target - num) already exists

Time  : O(n)
Space : O(n)

Notes / Mistakes:
  - Check first, then insert, otherwise the same element can be reused
"""
```

## ▶️ How to Run

```bash
python 03_hashing/easy/two_sum.py
```

Each file contains simple `assert` test cases at the bottom.

## ➕ Add a New Problem

```bash
python new.py <topic> <level> <problem_name>

# example
python new.py hashing easy two_sum
```

## 📊 Progress

| Topic | Easy | Medium | Hard | Total |
|-------|:----:|:------:|:----:|:-----:|
| Arrays | 0 | 0 | 0 | 0 |
| Strings | 0 | 0 | 0 | 0 |
| Hashing | 0 | 0 | 0 | 0 |
| Two Pointers | 0 | 0 | 0 | 0 |
| Sliding Window | 0 | 0 | 0 | 0 |
| Binary Search | 0 | 0 | 0 | 0 |
| Linked List | 0 | 0 | 0 | 0 |
| Stack / Queue | 0 | 0 | 0 | 0 |
| Recursion / Backtracking | 0 | 0 | 0 | 0 |
| Trees | 0 | 0 | 0 | 0 |
| Heap | 0 | 0 | 0 | 0 |
| Graphs | 0 | 0 | 0 | 0 |
| Dynamic Programming | 0 | 0 | 0 | 0 |
| Greedy | 0 | 0 | 0 | 0 |
| **Total** | **0** | **0** | **0** | **0** |

## 📚 Problem Index

| # | Problem | Platform | Difficulty | Pattern | Date |
|---|---------|----------|:----------:|---------|------|
| 1 | [Two Sum](03_hashing/easy/two_sum.py) | LeetCode #1 | Easy | Hashing | 2026-11-12 |

## 🗺️ Roadmap

- [ ] Week 1: Arrays
- [ ] Week 2: Strings + Hashing
- [ ] Week 3: Two Pointers + Sliding Window
- [ ] Week 4: Binary Search
- [ ] Week 5: Linked List
- [ ] Week 6: Stack + Queue
- [ ] Week 7: Recursion + Backtracking
- [ ] Week 8: Trees
- [ ] Week 9: Heap + Greedy
- [ ] Week 10: Graphs
- [ ] Week 11-12: Dynamic Programming
- [ ] Week 13+: Revision + mock interviews

## 🔁 Revision Strategy

Hard or tricky problems are added to `docs/revision_list.md` and re-solved after
**1 day → 1 week → 1 month**.

## 🧾 Commit Convention

```
feat(hashing): add two_sum solution
refactor(strings): optimize valid_anagram to O(n)
docs: update README progress table
```

## 👤 Author

**Jay Prajapati**
- GitHub: https://github.com/Jay-Prajapati05
- LinkedIn: www.linkedin.com/in/
jay-prajapati-022007433

⭐ If you find this repo useful, consider giving it a star!