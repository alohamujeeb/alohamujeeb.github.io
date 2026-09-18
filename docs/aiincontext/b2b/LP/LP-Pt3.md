---
hide:
  - navigation
  
tags:
  - Linear Programming
  - LP Solver
  
---


# <font color='tomato'> Linear Programming Part 3 - Solving LP Problems</font>
*From an LP formulation to an optimal solution*

---
[▶ Linear Programming Part 0- About This Series](./LP-Pt0.md)

[▶ Linear Programming Part 1- Where LP Fits in AI Systems](./LP-Pt1.md)

[▶ Linear Programming Part 2- Fundamental Building Blocks](./LP-Pt2.md)

[▶ Linear Programming Part 3- Solving LP Problems](./LP-Pt3.md)

[▶ Linear Programming Part 4- Practical Scenarios](./LP-Pt4.md)

[▶ Linear Programming Part 5- LP Algorithms](./LP-Pt5.md)


---
## <font color='green'> 1. Introduction </font>

In Part 2, we learned how to **formulate** a Linear Programming problem using:

- **Decision Variables**
- **Objective Function**
- **Constraints**

For example:

$$
\text{Maximize } 10x + 15y
$$

Subject to:

$$
2x + 4y \leq 20
$$

$$
3x + 2y \leq 18
$$

$$
x \geq 0,\qquad y \geq 0
$$

Formulating the problem is only the first step.

The next step is to **solve the LP problem** and find the values of the decision variables that give the best possible objective value while satisfying all constraints.

There are two ways we will look at this:

1. **Solve a small problem manually** to understand what is happening.
2. **Use a solver** to handle the calculations automatically.

A **solver** is a software tool that takes an optimization problem and searches for its optimal solution.

The basic process is:

$$
\boxed{
\text{LP Formulation}
\rightarrow
\text{Solver}
\rightarrow
\text{Optimal Solution}
}
$$

For small problems, we can understand the process manually. For larger problems, a solver can perform the calculations for us.


---
## <font color='green'> 2. Solving the LP Problem Manually </font>

Let's continue with the **same problem from Part 2**.

The LP problem is:

$$
\boxed{\text{Maximize } 10x + 15y}
$$

Subject to:

$$
2x + 4y \leq 20
$$

$$
3x + 2y \leq 18
$$

$$
x \geq 0
$$

$$
y \geq 0
$$

Our goal is to find the values of $x$ and $y$ that give the **maximum possible profit** while satisfying all constraints.

---
### 2.1 Finding Where the Constraints Meet

Our two main constraints are inequalities:

$$
2x + 4y \leq 20
$$

$$
3x + 2y \leq 18
$$

The inequality tells us that we can use **up to** the available resources.

For example:

$$
2x + 4y \leq 20
$$

means that the company can use 20 units of material or less.

The **boundary** of this constraint is where exactly 20 units of material are used:

$$
2x + 4y = 20
$$

Similarly, the boundary of the labor constraint is:

$$
3x + 2y = 18
$$

We use the equality because we want to find where the **two constraint boundaries intersect**.

So, temporarily, we convert the inequalities into equations:

$$
2x + 4y = 20
$$

$$
3x + 2y = 18
$$

Now we can solve these two equations to find their intersection.

---
### 2.2 Solve for $x$ and $y$

Start with the first equation:

$$
2x + 4y = 20
$$

Divide everything by 2:

$$
x + 2y = 10
$$

Rearrange to get $x$:

$$
x = 10 - 2y
$$

Now substitute this into the second equation:

$$
3x + 2y = 18
$$

$$
3(10 - 2y) + 2y = 18
$$

Expand:

$$
30 - 6y + 2y = 18
$$

$$
30 - 4y = 18
$$

Therefore:

$$
-4y = -12
$$

$$
y = 3
$$

Now substitute $y=3$ into:

$$
x = 10 - 2y
$$

$$
x = 10 - 2(3)
$$

$$
x = 4
$$

Therefore, the two constraint boundaries intersect at:

$$
\boxed{(x,y) = (4,3)}
$$

---
### 2.3 Check the Solution Against the Constraints

We found:

$$
x=4,\qquad y=3
$$

Now we check the original inequalities.

**Material constraint:**

$$
2(4) + 4(3) = 20
$$

Therefore:

$$
20 \leq 20
$$

The material constraint is satisfied.

**Labor constraint:**

$$
3(4) + 2(3) = 18
$$

Therefore:

$$
18 \leq 18
$$

The labor constraint is also satisfied.

And:

$$
x=4 \geq 0
$$

$$
y=3 \geq 0
$$

So $(4,3)$ is a **feasible solution**.

---
### 2.4 Calculate the Profit

Our objective function is:

$$
\text{Profit} = 10x + 15y
$$

Substitute:

$$
x=4,\qquad y=3
$$

$$
\text{Profit} = 10(4) + 15(3)
$$

$$
=40+45
$$

$$
=85
$$

Therefore, this solution produces:

$$
\boxed{\$85\text{ profit}}
$$

We have now found **one feasible solution** and calculated its profit.

The important question is:

> **Is $(4,3)$ the best feasible solution, or is there another feasible solution with a higher profit?**

We need to answer that before calling $(4,3)$ the optimal solution.

---
## <font color='green'> 3. Finding the Optimal Solution </font>

Finding one feasible solution is not enough.

We need to compare the feasible solutions and determine which one gives the **highest profit**.

For a simple two-variable LP problem, the optimal solution can be found by checking the **corner points of the feasible region**.

![solution region](images/solution_region.png)


For our problem, the corner points are:

$$
(0,0),\quad (6,0),\quad (4,3),\quad (0,5)
$$

We can calculate the profit at each point using:

$$
\text{Profit} = 10x + 15y
$$

### Check each corner point

**Point 1: $(0,0)$**

$$
10(0) + 15(0) = 0
$$

Profit:

$$
\$0
$$

**Point 2: $(6,0)$**

$$
10(6) + 15(0) = 60
$$

Profit:

$$
\$60
$$

**Point 3: $(4,3)$**

$$
10(4) + 15(3) = 85
$$

Profit:

$$
\$85
$$

**Point 4: $(0,5)$**

$$
10(0) + 15(5) = 75
$$

Profit:

$$
\$75
$$

We can summarize the results:

| $x$ | $y$ | Profit |
|---:|---:|---:|
| 0 | 0 | $0 |
| 6 | 0 | $60 |
| 4 | 3 | $85 |
| 0 | 5 | $75 |

The highest profit is:

$$
\boxed{\$85}
$$

at:

$$
\boxed{x=4,\qquad y=3}
$$

Therefore, the **optimal solution** is:

- Produce **4 units of Product A**
- Produce **3 units of Product B**
- Maximum profit = **$85**

This demonstrates the basic manual solution process:

$$
\boxed{
\text{Find feasible region}
\rightarrow
\text{Find corner points}
\rightarrow
\text{Calculate objective}
\rightarrow
\text{Choose the best}
}
$$


---
## <font color='green'> 4. Solving Larger LP Problems </font>

The manual approach works well for a small problem with two variables.

However, real LP problems can have:

- Hundreds or thousands of decision variables
- Many constraints
- Large numbers of possible solutions

Checking every possible solution manually is not practical.

This is where **LP algorithms and solvers** become useful.

An **LP solver** is software that takes the mathematical formulation of an LP problem and calculates the optimal solution automatically.

[LP Solver Website](https://opensolver.org/)

Conceptually:

$$
\boxed{
\text{LP Formulation}
\rightarrow
\text{LP Solver}
\rightarrow
\text{Optimal Solution}
}
$$

The solver handles the mathematical search for us.

We do not need to manually calculate every possible combination of decision variables.

### Common LP Algorithms

Some commonly used algorithms for solving LP problems are:

- **Simplex Method**
- **Revised Simplex Method**
- **Interior-Point Methods**

You do not need to learn the internal details of these algorithms for now.

The important idea is:

> **We formulate the optimization problem. The solver uses an algorithm to find the optimal solution.**

For small problems, solving manually helps us understand what the solver is doing.

For larger problems, we normally let the solver do the computational work.


---
## <font color='green'> 5. Solving LP with Python </font>

Once we understand how an LP problem works manually, we can use Python to solve the same problem automatically.

For basic LP problems, **SciPy** provides an optimization function called `linprog`.

The LP problem from our example is:

$$
\text{Maximize } 10x + 15y
$$

Subject to:

$$
2x + 4y \leq 20
$$

$$
3x + 2y \leq 18
$$

$$
x \geq 0,\qquad y \geq 0
$$

### Using `scipy.optimize.linprog`

One detail is important: `linprog` solves **minimization** problems by default.

Our problem is a maximization problem, so we can minimize the negative of the objective:

$$
\text{Minimize } -10x - 15y
$$

The Python code is:

    from scipy.optimize import linprog

    result = linprog(
        c=[-10, -15],
        A_ub=[
            [2, 4],
            [3, 2]
        ],
        b_ub=[20, 18],
        bounds=[
            (0, None),
            (0, None)
        ],
        method="highs"
    )

    print(result.x)
    print(-result.fun)

The solver returns approximately:

    [4. 3.]
    85.0

So Python gives us:

$$
x=4,\qquad y=3
$$

and:

$$
\text{Maximum Profit} = \$85
$$

This matches the result we obtained manually.

---
### What Did We Give the Solver?

We provided the same three building blocks we learned in Part 2:

| LP Component | Python |
|---|---|
| Decision Variables | `x`, `y` |
| Objective Function | `c=[-10, -15]` |
| Constraints | `A_ub`, `b_ub` |
| Variable Bounds | `bounds` |

<font color='red'> The important point is that Python is **not replacing the LP formulation**. </font>

>We still need to understand and formulate the problem correctly.

> Python and the solver simply perform the mathematical computation needed to find the solution.


---
## <font color='green'> 6. Summary </font>

We started with the LP problem we formulated in Part 2:

$$
\text{Maximize } 10x + 15y
$$

Subject to:

$$
2x + 4y \leq 20
$$

$$
3x + 2y \leq 18
$$

$$
x \geq 0,\qquad y \geq 0
$$

We then solved it manually by:

1. Finding where the constraint boundaries intersect
2. Checking feasible solutions
3. Evaluating the objective function
4. Identifying the optimal solution

The optimal solution was:

$$
\boxed{x=4,\qquad y=3}
$$

with a maximum profit of:

$$
\boxed{\$85}
$$

We then used a Python LP solver to solve the same problem automatically and obtained the same result.

The overall process is:

$$
\boxed{
\text{Formulate}
\rightarrow
\text{Solve}
\rightarrow
\text{Check}
\rightarrow
\text{Optimal Solution}
}
$$

For small problems, we can understand the solution process manually.

For larger problems, an LP solver or Python can perform the computational work for us.


---
## Relevant Link(s)

[AI in Context Main Page](../../index.md)

[LP Solver Website](https://opensolver.org/)


