---
hide:
  - navigation
  
tags:
  - Linear Programming
  - Limitations of Linear Programming
  
---

# <font color='tomato'> Linear Programming Part 7 - Limitations of Linear Programming</font>
*Understanding when LP is not the right optimization approach. Linearity, continuous variables, uncertainty, computational considerations, and alternative approaches*


---
[▶ Linear Programming Part 0- About This Series](./LP-Pt0.md)

[▶ Linear Programming Part 1- Where LP Fits in AI Systems](./LP-Pt1.md)

[▶ Linear Programming Part 2- Fundamental Building Blocks](./LP-Pt2.md)

[▶ Linear Programming Part 3 - Solving LP Problems](./LP-Pt3.md)

[▶ Linear Programming Part 4 - Practical Scenarios](./LP-Pt4.md)

[▶ Linear Programming Part 5 - LP Algorithms](./LP-Pt5.md)

[▶ Linear Programming Part 6- LP vs Integer Programming vs Mixed-Integer Programming](./LP-Pt6.md)

[▶ Linear Programming Part 7- Limiations of LP](./LP-Pt7.md)

[▶ Linear Programming Part 8- Sensitivity Anddalysis](./LP-Pt8.md)

[▶ Linear Programming Part 9- Understanding Solver Output](./LP-Pt9.md)

[▶ Linear Programming Part 10- End to End Case Study](./LP-Pt10.md)

---
## <font color='green'> 1. Introduction </font>

LP is a powerful and widely applicable optimization technique, but it is **not suitable for every problem**.

We want to understand **where LP starts to break down** and when another optimization approach may be more appropriate.

The main limitations we will examine are:

- **Linearity**: Relationships must be represented linearly
- **Variable types**: Basic LP assumes continuous variables
- **Complex relationships**: Some real-world relationships are difficult to express with linear constraints
- **Uncertainty**: Standard LP assumes known parameters
- **Computational considerations**: Some extensions can become significantly harder to solve

Understanding these limitations is important because choosing an optimization technique is not only about knowing how to formulate a problem.

It is also about knowing **when not to use a particular technique**.

---
## <font color='green'> 2. Linearity Assumption </font>

LP assumes that the relationships in the model are **linear**.

For example:

$$
y = 10x
$$

is linear.

But:

$$
y = x^2
$$

is not linear.

Many real-world relationships are not naturally linear. For example:

- Production cost may increase at different rates as production increases
- Discounts may depend on purchase volume
- Risk may change non-linearly with investment
- Performance may have diminishing returns
- Interaction effects may exist between variables
- Fixed costs and threshold effects may be present


A linear approximation can sometimes be used, but this may introduce errors or require additional modeling techniques.

If an important relationship is inherently non-linear, a **Nonlinear Programming (NLP)** approach may be more appropriate, which is outside the scope of this short series.



---
## <font color='green'> 3. Continuous Decision Variables </font>

Standard LP assumes that decision variables can take **continuous values**.

For example:

$$
x = 4.5
$$

is a valid LP solution.

This is appropriate when fractional values make sense, such as:

- Hours
- Weight
- Volume
- Budget allocation
- Resource usage

However, some decisions must be whole numbers.

For example:

$$
x = \text{number of employees}
$$

A solution such as:

$$
x = 4.5
$$

would not make practical sense.

In such cases, integer or binary variables are required, leading to **ILP or MILP**, as discussed in the previous part.

---
## <font color='green'> 4. Uncertainty and Changing Conditions </font>

Standard LP assumes that the values used in the model are **known and fixed**.

For example:

$$
2x + 4y \leq 20
$$

assumes that the available resource is exactly 20 units.

In real-world problems, these values may be uncertain or change over time.

Examples include:

- Demand may be different from the forecast
- Resource availability may change
- Costs may increase or decrease
- Processing times may vary
- Predictions may contain errors

A solution that is optimal for one set of assumptions may therefore not remain optimal when those assumptions change.

Standard LP does not directly model this uncertainty.

When uncertainty is an important part of the problem, approaches such as **Stochastic Programming** or **Robust Optimization** may be considered.


---
## <font color='green'> 5. Computational Considerations </font>

LP problems can often be solved efficiently, even when they contain many variables and constraints.

However, adding additional requirements can make the optimization problem significantly harder to solve.

For example:

- Integer or binary variables
- Large numbers of constraints
- Complex logical relationships
- Many interacting decisions

In particular, **ILP and MILP problems are generally more computationally difficult than standard LP problems**.

This does not mean they cannot be solved.

Modern optimization solvers can handle many large-scale problems, but solution time and computational resources can become important considerations.

Therefore, when building an optimization model, unnecessary constraints or integer restrictions should be avoided when they do not represent a real business requirement.


---
## <font color='green'> 6. When to Consider Other Optimization Methods </font>

LP may not be the right approach when the problem violates one or more of its basic assumptions.

Some common alternatives are:

| Problem Characteristic | Possible Approach |
|---|---|
| Non-linear relationships | Nonlinear Programming (NLP) |
| Integer or binary decisions | ILP / MILP |
| Uncertain parameters | Stochastic Programming |
| Need solutions that remain effective under uncertainty | Robust Optimization |
| Very complex search space | Metaheuristics or other optimization methods |

The choice depends on the structure of the problem.

The important point is:

$$
\boxed{
\text{Understand the Problem}
\rightarrow
\text{Identify Its Structure}
\rightarrow
\text{Choose the Appropriate Optimization Approach}
}
$$

LP should be used when its assumptions are a reasonable representation of the problem.


---
## <font color='green'> 7. Practical Decision Checklist </font>

Before choosing LP, check:

- **Are the important relationships linear?**
- **Can the decision variables be continuous?**
- **Are the model parameters sufficiently known for the decision being made?**
- **Is the resulting problem computationally practical to solve?**

If these assumptions hold reasonably well, LP may be appropriate.

If not, consider whether the problem requires:

- Integer or binary variables
- Nonlinear optimization
- Stochastic or robust optimization
- Another optimization approach

The goal is not to force every optimization problem into an LP model.

The goal is to choose a model that represents the **actual decision problem** well.

---
## <font color='green'> 8. Summary </font>

LP works well when:

- Relationships can be represented linearly
- Decision variables can be continuous
- Model parameters are sufficiently known
- The problem can be solved within practical computational limits

Its main limitations are:

- **Non-linearity**
- **Continuous-variable assumption**
- **Uncertainty**
- **Computational complexity**

When these limitations become important, other approaches such as **ILP, MILP, NLP, Stochastic Programming, or Robust Optimization** may be more appropriate.

The key takeaway is:

$$
\boxed{
\text{Understand the Problem}
\rightarrow
\text{Check LP Assumptions}
\rightarrow
\text{Choose the Right Optimization Approach}
}
$$

---
## Relevant Link(s)

[AI in Context Main Page](../../index.md)



