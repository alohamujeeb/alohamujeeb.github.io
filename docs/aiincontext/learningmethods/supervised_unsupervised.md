---
hide:
  - navigation
  
tags:
  - Supervised Learning
  - Unsupervised Learning
  
---

# <font color='green'>Supervised vs. Unsupervised Learning (Teaching vs. Self Learning)</font>
*When We Teach Machines the Answer, and When We Let Them Discover*


---
## <font color='green'>1. Two Ways of Learning</font>

There are two simple ways in which humans learn.

1. **Someone teaches us.**  
   A teacher gives us examples, explains what is right or wrong, and guides us towards the desired answer.

2. **We learn on our own.**  
   We observe the world, notice patterns, experiment, and gradually build our own understanding.

Machines can learn in similar ways.

In AI, these two broad approaches are commonly described as **supervised learning** and **unsupervised learning**.

> **Supervised learning: someone provides the answers.**  
> **Unsupervised learning: the machine discovers patterns for itself.**

---
## <font color='green'>2. Supervised Learning: Someone Teaches the Machine</font>

This is **Way 1 of Learning: someone teaches us**.

A teacher provides examples, tells us the correct answers, and helps us learn from those examples.

Imagine teaching a child to recognize apples.

You show the child an apple and say, **"This is an apple."** You show another fruit and say, **"This is not an apple."** After seeing enough examples, the child begins to recognize apples independently.

Supervised learning follows the same basic idea.

We provide the machine with examples where the **correct answer is already known**. The machine learns the relationship between the input and the expected answer, and then uses what it has learned to make predictions about new data.

**Examples + Known Answers → Learning → New Examples → Prediction**

> **Supervised learning is learning with a teacher.**

---
## <font color='green'>3. Unsupervised Learning: Learning on Its Own</font>

This is **Way 2 of Learning: we learn on our own**.

Nobody tells us the answers. We observe, compare, notice patterns, and gradually discover structure for ourselves.

Imagine walking into a room full of unfamiliar objects. Nobody tells you what they are. You might notice that some objects look similar, some are larger, some have similar shapes, and some seem to belong together.

Unsupervised learning works in a similar way.

We give the machine data **without predefined answers** and allow it to discover patterns, relationships, or groups within that data.

**Data → Discover Patterns → Find Structure**

For example, a system might examine thousands of customer records and discover groups of customers with similar behaviour, even though nobody defined those groups beforehand.

> **Unsupervised learning is learning without a teacher.**


---
## <font color='green'>4. The Key Difference: Answers vs. Discovery</font>

The simplest way to see the difference is to look at what we give the machine.

### Supervised Learning

We provide:

**Data + Correct Answers**

The machine learns how to produce the correct answer for new data.

### Unsupervised Learning

We provide:

**Data**

The machine looks for patterns, relationships, or groups within the data.

The difference is therefore not simply about the algorithms being used. It is fundamentally about **whether the learning process has predefined answers to learn from**.

| | Supervised Learning | Unsupervised Learning |
|---|---|---|
| **Input** | Data + answers | Data |
| **Guidance** | Teacher / labels | No predefined answers |
| **Goal** | Learn to predict the answer | Discover patterns or structure |
| **Typical use** | Classification, prediction | Clustering, discovery |

> **Supervised learning learns from answers. Unsupervised learning learns from structure.**

---
## <font color='green'>5. What Does the Machine Actually Learn?</font>

In both approaches, the machine is trying to find **patterns in the data**.

The difference is what guides the search.

In supervised learning, the known answers tell the machine whether its predictions are getting better or worse.

In unsupervised learning, there are no predefined answers. The machine has to find useful patterns using properties of the data itself.

For example, given information about thousands of customers:

**Supervised:**  
"Given these customer details, will this customer leave?"

**Unsupervised:**  
"Are there naturally occurring groups of customers with similar behaviour?"

The first has a predefined target. The second asks the machine to discover structure.

> **Both learn patterns. The difference is whether we provide a target for the machine to learn.**

---
## <font color='green'>6. Two Approaches, Different Problems</font>

The difference becomes clearer when we look at real situations.

### Supervised Learning

- **Email filtering:** learn from emails already marked as spam or not spam.
- **Medical diagnosis:** learn from cases where the diagnosis is already known.
- **House prices:** learn from houses with known sale prices.
- **Image recognition:** learn from images that have already been labelled.

### Unsupervised Learning

- **Customer groups:** discover groups of customers with similar behaviour.
- **Fraud discovery:** identify unusual patterns without having every fraudulent case labelled.
- **Document analysis:** discover themes or groups within a large collection of documents.
- **Data exploration:** find relationships or structures that were not known beforehand.

The choice depends largely on what information is available.

> **If we have reliable answers, we can teach the machine from them. If we do not, we may ask the machine to discover structure in the data.**


----
## <font color='green'>7. Common Algorithms</font>

The following are some of the commonly used approaches in supervised and unsupervised learning.

### Supervised Learning Algorithms

- Linear Regression
- Logistic Regression
- Decision Trees
- Random Forests
- Support Vector Machines
- k-Nearest Neighbours
- Neural Networks

### Unsupervised Learning Algorithms

- k-Means Clustering
- Hierarchical Clustering
- DBSCAN
- Gaussian Mixture Models
- Principal Component Analysis (PCA)
- Autoencoders
- Association Rule Learning

This list is provided mainly as a reference. Individual methods can be explored separately as the project develops.

---
## <font color='green'>8. Summary</font>

Supervised and unsupervised learning are two fundamental ways of learning from data.

**Supervised learning** learns from labelled examples where the desired answer is known. Common algorithms include:

- Linear Regression
- Logistic Regression
- Decision Trees
- Random Forests
- Support Vector Machines
- k-Nearest Neighbours
- Neural Networks

**Unsupervised learning** works without predefined answers and looks for patterns or structure in the data. Common algorithms include:

- k-Means Clustering
- Hierarchical Clustering
- DBSCAN
- Gaussian Mixture Models
- Principal Component Analysis (PCA)
- Autoencoders
- Association Rule Learning

The key distinction is simple:

> **Supervised learning learns from known answers. Unsupervised learning discovers structure without predefined answers.**

These are broad approaches rather than individual algorithms. The choice of algorithm depends on the problem, the available data, and what we want the system to learn.




---
## Relevant Link(s)

[AI in Context Main Page](../index.md)

