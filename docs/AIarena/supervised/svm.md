---
hide:
  - navigation
  
  
tags:
  - Support Vector Machine
  - SVM
---

# Support Vector Machine (SVM)

---
## 1. What is SVM

* SVM a type of machine learning algorithm used to:

		1. classify things into categories, 
		
		2. predict values.

* It is like: **drawing the best possible dividing line between two groups of data.**

---
## 2. A simple example
* Suppose we want a machine to identify:

		1. cat
		2. dog

* We give it 2 parameters (features) only:
		---
## 1. What is SVM
		1. weight
		2. size
		
### Step 1: Create dataset

| Animal | Weight (kg) | Size (cm) |
|--------|-------------|------------|
| Cat    | 4           | 25         |
| Cat    | 5           | 28         |
| Cat    | 6           | 30         |
| Dog    | 18          | 60         |
| Dog    | 22          | 70         |
| Dog    | 25          | 75         |

### Step 2: Plot the points
- Imagine a graph:

		x-axis = weight
		y-axis = size

- Cats appear clustered in one area:

		smaller
		lighter

- Dogs appear in another:
		
		larger
		heavier

### Step 3: Draw a boundary
- SVM draws a line between them.

- For exammple: 
	
		y = mx + b

- But **many lines could separate them**.

- SVM chooses the line with:

		- the largest safety gap
		- maximum distance from both groups

---
## 3. The actual math

Internally, SVM computes something like:

$$
w_1 x_1 + w_2 x_2 + b = 0
$$

Where,

$$
\begin{aligned}
x_1 &= \text{weight} \\
x_2 &= \text{size} \\
w_1, w_2 &= \text{importance of each feature} \\
b &= \text{boundary offset}
\end{aligned}
$$


---
## 4. Python example

``` python
from sklearn import svm

# X = [weight, size]
# weight = mass of the animal (kg)
# size   = height/length of the animal (cm

X = [
    [4, 25],
    [5, 28],
    [6, 30],
    [18, 60],
    [22, 70],
    [25, 75]
]

y = [-1, -1, -1, 1, 1, 1]

model = svm.SVC(kernel='linear')
model.fit(X, y)

test_point = [[20, 65]]
prediction = model.predict(test_point)[0]

print("Prediction:", "Dog 🐶" if prediction == 1 else "Cat 🐱")

print("Weights:", model.coef_[0])
print("Bias:", model.intercept_[0])
```

**expected output**
``` text
Prediction: Dog 🐶
Weights: [0.32258065 0.80645161]
Bias: -25.61290323
```

---
## 5. Three parameter example

- This is a Support Vector Machine (SVM) example for a loan approval system.

- It uses **three** features, income, credit score, and debt ratio to classify whether a loan should be approved or rejected based on past data.

- actual maths is:

$$
w_1 x_1 + w_2 x_2 + w_3 x_3 + b = 0
$$

!!! note "High-dimensional SVM (important intuition)"
    Mathematically, SVM is not limited to 2D or 3D.  
    The same idea extends to **N dimensions**, where each feature adds another dimension to the space.

    In real-world machine learning problems, models often work with **tens, hundreds, or even thousands of features**, forming a high-dimensional space that cannot be visualized physically.

    Unlike physical space (which is limited to 3 dimensions), mathematical feature spaces can scale to **N-dimensional space**, and SVM simply finds a separating hyperplane in that space.
    


``` python
from sklearn import svm

# [income, credit_score, debt_ratio]
X = [
    [2, 450, 0.8],
    [3, 500, 0.7],
    [4, 550, 0.6],
    [8, 700, 0.3],
    [10, 750, 0.2],
    [12, 800, 0.1]
]

# 0 = reject, 1 = approve
y = [0, 0, 0, 1, 1, 1]

model = svm.SVC(kernel='linear')
model.fit(X, y)

test_point = [[6, 600, 0.4]]
prediction = model.predict(test_point)[0]

print("Approved" if prediction == 1 else "Rejected")
```

**expected output**
``` text
Approved
```




