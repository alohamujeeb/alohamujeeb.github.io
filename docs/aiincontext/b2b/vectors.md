---
hide:
  - navigation
tags:
  - AI in Context
  - Vectors
  - Embeddings
  
---

# <font color='green'>Vectors: The Language of Modern AI</font>

Vectors are one of the fundamental mathematical structures behind many modern AI systems.

They provide a way to represent data, features, relationships, and meaning in a form that machines can process computationally.

**This article assumes a basic understanding of vectors at the pre-university mathematics level.**

---

## <font color='green'>1. Why Are Vectors Important in AI?</font>

One practical reason vectors are so important is that **modern computers, especially GPUs and other AI accelerators, are highly optimized for operations on vectors and matrices**.

As a result:

> Much of the data used by AI systems is represented numerically as **vectors**, and collections or transformations of these vectors naturally lead to **matrices and higher-dimensional structures**.

This gives us a powerful combination:

> **Real-world data → numerical representation → vectors → matrices → highly optimized computation**

Understanding vectors is therefore not just a matter of mathematical elegance. It is closely connected to **how modern AI systems actually perform computation**.

---

## <font color='green'>2. What Is a Vector?</font>

At its simplest, **a vector is an ordered collection of numbers.**

In mathematics, vectors can represent quantities such as **magnitude and direction**. In AI, however, vectors are often used more generally as a convenient numerical representation of information.

> In AI, the key advantage of vectors is not direction, but **the efficient mathematical operations they support**, especially at large scale.

For example, a vector might represent:

- the properties of an object
- the features of an image
- the characteristics of a word
- the state of a system
- the parameters of a model

A vector is simply an ordered collection of numbers:

**x = [x₁, x₂, x₃]**

Here, the vector has three components, or dimensions.

The important idea is:

> **Convert information into numbers so that mathematical operations can be performed on it.**

Once information is represented as vectors, AI algorithms can compare, transform, combine, and process that information efficiently.

The important idea for AI is not simply that a vector contains numbers. It is that **a collection of numbers can represent something meaningful that a computer can process mathematically**.

**Examples of vectors in AI:**

- An image can be represented by a vector of pixel values. 2D or 3D matrices are also used.
- A word or sentence can be represented by a vector of numbers.
- A person can be represented by a vector of characteristics.
- A machine learning model can represent features as vectors.

As we move from simple examples to modern AI, the number of dimensions can become very large. This allows complex information to be represented in a form suitable for mathematical computation.

---

## <font color='green'>3. Vector Operations</font>

Vectors become useful in AI because we can perform mathematical operations on them.

Some of the most important operations are:

- Addition and subtraction
- Scalar multiplication
- Dot product
- Magnitude
- Distance
- Similarity

These operations allow AI systems to **compare, transform, and combine numerical representations**.

For example, the **dot product** provides a simple way of measuring how strongly two vectors are related mathematically. This idea becomes important later in machine learning, embeddings, and neural networks.

### Vector Operations in Python

For basic vector operations, Python libraries such as NumPy provide convenient implementations.

| Operation | Python / NumPy |
|---|---|
| Addition | `a + b` |
| Subtraction | `a - b` |
| Scalar multiplication | `3 * a` |
| Dot product | `np.dot(a, b)` |
| Magnitude | `np.linalg.norm(a)` |
| Distance | `np.linalg.norm(a - b)` |
| Similarity | `np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))` |

For the examples above:

    import numpy as np

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

---

## <font color='green'>4. From Features to Vectors to Matrices</font>

In machine learning, information about an object or event is often described through **features**.

For example, a house may have features such as:

- Size
- Number of rooms
- Age
- Location

These features can be represented as numbers and arranged into a vector:

**house = [size, rooms, age, location]**

> **Information → Features → Vector → Machine Learning Model**

When we have many examples, their feature vectors can be arranged together to form a **matrix**.

For example:

**house₁ = [1200, 3, 10, 2]**

**house₂ = [1800, 4, 5, 3]**

**house₃ = [950, 2, 20, 1]**

These vectors can be arranged as rows in a matrix, giving us a convenient way to represent **many examples and their features together**.

> **One example → Vector**  
> **Many examples → Matrix**

This progression from **features to vectors to matrices** is fundamental to how machine learning systems represent and process data.

---

## <font color='green'>5. Vector Similarity</font>

In many AI applications, we want to know how similar two vectors are.

This is particularly important when vectors represent things such as words, documents, images, or other forms of information.

One common measure is **cosine similarity**, which compares the relationship between two vectors.

### Cosine Similarity

Cosine similarity measures how closely two vectors are aligned. It is useful when we want to compare the **pattern or proportion of values** rather than their absolute size.

The value ranges from **-1 to 1**:

- **1** = same direction
- **0** = unrelated directions
- **-1** = opposite directions

### Example 1: Similar Data

Suppose we represent two houses using two features: **size** and **number of rooms**.

**House A = [100, 4]**

**House B = [200, 8]**

House B is twice the size of House A and has twice as many rooms. The two vectors have exactly the same proportions, so they point in the same direction.

**Cosine similarity = 1.0**

The vectors have different magnitudes, but their pattern is identical.

### Example 2: Different Data

Now consider:

**House A = [100, 4]**

**House C = [100, 1]**

The houses have the same size, but their number of rooms is very different. The vectors therefore point in different directions.

**Cosine similarity ≈ 0.97**

The value is still high because the size feature dominates the vectors. This also illustrates that cosine similarity considers the **relationship between the components**, not their absolute values.

> <font color='red'>**Mathematically, "same direction" means the vectors point in the same direction. In AI, it means that the information represented by the vectors has a similar pattern or meaning.**</font>



### Computing Cosine Similarity

Cosine similarity is calculated using the **dot product** of two vectors and their **magnitudes**.

**Cosine similarity = (A · B) / (|A| × |B|)**

### Example 1: Two-Value Vectors

Consider two vectors:

**A = [2, 3]**

**B = [4, 6]**

The dot product is:

**A · B = (2 × 4) + (3 × 6) = 26**

Their magnitudes are:

**|A| = √(2² + 3²) = √13**

**|B| = √(4² + 6²) = √52**

Therefore:

**Cosine similarity = 26 / (√13 × √52) = 1**

The vectors have the same proportions, so their cosine similarity is **1**.

In Python:

    import numpy as np

    A = np.array([2, 3])
    B = np.array([4, 6])

    similarity = np.dot(A, B) / (
        np.linalg.norm(A) * np.linalg.norm(B)
    )

    print(similarity)

Output:

    1.0

### Example 2: Two 2×2 Matrices

Cosine similarity can also be applied to matrices by treating each matrix as a single vector.

Consider:

**A = [[1, 2], [3, 4]]**

**B = [[1, 2], [4, 3]]**

First, flatten the matrices:

**A → [1, 2, 3, 4]**

**B → [1, 2, 4, 3]**

We can now calculate their cosine similarity just as we did with ordinary vectors.

In Python:

    A = np.array([[1, 2], [3, 4]])
    B = np.array([[1, 2], [4, 3]])

    similarity = np.dot(
        A.flatten(),
        B.flatten()
    ) / (
        np.linalg.norm(A) * np.linalg.norm(B)
    )

    print(similarity)

Output:

    0.9333

The matrices are similar, but not identical, so their cosine similarity is less than **1**.

> **A matrix can be flattened into a vector, allowing vector-based similarity measures such as cosine similarity to be applied to it.**

> <font color='red'>Cosine similarity is fundamentally a vector operation. For matrices or higher-dimensional tensors, they can be flattened into vectors, or similarity can be calculated along specific dimensions depending on what the dimensions represent. </font>


### Applications of Vector Similarity

- **Semantic search:** Find documents whose embeddings are most similar to a user's query.
- **Recommendation:** Find products similar to a product the user likes.
- **Image search:** Find images visually similar to a reference image.
- **Duplicate detection:** Identify documents or images with highly similar representations.
- **Classification:** Compare a new data point with known examples or class representations.
- **RAG:** Find relevant information for an LLM query.


---

## <font color='green'>6. Embeddings: From Information to Vectors</font>

An **embedding** is a vector representation of information such as a word, sentence, image, or other object.

The key idea is that information with similar characteristics can be represented by vectors that are close or similar in the vector space.

For example, words such as:

**cat → [ ... ]**

**dog → [ ... ]**

may have similar representations because they have similar meanings or occur in similar contexts.

This allows AI systems to use mathematical operations to work with relationships between pieces of information.

> **Information → Embedding → Vector → Mathematical Comparison**

### Feature Vectors and Embeddings

A **feature vector** and an **embedding** are both vector representations of information.

The main difference is how they are produced:

- **Feature vector:** features are usually explicitly selected or calculated.
- **Embedding:** <font color='red'>features are typically learned automatically from data.</font>

In both cases, the result is a vector that allows a machine learning system to perform mathematical operations on the represented information.

> **Feature vector and embedding are both ways of representing information as vectors.**

---

## <font color='green'>7. High-Dimensional Vectors</font>

Modern AI systems often work with vectors containing hundreds or thousands of dimensions.

A vector is still simply an ordered collection of numbers:

**[0.21, -0.47, 0.83, ... , 0.12]**

When these vectors are combined into larger structures, they form **matrices and higher-dimensional arrays (tensors)**.

For example:

> **Vector → Matrix → Higher-dimensional array (Tensor)**

These higher-dimensional structures allow AI systems to represent and process increasingly complex data.

The underlying mathematics remains the same. The structures simply become larger and more complex.

---

## <font color='green'>8. Vectors in Modern AI Models</font>

Vectors and matrices are fundamental to how modern AI models represent and process information.

### Neural Networks

Neural networks perform a large number of mathematical operations on vectors and matrices.

Input data is represented as vectors, which are processed through the network using weights, biases, and activation functions.

> **Input Vector → Neural Network → Output Vector**

The weights of a neural network are also represented using vectors and matrices. During training, these values are adjusted to improve the model's output.

Understanding vectors and matrices therefore helps explain what is happening inside a neural network.

### Large Language Models

Large Language Models also rely heavily on vector representations.

Words and tokens are converted into vectors that a neural network can process. These vectors are repeatedly processed by the network to capture relationships and context within the text.

> **Text → Tokens → Vectors → Neural Network → Output**

This is one of the fundamental ways mathematical representations connect to modern language models.

### Computer Vision

Images can also be represented using vectors and matrices.

A digital image consists of pixels, with each pixel represented by numerical values. These values can be arranged into matrices or converted into vectors for processing by AI models.

> **Image → Pixel Values → Matrix / Vector → AI Model → Prediction**

Modern computer vision models process these numerical representations to identify patterns such as shapes, objects, and other visual features.

---

## <font color='green'>9. Conclusion</font>

Vectors provide an efficient way to represent **features and other numerical information** so that AI systems can perform mathematical operations on them at large scale.

We have seen how vectors can be used to:

- Represent features and information
- Organize multiple examples into matrices
- Compare representations using **vector similarity**
- Measure relationships between data using **cosine similarity**
- Represent learned features through **embeddings**
- Support computation in neural networks
- Represent text in Large Language Models
- Represent numerical image data in computer vision

The key progression is:

> **Information → Features → Vectors → Matrices → AI Computation**

Understanding vectors therefore provides a practical foundation for understanding how modern AI systems **represent, compare, transform, and process information**.



---
## Relevant Link(s)

[AI in Context Main Page](../index.md)

[▶ Beyond 3D: Extending the Mathematics We Already Know](../../blog/posts/2026-07-08-HigherDimensionMaths.md)

[▶ Tensors: Extending Vectors and Matrices](./tensors.md)
