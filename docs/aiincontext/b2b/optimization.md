---
hide:
  - navigation
  
tags:
  - AI in Context
  - Optimization
  - Gradient Descent
  
---

# <font color='green'>Optimization: How Machines Find Better Solutions</font>

Optimization is the process of finding a solution that best satisfies a defined objective, often within a large space of possible solutions.

It is fundamental to AI and computational systems, providing methods for improving models, making decisions, and finding effective solutions to complex problems.

---
## <font color='green'>1. What Is Optimization?</font>

**Optimization is about finding the best, or a sufficiently good, solution to a problem according to a defined objective.**

The objective may be to minimize something, such as error or cost, or maximize something, such as accuracy or efficiency.

### The Basic Idea

An optimization problem usually involves:

- **A set of possible solutions**
- **An objective** that defines what we want to improve
- **A method** for searching for better solutions

In simple terms:

> **Define what “better” means: search for better solutions → stop when a satisfactory solution is found.**

### Examples

Optimization appears in many practical problems:

- Finding the shortest route
- Minimizing production costs
- Allocating limited resources
- Scheduling tasks
- Improving a machine learning model
- Choosing the best parameters for a system

The meaning of **“best”** depends entirely on the problem and the objective we define.

> **Optimization does not decide what is important. It helps us find a better solution according to what we specify.**

---
## <font color='green'>2. Objective Functions</font>

An objective function provides a way to measure how good a particular solution is.

In an optimization problem, we define a quantity that we want to minimize or maximize.

For example, if we want to minimize error:

**Objective = Error**

If we want to maximize performance:

**Objective = Performance**

The optimization process then searches for values that improve the objective.

### <font color='green'>Minimization and Maximization</font>

Two common forms of optimization are:

- **Minimization:** find the smallest possible value
- **Maximization:** find the largest possible value

A maximization problem can often be converted into a minimization problem by changing the sign of the objective.

### <font color='green'>Loss Functions</font>

In machine learning, an objective function is often called a **loss function**.

The loss measures how far the model's output is from the desired result.

For example:

**Data → Model → Prediction → Loss**

Training then attempts to reduce the loss by changing the model's parameters.

> **The objective function tells the optimization process what “better” means.**


---
## <font color='green'>3. The Optimization Landscape</font>

In many real problems, there is no practical way to try every possible solution.

For example:

- Finding the best route through thousands of locations
- Finding the best schedule for hundreds of tasks
- Finding the best combination of resources
- Finding the best parameters for a machine learning model

Instead, we can think of the possible solutions as an **optimization landscape**, where some solutions are better than others.

Optimization methods try to navigate this landscape and move towards better solutions.

> **The optimization landscape represents the possible solutions and how good they are.***The challenge is not just finding a solution. It is finding a good solution without trying everything.**

---
## <font color='green'>4. Local vs Global Optima</font>

Suppose you are hiking in a landscape and want to reach the highest point.

You climb a nearby hill and reach its peak. From where you are standing, there is nowhere higher to go. But that does not mean you have found the highest point in the whole landscape. There may be a much higher mountain somewhere else.

Optimization can have the same problem.

A **local optimum** is a solution that looks best in its immediate neighbourhood.

A **global optimum** is the best solution we can find across the entire search space.

This matters because an optimization method may settle on a good solution simply because it cannot see, or cannot easily reach, something better elsewhere.

> **A solution can be the best nearby without being the best overall.**

---
## <font color='green'>5. How Do We Find Better Solutions?</font>

Now consider the practical question: if we cannot try every possible solution, how do we decide where to try next?

One simple approach is to make a small change, check whether the result is better, and continue in that direction.

For example, if we are adjusting the settings of a machine learning model, we might:

**Change the settings → measure the result → keep useful changes → repeat**

Different optimization methods use different ways of deciding what to try next.

Some follow a mathematical direction, some explore alternatives, and others use randomness or evolution to discover better solutions.

> **The heart of optimization is deciding what to try next.**

---
## <font color='green'>6. Optimization Methods</font>

There are many ways to search for better solutions. The method we choose depends on the structure of the problem, the information available, and the computational resources.

### Mathematical Optimization

These methods formulate problems using variables, objectives, and constraints.

- Linear Programming
- Integer Programming
- Mixed-Integer Programming
- Nonlinear Programming
- Convex Optimization
- Constraint Programming
- Network Optimization


### Numerical Optimization

Methods that repeatedly adjust numerical values to improve an objective.

- Gradient Descent
- Stochastic Gradient Descent
- Newton's Method
- Coordinate Descent
- Quasi-Newton Methods


### Search & Heuristic Methods

Methods that explore possible solutions when examining every possibility is impractical.

- Local Search
- Hill Climbing
- Random Search
- Simulated Annealing
- Bayesian Optimization

### Evolutionary Optimization

Methods that use variation and selection to search for better solutions.

- Genetic Algorithms
- Genetic Programming
- Evolution Strategies
- Evolutionary Programming
- Particle Swarm Optimization

> **Different problems call for different optimization methods. Understanding the alternatives is often as important as understanding any individual method.**


### How Are These Approaches Different?

| Approach | Main idea | Typical character |
|---|---|---|
| **Mathematical Optimization** | Describe the problem mathematically and solve it using its structure and constraints | More analytical and formulation-driven |
| **Numerical Optimization** | Repeatedly calculate improvements to numerical values | Computational and iterative |
| **Search & Heuristic Methods** | Explore possible solutions using rules or strategies that guide the search | Exploratory and problem-dependent |
| **Evolutionary Optimization** | Generate, evaluate, select, and modify candidate solutions | Population-based and adaptive |

> The boundaries are not rigid. Some methods can be combined, and many practical systems use more than one approach.

---
## <font color='green'>7. An Example: Gradient Descent</font>

Gradient Descent is only one of many optimization methods. Its importance in modern AI comes from its effectiveness in training neural networks. It is included here because of its popularity.

Imagine you are standing somewhere on a hilly landscape and want to reach the lowest point.

You cannot see the entire landscape, but you can feel the slope where you are standing. If the ground slopes downward to your left, you can take a small step in that direction. Then you check the slope again and take another step.

That is the basic idea behind **Gradient Descent**.

In a machine learning model, the landscape represents possible parameter values, while the height represents the model's error.

The process is repeated:

**Measure the error → determine the direction of steepest descent → take a small step → repeat**

The size of the step is controlled by the **learning rate**. A very large step may overshoot a good solution, while a very small step may make the process unnecessarily slow.

This simple idea becomes powerful when applied to models with thousands, millions, or even billions of parameters.

> **Gradient Descent does not search every possible solution. It uses the local slope to decide where to move next.**

**<font color='red'>A more detailed explanation will be provided in a separate section on Gradient Descent and Neural Networks.</font>**

---
## <font color='green'>8. Choosing an Optimization Method</font>

There is no single optimization method that works well for every problem.

The right approach depends on what we know about the problem, what kind of solutions we are looking for, how expensive it is to evaluate a solution, and how much structure we can exploit.

For some problems, we can describe the problem mathematically. For others, we may need numerical methods, search, heuristics, or evolutionary approaches.

> **Good optimization starts with understanding the problem, not choosing an algorithm.**

---
## <font color='green'>8. Summary</font>

Optimization is a general approach to finding better solutions.

Different problems call for different methods: mathematical optimization, numerical methods, search and heuristics, or evolutionary approaches.

Gradient Descent is one important example because of its role in modern neural networks, but it is only one part of a much larger optimization toolbox.

> **Optimization is not one algorithm. It is a collection of ways to search for better solutions.**



---
## Relevant Link(s)

[AI in Context Main Page](../index.md)

