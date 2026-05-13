---
date: 
  created: 2026-05-13
  posted:  2025-05-13
author:
  name: Mujeeb
  description: Creator
readtime: 10

categories: 
  - Artificial Intelligence
  - Programming 
tags:
   - AI

---
# AI vs Conventional Algorithms

- There are two broad types of algorithms used in software: conventional algorithms and AI algorithms. This section gives a brief comparison between the newer, increasingly popular AI-based algorithms and the older, conventional approach.
<!-- more -->

---
## 1. Conventional algorithms

- A conventional algorithm is used when we already know exactly how to solve a problem.

- We can clearly write down:
```
the steps
the rules
the calculations
the decisions
```
- Some examples include:
```
adding two numbers
calculating the area of a circle
sorting names alphabetically
checking temperature and turning a device on or off
```

---
## 2. AI algorithms

- AI algorithms on the other hand, are used when the rules are not clearly defined or are too difficult to explicitly write down.

- In many real-world problems, humans can recognize patterns easily, but **it is hard to express exact rules step by step**.

```
Examples:

Identifying one person from another
Distinguishing dog breeds
Voice recognition
Handwrite recognition
```

- This is difficult because features can overlap:

```
For example,there may not clear-cut boundaries to distinguish between two different animals
or
There may not be a way to write down how voice of people vary and how humans recognize them
```

- Since these **features can be subjective**, there is no single rule set that works for everyone.

- **Instead of fixed rules, AI systems learn patterns from data and examples.**

---
## 3. How AI Learns from data

- For conceptual understnading, one example of an AI algorithms is mentioned below (there are many more algorithms nowadays).

- Instead of manually writing strict rules, AI systems learn patterns from large amounts of examples and data.

```
Step 1: Collect data
Large numbers of samples are collected.

Step 2: Label data
Each sample is labeled with the correct output (e.g., husky, wolf, cat, dog).

Step 3: Train the model
An algorithm extracts patterns and uses optimization techniques to improve accuracy.

Step 4: Generate the model
The final result is a set of numerical values called weights, which represent learned patterns.
```

- **The model is not a set of human-written rules, but a learned numerical system**.

- The irony is that **humans often cannot directly interpret what these weights mean**, even though the system performs well. 

- This is why AI is often called a **black box,** though there are esearches going on to improve this, such as "Explainable AI"

- So AI learns patterns instead of fixed logic.


---
## 4. Algorithms that train AI block boxes (models)

AI systems are trained using **optimization-based algorithms** (such as gradient descent) that adjust weights to reduce errors.

| Examples                                                                                                                                                      | In these cases                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Neural Networks <br> Support Vector Machines (SVM) <br> Decision Trees <br> Random Forests <br> Gradient Boosting Machines <br> XGBoost / LightGBM / CatBoost | Learn patterns from data <br> Reduce prediction errors <br> Improve performance over time |

---
## 5. When to use AI (and when not to)

### When AI is NOT needed (clear rules)

- AI is unnecessary when rules are already clearly defined.

| Examples                                                                                                          | In these cases                                                                                  |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Calculating interest <br> Basic arithmetic <br> Unit conversion <br> Sorting data <br> Fixed rule-based decisions | Rules are explicit <br> Outcomes are predictable <br> Conventional algorithms are better suited |


### When AI IS needed (unclear rules)

- AI is useful when rules are unclear or subjective.

| Examples                                                                                                           | In these cases                                                                                |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| Face recognition <br> Speech recognition <br> Image classification <br> Spam detection <br> Recommendation systems | Features overlap <br> Definitions vary between humans <br> Rules cannot be explicitly written |


---
## Takeaway

Conventional algorithms follow explicit human-defined rules, while AI algorithms learn patterns from data when those rules are unclear, overlapping, or hard to define.

