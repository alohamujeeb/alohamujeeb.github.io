---
hide:
  - navigation
  
tags:
  - Linear Programming
  - LP Solver
  
---

# <font color='tomato'> Linear Programming Part 5 - LP Algorithms</font>
* Simplex, Revised Simplex, Interior-Point Methods, and how LP solvers work*

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

In the previous parts, we learned how to:

- Formulate an LP problem
- Define decision variables
- Define an objective function
- Define constraints
- Identify feasible solutions
- Find an optimal solution
- Solve LP problems using Python

> <font color='red'> For small LP problems, we can sometimes solve them manually.</font>

However, real-world LP problems can contain:

- Hundreds or thousands of decision variables
- Many constraints
- Large feasible regions
- Complex relationships between variables

Checking all possible solutions manually is not practical. This is where **LP algorithms** come in.

An LP algorithm is a systematic method used to find an optimal solution to a linear programming problem.

---
### Common Algorithms of LP

The main approaches we will look at are:

- **Simplex Method**
- **Revised Simplex Method**
- **Interior-Point Methods**

<font color='red'> The goal of this part is not to learn how to implement these algorithms from scratch. </font>

Instead, we want to understand:

- What each method is trying to do
- How the methods differ
- Why optimization solvers use them
- When they are useful

The overall process is:

$$
\boxed{
\text{LP Formulation}
\rightarrow
\text{LP Algorithm}
\rightarrow
\text{Optimal Solution}
}
$$

The LP formulation defines **what problem we want to solve**.

The algorithm defines **how the solver searches for the solution**.

---
## <font color='green'> 2. Simplex Method </font>

The **Simplex Method** is one of the classic algorithms for solving Linear Programming problems.

The basic idea is simple:

> Instead of checking every possible solution, the algorithm moves through promising solutions until it reaches an optimal one.

### 2.1 Starting with the Feasible Region

Consider our earlier LP:

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
x,y \geq 0
$$

With two variables, we can visualize the feasible region.

The feasible region has several **corner points**.

For a linear programming problem, an optimal solution can occur at one of these corner points.

### 2.2 Moving Between Solutions

> The Simplex Method starts from a feasible solution and moves from one feasible corner to another.

At each step, it looks for a direction that improves the objective function.

For a maximization problem:

$$
\text{Current Objective}
\rightarrow
\text{Improved Objective}
\rightarrow
\text{Improved Objective}
\rightarrow
\cdots
$$

The process continues until no neighboring feasible solution can improve the objective.

At that point, the current solution is optimal.

### 2.3 Conceptual Example

For our LP, the Simplex Method could move through feasible corner points such as:

$$
(0,0)
\rightarrow
(6,0)
\rightarrow
(4,3)
$$

The objective values are:

$$
0
\rightarrow
60
\rightarrow
85
$$

Since the objective improves as the algorithm moves, it eventually reaches:

$$
(x,y)=(4,3)
$$

with:

$$
\text{Profit}=85
$$

### 2.4 Key Idea

The Simplex Method does **not** search every possible point in the feasible region.

Instead, it systematically moves between candidate solutions, improving the objective until it reaches an optimal solution.

Conceptually:

$$
\boxed{
\text{Start}
\rightarrow
\text{Find Improvement}
\rightarrow
\text{Move}
\rightarrow
\text{Repeat}
\rightarrow
\text{Optimal Solution}
}
$$

This makes the Simplex Method much more practical than trying to evaluate every possible solution.

> The important thing to remember is that **Simplex is an algorithm for solving the LP formulation we already created**.


---
## <font color='green'> 3. Revised Simplex Method </font>

The **Revised Simplex Method** is an improved implementation of the Simplex Method.

The basic idea is still the same:

$$
\text{Start}
\rightarrow
\text{Improve the solution}
\rightarrow
\text{Move}
\rightarrow
\text{Repeat}
\rightarrow
\text{Optimal Solution}
$$

The main difference is **how the calculations are performed**.

### 3.1 Standard Simplex

The traditional Simplex Method works with a **tableau** that contains information about the LP problem.

As the algorithm moves between solutions, the tableau is updated.

For small problems, this approach is useful for understanding how Simplex works.

### 3.2 Revised Simplex

The Revised Simplex Method avoids maintaining the entire tableau.

Instead, it works with the important parts of the mathematical representation needed for each step.

This can reduce the amount of computation and memory required, especially when the LP contains many variables and constraints.

Conceptually:

$$
\boxed{
\text{Simplex}
=
\text{Work with the full tableau}
}
$$

$$
\boxed{
\text{Revised Simplex}
=
\text{Work with the necessary matrix information}
}
$$

### 3.3 Why It Matters

Real-world LP problems can contain thousands or even millions of variables and constraints.

Storing and repeatedly updating a complete tableau can become expensive.

The Revised Simplex Method is designed to handle large problems more efficiently by focusing calculations on the parts that are needed.

### 3.4 What You Need to Remember

You do not need to implement Revised Simplex to use LP effectively.

The key distinction is:

| Method | Basic Idea |
|---|---|
| Simplex | Moves between feasible solutions using a tableau |
| Revised Simplex | Performs the same basic process using more efficient matrix calculations |

Both methods are based on the same fundamental idea:

$$
\boxed{
\text{Move through feasible solutions while improving the objective}
}
$$

The next major approach is **Interior-Point Methods**, which take a different path through the feasible region.

---
## <font color='green'> 4. Interior-Point Methods </font>

**Interior-Point Methods** are another family of algorithms used to solve Linear Programming problems.

Unlike Simplex, which moves between **corner points**, Interior-Point Methods move through the **interior of the feasible region** toward the optimal solution.

### 4.1 Basic Idea

Consider the same LP:

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
x,y \geq 0
$$

The feasible region contains many possible solutions.

Instead of moving from corner to corner, an Interior-Point Method starts from a point inside the feasible region and moves toward the boundary where the optimal solution lies.

Conceptually:

$$
\boxed{
\text{Interior Point}
\rightarrow
\text{Better Point}
\rightarrow
\text{Better Point}
\rightarrow
\text{Optimal Solution}
}
$$

### 4.2 Simplex vs Interior-Point

The main difference is how they move through the feasible region:

| Method | Movement |
|---|---|
| Simplex | Moves along the boundary between corner points |
| Interior-Point | Moves through the interior toward the optimal region |

Both methods ultimately aim to find the same thing:

$$
\boxed{\text{Optimal Solution}}
$$

### 4.3 Why Interior-Point Methods Matter

Interior-Point Methods can be particularly useful for **large-scale LP problems**.

They use mathematical techniques that allow the algorithm to move toward the optimal solution without explicitly visiting each corner point.

Modern optimization solvers can use both Simplex-based and Interior-Point approaches depending on the problem.

### 4.4 What You Need to Remember

The key idea is:

$$
\boxed{
\text{Simplex}
\rightarrow
\text{Corner-to-Corner}
}
$$

$$
\boxed{
\text{Interior-Point}
\rightarrow
\text{Through the Interior}
}
$$

You do not need to implement either method from scratch for most practical AI/ML work.

What matters is understanding that **LP solvers use algorithms such as these to turn an LP formulation into an optimal solution**.

---
## <font color='green'> 5. How LP Solvers Work </font>

In practice, we usually do not implement Simplex or Interior-Point Methods ourselves.

Instead, we use an **LP solver**.

An LP solver takes our mathematical formulation and uses an optimization algorithm to find the optimal solution.

### 5.1 The Basic Process

The overall process is:

$$
\boxed{
\text{Define LP}
\rightarrow
\text{Give LP to Solver}
\rightarrow
\text{Solver Runs Algorithm}
\rightarrow
\text{Optimal Solution}
}
$$

For example, our LP is:

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
x,y \geq 0
$$

We give this formulation to a solver.

The solver then performs the mathematical calculations needed to find:

$$
x=4,\qquad y=3
$$

and:

$$
\text{Maximum Profit}=85
$$

### 5.2 What Happens Inside the Solver?

At a high level:

1. The solver receives the LP formulation.
2. It checks whether the problem is valid.
3. It determines whether feasible solutions exist.
4. It applies an optimization algorithm.
5. It searches for an optimal solution.
6. It returns the solution and additional information.

The algorithm may be based on:

- **Simplex**
- **Revised Simplex**
- **Interior-Point Methods**

The exact algorithm depends on the solver and the problem.

### 5.3 What the Solver Returns

A solver typically provides more than just the values of the decision variables.

It may provide:

- Optimal variable values
- Objective value
- Whether the problem was solved successfully
- Whether the problem is infeasible
- Whether the objective is unbounded
- Additional optimization information

For example:

$$
x=4,\qquad y=3
$$

and:

$$
\text{Objective}=85
$$

means the solver found an optimal feasible solution with an objective value of 85.

### 5.4 Practical Perspective

For most users, the important workflow is:

$$
\boxed{
\text{Formulate Correctly}
\rightarrow
\text{Choose a Solver}
\rightarrow
\text{Solve}
\rightarrow
\text{Interpret the Result}
}
$$

The difficult part is often **formulating the real-world problem correctly**.

The solver handles the numerical optimization.

This is why understanding decision variables, objectives, and constraints is more important than memorizing the internal steps of an algorithm.


---
## <font color='green'> 6. When to Use Each Approach </font>

Different LP algorithms can be useful for different types of problems.

The choice is usually handled by the **optimization solver**, rather than manually by the user.

### Simplex Method

Simplex is useful when:

- The LP has a manageable number of variables and constraints
- A solution along the boundary is useful for the problem
- The solver benefits from the structure of the LP

The main idea is:

$$
\boxed{\text{Move between feasible corner solutions}}
$$

### Revised Simplex Method

Revised Simplex is useful when:

- The LP is large
- Storing a complete Simplex tableau would be inefficient
- Matrix-based calculations can be used more efficiently

The main idea is:

$$
\boxed{\text{Simplex approach with more efficient matrix calculations}}
$$

### Interior-Point Methods

Interior-Point Methods are useful when:

- The LP is very large
- The problem has many variables and constraints
- Moving through the interior of the feasible region is computationally useful

The main idea is:

$$
\boxed{\text{Move through the interior toward the optimal solution}}
$$

### Simple Comparison

| Approach | Basic Idea | Main Characteristic |
|---|---|---|
| **Simplex** | Move between corner solutions | Works along the boundary of the feasible region |
| **Revised Simplex** | Simplex using efficient matrix calculations | Reduces unnecessary calculations and memory usage |
| **Interior-Point** | Move through the interior | Uses a different path toward the optimal solution |

### Comparison by Practical Perspective

| Aspect | Simplex | Revised Simplex | Interior-Point |
|---|---|---|---|
| Basic path | Corner to corner | Corner to corner | Through the interior |
| Main concept | Improve solution iteratively | Improve solution using matrix operations | Move toward optimality from the interior |
| Large LPs | Can be useful | Designed for efficient large-scale calculations | Often useful for large-scale problems |
| Used by modern solvers | Yes | Yes | Yes |
| Need to implement manually? | Usually no | Usually no | Usually no |

In practice, you usually **do not need to choose the algorithm manually**.

An optimization library or solver can select an appropriate method based on the problem.

The important takeaway is to understand the **role of these algorithms**, rather than memorizing their mathematical implementation.


---
## <font color='green'> 7. Summary </font>

We have now covered the main ideas behind common LP algorithms.

### What We Learned

- **Simplex Method** moves between feasible corner solutions.
- **Revised Simplex Method** uses more efficient matrix calculations while following the Simplex approach.
- **Interior-Point Methods** move through the interior of the feasible region toward the optimal solution.
- **LP Solvers** use these algorithms to calculate optimal solutions automatically.

The overall process is:

$$
\boxed{
\text{Real-World Problem}
\rightarrow
\text{LP Formulation}
\rightarrow
\text{LP Solver}
\rightarrow
\text{Algorithm}
\rightarrow
\text{Optimal Solution}
}
$$

The most important distinction is:

$$
\boxed{
\text{LP Formulation} = \text{What problem are we solving?}
}
$$

$$
\boxed{
\text{LP Algorithm} = \text{How do we solve it?}
}
$$

For practical AI/ML work, we will usually focus on **formulating the optimization problem correctly** and using an existing solver rather than implementing the optimization algorithm ourselves.



---
## Relevant Link(s)

[AI in Context Main Page](../../index.md)

[LP Solver Website](https://opensolver.org/)


