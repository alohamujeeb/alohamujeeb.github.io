---
hide:
  - navigation
  
tags:
  - Feature Engineerng
  - Handcrafted Features
  - Learnt Features
  - Learned Features
 
---

# <font color='tomato'>Feature Engineering in AI</font>
*How Raw Data Is Transformed into Useful Features for Machine Learning.*

This article is a sequel to [Data and Features in AI](dataandfeatures.md).

---

## <font color='green'>1. Types of Features</font>

Features can have different types depending on the kind of information they represent.

Understanding feature types is important because different types of features may need to be represented and processed differently before they are used by a machine-learning model.

### Numerical Features

**Numerical features** represent quantities that can be expressed using numbers.

Examples:

- Age
- Temperature
- Heart rate
- Blood pressure
- Speed
- Price

For example, a health-monitoring system might represent a person's measurements as:

```python
[42, 72, 120, 80, 98]
```

Here, age, heart rate, systolic blood pressure, diastolic blood pressure, and SpO₂ are numerical features.

### Categorical Features

**Categorical features** represent values that belong to a set of categories.

Examples:

- Blood type: A, B, AB, O
- Device type: watch, phone, chest strap
- Activity: walking, running, sitting
- Country: Singapore, Japan, India

For example:

```python
activity = "walking"
```

The value represents a category rather than a numerical quantity.

Categorical values usually need to be converted into a numerical representation before being given to many machine-learning algorithms.

### Binary Features

A **binary feature** has only two possible values.

Examples:

- Smoker: yes / no
- Disease detected: true / false
- Device connected: 1 / 0
- Alarm triggered: yes / no

A binary feature can often be represented directly using `0` and `1`:

```python
alarm_triggered = 1
```

Here, `1` means the alarm was triggered and `0` could represent that it was not triggered.

### Ordinal Features

An **ordinal feature** contains categories that have a meaningful order.

For example, an activity intensity feature might be:

```text
Low < Moderate < High
```

Similarly, a rating might be:

```text
Poor < Fair < Good < Excellent
```

The categories have an order, but the numerical difference between consecutive categories does not necessarily have a meaningful interpretation.

For example:

```text
Low      = 1
Moderate = 2
High     = 3
```

The values indicate order, but `High` is not necessarily three times `Low`.

### Continuous vs. Discrete Features

Numerical features can also be described as **continuous** or **discrete**.

A **continuous feature** can take any value within a range.

Examples:

- Temperature: `36.7 °C`
- Weight: `68.4 kg`
- Blood pressure: `120.5 mmHg`
- Voltage: `3.72 V`

A **discrete feature** takes separate, countable values.

Examples:

- Number of previous hospital visits: `0`, `1`, `2`, `3`, ...
- Number of detected abnormal beats: `0`, `1`, `2`, ...
- Number of devices connected: `1`, `2`, `3`, ...

The distinction is based on the nature of the values, not simply whether the feature is stored as an integer or floating-point number.


### Why Classify Features?

Classifying features is useful because **different types of features require different ways of representing and processing them**.

For example:

- **Numerical features** may need scaling when their ranges are very different.
- **Categorical features** often need to be encoded into numerical values.
- **Binary features** can often be represented directly as `0` and `1`.
- **Ordinal features** need a representation that preserves their natural order.
- **Continuous and discrete features** may require different statistical or modeling considerations.

Consider a health-monitoring dataset:

```text
Age              = 42
Activity         = "walking"
Smoker           = "no"
Activity level   = "High"
Temperature      = 36.7
Abnormal beats   = 3
```

These values do not all represent information in the same way.

```text
Age              -> Numerical
Activity         -> Categorical
Smoker           -> Binary
Activity level   -> Ordinal
Temperature      -> Continuous
Abnormal beats   -> Discrete
```

Knowing the feature type helps us decide **how the feature should be represented and what preprocessing may be appropriate before using it in a machine-learning model**.

This becomes particularly important during **feature engineering**, where we modify raw data into a form that a model can use effectively.


### Summary 

The main feature types discussed here are:

| Feature Type | Example |
|---|---|
| Numerical | Heart rate = `72` |
| Categorical | Activity = `walking` |
| Binary | Alarm = `1` |
| Ordinal | Intensity = `High` |
| Continuous | Temperature = `36.7` |
| Discrete | Abnormal beats = `3` |

A single dataset can contain several of these feature types at the same time.

The next step is to understand how we **create, transform, scale, encode, and select features** for a machine-learning model.

---
## <font color='green'>2. Feature Engineering</font>

Feature engineering is the process of **creating, transforming, scaling, encoding, and selecting features** so that the data is in a useful form for a machine-learning model.

The goal is not simply to create more features. The goal is to create features that provide useful information for the particular task.

The main activities in feature engineering are:

- Creating new features
- Transforming existing features
- Scaling numerical features
- Encoding categorical features
- Selecting useful features

### Creating New Features

Sometimes the original data does not directly contain the information needed by the model.

We can create a new feature by combining or processing existing data.

For example, suppose a health-monitoring system records:

```text
Resting heart rate = 72 BPM
Maximum heart rate = 160 BPM
```

We could create a new feature:

```text
Heart-rate range = Maximum heart rate - Resting heart rate
                 = 160 - 72
                 = 88 BPM
```

The new feature contains information derived from existing features.

Other examples include:

```text
BMI = weight / height²

Age group = derived from age

Daily activity ratio = active time / total monitoring time

Average speed = distance / time
```

The important idea is that **a feature does not have to exist directly in the original dataset**. It can be derived from existing data.

### Transforming Features

Feature transformation changes the representation of an existing feature.

For example, a model may perform better when a highly skewed feature such as income is transformed using a logarithm:

```python
import numpy as np

income = 100000
log_income = np.log(income)
```

Other transformations can include:

- Logarithmic transformation
- Square-root transformation
- Binning
- Mathematical combinations of features

The purpose of a transformation depends on the data and the machine-learning algorithm being used.

### Scaling Features

Numerical features can have very different ranges.

For example:

```text
Age          = 42
Income       = 85000
Heart rate   = 72
Temperature  = 36.7
```

If an algorithm uses distances or magnitudes, features with larger numerical ranges can have a disproportionate influence.

Scaling transforms numerical features to a more comparable range.

For example, **standardization** transforms a feature using:

```text
z = (x - mean) / standard deviation
```

Python provides tools for this:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

Scaling is not required for every machine-learning algorithm. Its importance depends on the algorithm and how it uses the feature values.

### Encoding Categorical Features

Machine-learning models generally work with numerical representations, while many real-world datasets contain categorical values.

For example:

```text
Activity
--------
walking
running
sitting
```

These categories cannot always be passed directly to a numerical model.

One common approach is **one-hot encoding**:

```text
Activity    Walking    Running    Sitting
walking       1           0          0
running       0           1          0
sitting       0           0          1
```

In Python:

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()

activity = [
    ["walking"],
    ["running"],
    ["sitting"]
]

encoded = encoder.fit_transform(activity)
```

The appropriate encoding depends on the type of categorical feature and the model being used.

### Selecting Useful Features

A dataset may contain many features, but not all of them are useful for a particular task.

Some features may:

- Contain little useful information
- Be redundant with other features
- Add noise
- Increase computational cost
- Make the model unnecessarily complex

Feature selection attempts to keep useful features and remove unnecessary ones.

For example, if a model for detecting abnormal cardiac activity uses:

```text
Heart rate
Heart-rate variability
Beat interval
Body temperature
Random device identifier
```

The device identifier may have no meaningful relationship to the physiological condition being predicted.

Removing irrelevant features can produce a simpler and more useful representation of the data.

### Putting It Together

Feature engineering can therefore be viewed as a sequence of operations:

```text
Raw data
   |
   v
Create useful features
   |
   v
Transform features
   |
   v
Scale numerical features
   |
   v
Encode categorical features
   |
   v
Select useful features
   |
   v
Machine-learning model
```

Not every dataset requires every operation.

The appropriate feature-engineering steps depend on the **data, the machine-learning task, and the model being used**.

---
## <font color='green'>3. Hand-Crafted Features</font>

Before modern machine-learning models could learn useful representations directly from raw data, engineers often had to **design features manually**.

These are called **hand-crafted features**.

The engineer examines the data, identifies characteristics that may be relevant to the task, and creates features that represent those characteristics.

### Why Humans Design Features

Raw data can contain a large amount of information, but much of it may not be directly useful for a particular machine-learning task.

For example, consider an ECG signal:

```text
Raw ECG signal
      |
      v
Human identifies useful characteristics
      |
      v
Heart rate
Beat-to-beat interval
Signal amplitude
Peak frequency
      |
      v
Feature vector
      |
      v
ML model
```

The engineer decides which characteristics to extract based on knowledge of:

- The data
- The problem being solved
- The domain
- The behavior of the system

This can make the learning problem easier because the model receives information that has already been processed into meaningful characteristics.

### Practical Examples

#### Example 1: Image Classification

Suppose we want to classify images of vehicles.

A traditional computer-vision system might manually extract features such as:

- Edge information
- Shape
- Texture
- Color distribution
- Object contours

These features are then provided to a machine-learning algorithm.

```text
Image
  |
  v
Edge / shape / texture extraction
  |
  v
Feature vector
  |
  v
ML classifier
  |
  v
Prediction
```

#### Example 2: Audio Classification

For an audio signal, an engineer might extract:

- Pitch
- Energy
- Spectral characteristics
- Frequency distribution
- MFCCs

Different combinations of these features can be useful for tasks such as speech recognition, speaker identification, or emotion recognition.

#### Example 3: Health Monitoring

For a health-monitoring system, features might include:

- Average heart rate
- Heart-rate variability
- Beat-to-beat intervals
- Average activity level
- Maximum activity level
- Sleep duration

These features can be calculated from raw sensor measurements and then used by a machine-learning model.

### Strengths of Hand-Crafted Features

Hand-crafted features can be useful because they can:

- Incorporate domain knowledge
- Reduce the amount of raw data presented to the model
- Make the input representation more interpretable
- Work well when the relevant characteristics are well understood

For example, an engineer working with ECG data may know that heartbeat intervals are relevant to a particular task. That knowledge can be explicitly incorporated into the feature representation.

### Limitations of Hand-Crafted Features

However, manually designing features also has limitations.

**1. Requires domain knowledge**

The engineer needs to understand which characteristics may be relevant to the problem.

**2. Time-consuming**

Designing and testing useful features can require substantial experimentation.

**3. May miss useful patterns**

An engineer can only design features based on patterns they know or can identify. Important patterns may exist in the raw data that are difficult to describe manually.

**4. Features may not generalize across tasks**

A feature that is useful for one task may not be useful for another.

For example:

```text
Same raw audio
      |
      +--> Speaker identification
      |       -> speaker characteristics
      |
      +--> Emotion recognition
      |       -> pitch variation, energy, speaking rate
      |
      +--> Speech recognition
              -> speech-related patterns
```

The useful representation depends on the task.

These limitations lead to an important question:

> **Can a machine-learning model learn useful features directly from the data instead of requiring humans to design them?**

This leads to **learned representations** and, more broadly, **representation learning**.

---
## <font color='green'>4. From Features to Learned Representations</font>

Hand-crafted features require humans to decide which characteristics of the data are useful.

This works well when the important patterns are already understood. However, many real-world datasets contain complex patterns that are difficult to describe manually.

### Limitations of Manually Designed Features

Consider an image classification problem.

A traditional system might use manually designed features such as:

```text
Image
  |
  v
Edges
Shapes
Textures
Color patterns
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

The engineer must decide which visual characteristics to extract.

But an image contains much more information than these manually selected features.

For example, recognizing a particular object may depend on combinations of:

- Edges
- Shapes
- Textures
- Parts of objects
- Spatial relationships
- Higher-level structures

Designing all of these features manually becomes difficult as the problem becomes more complex.

### Why Models Can Learn Features

Instead of manually specifying every useful feature, a model can **learn representations from the data**.

The basic idea is:

```text
Raw data
   |
   v
Learning process
   |
   v
Learned representation
   |
   v
Prediction
```

During training, the model adjusts its internal parameters based on the available data and the learning objective.

As a result, the model can learn representations that capture patterns useful for the task.

For example, in image recognition, a neural network may learn increasingly complex patterns:

```text
Pixels
  |
  v
Edges
  |
  v
Simple shapes
  |
  v
Object parts
  |
  v
Objects
  |
  v
Prediction
```

These representations are not explicitly designed by the engineer. They are **learned from the data**.

### Representation Learning

**Representation learning** is the process of allowing a machine-learning model to learn useful representations of data rather than relying entirely on manually designed features.

This changes the traditional approach:

```text
Traditional ML:

Raw data
   |
   v
Human-designed features
   |
   v
ML model
   |
   v
Prediction
```

to:

```text
Representation learning:

Raw data
   |
   v
Model learns representations
   |
   v
Learned features
   |
   v
Prediction
```

This idea is fundamental to modern AI systems.

Neural networks can learn multiple levels of representation from raw or relatively unprocessed data. This ability becomes especially important when working with complex data such as images, audio, text, and video.

---
## <font color='green'>Summary and Takeaways</font>

- Features can be **numerical, categorical, binary, ordinal, continuous, or discrete**.
- Classifying features helps determine how they should be represented and processed.
- **Feature engineering** involves creating, transforming, scaling, encoding, and selecting features.
- **Hand-crafted features** are designed by humans using knowledge of the data, task, and domain.
- Hand-crafted features can be useful, but they can also be time-consuming and may miss complex patterns.
- **Representation learning** allows models to learn useful representations directly from data.
- Modern AI systems increasingly rely on **learned representations** instead of depending entirely on manually designed features.

The progression can be summarized as:

```text
Raw Data
   |
   v
Hand-Crafted Features
   |
   v
Feature Vector
   |
   v
Machine-Learning Model
```

and, with representation learning:

```text
Raw Data
   |
   v
Learned Representations
   |
   v
Machine-Learning Model
```

The key idea is that **the way data is represented has a major impact on how a machine-learning model can learn from it**.



---
## Relevant Link(s)

[Data and Features in AI](dataandfeatures.md)

[AI in Context Main Page](../../index.md)

