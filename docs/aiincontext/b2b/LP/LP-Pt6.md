---
hide:
  - navigation
  
tags:
  - Linear Programming
  - LP Solver
  
---

# <font color='tomato'> Linear Programming Part 6- LP vs Integer Programming vs Mixed-Integer Programming</font>
*Choosing the right optimization model for real-world decisions*


---
[▶ Linear Programming Part 0- About This Series](./LP-Pt0.md)

[▶ Linear Programming Part 1- Where LP Fits in AI Systems](./LP-Pt1.md)

[▶ Linear Programming Part 2- Fundamental Building Blocks](./LP-Pt2.md)

[▶ Linear Programming Part 3 - Solving LP Problems](./LP-Pt3.md)

[▶ Linear Programming Part 4 - Practical Scenarios](./LP-Pt4.md)

[▶ Linear Programming Part 5 - LP Algorithms](./LP-Pt5.md)

[▶ Linear Programming Part 6- LP vs Integer Programming vs Mixed-Integer Programming](./LP-Pt6.md)


---
## <font color='green'> 1. Introduction </font>

In the previous parts, we focused on **Linear Programming (LP)**.

LP works well when decision variables can take **continuous values**.

For example:

$$
x = 4.5
$$

can be a perfectly valid solution if $x$ represents something such as hours, kilograms, or dollars.

However, many real-world decisions are not continuous.

You cannot usually:

- Hire 4.5 employees
- Open 2.7 warehouses
- Select 3.4 projects
- Build 0.6 machines

These situations require decision variables to follow additional restrictions.

This leads to two important extensions of LP:

- **Integer Linear Programming (ILP)**, where some or all decision variables must be integers
- **Mixed-Integer Linear Programming (MILP)**, where some variables are integers and others can remain continuous

The basic progression is:

$$
\boxed{
\text{LP}
\rightarrow
\text{ILP}
\rightarrow
\text{MILP}
}
$$

The mathematical structure remains similar:

$$
\boxed{
\text{Decision Variables}
+
\text{Objective}
+
\text{Constraints}
}
$$

The main difference is the **type of values allowed for the decision variables**.

In this part, we will focus on understanding when to use LP, ILP, or MILP in practical optimization problems.


---
## <font color='green'> 2. Why LP Is Not Always Enough </font>

The key assumption in Linear Programming is that decision variables can take **continuous values**.

For example:

$$
x = 2.5
$$

is allowed if $x$ represents something like hours or kilograms.

But many business decisions are **discrete**.

For example:

- Number of employees
- Number of vehicles
- Number of machines
- Number of facilities
- Number of projects selected

These decisions usually need to be whole numbers.

### Example

Suppose a company wants to decide how many delivery vehicles to purchase.

Let:

$$
x = \text{number of vehicles}
$$

An LP might produce:

$$
x = 4.6
$$

Mathematically, this could be a valid LP solution.

Practically, however:

$$
4.6\text{ vehicles}
$$

does not make sense.

We need:

$$
x \in \{0,1,2,3,\ldots\}
$$

This is where **Integer Linear Programming** becomes useful.

### Binary Decisions

Some decisions are even more restrictive.

For example:

$$
x =
\begin{cases}
1 & \text{if a warehouse is opened} \\
0 & \text{otherwise}
\end{cases}
$$

This is called a **binary variable**.

Binary variables are useful for yes/no decisions such as:

- Open or close
- Select or reject
- Build or not build
- Assign or not assign

### The Key Difference

The important question is:

> **What values should my decision variables be allowed to take?**

This gives us the basic distinction:

$$
\boxed{
\text{LP} \rightarrow \text{Continuous Variables}
}
$$

$$
\boxed{
\text{ILP} \rightarrow \text{Integer Variables}
}
$$

$$
\boxed{
\text{MILP} \rightarrow \text{Integer + Continuous Variables}
}
$$

The objective function and constraints can still remain linear.

Only the **variable type restrictions** change.


---
## <font color='green'> 3. Integer Linear Programming (ILP) </font>

In **Integer Linear Programming (ILP)**, decision variables are required to take **integer values**.

For example:

$$
x \in \{0,1,2,3,\ldots\}
$$

This is useful when fractional decisions do not make practical sense.

### Example

A company needs to decide how many delivery vehicles to purchase.

Let:

$$
x = \text{number of vehicles purchased}
$$

If each vehicle costs $20,000 and the company has a $100,000 budget:

$$
20x \leq 100
$$

with:

$$
x \in \mathbb{Z}_{\geq 0}
$$

The solution could be:

$$
x=5
$$

but not:

$$
x=4.5
$$

The objective function and constraints can still be linear. The key difference is the **integer restriction on the decision variables**.


---
## <font color='green'> 4. Mixed-Integer Linear Programming (MILP) </font>

**Mixed-Integer Linear Programming (MILP)** allows a problem to contain both:

- **Integer variables**
- **Continuous variables**

### Example

A company needs to decide:

- How many machines to purchase
- How many hours to operate them

Let:

$$
x = \text{number of machines purchased}
$$

$$
y = \text{hours of machine operation}
$$

The machine count must be an integer:

$$
x \in \mathbb{Z}_{\geq 0}
$$

The operating hours can be continuous:

$$
y \geq 0
$$

Suppose each machine costs $10,000 and each operating hour costs $50, with a total budget of $100,000:

$$
10000x + 50y \leq 100000
$$

If the objective is to minimize total cost:

$$
\boxed{\text{Minimize } 10000x + 50y}
$$

The important distinction is:

$$
\boxed{
\text{MILP} =
\text{Integer Variables}
+
\text{Continuous Variables}
}
$$

MILP is useful when a real-world problem contains both **discrete decisions** and **continuous quantities**.

---
## <font color='green'> 5. Binary Decision Variables </font>

A **binary variable** is a special type of integer variable that can take only two values:

$$
x \in \{0,1\}
$$

These values usually represent a **yes/no decision**.

For example:

$$
x =
\begin{cases}
1 & \text{if a warehouse is opened} \\
0 & \text{otherwise}
\end{cases}
$$

### Example

Suppose a company can open a new warehouse at a cost of $50,000.

Let:

$$
x = \text{whether the warehouse is opened}
$$

The cost can be represented as:

$$
50000x
$$

If the warehouse is opened:

$$
x=1 \Rightarrow \$50,000
$$

If it is not opened:

$$
x=0 \Rightarrow \$0
$$

Binary variables are commonly used for decisions such as:

- Select / don't select
- Open / don't open
- Build / don't build
- Assign / don't assign
- Activate / don't activate

Binary variables are particularly important in **MILP**, because many real-world decisions are naturally yes/no choices.

$$
\boxed{x \in \{0,1\}}
$$

is therefore one of the most useful modeling tools in integer optimization.


---
## <font color='green'> 6. LP vs ILP vs MILP </font>

The main difference between the three formulations is the **type of decision variables they allow**.

| Formulation | Variable Types | Example |
|---|---|---|
| **LP** | Continuous | $x = 4.5$ hours |
| **ILP** | Integer | $x = 5$ vehicles |
| **MILP** | Integer + Continuous | $x = 5$ vehicles, $y = 4.5$ hours |

### Practical Interpretation

**LP**

Use when fractional values make sense.

$$
x \geq 0
$$

**ILP**

Use when decisions must be whole numbers.

$$
x \in \mathbb{Z}_{\geq 0}
$$

**MILP**

Use when a problem contains both types.

$$
x \in \mathbb{Z}_{\geq 0},\qquad y \geq 0
$$

Binary variables are a special case of integer variables:

$$
x \in \{0,1\}
$$

### Simple Decision Rule

Ask:

> **Can this decision meaningfully take a fractional value?**

If yes, LP may be sufficient.

If it must be a whole number, use ILP.

If the problem contains both whole-number and continuous decisions, use MILP.

$$
\boxed{
\text{Continuous}
\rightarrow
\text{LP}
}
$$

$$
\boxed{
\text{Integer}
\rightarrow
\text{ILP}
}
$$

$$
\boxed{
\text{Integer + Continuous}
\rightarrow
\text{MILP}
}
$$

---
## <font color='green'> 7. Formulation Changes </font>

Moving from LP to ILP or MILP does **not** fundamentally change how we define:

- Decision variables
- Objective function
- Constraints

The main change is the **type restriction placed on the decision variables**.

For LP:

$$
x \geq 0
$$

For ILP:

$$
x \in \mathbb{Z}_{\geq 0}
$$

For MILP:

$$
x \in \mathbb{Z}_{\geq 0},
\qquad
y \geq 0
$$

So the formulation pattern remains:

$$
\boxed{
\text{Variables}
+
\text{Objective}
+
\text{Constraints}
}
$$

with an additional **variable-type restriction** when integer or binary decisions are required.

That is the primary formulation difference between LP, ILP, and MILP.

---
## <font color='green'> 8. Solver and Computational Differences </font>

The formulation may look almost identical, but **ILP and MILP are generally harder to solve computationally than LP**.

For LP, solvers can use methods such as:

- Simplex
- Revised Simplex
- Interior-Point Methods

For ILP and MILP, solvers typically need additional techniques to enforce the integer restrictions.

A common approach is **Branch-and-Bound**.

Other techniques include:

- Branch-and-Cut
- Cutting Planes

Conceptually:

$$
\text{LP}
\rightarrow
\text{LP Solver}
$$

while:

$$
\text{ILP/MILP}
\rightarrow
\text{Integer Optimization Solver}
\rightarrow
\text{Additional Integer-Handling Techniques}
$$

This is the important practical difference:

> **Adding integer or binary restrictions can make an optimization problem substantially more computationally difficult.**

You therefore should not add integer restrictions unless the real-world decision actually requires them.

---
## <font color='green'> 9. Solving LP, ILP, and MILP with Python </font>

The formulation remains largely the same in Python.

The main difference is how we specify the **variable types**.

### LP

For a continuous LP, we can use `linprog`:

    from scipy.optimize import linprog

    result = linprog(
        c=[-10, -15],
        A_ub=[[2, 4], [3, 2]],
        b_ub=[20, 18],
        bounds=[(0, None), (0, None)],
        method="highs"
    )

    print(result.x)
    print(-result.fun)

The variables are continuous.

### ILP

For an integer problem, use `scipy.optimize.milp` and specify the variables as integer:

    from scipy.optimize import milp, LinearConstraint, Bounds

    result = milp(
        c=[-10, -15],
        integrality=[1, 1],
        bounds=Bounds([0, 0], [float("inf"), float("inf")]),
        constraints=LinearConstraint(
            [[2, 4], [3, 2]],
            [-float("inf"), -float("inf")],
            [20, 18]
        )
    )

    print(result.x)
    print(-result.fun)

Here:

    integrality=[1, 1]

means both decision variables must be integers.

### MILP

For a mixed-integer problem, some variables can be integer while others remain continuous.

For example:

    integrality=[1, 0]

means:

- First variable → integer
- Second variable → continuous

The rest of the formulation can remain the same.

### The Important Difference

In Python, the key modeling change is essentially:

    LP:
    continuous variables

    ILP:
    integrality=[1, 1, ...]

    MILP:
    integrality=[1, 0, 1, ...]

So the practical workflow remains:

$$
\boxed{
\text{Formulate}
\rightarrow
\text{Specify Variable Types}
\rightarrow
\text{Solver}
\rightarrow
\text{Solution}
}
$$

You do not need a completely different mathematical formulation for ILP or MILP.

The main additional information the solver needs is **which variables must be integer or binary**.

---
## <font color='green'> 10. Summary </font>

The main distinction between LP, ILP, and MILP is the **type of decision variables**.

| Model | Variable Type |
|---|---|
| **LP** | Continuous |
| **ILP** | Integer |
| **MILP** | Integer + Continuous |
| **Binary** | 0 or 1 |

The basic formulation remains:

$$
\boxed{
\text{Decision Variables}
+
\text{Objective}
+
\text{Constraints}
}
$$

The additional requirement is the variable type.

In Python, this is reflected through the solver configuration, such as:

    integrality=[1, 0]

where `1` represents an integer variable and `0` represents a continuous variable.

The practical takeaway is:

> **Choose the variable type based on the real-world decision, then choose the appropriate optimization model and solver.**

LP, ILP, and MILP are therefore not completely different optimization concepts. They are closely related formulations with different restrictions on the decision variables.




---
## Relevant Link(s)

[AI in Context Main Page](../../index.md)



