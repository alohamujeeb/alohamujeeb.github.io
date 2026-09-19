---
hide:
  - navigation
  
tags:
  - Linear Programming
  - Sensitivity Analysis
  
---

# <font color='tomato'> Linear Programming Part 9- Understanding Solver Output<</font>
*Reading solver status and validating optimization results. Solver status, solution validation, common solver outcomes, practical interpretation*

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

An optimization solver does not always return a usable optimal solution.

Depending on the LP formulation and the solver's execution, the result may be:

- An optimal solution
- No feasible solution
- An unbounded solution
- An incomplete solve due to computational limits

Therefore, getting output from a solver is not the same as having a valid optimization result.

Before using the solution, we should check:

$$
\boxed{
\text{Solver Status}
\rightarrow
\text{Solution}
\rightarrow
\text{Validation}
}
$$

This part focuses on reading solver output and checking whether the result can be safely used.


---
## <font color='green'> 2. Solver Status </font>

The **solver status** tells us what happened when the solver finished.

A solver may return output even when an optimal solution was not found. Therefore, we should check the status before using the result.

Common solver outcomes are:

| Status | Meaning |
|---|---|
| **Optimal** | A valid optimal solution was found |
| **Infeasible** | No solution satisfies all constraints |
| **Unbounded** | The objective can improve without a finite limit |
| **Time/Iteration Limit** | The solver stopped before proving optimality |
| **Numerical Difficulty** | The solver encountered numerical problems |

For example, with SciPy:

```python
result = linprog(
    c=[-10, -15],
    A_ub=[[2, 4], [3, 2]],
    b_ub=[20, 18],
    bounds=[(0, None), (0, None)],
    method="highs"
)

print(result.success)
print(result.status)
print(result.message)
```

The main fields to check are:

- `result.success`: whether the solver successfully found an optimal solution
- `result.status`: numerical code describing the solver outcome
- `result.message`: explanation of the outcome

For example:

```text
True
0
Optimization terminated successfully.

```

This indicates that the solver successfully found an optimal solution.

If the status indicates **infeasible**, **unbounded**, or a computational problem, the result should not be treated as a confirmed optimal solution.

**Key point:** Always check the solver status before using optimization results.

---
## <font color='green'> 3. Solution Validation </font>

After the solver reports a successful result, we should **validate the solution before using it**.

The main checks are:

1. **Decision variables are valid**
2. **All constraints are satisfied**
3. **Objective value matches the reported solution**

For the LP from earlier, suppose the solver returns:

```python
result.x
```

with:

```text
[4. 3.]
```

This means:

$$
x = 4,\qquad y = 3
$$

We can check the constraints manually:

$$
2(4)+4(3)=20
$$

$$
3(4)+2(3)=18
$$

Both constraints are satisfied.

We can also verify the objective:

$$
10(4)+15(3)=85
$$

So the reported solution is internally consistent.

For practical applications, validation is important because solver output can be affected by:

- Incorrect model formulation
- Incorrect input data
- Numerical precision
- Unexpected solver termination

**Key point:** A successful solver status is not a substitute for checking that the returned solution actually satisfies the model.


---
## <font color='green'> 4. Common Solver Outcomes </font>

Different solver outcomes require different actions.

### Infeasible

The constraints cannot all be satisfied simultaneously.

For example:

$$
x \geq 10
$$

and

$$
x \leq 5
$$

cannot both be true.

**What to check:**

- Conflicting constraints
- Incorrect constraint values
- Missing or incorrect variable bounds
- Overly restrictive requirements

### Unbounded

The objective can continue improving without reaching a finite optimum.

For example, a maximization problem might allow:

$$
x \rightarrow \infty
$$

without any constraint limiting $x$.

**What to check:**

- Missing constraints
- Incorrect constraint directions
- Missing variable bounds

### Time or Iteration Limit

The solver stopped before completing the optimization.

This does **not** necessarily mean the problem is infeasible or unbounded. It means the solver did not finish within the allowed computational limit.

**What to check:**

- Solver runtime
- Problem size
- Number of variables and constraints
- Whether the formulation can be simplified

### Numerical Difficulty

The solver encountered numerical problems while processing the model.

**What to check:**

- Very large or very small coefficients
- Poorly scaled data
- Nearly redundant constraints
- Numerical precision issues

**Key point:** The solver outcome tells us what happened. It also tells us what should be checked before the result is used.



---
## <font color='green'> 5. Practical Interpretation </font>

Once the solver result has been validated, the next step is to translate the output into a **decision that can be used in practice**.

A solver may return values such as:

```python
result.x
```

which could give:

```text
[4. 3.]
```

These values only become useful when mapped back to the original decision variables:

$$
x = 4 \quad \text{Product A}
$$

$$
y = 3 \quad \text{Product B}
$$

The objective value tells us the resulting performance:

$$
\text{Profit} = 85
$$

A practical interpretation therefore connects:

$$
\boxed{
\text{Solver Output}
\rightarrow
\text{Decision Variables}
\rightarrow
\text{Business Meaning}
}
$$

Before using the result, confirm:

- What does each variable represent?
- What does the objective value represent?
- Are all constraints satisfied?
- Is the solution actually implementable?
- Are the assumptions and input values still valid?

This final step is important because **an optimization solver solves the mathematical model, not the real-world problem itself**.

**Key point:** Solver output becomes useful only after it is interpreted in the context of the original problem.


---
## <font color='green'> 6. Summary </font>

Before using an LP solver result, follow a simple validation process:

$$
\boxed{
\text{Solver Status}
\rightarrow
\text{Solution Validation}
\rightarrow
\text{Practical Interpretation}
}
$$

- **Solver Status** tells us what happened during optimization.
- **Solution Validation** confirms that the returned values satisfy the model.
- **Practical Interpretation** maps the mathematical result back to the real-world decision.

The main lesson is:

> **A solver returning a result does not automatically mean the result is a valid, usable optimal solution.**

Always check the status, validate the solution, and then interpret it in the context of the original problem.



---
## Relevant Link(s)

[AI in Context Main Page](../../index.md)



