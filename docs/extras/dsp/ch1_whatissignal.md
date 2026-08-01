---
hide:
  - navigation
  
search:
  exclude: true
  
---

# <font color='green'>Chapter 1: What is Signal</font>

**Goal:** Students understand what a signal is, why signals exist everywhere, and why engineers process them.

---
## <font color='green'>1.1 What is a Signal?</font>

A **signal** is simply **any quantity that changes and carries useful information**.

It could be a physical quantity such as temperature or pressure, an electrical quantity such as voltage, or even a financial quantity such as a stock price.

The important idea is:

> **If something changes and those changes tell us something useful, it can be treated as a signal.**

### Examples of Signals

| Domain | Examples of Signals |
|--------|----------------------|
| **Physics** | Temperature, pressure, force, displacement, velocity, acceleration |
| **Electrical** | Voltage, current, power |
| **Mechanical** | Vibration, strain, torque, rotational speed |
| **Acoustics** | Sound pressure, speech, music |
| **Optics** | Light intensity, color, laser power |
| **Biomedical** | ECG, EEG, EMG, blood pressure, heart rate, oxygen saturation |
| **Communications** | Radio waves, Wi-Fi, Bluetooth, 5G, GPS signals |
| **Industrial** | Flow rate, liquid level, motor current, machine vibration |
| **Environmental** | Humidity, rainfall, wind speed, air quality, CO₂ concentration |
| **Financial** | Stock price, exchange rate, trading volume |

### Signal Processing Across Many Fields

As we have seen, a **signal** can represent almost any measurable quantity. Therefore, **signal processing (SP)** is used in many different fields, each with its own specialized techniques and tools.

Although signal processing originated in **electrical and communication engineering**, its principles are now widely applied in areas such as mechanical engineering, biomedical engineering, finance, robotics, geophysics, and many others.

### Scope of This Course

This course focuses on the **fundamental principles of signal processing**, independent of any specific application domain.

Although we'll use examples from audio, biomedical, communications, and other fields, our goal is to learn the core techniques that are common to all of them. Each application area has its own advanced methods, algorithms, and specialized tools, which are beyond the scope of this course.

### Key Takeaway

The actual quantity doesn't matter.

What matters is that it **varies over time (or space)** and those variations carry useful information.

A good rule of thumb is:

> **If you can measure it, record it, and plot it, you can usually treat it as a signal.**


---
## <font color='green'>1.2 Representing a Signal</font>

A signal is useful only if we can **observe** and **represent** it.

The most common way to represent a signal is by plotting **its value against time**.

For example:

- Temperature changes throughout the day.
- Blood pressure changes with each heartbeat.
- Voltage changes in an electrical circuit.
- Sound pressure changes as we speak.

All of these can be represented as a graph.

```
Signal Value
    ^
    |
    |        /\
    |       /  \__
    |______/_______\______> Time
```

In this course, we will mainly work with **time-varying signals**, where the signal value changes with time.

Although signals can also vary with other quantities such as position or space (e.g., an image varies over two spatial dimensions), the underlying concepts remain the same.

### Key Takeaway

> A signal is usually represented as **its value versus an independent variable**, most commonly **time**.


---
## <font color='green'>1.3 Analog and Discrete Signals</font>

Most signals in the real world are **analog**, meaning they change **continuously**.

For example, consider the temperature of a room. Between **1 second** and **2 seconds**, the temperature has a value at every instant—not just every second, but every millisecond, microsecond, or even smaller intervals.

In other words, an analog signal has a value **at every point in time**.

### Discrete Signals

In practice, we often record a signal only at specific instants.

For example, we may measure the temperature:

- Every 1 second
- Every 100 milliseconds
- Every 1 millisecond

Instead of having a value at every instant, we now have a **sequence of measurements** taken at discrete points in time.

```
Analog Signal

Time ───────────────────────────────▶
      ●────────●────────●────────●
     (value exists everywhere)


Discrete Signal

Time ───────────────────────────────▶
      ●         ●         ●         ●
    Sample    Sample    Sample    Sample
```

### Important Note

<font color='red'>A **discrete** signal is **not necessarily digital**.</font>

A discrete signal simply means the signal is available **only at specific points in time**. The sample values can still be continuous (for example, 23.4567°C, 23.4571°C, ...).

> A **discrete** signal becomes **digital** only after these sample values are represented using a finite number of bits inside a computer. We will discuss this in the next section.

### Key Takeaway

- **Analog signals** have a value at every instant of time.
- **Discrete signals** have values only at specific instants.
- **Discrete does not mean digital.**
- A discrete signal becomes **digital** only after it is represented using finite-precision numbers.

---
## <font color='green'>1.4 Discrete vs Digital Signals</font>

In the previous section, we learned that a **discrete** signal has values only at specific points in time.

However, the value of each sample can still be **any real number**.

For example, a temperature sensor may produce the following discrete samples:

```
23.4512
23.4876
23.5091
23.4728
...
```

These values are **discrete in time**, but **continuous in amplitude**.

### Digital Signals

A digital signal is both:

- **Discrete in time**, and
- **Discrete in amplitude**

Instead of allowing any value, each sample is rounded to one of a finite number of levels.

For example,

```
Discrete Signal

23.4512
23.4876
23.5091
23.4728


Digital Signal

23.45
23.49
23.51
23.47
```

or inside a computer,

```
01011110
01011111
01100000
...
```

The exact representation depends on the number of bits used.

The process of converting a discrete signal into a digital signal is called **quantization**, which will be discussed in detail later.

### Key Takeaway

- A **discrete signal** is sampled in time.
- A **digital signal** is sampled in time **and** represented using a finite number of levels (bits).
- Every digital signal is discrete, but **not every discrete signal is digital**.

---
## <font color='green'>1.5 From Analog to Digital (Oveview) </font>

So far, we have learned that:

- The real world consists mostly of **analog signals**.
- These signals are first converted into **discrete signals** by **sampling**.
- The discrete samples are then converted into **digital signals** by **quantization**.

The complete process is illustrated below.

```text
Analog Signal
      │
      ▼
 Sampling
      │
      ▼
Discrete Signal
      │
      ▼
 Quantization
      │
      ▼
Digital Signal
```

This process is known as **Analog-to-Digital Conversion (ADC)**.


---
## 1.6 Chapter Summary

In this chapter, we introduced the fundamental concepts of **signals** and their role in digital signal processing.

The key points are:

- A **signal** is any quantity that changes and carries useful information.
- Signals exist in many domains, including physics, engineering, medicine, communications, and finance.
- Signal processing provides a common set of techniques for analyzing and manipulating signals, regardless of their application.
- Most real-world signals are **analog**, meaning they vary continuously with time.
- A **discrete** signal is obtained by observing an analog signal at specific points in time.
- A **discrete** signal is **not necessarily digital**.
- A **digital** signal is both discrete in time and represented using a finite number of levels.
- Converting an analog signal into a digital signal involves two fundamental operations:
  - **Sampling** (continuous → discrete)
  - **Quantization** (discrete → digital)

In the next chapter, we will study **Analog-to-Digital Conversion (ADC)** in detail, beginning with sampling, the Nyquist Sampling Theorem, aliasing, and quantization.
In this chapter, we introduced the overall idea. In the next chapter, we will study **sampling** and **quantization** in detail.


---
## **Relevant Links**

[Back to DSP Undergrade Level](index.md)

[Back to DSP Courses (All)](../index.md)
