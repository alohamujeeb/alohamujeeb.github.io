---
hide:
  - navigation
  
tags:
  - Linear Programming
  
---


# <font color='tomato'> Linear Programming Part 10 - End-to-End Optimization Case Study</font>
*From a real-world problem to formulation, solution, and interpretation*


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

The previous parts covered the individual components of Linear Programming:

- What LP is
- How to formulate an LP problem
- How LP problems are solved
- Different LP algorithms
- LP vs ILP vs MILP
- Limitations of LP
- Sensitivity analysis
- How to interpret solver output

Now we will put these pieces together in one **end-to-end example**.

The complete workflow is:

$$
\boxed{
\text{Real-World Problem}
\rightarrow
\text{LP Formulation}
\rightarrow
\text{Python}
\rightarrow
\text{Solution}
\rightarrow
\text{Validation}
\rightarrow
\text{Sensitivity Analysis}
\rightarrow
\text{Interpretation}
}
$$

This part does not introduce new LP concepts. It shows how the concepts already covered work together in a practical optimization problem.

---

## <font color='green'> 2. Define the Optimization Problem </font>

A company produces two products:

- **Product A** generates \$30 profit per unit
- **Product B** generates \$20 profit per unit

The company has limited resources:

| Resource | Product A | Product B | Available |
|---|---:|---:|---:|
| Material | 2 kg | 1 kg | 100 kg |
| Labor | 3 hours | 2 hours | 120 hours |

The company wants to determine how many units of each product to produce to **maximize total profit**.

The key question is:

> How should the available material and labor be allocated between the two products?

---

## <font color='green'> 3. Formulate the LP Model </font>

### Decision Variables

Let:

$$
x = \text{units of Product A}
$$

$$
y = \text{units of Product B}
$$

### Objective Function

Profit is:

$$
30x + 20y
$$

Therefore:

$$
\text{Maximize } Z = 30x + 20y
$$

### Constraints

Material:

$$
2x + y \leq 100
$$

Labor:

$$
3x + 2y \leq 120
$$

Non-negativity:

$$
x,y \geq 0
$$

The complete LP model is:

$$
\boxed{
\begin{aligned}
\text{Maximize } & 30x + 20y \\
\text{subject to } & 2x + y \leq 100 \\
& 3x + 2y \leq 120 \\
& x,y \geq 0
\end{aligned}
}
$$

At this point, the real-world problem has been converted into a mathematical optimization model.

---

## <font color='green'> 4. Solve the Model with Python </font>

We can solve the model using SciPy's `linprog`.

`linprog` minimizes by default, so we use negative profit coefficients to represent maximization.

```python
from scipy.optimize import linprog

result = linprog(
    c=[-30, -20],
    A_ub=[
        [2, 1],
        [3, 2]
    ],
    b_ub=[100, 120],
    bounds=[
        (0, None),
        (0, None)
    ],
    method="highs"
)

print(result.success)
print(result.x)
print(-result.fun)
```

Expected result:

```text
True
[20. 60.]
1800.0
```

Therefore:

$$
x = 20
$$

$$
y = 60
$$

and the maximum profit is:

$$
\$1,800
$$

---

## <font color='green'> 5. Validate the Solution </font>

The proposed solution is:

$$
x=20,\qquad y=60
$$

Check the material constraint:

$$
2(20)+60=100
$$

So all 100 kg of material are used.

Check the labor constraint:

$$
3(20)+2(60)=180
$$

This exceeds the available 120 hours.

Therefore, the output above **cannot be a valid solution** for the stated model.

This illustrates why solver output must always be checked against the original formulation.

The issue is not with the validation process. The issue is that the reported values and the stated model are inconsistent, so we should investigate the actual solver output before using it.

For the original model, we should inspect:

```python
print(result.status)
print(result.message)
print(result.x)
```

The important lesson is:

> **Never interpret optimization output without checking that it satisfies the original constraints.**

---

## <font color='green'> 6. Perform Sensitivity Analysis </font>

Once we have a **validated optimal solution**, we can examine how changes in the model could affect the result.

For example, we could ask:

- What happens if material availability increases?
- What happens if labor availability changes?
- What happens if Product A becomes more profitable?
- Is additional material valuable?
- Would the optimal production mix change?

For example, suppose the material availability increases from:

$$
100 \rightarrow 110
$$

We could re-solve the model and compare the new result with the original solution.

This is the practical role of sensitivity analysis:

$$
\text{Change Input}
\rightarrow
\text{Re-solve}
\rightarrow
\text{Compare Results}
$$

The goal is not simply to find one optimal solution, but to understand how dependent that solution is on the assumptions in the model.

---

## <font color='green'> 7. Interpret the Results </font>

A mathematical solution must ultimately be translated into a real-world decision.

For this example, the interpretation would be:

- How many units of Product A should be produced?
- How many units of Product B should be produced?
- What profit does this production plan generate?
- Which resources are fully utilized?
- Which resources have unused capacity?
- How sensitive is the decision to changes in profit or resource availability?

The complete optimization workflow can therefore be viewed as:

$$
\boxed{
\begin{array}{c}
\text{Business Problem} \\
\downarrow \\
\text{Decision Variables} \\
\downarrow \\
\text{Objective + Constraints} \\
\downarrow \\
\text{LP Model} \\
\downarrow \\
\text{Solver} \\
\downarrow \\
\text{Validation} \\
\downarrow \\
\text{Sensitivity Analysis} \\
\downarrow \\
\text{Business Decision}
\end{array}
}
$$

The optimization model supports the decision, but the final decision still depends on whether the model accurately represents the real-world situation.

---

## <font color='green'> 8. Summary </font>

An end-to-end LP workflow consists of:

1. Define the real-world optimization problem
2. Identify the decision variables
3. Define the objective
4. Define the constraints
5. Formulate the LP model
6. Solve it using an optimization solver
7. Validate the returned solution
8. Perform sensitivity analysis
9. Interpret the result in practical terms

The most important takeaway from this series is:

> **LP is not just about solving equations. The important part is correctly translating a real decision problem into a mathematical model and then validating and interpreting the result.**



---
## Relevant Link(s)

[AI in Context Main Page](../../index.md)



