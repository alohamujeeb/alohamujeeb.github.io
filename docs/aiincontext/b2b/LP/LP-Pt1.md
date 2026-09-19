---
hide:
  - navigation
  
tags:
  - Linear Programming
  
---

# <font color='tomato'> Linear Programming Part 1 - Where LP Fits Into AI Systems</font>
* What LP is and where it fits in AI systems*

---
[▶ Linear Programming Part 0- About This Series](./LP-Pt0.md)

[▶ Linear Programming Part 1- Where LP Fits in AI Systems](./LP-Pt1.md)

[▶ Linear Programming Part 2- Fundamental Building Blocks](./LP-Pt2.md)

[▶ Linear Programming Part 3- Solving LP Problems](./LP-Pt3.md)

[▶ Linear Programming Part 4- Practical Scenarios](./LP-Pt4.md)

[▶ Linear Programming Part 5- LP Algorithms](./LP-Pt5.md)

[▶ Linear Programming Part 6- LP vs Integer Programming vs Mixed-Integer Programming](./LP-Pt6.md)

[▶ Linear Programming Part 7- Limiations of LP](./LP-Pt7.md)

[▶ Linear Programming Part 8- Sensitivity Anddalysis](./LP-Pt8.md)

[▶ Linear Programming Part 9- Understanding Solver Output](./LP-Pt9.md)

[▶ Linear Programming Part 10- End to End Case Study](./LP-Pt10.md)

---

## <font color='green'> 1. LP is not AI </font>

**Linear Programming (LP)** is an optimization technique, not an AI model.

AI/ML typically learns patterns from data and uses those patterns to make predictions, classifications, or scores.

LP does something different. It finds the **best possible decision** while satisfying a set of constraints.

LP is introduced here because, in a real AI system, the AI/ML model is often only one part of the overall system. Other components may be responsible for turning predictions into actual decisions.

A simplified AI system might look like:

    Data
      ↓
    AI / ML Model
      ↓
    Predictions / Scores
      ↓
    Optimization / Rules
      ↓
    Final Decision
      ↓
    Application

LP is one optimization technique that can be used in this broader system.

> The goal here is not to treat LP as AI, but to understand **where LP can fit into an AI system and what role it can play**.


---
## <font color='green'> 2 What Does LP Actually Do? </font>

LP answers practical questions such as:

- How many products should we produce?
- How should we allocate a limited budget?
- How should available workers be assigned?
- How should limited materials be distributed?
- How should delivery capacity be allocated?

The basic idea is:

> **Choose the values of some decision variables so that an objective is optimized while all constraints are satisfied.**

For example, a company produces two products:

- Product A makes $10 profit
- Product B makes $15 profit

But the company has limited materials and labor.

LP can determine:

> **How many A and B should we produce to maximize profit without exceeding our available resources?**

So LP is mainly about **decision-making under constraints**.

---

## <font color='green'>  3. AI Predicts, LP Optimizes </font>

A useful way to distinguish them is:

| AI/ML | Linear Programming |
|---|---|
| Learns patterns from data | Optimizes decisions |
| Makes predictions or scores | Finds the best feasible solution |
| "What is likely to happen?" | "What should we do?" |
| Example: predict product demand | Example: decide how much to produce |

They can also work together.

AI might predict that demand for a product will be 1,000 units next month.

LP can then use that prediction, together with production capacity, labor, materials, and costs, to determine **how much to actually produce**.

---

## <font color='green'> 4. Real AI Systems Contain More Than the AI Model </font>

A real-world AI application is rarely just an ML model.

A simplified system might look like:

    Data
      ↓
    AI / ML Model
      ↓
    Predictions / Scores
      ↓
    Optimization / Rules
      ↓
    Final Decision
      ↓
    Application

The AI model provides information that helps the system make a decision.

Optimization can then determine what action should actually be taken while respecting practical constraints.

LP is one possible optimization technique used in this supporting layer.

---

## <font color='green'> 5. Example: Movie Recommendation System </font>

Suppose a movie recommendation system uses an ML model to predict how much a user may like each movie:

    Movie A → 0.91
    Movie B → 0.87
    Movie C → 0.84
    Movie D → 0.81
    ...

The ML model answers:

> **Which movies is the user likely to enjoy?**

But the application may need to select only 10 movies and follow additional rules:

- Maximum 3 movies from the same genre
- At least 2 new releases
- Maximum 5 movies the user has already watched

An optimization model can use the ML scores and these constraints to decide which 10 movies to show.

So the roles are different:

    ML
      ↓
    Predict how much the user may like each movie
      ↓
    LP / Optimization
      ↓
    Select the best combination subject to constraints

The important distinction is:

> **AI/ML can provide predictions or scores. LP can use those results to make an optimized decision under constraints.**

This is why LP is useful to understand even though **LP itself is not AI**.



---
## Relevant Link(s)

[AI in Context Main Page](../../index.md)

