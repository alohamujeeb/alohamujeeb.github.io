---
hide:
  - navigation
  
tags:
  - AI in Context
  - Tensors
  
---

# <font color='green'>Tensors: Extending Vectors and Matrices</font>

Tensors extend the idea of vectors and matrices to higher dimensions, providing a practical way to represent and process complex numerical data.

They are fundamental to modern AI systems because they allow large amounts of structured data to be handled efficiently.

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
## <font color='green'>3. Dimensions, Axes and Shape</font>

When working with tensors, **dimensions** describe how many axes the tensor has, while **shape** describes the size along each axis.

For example, a colour image might have the shape:

**[224, 224, 3]**

This means:

- **224** pixels in height
- **224** pixels in width
- **3** colour channels

A batch of 32 such images could have the shape:

**[32, 224, 224, 3]**

Here, the four axes represent:

**Batch × Height × Width × Channels**

> **Dimensions tell us how many axes a tensor has. Shape tells us the size of each axis.**

---
## <font color='green'>4. Tensor Operations</font>

Tensors are useful not simply because they can store multi-dimensional data, but because we can perform mathematical operations on them efficiently <font color='red'>**and in parallel**.</font>

Common operations include:

- Addition and subtraction
- Multiplication
- Matrix multiplication
- Reshaping
- Transposing
- Slicing
- Aggregation

For example, a tensor can be reshaped without changing the underlying values, allowing the same data to be organized differently for different computations.

These operations form the basic building blocks used by neural networks and other AI models.

> **Represent data as tensors → perform mathematical operations → produce new tensors**

---
## <font color='green'>5. Tensors in AI</font>

Modern AI models process large amounts of numerical data, making tensors a natural representation for both **data and model parameters**.

For example:

- Images can be represented as tensors.
- Text and embeddings can be represented as tensors.
- Neural network weights can be stored as tensors.
- Intermediate results inside a neural network are tensors.

This allows AI frameworks to perform large numbers of mathematical operations efficiently, often in parallel on GPUs and other AI accelerators.

> **Data → Tensors → Mathematical Operations → AI Model → Output**


---
## <font color='green'>6. Tensors in Computer Vision and Language Models</font>

Tensors are used extensively in both computer vision and language models, although the data they represent is different.

### Computer Vision

An image can be represented as a tensor containing its pixel values.

For example:

**Height × Width × Channels**

A batch of images adds another dimension:

**Batch × Height × Width × Channels**

This allows vision models to process many pixels and many images through tensor operations in parallel.

### Language Models

Language models also work with tensors.

Text is first converted into tokens, which are then represented numerically. These representations are stored and processed as tensors throughout the neural network.

> **Text → Tokens → Tensor representations → Neural Network → Output**

The same underlying tensor operations can therefore support very different types of AI data.


---
## <font color='green'>7. Tensors and AI Hardware</font>

Tensors fit naturally with modern AI hardware because their operations can be performed **in parallel**.

GPUs contain many processing units that can perform large numbers of similar mathematical operations simultaneously. This makes them particularly effective for the matrix and tensor operations used by neural networks.

This is one reason modern AI systems can process very large models and datasets efficiently.

> **Tensors provide the data structure; AI hardware provides the parallel computation.**

The combination of suitable numerical structures and highly parallel hardware is a key part of modern AI computing.

---
## <font color='green'>8. Practical Tensor Operations with Python</font>

Python libraries such as **NumPy** and **PyTorch** provide simple ways to create and manipulate tensors.

For example, with PyTorch:

    import torch

    x = torch.tensor([[1, 2, 3],
                      [4, 5, 6]])

    print(x.shape)
    print(x + 10)
    print(x * 2)

The same basic ideas we have seen with vectors and matrices extend naturally to tensors.

| Operation | PyTorch |
|---|---|
| Create tensor | `torch.tensor(...)` |
| Shape | `x.shape` |
| Addition | `x + y` |
| Multiplication | `x * y` |
| Matrix multiplication | `x @ y` |
| Reshape | `x.reshape(...)` |
| Transpose | `x.T` |

The purpose here is not to learn PyTorch in depth, but to see how the mathematical concepts translate directly into practical AI programming.

---
## <font color='green'>9. Working with Tensors</font>

Tensors can be created, manipulated, and processed using several popular Python frameworks.

### Python
**NumPy** provides general-purpose multi-dimensional arrays and is useful for understanding the basic operations underlying tensor computation.


### PyTorch
**PyTorch** provides tensors specifically designed for machine learning, including GPU computation and automatic differentiation.


### TensorFlow

**TensorFlow** provides its own tensor structure and a broad ecosystem for building and training machine learning models. It supports CPU, GPU, and other hardware acceleration.


### Other Frameworks

Other libraries and frameworks provide additional capabilities for tensor computation, model training, and hardware acceleration. These include:

- JAX
- MXNet
- ONNX
- CuPy

The choice of framework depends on the task, hardware, ecosystem, and other engineering requirements.


> **The tensor concept is independent of any particular framework. The frameworks provide tools for creating, manipulating, and computing with tensors.**


---
## <font color='green'>10. Summary</font>

Tensors provide a common way to represent and process numerical data across different dimensions.

The progression is:

**Scalar → Vector → Matrix → Tensor**

Vectors and matrices are therefore not separate from tensors. They are simpler cases of the same general concept.

Tensors are important in modern AI because they allow large amounts of structured numerical data to be processed efficiently and in parallel.

They are used throughout modern AI, including:

- Neural networks
- Computer vision
- Large Language Models
- Embeddings
- AI accelerators

> **Data → Numerical Representation → Tensor → Parallel Computation → AI Model**

Understanding tensors provides an important foundation for understanding how modern AI systems represent and process data.



---
## Relevant Link(s)

[AI in Context Main Page](../index.md)

[▶ Beyond 3D: Extending the Mathematics We Already Know](../../blog/posts/2026-07-08-HigherDimensionMaths.md)

[▶ Vectors: Language of AI](./vectors.md)
