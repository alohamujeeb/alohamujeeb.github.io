---
hide:
  - navigation
  
search:
  exclude: true
  
---
# <font color='green'>Chapter 4: Signal vs Data</font>

**Goal:**

Students understand the distinction between a physical **signal** and its digital **data representation**, and why DSP operates on data rather than directly on real-world signals.

---

## <font color='green'>4.1 Signal vs Data</font>

A **signal** is a physical quantity that carries information.

**Data** is the digital representation of that information inside a computer.

In simple terms,

> **Signals belong to the physical world. Data belongs to the digital world.**

```
Physical World
      │
   Signal
      │
ADC / Measurement
      │
      ▼
     Data
```

### Examples

| Signal | Data |
|---------|------|
| Pressing a keyboard key | ASCII / Unicode code |
| Sound pressure | Audio samples (WAV, MP3) |
| Room temperature | 25.4 °C stored as a number |
| ECG waveform | Digital ECG samples |
| Light intensity | Pixel values in an image |
| Radio wave | Digital bits in a receiver |

### Key Takeaway

A **signal** carries information in the physical world, while **data** is the digital representation of that signal that a computer can store and process.

---

## <font color='green'>4.2 Why the Difference Matters</font>

Signal Processing begins with **signals**, but Digital Signal Processing (DSP) works with **data**.

The goal of DSP is to analyze, improve, compress, or extract information from the data so that we can better understand the original signal.

For example:

- A microphone measures a **sound signal**.
- The ADC converts it into **digital audio samples**.
- DSP processes those samples.
- A DAC converts them back into a **sound signal**.

### Key Takeaway

> **DSP never processes the physical signal directly—it processes the digital data that represents the signal.**

---

## <font color='green'>4.3 Chapter Summary</font>

In this chapter, we distinguished between **signals** and **data**, two terms that are often used interchangeably but represent different concepts.

The key points are:

- A **signal** is a physical quantity that carries information.
- **Data** is the digital representation of that information.
- Signals belong to the **physical world**, while data belongs to the **digital world**.
- DSP does **not** process physical signals directly—it processes the **data** representing those signals.

Some examples are shown below:

| Physical Signal | Digital Data |
|-----------------|--------------|
| Pressing a keyboard key | ASCII / Unicode character |
| Human speech | Audio samples (WAV, MP3) |
| Room temperature | Numerical temperature value |
| ECG waveform | ECG samples stored in memory |
| Light falling on a camera sensor | Pixel values in an image |
| Radio waves | Digital bit stream |
| Machine vibration | Time-series sensor data |
| GPS satellite signals | Latitude and longitude values |

Although DSP algorithms operate on **data**, their ultimate goal is to analyze, understand, or modify the underlying **physical signals**.



---
## **Relevant Links**

[Back to DSP Undergrade Level](index.md)

[Back to DSP Courses (All)](../index.md)


