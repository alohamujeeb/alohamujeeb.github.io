---
hide:
  - navigation
  
tags:
  - Linear Programming
  - LP Solver
  
---



# <font color='tomato'> Linear Programming Part 4 - Practical Scenarios</font>
*Applying LP concepts to real-world optimization problems*

---
[▶ Linear Programming Part 0- About This Series](./LP-Pt0.md)

[▶ Linear Programming Part 2- Fundamental Building Blocks](./LP-Pt2.md)

[▶ Linear Programming Part 3 - Solving LP Problems](./LP-Pt3.md)

[▶ Linear Programming Part 4 - Practical Scenarios](./LP-Pt4.md)

[▶ Linear Programming Part 5 - LP Algorithms](./LP-Pt5.md)




---
## <font color='green'> 1. Introduction </font>

In the previous parts, we learned how to:

- Identify **decision variables**
- Define an **objective function**
- Define **constraints**
- Formulate an LP problem
- Find an **optimal solution**

Now we will look at how these ideas appear in different real-world situations.

The purpose of these examples is not to learn a new LP technique for every problem.

Instead, we want to recognize the same basic pattern:

$$
\boxed{
\text{Real-World Problem}
\rightarrow
\text{Decision Variables}
\rightarrow
\text{Objective}
\rightarrow
\text{Constraints}
\rightarrow
\text{LP Formulation}
}
$$

The scenario may change, but the underlying structure remains largely the same.

We will look at several simple examples from areas such as:

- Production
- Resource allocation
- Budget allocation
- Workforce planning
- Transportation
- Marketing
- Portfolio allocation
- AI/ML systems

For each scenario, we will focus mainly on **how the real-world problem is translated into an LP formulation**.

---
## <font color='green'> 2. Production Planning </font>

A common use of LP is deciding **how much of each product to produce** when resources are limited.

### Scenario

A factory produces two products:

- **Product A**
- **Product B**

Each product requires material and labor.

| | Product A | Product B |
|---|---:|---:|
| Profit per unit | $30 | $20 |
| Material per unit | 2 kg | 1 kg |
| Labor per unit | 3 hours | 2 hours |

The factory has:

- **100 kg of material**
- **120 hours of labor**

The goal is to determine how many units of each product should be produced to **maximize profit**.

### Decision Variables

Let:

$$
x = \text{number of Product A units}
$$

$$
y = \text{number of Product B units}
$$

### Objective Function

Product A generates $30 profit per unit and Product B generates $20.

Therefore:

$$
\boxed{\text{Maximize } 30x + 20y}
$$

### Constraints

**Material:**

Each A uses 2 kg and each B uses 1 kg. With 100 kg available:

$$
2x + y \leq 100
$$

**Labor:**

Each A uses 3 hours and each B uses 2 hours. With 120 hours available:

$$
3x + 2y \leq 120
$$

**Non-negativity:**

$$
x \geq 0
$$

$$
y \geq 0
$$

### Complete LP Formulation

$$
\boxed{\text{Maximize } 30x + 20y}
$$

Subject to:

$$
2x + y \leq 100
$$

$$
3x + 2y \leq 120
$$

$$
x \geq 0
$$

$$
y \geq 0
$$

The same three building blocks appear again:

**What to produce?** → Decision variables

**What to optimize?** → Profit

**What limits production?** → Material and labor

---
## <font color='green'> 3. Resource Allocation </font>

LP can also be used when a limited resource needs to be **distributed among different activities**.

### Scenario

A company has **100 hours of engineering time** available.

The company can use this time for two activities:

- **Model development**
- **Data preparation**

Each hour allocated to model development contributes 8 units of value.

Each hour allocated to data preparation contributes 5 units of value.

The company wants to decide how to allocate its available engineering time to **maximize total value**.

### Decision Variables

Let:

$$
x = \text{hours allocated to model development}
$$

$$
y = \text{hours allocated to data preparation}
$$

### Objective Function

Each hour of model development contributes 8 units of value, while each hour of data preparation contributes 5.

Therefore:

$$
\boxed{\text{Maximize } 8x + 5y}
$$

### Constraint

Only 100 engineering hours are available:

$$
x + y \leq 100
$$

We also cannot allocate a negative number of hours:

$$
x \geq 0
$$

$$
y \geq 0
$$

### Complete LP Formulation

$$
\boxed{\text{Maximize } 8x + 5y}
$$

Subject to:

$$
x + y \leq 100
$$

$$
x \geq 0
$$

$$
y \geq 0
$$

The structure is the same as the production example.

The difference is the **meaning of the decision variables and resource**.

In this case:

- **Decision variables** → Where to allocate the engineering hours
- **Objective** → Maximize total value
- **Constraint** → Only 100 hours are available

This is the general idea of **resource allocation**: deciding how to distribute limited resources across competing uses.

---
## <font color='green'> 4. Budget Allocation </font>

LP can be used to decide **how to distribute a limited budget** across different activities.

### Scenario

A company has a marketing budget of **$100,000**.

It can spend the budget on two channels:

- **Online advertising**
- **TV advertising**

Suppose:

- Each $1,000 spent on online advertising generates 8 units of expected value.
- Each $1,000 spent on TV advertising generates 5 units of expected value.

The company wants to allocate its budget to **maximize the expected value**.

### Decision Variables

Let:

$$
x = \text{thousands of dollars spent on online advertising}
$$

$$
y = \text{thousands of dollars spent on TV advertising}
$$

### Objective Function

Online advertising generates 8 units of value per $1,000, while TV advertising generates 5.

Therefore:

$$
\boxed{\text{Maximize } 8x + 5y}
$$

### Constraint

The total budget is ```$100,000```, which is 100 units of ```$1,000```:

$$
x + y \leq 100
$$

We also cannot spend a negative amount:

$$
x \geq 0
$$

$$
y \geq 0
$$

### Complete LP Formulation

$$
\boxed{\text{Maximize } 8x + 5y}
$$

Subject to:

$$
x + y \leq 100
$$

$$
x \geq 0
$$

$$
y \geq 0
$$

Again, the LP structure remains the same:

- **Decision variables** → How much to spend on each channel
- **Objective** → Maximize expected value
- **Constraint** → Stay within the available budget

---
## <font color='green'> 5. Workforce Scheduling </font>

LP can be used to decide **how many workers should be assigned to different shifts** while satisfying staffing requirements.

### Scenario

A company needs workers for two shifts:

- **Morning shift**
- **Evening shift**

Each worker can be assigned to one shift.

The company needs at least:

- 20 workers in the morning
- 15 workers in the evening

Each worker costs:

- $100 for the morning shift
- $120 for the evening shift

The company wants to **minimize total staffing cost**.

### Decision Variables

Let:

$$
x = \text{number of workers assigned to the morning shift}
$$

$$
y = \text{number of workers assigned to the evening shift}
$$

### Objective Function

The morning shift costs $100 per worker, while the evening shift costs $120.

Therefore:

$$
\boxed{\text{Minimize } 100x + 120y}
$$

### Constraints

At least 20 workers are required for the morning shift:

$$
x \geq 20
$$

At least 15 workers are required for the evening shift:

$$
y \geq 15
$$

Workers cannot be negative:

$$
x \geq 0
$$

$$
y \geq 0
$$

### Complete LP Formulation

$$
\boxed{\text{Minimize } 100x + 120y}
$$

Subject to:

$$
x \geq 20
$$

$$
y \geq 15
$$

$$
x \geq 0
$$

$$
y \geq 0
$$

The LP structure is:

- **Decision variables** → Number of workers assigned to each shift
- **Objective** → Minimize staffing cost
- **Constraints** → Meet the required staffing levels

This is a simple example of **workforce scheduling**. More realistic scheduling problems may include additional constraints such as worker availability, maximum working hours, and shift coverage.

---
## <font color='green'> 6. Transportation and Delivery </font>

LP can be used to decide **how much to transport from different locations** while minimizing delivery costs.

### Scenario

A company has two warehouses:

- **Warehouse A**
- **Warehouse B**

It needs to deliver products to two stores:

- **Store 1**
- **Store 2**

The available supply and store requirements are:

| Location | Amount |
|---|---:|
| Warehouse A supply | 60 units |
| Warehouse B supply | 40 units |
| Store 1 demand | 50 units |
| Store 2 demand | 50 units |

The transportation cost per unit is:

| Route | Cost per unit |
|---|---:|
| A → Store 1 | $4 |
| A → Store 2 | $6 |
| B → Store 1 | $5 |
| B → Store 2 | $3 |

The company wants to **minimize total transportation cost**.

### Decision Variables

Let:

$$
x_1 = \text{units shipped from A to Store 1}
$$

$$
x_2 = \text{units shipped from A to Store 2}
$$

$$
x_3 = \text{units shipped from B to Store 1}
$$

$$
x_4 = \text{units shipped from B to Store 2}
$$

### Objective Function

The total transportation cost is:

$$
\boxed{\text{Minimize } 4x_1 + 6x_2 + 5x_3 + 3x_4}
$$

### Constraints

Warehouse A has at most 60 units:

$$
x_1 + x_2 \leq 60
$$

Warehouse B has at most 40 units:

$$
x_3 + x_4 \leq 40
$$

Store 1 needs 50 units:

$$
x_1 + x_3 \geq 50
$$

Store 2 needs 50 units:

$$
x_2 + x_4 \geq 50
$$

All shipment quantities must be non-negative:

$$
x_1,x_2,x_3,x_4 \geq 0
$$

### Complete LP Formulation

$$
\boxed{\text{Minimize } 4x_1 + 6x_2 + 5x_3 + 3x_4}
$$

Subject to:

$$
x_1 + x_2 \leq 60
$$

$$
x_3 + x_4 \leq 40
$$

$$
x_1 + x_3 \geq 50
$$

$$
x_2 + x_4 \geq 50
$$

$$
x_1,x_2,x_3,x_4 \geq 0
$$

The structure is:

- **Decision variables** → How much to ship along each route
- **Objective** → Minimize transportation cost
- **Constraints** → Respect warehouse supply and store demand

This type of problem is commonly called a **transportation problem**, which is a specific class of optimization problem that can be formulated as an LP.

---
## <font color='green'> 7. Marketing Allocation </font>

LP can be used to decide **how to distribute a limited marketing budget across different channels**.

### Scenario

A company has a marketing budget of **$50,000**.

It can spend the budget on:

- **Social media advertising**
- **Search advertising**

Suppose:

- Each $1,000 spent on social media generates 12 units of expected reach.
- Each $1,000 spent on search advertising generates 8 units of expected reach.

The company wants to **maximize expected reach**.

However, the company wants to spend at least $10,000 on search advertising.

### Decision Variables

Let:

$$
x = \text{thousands of dollars spent on social media}
$$

$$
y = \text{thousands of dollars spent on search advertising}
$$

### Objective Function

The expected reach is:

$$
\boxed{\text{Maximize } 12x + 8y}
$$

### Constraints

The total marketing budget is $50,000:

$$
x + y \leq 50
$$

At least $10,000 must be spent on search advertising:

$$
y \geq 10
$$

Spending cannot be negative:

$$
x \geq 0
$$

$$
y \geq 0
$$

### Complete LP Formulation

$$
\boxed{\text{Maximize } 12x + 8y}
$$

Subject to:

$$
x + y \leq 50
$$

$$
y \geq 10
$$

$$
x \geq 0
$$

$$
y \geq 0
$$

The structure is:

- **Decision variables** → How much to spend on each marketing channel
- **Objective** → Maximize expected reach
- **Constraints** → Stay within the budget and satisfy minimum spending requirements

The same LP pattern can therefore be applied to marketing decisions involving multiple channels, budgets, and business requirements.

---
## <font color='green'> 8. Portfolio Allocation </font>

LP can be used to decide **how to distribute a limited amount of money across different investments**.

### Scenario

An investor has **$100,000** to allocate between two investment options:

- **Investment A**
- **Investment B**

Suppose:

- Investment A generates 6 units of expected return per $1,000 invested.
- Investment B generates 4 units of expected return per $1,000 invested.

The investor wants to **maximize expected return**.

However, the investor wants to keep at least $30,000 in Investment B.

### Decision Variables

Let:

$$
x = \text{thousands of dollars invested in Investment A}
$$

$$
y = \text{thousands of dollars invested in Investment B}
$$

### Objective Function

The expected return is:

$$
\boxed{\text{Maximize } 6x + 4y}
$$

### Constraints

The total available investment is $100,000:

$$
x + y \leq 100
$$

At least $30,000 must be invested in Investment B:

$$
y \geq 30
$$

Investment amounts cannot be negative:

$$
x \geq 0
$$

$$
y \geq 0
$$

### Complete LP Formulation

$$
\boxed{\text{Maximize } 6x + 4y}
$$

Subject to:

$$
x + y \leq 100
$$

$$
y \geq 30
$$

$$
x \geq 0
$$

$$
y \geq 0
$$

The structure is:

- **Decision variables** → How much money to allocate to each investment
- **Objective** → Maximize expected return
- **Constraints** → Stay within the available money and satisfy allocation requirements

In real portfolio optimization, additional constraints may represent risk limits, diversification requirements, or investment restrictions.


---
## <font color='green'> 9. AI/ML-Related Optimization Examples </font>

LP can also appear in **AI/ML systems**, usually as a supporting optimization component rather than the machine learning model itself.

The ML model may produce predictions, scores, or probabilities.

An optimization method can then use those outputs to make the final decision while satisfying business constraints.
---

### **Scenario 1: Recommendation Selection**

Suppose an ML model gives each movie a recommendation score.

We want to select movies for a user's recommendation list.

Let:

$$
x_i =
\begin{cases}
1 & \text{if movie } i \text{ is selected} \\
0 & \text{otherwise}
\end{cases}
$$

If movie $i$ has recommendation score $s_i$, the objective could be:

$$
\boxed{\text{Maximize } \sum_i s_i x_i}
$$

Suppose we want to recommend exactly 5 movies:

$$
\sum_i x_i = 5
$$

We could also add constraints such as:

$$
\sum_{i \in \text{Action}} x_i \leq 2
$$

This prevents more than two Action movies from appearing in the list.

---
### **Scenario 2: Resource Allocation for ML Systems**

Suppose an AI system has limited computing resources.

We need to decide how much computing capacity to allocate to different ML workloads.

Let:

$$
x = \text{computing resources allocated to Model A}
$$

$$
y = \text{computing resources allocated to Model B}
$$

If the expected value produced by each resource unit is 8 and 5:

$$
\boxed{\text{Maximize } 8x + 5y}
$$

With a total resource limit:

$$
x + y \leq 100
$$

And:

$$
x,y \geq 0
$$

### Key Idea

In these examples:

$$
\text{ML Model}
\rightarrow
\text{Predictions / Scores}
\rightarrow
\text{Optimization}
\rightarrow
\text{Final Decision}
$$

The ML model produces information that can be used by an optimization problem.

Therefore, LP is **not replacing the ML model**.

Instead, it can help turn model outputs into decisions while respecting constraints.

---
## <font color='green'> 10. Summary </font>

Across all these scenarios, the same basic pattern appears:

$$
\boxed{
\text{Real-World Problem}
\rightarrow
\text{Decision Variables}
\rightarrow
\text{Objective}
\rightarrow
\text{Constraints}
\rightarrow
\text{LP Formulation}
}
$$

The application changes, but the underlying LP structure remains similar.

We covered examples involving:

- Production planning
- Resource allocation
- Budget allocation
- Workforce scheduling
- Transportation
- Marketing allocation
- Portfolio allocation
- AI/ML systems

The main skill to develop is recognizing **what decisions need to be made, what should be optimized, and what limitations must be satisfied**.




---
## Relevant Link(s)

[AI in Context Main Page](../../index.md)

[LP Solver Website](https://opensolver.org/)


