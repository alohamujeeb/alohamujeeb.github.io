---
hide:
  - navigation
  
search:
  exclude: true
  
---

# <font color='green'>Chapter 2: Analog-to-Digital Conversion (ADC)</font>

**Goal:**

Students understand how an analog signal is converted into a digital signal through **sampling** and **quantization**, and the practical limitations introduced by this conversion.

---
## <font color='green'> 2.1 Introduction to ADC </font>

In the previous chapter, we learned that computers can only process **digital signals**, while most real-world signals are **analog**.

The purpose of an **Analog-to-Digital Converter (ADC)** is to convert an analog signal into a digital signal that can be stored, transmitted, and processed by a computer.

This conversion involves two fundamental steps:

1. **Sampling** – Converting a continuous-time signal into a discrete-time signal.
2. **Quantization** – Converting each sample into one of a finite number of digital values.

In this chapter, we will study each of these steps in detail.

---
## <font color='green'>2.2 Why Sampling?</font>

The real world is **continuous**. For example, the temperature of a room exists at every instant of time.

A computer, however, cannot continuously observe a signal. It can only read or store values at specific instants.

Therefore, instead of recording every possible value, we measure the signal at regular time intervals. This process is called **sampling**.

For example, instead of measuring the temperature continuously, we may record it:

- Every 1 second
- Every 100 milliseconds
- Every 10 milliseconds

Each measurement is called a **sample**, and the collection of these samples forms a **discrete-time signal**.

### Key Takeaway

> **Sampling** converts a continuous-time (analog) signal into a **discrete-time** signal by taking measurements at regular time intervals.

---
## <font color='green'>2.3 Sampling Interval and Sampling Rate</font>

When sampling a signal, two quantities are important:

- **Sampling Interval (\(T_s\))** – The time between two consecutive samples.
- **Sampling Rate (\(f_s\))** – The number of samples taken per second.

These two quantities are related by:

\[
f_s=\frac{1}{T_s}
\]

### Example

| Sampling Interval (\(T_s\)) | Sampling Rate (\(f_s\)) |
|------------------------------|-------------------------|
| 1 second | 1 sample/second (1 Hz) |
| 100 ms | 10 samples/second (10 Hz) |
| 10 ms | 100 samples/second (100 Hz) |
| 1 ms | 1000 samples/second (1 kHz) |

Notice that:

- A **smaller sampling interval** means samples are taken more frequently.
- A **higher sampling rate** captures more information about the signal.

The choice of sampling rate is important. If the sampling rate is too low, important information may be lost. We will study this in the next section.

### Key Takeaway

- **Sampling Interval (\(T_s\))** is the time between successive samples.
- **Sampling Rate (\(f_s\))** is the number of samples taken per second.
- A higher sampling rate provides a more accurate representation of the original signal.

---
## <font color='green'>2.4 How Fast Should We Sample?</font>

A natural question arises:

> **How many samples per second are enough to accurately represent an analog signal?**

Intuitively, taking more samples captures more information about the signal. However, taking too many samples increases storage, transmission bandwidth, and computational cost.

On the other hand, taking too few samples may cause important information to be lost.

Is there a minimum sampling rate that still allows us to reconstruct the original signal?

The answer is **yes**.

This is given by the **Nyquist Sampling Theorem**.

### Nyquist Sampling Theorem

If the highest frequency present in a signal is **\(f_{max}\)**, then the sampling rate must satisfy

\[
f_s \ge 2f_{max}
\]

The quantity

\[
2f_{max}
\]

is called the **Nyquist Rate**.

### Example

Suppose a signal contains frequencies up to **5 kHz**.

Then the minimum sampling rate is

\[
f_s \ge 10\ \text{kHz}
\]

In practice, engineers usually sample at a rate slightly higher than the Nyquist rate to provide a safety margin.

### Key Takeaway

To avoid losing information, the sampling rate should be **at least twice the highest frequency present in the signal**.

> <font color='red'><b>Note:</b> At this stage, we are not concerned with the mathematical proof or derivation of the Nyquist Sampling Theorem. Our goal is simply to understand **when** and **why** it is used in practice. The mathematical derivation will be discussed later when we study the frequency domain and the Fourier Transform.</font>

---
## <font color='green'>2.5 Aliasing</font>

What happens if we sample a signal **below the Nyquist rate**?

The answer is **aliasing**.

Aliasing occurs when the sampling rate is too low to capture all the frequency components present in the original signal.

As a result, **high-frequency components appear as lower frequencies** in the sampled signal. Once this happens, the original signal **cannot be recovered**, even if we later increase the sampling rate.

### A Simple Example

Suppose a signal contains a frequency of **8 kHz**.

If we sample it at **10 kHz**, the Nyquist rate is violated because:

\[
10\ \text{kHz} < 2 \times 8\ \text{kHz} = 16\ \text{kHz}
\]

The sampled signal will no longer represent the original 8 kHz signal correctly. Instead, it will appear as a different (lower) frequency.

This phenomenon is called **aliasing**.

### Preventing Aliasing

Aliasing can be prevented in two ways:

1. Sample at or above the **Nyquist rate**.
2. Remove frequencies above the Nyquist limit using an **anti-aliasing filter** before sampling.

The anti-aliasing filter will be discussed in a later chapter on digital filters.

### Key Takeaway

- **Aliasing** occurs when a signal is sampled below the Nyquist rate.
- High-frequency components are misrepresented as lower frequencies.
- Once aliasing occurs, the lost information cannot be recovered.

> <font color='red'><b>Note:</b> At this stage, we are not concerned with the mathematical explanation of **why aliasing occurs** or how the alias frequency is calculated. Our goal is simply to understand **what aliasing is**, **why it happens**, and **how to prevent it** in practice. The mathematical explanation will become clearer when we study the frequency domain and the Fourier Transform.</font>

---
## <font color='green'>2.6 Quantization</font>

After sampling, we have a **discrete-time signal**. However, each sample can still take **any real value**.

A computer cannot store an infinite number of possible values. Instead, each sample must be rounded to one of a finite number of levels.

This process is called **quantization**.

For example, suppose the actual sample values are:

```
23.41
23.67
23.89
24.12
```

If we quantize to one decimal place, they become:

```
23.4
23.7
23.9
24.1
```

Notice that the quantized values are close to the original values, but not exactly the same. This small difference is the price we pay for representing signals digitally.

The number of available quantization levels depends on the **number of bits** used to represent each sample.

### Key Takeaway

- **Sampling** makes a signal **discrete in time**.
- **Quantization** makes a signal **discrete in amplitude**.
- Quantization introduces a small approximation error because sample values are rounded to finite levels.

---
## <font color='green'>2.7 Bit Depth and Quantization Error</font>

The accuracy of a digital signal depends on the **number of bits** used to represent each sample. This is known as the **bit depth**.

If a sample is represented using **\(n\)** bits, then the number of possible quantization levels is

\[
2^n
\]

Some common examples are shown below.

| Bit Depth | Quantization Levels |
|-----------|---------------------:|
| 8-bit | 256 |
| 12-bit | 4,096 |
| 16-bit | 65,536 |
| 24-bit | 16,777,216 |

A higher bit depth provides more quantization levels, allowing the digital signal to represent the original analog signal more accurately.

### Quantization Error

Since each sample is rounded to the nearest quantization level, a small difference exists between the original sample value and its digital representation.

This difference is called the **quantization error**.

In general:

- Higher bit depth → Smaller quantization error
- Lower bit depth → Larger quantization error

### Key Takeaway

- **Bit depth** determines the number of quantization levels.
- More bits provide a more accurate representation of the original signal.
- Quantization always introduces a small error, but increasing the bit depth reduces this error.


---
## <font color='green'>2.8 The Complete ADC Process</font>

We can now summarize the complete process of converting an analog signal into a digital signal.

```text
Analog Signal
      │
      ▼
  Sampling
      │
      ▼
Discrete-Time Signal
      │
      ▼
 Quantization
      │
      ▼
Digital Signal
```

The two key operations are:

1. **Sampling** – Converts a continuous-time signal into a discrete-time signal.
2. **Quantization** – Converts each sample into one of a finite number of digital values.

The resulting digital signal can now be:

- Stored in memory
- Processed by a computer
- Transmitted over a network
- Used by DSP algorithms

---
## <font color='green'>2.9 Chapter Summary</font>

- Real-world signals are continuous (analog).
- Sampling converts an analog signal into a discrete-time signal.
- The sampling rate must satisfy the Nyquist criterion to avoid aliasing.
- Quantization converts sample values into finite digital levels.
- Higher bit depth reduces quantization error.
- Together, sampling and quantization form the **Analog-to-Digital Conversion (ADC)** process.

### What's Next?

So far, we have learned how real-world signals enter a digital system.

In the next chapter, we will study the reverse process—**Digital-to-Analog Conversion (DAC)**—which converts digital signals back into analog signals that can be heard, displayed, or measured in the real world.




---
## **Relevant Links**

[Back to DSP Undergrade Level](index.md)

[Back to DSP Courses (All)](../index.md)


