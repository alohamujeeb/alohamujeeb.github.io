---
hide:
  - navigation
  
tags:
  - Linear Programming
  - Sensitivity Analysis
  
---

# <font color='tomato'> Linear Programming Part 8- Sensitivity Analysis</font>
*Understanding how changes in inputs affect an LP solution. What-if analysis, objective coefficients, constraint values,shadow prices, reduced costs, and practical interpretation*


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

An LP solution depends on the **values used in the model**.

For example, changes in:

- Product profits
- Resource availability
- Production costs
- Demand requirements

can change the optimal solution.

**Sensitivity Analysis** examines how changes in these inputs affect the LP solution.

The goal is not to solve a completely new problem each time.

Instead, we ask questions such as:

- What happens if profit per unit changes?
- What happens if more resources become available?
- How valuable is an additional unit of a limited resource?
- How much can an input change before the current solution changes?

Sensitivity analysis is therefore useful for understanding the **stability and practical implications of an optimization solution**.

The basic idea is:

$$
\boxed{
\text{Change in Inputs}
\rightarrow
\text{Impact on Optimal Solution}
}
$$


---
## <font color='green'> 2. What-If Analysis </font>

**What-if analysis** asks how the solution changes when we modify one or more inputs to the LP model.

Consider:

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

Suppose the optimal solution is:

$$
x=4,\qquad y=3
$$

with:

$$
\text{Profit}=85
$$

We can then ask:

**What if the profit of Product A increases from 10 to 12?**

The objective becomes:

$$
\text{Maximize } 12x + 15y
$$

Or:

**What if the available material increases from 20 to 25?**

The constraint becomes:

$$
2x + 4y \leq 25
$$

The solver can determine whether the optimal solution changes.

This allows us to evaluate different assumptions without redesigning the entire optimization model.

$$
\boxed{
\text{Change an Input}
\rightarrow
\text{Re-solve}
\rightarrow
\text{Compare Results}
}
$$

Sensitivity analysis extends this idea by providing information about **how much an input can change and what effect that change has on the solution**.

---
## <font color='green'> 3. Changes in Objective Coefficients </font>

The **objective coefficients** determine how much each decision variable contributes to the objective.

For example:

$$
\text{Maximize } 10x + 15y
$$

Here:

- $10$ is the objective coefficient for $x$
- $15$ is the objective coefficient for $y$

Suppose the profit of Product A changes from $10$ to $12:

$$
\text{Maximize } 12x + 15y
$$

The optimal solution may change because the relative value of the products has changed.

Sensitivity analysis can help determine:

- How much an objective coefficient can change
- Whether the current optimal solution remains optimal
- How the objective value changes
- When a different solution becomes preferable

This is useful when prices, profits, costs, or other objective-related values are uncertain.

The key idea is:

$$
\boxed{
\text{Change Objective Coefficient}
\rightarrow
\text{Check Impact on Optimal Solution}
}
$$


---
## <font color='green'> 4. Changes in Constraint Values </font>

Sensitivity analysis can also examine changes in the **right-hand side values of constraints**.

For example:

$$
2x + 4y \leq 20
$$

Here, $20$ represents the available amount of the resource.

Suppose the available resource increases:

$$
2x + 4y \leq 25
$$

The additional resource may allow the optimization problem to achieve a better objective value.

Sensitivity analysis helps answer questions such as:

- What happens if more resources become available?
- What happens if resources become more limited?
- How much can a constraint value change before the optimal solution changes?
- What is the value of obtaining additional resources?

This is particularly useful for decisions involving limited resources such as:

- Budget
- Labor
- Materials
- Production capacity
- Computing resources

The key idea is:

$$
\boxed{
\text{Change Constraint}
\rightarrow
\text{Measure Impact on Solution}
}
$$


---
## <font color='green'> 5. Shadow Prices </font>

A **shadow price** measures the change in the optimal objective value resulting from a small increase in the right-hand side of a constraint, within the applicable sensitivity range.

For example, consider:

$$
2x + 4y \leq 20
$$

Suppose the shadow price of this constraint is **3**.

This means that, within the valid sensitivity range, increasing the available resource by one unit would improve the optimal objective value by approximately:

$$
3
$$

So:

$$
20 \rightarrow 21
$$

could increase the optimal objective value by approximately:

$$
85 \rightarrow 88
$$

### Practical Interpretation

Shadow prices help answer:

> **How much is one additional unit of a limited resource worth?**

For example, if the shadow price of a labor constraint is $12, then an additional hour of available labor is worth approximately $12 in terms of the objective value, within the applicable range.

This can help with decisions such as:

- Whether to purchase additional resources
- Whether to increase capacity
- Whether additional labor is worth its cost
- Which constrained resources are most valuable

A shadow price is therefore a useful way to connect an optimization model with a real-world resource decision.

$$
\boxed{
\text{Shadow Price}
=
\text{Marginal Value of a Constraint Resource}
}
$$

---
## <font color='green'> 6. Reduced Costs </font>

A **reduced cost** is associated with a decision variable that is at its bound, typically zero in a maximization problem.

It indicates how much the objective coefficient would need to improve before that variable could become part of an optimal solution, subject to the solver's sign convention.

For example, suppose:

$$
\text{Maximize } 10x + 15y
$$

and the optimal solution is:

$$
x=0,\qquad y=5
$$

If the solver reports a reduced cost of **-2** for $x$, the interpretation is that the objective coefficient for $x$ would need to improve by 2 units before $x$ becomes attractive to enter the optimal solution, under the usual maximization convention.

So the current coefficient:

$$
10
$$

would need to increase to approximately:

$$
12
$$

### Practical Interpretation

Reduced costs help answer:

> **How much would the value of a currently unused decision need to improve before it becomes worthwhile?**

They can therefore be useful for understanding:

- Why a variable is zero in the optimal solution
- How competitive an unused option is
- How much an objective coefficient needs to change
- Which currently excluded decisions are close to becoming attractive

The exact sign and interpretation depend on the solver and formulation convention, so solver documentation should be checked when interpreting reported reduced costs.

$$
\boxed{
\text{Reduced Cost}
\rightarrow
\text{How Much an Unused Variable's Value Must Improve}
}
$$


---
## <font color='green'> 7. Practical Interpretation </font>

Sensitivity analysis is mainly useful for understanding **how robust an LP solution is to changes in the model inputs**.

The main outputs can be interpreted as:

| Analysis | Practical Question |
|---|---|
| Objective coefficient | How much can profit or cost change before the solution changes? |
| Constraint value | What happens if available resources or requirements change? |
| Shadow price | What is one additional unit of a constrained resource worth? |
| Reduced cost | How much must an unused option improve before it becomes attractive? |

For example, a business may use an LP model to determine an optimal production plan.

Sensitivity analysis can then help answer:

- Should we acquire more raw material?
- Is additional production capacity valuable?
- How sensitive is the solution to changes in product profit?
- Which unused product or activity could become attractive if its economics improve?

This makes the LP solution more useful for **decision-making under changing business conditions**, rather than treating the optimal solution as a fixed answer.


---
## <font color='green'> 8. Summary </font>

Sensitivity Analysis helps us understand how changes in an LP model affect its solution.

The main concepts are:

- **Objective coefficient changes**: How changes in profits or costs affect the solution
- **Constraint value changes**: How changes in available resources or requirements affect the solution
- **Shadow prices**: The marginal value of additional constrained resources
- **Reduced costs**: How much an unused variable's objective value needs to improve before it becomes attractive

The overall idea is:

$$
\boxed{
\text{Change in Model Inputs}
\rightarrow
\text{Analyze Impact}
\rightarrow
\text{Understand Solution Stability}
}
$$

Sensitivity analysis therefore adds an important layer beyond simply finding an optimal solution.

It helps answer not only:

> **What is the optimal decision?**

but also:

> **How does that decision behave when our assumptions change?**


---
## Relevant Link(s)

[AI in Context Main Page](../../index.md)



