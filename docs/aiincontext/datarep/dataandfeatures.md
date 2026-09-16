---
hide:
  - navigation
  
tags:
  - Features
  - Feature Vector
  - Feature Matrix
 
---

# <font color='tomato'>Data and Features in AI</font>
*How raw data is converted into features that ML algorithms can use.*


---
## <font color='green'>1. From Data to Features</font>

### What is Data?

Data is the information collected from the real world.

Depending on the problem, data can take many forms:

- **Numerical data**: temperature, speed, price, age
- **Tabular data**: customer records, transactions, sensor readings
- **Text**: emails, documents, messages
- **Images**: photographs, X-rays, camera frames
- **Audio**: speech, music, machine sounds
- **Signals**: ECG, EEG, vibration, accelerometer readings
- **Video**: surveillance footage, driving scenes

In many real-world AI systems, the raw data comes directly from **sensors or other measurement devices**.


---

### Data to Feature Conversion

Consider a health-monitoring system.

A wearable device may continuously collect raw signals such as:

- ECG signal
- Blood-pressure measurements
- Accelerometer data
- Temperature
- Oxygen saturation

The raw ECG signal, for example, is a sequence of electrical measurements recorded over time.

A small portion might look conceptually like:

```text
0.12, 0.18, 0.31, 0.76, 1.42, 0.82, 0.35, 0.19, ...
```

These raw measurements contain useful information, but an application may need more meaningful quantities.

We can process the raw signal and extract features such as:

```text
Heart rate       = 72 BPM
Blood pressure   = 120 / 80 mmHg
SpO₂             = 98%
Body temperature = 36.7 °C
Activity level   = Moderate
```

These are **features** extracted from the underlying data.

The overall process can be viewed as:

```text
Raw sensor data
       |
       v
Signal processing / feature extraction
       |
       v
Heart rate
Blood pressure
SpO₂
Temperature
Activity level
       |
       v
Machine-learning model
       |
       v
Prediction / classification / decision
```

The important point is that the **raw data and the features are not the same thing**.

The raw ECG signal contains a large sequence of measurements.

Heart rate is a higher-level quantity calculated from that signal.

---

### What is a Feature?

A **feature** is a measurable property derived from, or selected from, the original data that provides useful information for a particular machine-learning task.

For example, from a raw ECG signal, we might calculate:

- Heart rate
- Average signal amplitude
- Signal variability
- Time between heartbeats
- Number of abnormal peaks

These values can then be represented as a feature vector:

```python
[72, 0.43, 0.12, 0.83, 2]
```

Each value represents a different characteristic extracted from the original signal.

A machine-learning model can use these features to perform a task such as detecting an abnormal cardiac pattern.


---
### Why Features?

Features give a machine-learning model a more structured description of the information contained in raw data.

Instead of asking a traditional ML model to work directly with a long raw sensor signal, we can provide measurements that summarize characteristics relevant to the problem.

For example:

```text
Raw ECG signal
       |
       v
Extract useful characteristics
       |
       v
Heart rate
Heart-rate variability
Beat intervals
Signal characteristics
       |
       v
Feature vector
       |
       v
ML model
       |
       v
Prediction
```

Traditionally, deciding which characteristics to extract was largely the responsibility of the engineer.

This leads to an important question:

> **How do we decide which features to create, and how do we transform raw data into useful features?**

That is the subject of **Feature Engineering**.


---
## <font color='green'>2. Features Depend on the Task</font>

The useful features depend on what we are trying to accomplish.

For example, the same health-monitoring data could be used for different tasks.

For **activity recognition**, useful features might include:

- Average acceleration
- Maximum acceleration
- Movement frequency
- Duration of movement

For **cardiac monitoring**, useful features might include:

- Heart rate
- Heart-rate variability
- Beat-to-beat interval
- ECG waveform characteristics

For **health-risk prediction**, the model might use a combination of features:

- Heart rate
- Blood pressure
- Temperature
- Activity level
- Age

So there is no single universal set of features for a particular piece of raw data.

The useful features depend on the **task**.

### Example 2: Audio Data

Consider a recording of a person's voice.

The raw audio signal is the same, but the useful features can be different depending on the task.

For **speaker identification**, useful features might include:

- Pitch
- Spectral characteristics
- MFCCs
- Voice frequency patterns
- Energy distribution

For **speech emotion recognition**, useful features might include:

- Pitch variation
- Speech energy
- Speaking rate
- Voice intensity
- Spectral characteristics

The same raw audio can therefore be converted into different feature sets depending on what we want the ML model to accomplish.

```text
Raw audio
    |
    +----> Features for speaker identification
    |          - Pitch
    |          - Spectral characteristics
    |          - MFCCs
    |          - Voice frequency patterns
    |
    +----> Features for emotion recognition
               - Pitch variation
               - Speech energy
               - Speaking rate
               - Voice intensity
```

The key idea is:

> **Features are not determined only by the data. They are also determined by the task we want to solve.**



---
## <font color='green'>3. Feature Vector</font>

### What is a Feature Vector?

A **feature vector** is a collection of feature values used to represent one data sample.

We have already seen that we can extract useful features from raw data.

For example, from a health-monitoring system, we might extract:

- Heart rate
- Blood pressure
- SpO₂
- Body temperature
- Activity level

For one person, these features could be represented as:

```python
[72, 120, 80, 98, 36.7, 0.65]
```

Each value represents one feature.

The collection of these values is the **feature vector** for that particular data sample.

---

### Representing One Data Sample

Suppose our features are:

| Feature | Value |
|---|---:|
| Heart rate | 72 |
| Systolic BP | 120 |
| Diastolic BP | 80 |
| SpO₂ | 98 |
| Temperature | 36.7 |
| Activity level | 0.65 |

The feature vector can be written as:

```python
[72, 120, 80, 98, 36.7, 0.65]
```

The position of each value has meaning.

For example:

```text
Position 1  = Heart rate
Position 2  = Systolic BP
Position 3  = Diastolic BP
Position 4  = SpO₂
Position 5  = Temperature
Position 6  = Activity level
```

So the model knows that the first value represents heart rate, the second represents systolic blood pressure, and so on.

---

### Why Use a Vector?

Machine-learning algorithms operate on numerical representations.

A feature vector gives the model a consistent numerical representation of one sample.

For example:

```text
Patient A
[72, 120, 80, 98, 36.7, 0.65]

Patient B
[85, 135, 90, 95, 37.1, 0.82]

Patient C
[65, 110, 70, 99, 36.5, 0.40]
```

Each patient is represented by the same set of features and in the same order.

This allows an ML algorithm to process and compare the samples.

---

### Another Example: Audio

Suppose we are analysing a short audio recording.

For a particular task, we might extract:

- Average pitch
- Speech energy
- Speaking rate
- Spectral characteristics

One audio sample could then be represented as:

```python
[185.4, 0.72, 4.8, 0.35]
```

Again, this is a feature vector. 

The values describe selected characteristics of the original audio signal.

---

### Feature Vector Is a Representation

The original data can be complex:

```text
ECG signal
Audio recording
Image
Customer record
```

After extracting useful features, one sample can be represented by a vector:

```text
Feature 1
Feature 2
Feature 3
Feature 4
...
Feature N
```

Mathematically, a feature vector can be written as:

$$
\mathbf{x} = [x_1, x_2, x_3, \ldots, x_n]
$$

where each $x_i$ represents one feature.

For example:

$$
\mathbf{x} = [72, 120, 80, 98, 36.7, 0.65]
$$

Here, the vector contains six feature values.

The important idea is:

> **A feature vector is a numerical representation of one data sample using a defined set of features.**

The next step is to see what happens when we have **many data samples**, each represented by its own feature vector. This leads to the idea of a **feature matrix**.


---
## <font color='green'>4. Feature Matrix</font>

A feature vector represents **one data sample**. In a real machine-learning problem, we usually have **many samples.**

For example, suppose we collect health data from several people. Each person can be represented by a feature vector:

```python
Patient A = [72, 120, 80, 98, 36.7, 0.65]
Patient B = [85, 135, 90, 95, 37.1, 0.82]
Patient C = [65, 110, 70, 99, 36.5, 0.40]
```

We can put all these feature vectors together to form a **feature matrix**.

---

### What is a Feature Matrix?

A **feature matrix** is a collection of feature vectors representing multiple data samples.

For example:

```text
                 Heart Rate   Sys BP   Dia BP   SpO₂   Temp   Activity
Patient A            72        120       80      98    36.7     0.65
Patient B            85        135       90      95    37.1     0.82
Patient C            65        110       70      99    36.5     0.40
```

Each **row** represents one data sample.

Each **column** represents one feature.

So:

```text
Rows    = data samples
Columns = features
```

---

### Feature Matrix in Machine Learning

A feature matrix is commonly represented as `X` in machine-learning code.

For the example above:

```python
X = [
    [72, 120, 80, 98, 36.7, 0.65],
    [85, 135, 90, 95, 37.1, 0.82],
    [65, 110, 70, 99, 36.5, 0.40]
]
```

If there are:

- 3 patients
- 6 features per patient

then the feature matrix has a shape of:

```text
3 × 6
```

or in Python:

```python
X.shape
# (3, 6)
```

---

### Feature Matrix and Target Values

In supervised learning, we usually have two main pieces of data:

- `X` contains the **features**
- `y` contains the **target values**

For example, suppose the task is to classify whether a patient's condition is normal or abnormal.

```python
X = [
    [72, 120, 80, 98, 36.7, 0.65],
    [85, 135, 90, 95, 37.1, 0.82],
    [65, 110, 70, 99, 36.5, 0.40]
]

y = [
    "normal",
    "abnormal",
    "normal"
]
```

The model learns a relationship between the features in `X` and the target values in `y`.

Conceptually:

```text
Feature Matrix X
        |
        v
   ML Model
        |
        v
Target y
```

---

### The Important Distinction

A useful way to remember the terminology is:

```text
One sample
    |
    v
Feature Vector

Many samples
    |
    v
Feature Matrix
```

For example:

```python
# One sample
x = [72, 120, 80, 98, 36.7, 0.65]

# Many samples
X = [
    [72, 120, 80, 98, 36.7, 0.65],
    [85, 135, 90, 95, 37.1, 0.82],
    [65, 110, 70, 99, 36.5, 0.40]
]
```

This distinction is important because most ML libraries expect training data in the form of a **feature matrix**.

The next section will put this into practice using Python and a simple machine-learning model.



---
## <font color='green'>5. Python Example</font>

Now let's put the ideas of **features, feature vectors, and feature matrices** into practice.

We will use a small health-monitoring example.

Suppose we want to classify whether a person's health measurements indicate a **normal** or **abnormal** condition.

### Create the Feature Matrix

We will use four features:

- Heart rate
- Systolic blood pressure
- SpO₂
- Body temperature

```python
X = [
    [72, 120, 98, 36.7],
    [68, 115, 99, 36.5],
    [85, 140, 95, 37.2],
    [92, 150, 93, 37.5],
    [70, 118, 98, 36.6],
    [88, 145, 94, 37.3]
]
```

Each row represents one person.

Each column represents one feature.

The corresponding target values are:

```python
y = [
    "normal",
    "normal",
    "abnormal",
    "abnormal",
    "normal",
    "abnormal"
]
```

---

### Train a Simple Model

We can use a Decision Tree classifier:

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(max_depth=3)

model.fit(X, y)
```

The model looks at the feature values in `X` and the corresponding labels in `y`.

It learns patterns that can be used to classify new samples.

---

### Predict a New Sample

Suppose we receive measurements from a new person:

```python
new_patient = [[80, 130, 97, 36.9]]
```

We can ask the model for a prediction:

```python
prediction = model.predict(new_patient)

print(prediction)
```

The model returns a predicted class based on the patterns it learned from the training data.

---

### What Happened?

The complete process was:

```text
Health measurements
        |
        v
Features
        |
        v
Feature vectors
        |
        v
Feature matrix X
        |
        v
Decision Tree
        |
        v
Prediction
```

This is the basic pattern used by many traditional machine-learning models.

The important part is that we manually decided which measurements would become features.

In this example, we chose:

```text
Heart rate
Systolic blood pressure
SpO₂
Body temperature
```

The next question is:

> **How do we decide which features to use, how do we transform them, and how can we create better features from existing data?**


---
## <font color='green'>6. Summary and Takeaways</font>

The key ideas from this article are:

- **Data** is the information collected from the real world.
- A **feature** is a measurable property extracted from or selected from the data.
- Features are created because ML models need information in a structured form that they can process.
- The useful features depend on the **task** we want to solve.
- One data sample can be represented as a **feature vector**.
- Multiple feature vectors can be combined into a **feature matrix**.
- In many ML libraries, the feature matrix is represented as `X`.
- In traditional ML, features are often designed or selected by humans.
- Features provide a bridge between **raw data** and an **ML model**.

The overall picture is:

```text
Raw Data
    |
    v
Features
    |
    v
Feature Vector
    |
    v
Feature Matrix
    |
    v
ML Model
    |
    v
Prediction / Decision
```

The next article, **[Feature Engineering](featureeng.md)**, will look at what happens when the features we have are not yet suitable for the task.

We will look at how to:

- Create new features
- Transform existing features
- Select useful features
- Scale numerical features
- Encode categorical features
- Deal with irrelevant or redundant features



---
## Relevant Link(s)

[Feature Engineering](featureeng.md)

[AI in Context Main Page](../../index.md)

