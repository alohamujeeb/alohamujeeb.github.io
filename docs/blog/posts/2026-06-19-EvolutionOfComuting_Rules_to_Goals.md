---
date: 
  created: 2026-06-18
  posted:  2025-05-19
author:
  name: Mujeeb
  description: Creator
readtime: 8

categories: 
  - Artificial Intelligence
  - Machine Learning
tags:
   - Algorithms
   - Machine Learning
   - Artificial Intelligence
   
---
# <font color='green'>The Evolution of Computing: From Rules to Goals</font>
This blog is about **three ways computers solve problems**: by following rules, by learning patterns from data, and by generating answers that may not have a clear right or wrong.
<!-- more -->

---
## 1. Rule-Based Programming

- Computing started with rules; When we know how to perform a task, we can write down the exact steps and ask a computer to follow them.

- For example:

```
- Sort a list of numbers from smallest to largest.
- Search for a name in a list.
- Turn a machine on when a button is pressed.
- Turn a machine off when a sensor reports a fault.
- Calculate the total amount on an invoice.
```

- In each of these cases, the steps are well understood. We can describe exactly what the computer should do and in what order.

- As a result, **both the process and the outcome are clear.**

```
- We know how the task is performed because we wrote the rules ourselves. 
- We also know what the correct result should be and can easily verify it.
```

**Human contribution:** Define the rules.

**Machine contribution:** Execute the rules.

---
## 2. Machine Learning

- Rule-based programming works well when humans know the rules.

- But some problems are difficult because we do not know how to write the rules ourselves.

- Example: 
```
- How do you distinguish one dog breed from another?
- How do you recognize one person's face from millions of others?
```

> Humans can do these tasks, but writing an exact set of rules is difficult and very subjective. Different people may define rules differently and still may not be good enough.

- Instead of defining the rules, we provide examples and let the machine learn the rules from data.

**Human contribution:** Define the objective and provide examples.

**Machine contribution:** Learn the rules.


---
## 3. Generative AI

- Machine Learning (previous section) works well when we can determine whether an answer is correct or not.

- **But some problems are different because there may not be a single correct answer.**

- Examples:

```
- How should I design my new product?
- What is the best architecture for this software system?
- How should I respond to this customer complaint?
- What is a good marketing strategy for my business?
- Write a blog post about a topic.
```

> Different people may give different answers to these questions. In many cases, there is no objective way to prove that one answer is correct and all others are wrong.

- Instead of learning to produce a specific correct answer, the machine generates a possible solution based on patterns it has learned from large amounts of data.

- Unlike traditional Machine Learning, the challenge is no longer just learning the rules. The challenge is that the quality of the answer itself may be subjective.

- As a result, **both the process and the outcome become less clear.**

```
- We do not know exactly how the machine arrived at a particular answer.
- We often cannot objectively verify whether the answer is correct.
- We can only judge whether the answer appears useful, reasonable, or relevant.
```

**Human contribution:** Define the goal.

**Machine contribution:** Propose a solution.




---
## 4. A Simple Comparison

- At a high level, these three approaches differ in what humans provide, what machines contribute, and how easy it is to verify the result.


| Stage | Human Contribution | Machine Contribution | How? | Result? |
|---------|------------------|---------------------|-------|---------|
| Rule-Based Programming | Define the rules | Execute the rules | ✓ | ✓ |
| Machine Learning | Define the objective and provide examples | Learn the rules | ? | ✓ |
| Generative AI | Define the goal | Propose a solution | ? | ? |


- The progression is subtle but important.

```
- In Rule-Based Programming, humans define the rules and computers follow them.

- In Machine Learning, humans define the objective, but computers learn the rules.

- n Generative AI, humans define only the goal, while computers generate possible solutions.
```

> As we move down the table, more responsibility shifts from humans to machines.

---
## 5. Final Thoughts

These three approaches to computing coexist today. Modern software systems often use all three at the same time.

- Traditional software still relies on rule-based programming. 
- Machine Learning systems continue to solve classification and prediction problems. 
- Generative AI systems are increasingly being used to generate content, ideas, code, and recommendations.

What I find interesting is the shift in what we ask computers to do.

In Rule-Based Programming, we know the rules and we know what the correct answer looks like.

In Machine Learning, we do not know the rules, but we still know how to judge whether an answer is correct.

In Generative AI, we often know neither. We cannot fully explain how the answer was produced, and we may not even agree on what the correct answer should be.

This is why Generative AI feels fundamentally different from previous generations of computing.

Whether it should be called "true AI" is a matter of debate. But it is the first widely-used form of computing where both the process and the outcome can be uncertain.

Perhaps the evolution of computing can be summarized as:

```
Rule-Based Programming
  Know the rules.
  Know the result.

Machine Learning
  Don't know the rules.
  Know the result.

Generative AI
  Don't know the rules.
  Don't always know the result.
```


