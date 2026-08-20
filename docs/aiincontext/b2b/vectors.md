---
hide:
  - navigation
  
tags:
  - AI in Context
  - Vectors
  - Cosine Similarity
  - Embeddings
  
---

# <font color='green'>Vectors: The Language of Mern AI</font>

Tensors extend the idea of vectors and matrices to higher dimensions, providing a practical way to represent and process complex numerical data.

They are fundamental to modern AI systems because they allow large amounts of structured data to be handled efficiently.

Prerequisite: This article assumes a basic understanding of vectors and matrices.

---
## <font color='green'>1. Why Do We Need Tensors?</font>

AI systems often work with numerical data arranged in different numbers of dimensions.

A **tensor** is a general term for such a numerical structure. A scalar, vector, and matrix can all be considered tensors:

> **Scalar → 0D tensor**  
> **Vector → 1D tensor**  
> **Matrix → 2D tensor**  
> **3D, 4D, ... → Higher-dimensional tensors**

The need for tensors becomes particularly clear when data has more than two dimensions.

For example, a colour image can be represented as:

**Height × Width × Colour Channels**

A collection of images adds another dimension:

**Number of Images × Height × Width × Colour Channels**

Tensors provide a common structure for representing and processing this type of multi-dimensional data efficiently.

> **Tensor is the general concept; vectors and matrices are special cases.**

---
## <font color='green'>2. From Vectors and Matrices to Tensors</font>

The easiest way to understand tensors is to see how dimensions are added.

A **vector** is a one-dimensional collection of numbers:

**[1, 2, 3, 4]**

A **matrix** is a two-dimensional arrangement of numbers:

**[1, 2, 3]**  
**[4, 5, 6]**

A 3D tensor adds another dimension. For example, several matrices can be stacked together:

**Matrix 1**  
**Matrix 2**  
**Matrix 3**

The same idea continues for higher dimensions.

> **Vector → Matrix → 3D Tensor → 4D Tensor → ...**

The important change is not the numbers themselves, but **how many dimensions are needed to organize them**.

For example, a colour image naturally has three dimensions:

**Height × Width × Channels**

A batch of such images has four:

**Batch × Height × Width × Channels**



---
## Relevant Link(s)

[AI in Context Main Page](../index.md)

[▶ Beyond 3D: Extending the Mathematics We Already Know](../../blog/posts/2026-07-08-HigherDimensionMaths.md)

[▶ Tensors: Extending Vectors and Matrices](./tensors.md)
