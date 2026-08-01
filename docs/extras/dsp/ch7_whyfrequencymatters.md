---
hide:
  - navigation
  
search:
  exclude: true
  
---

# <font color='green'>Chapter 7: Why Frequency Matters</font>

**Goal:** Students understand the limitations of viewing signals only in the time domain and appreciate why frequency-domain analysis is one of the most powerful tools in classical Digital Signal Processing.

---

## <font color='green'>7.1 Why Frequency Matters</font>

So far, we have represented signals as **amplitude versus time**.

This representation is useful because it tells us **how a signal changes over time**.

However, mathematics offers another fascinating way of looking at signals.

> According to Fourier's theory, **any signal can be represented as a combination of simple sinusoidal signals**.

In other words, a complex signal can be **decomposed** into many sine waves, each having its own:

- Amplitude
- Frequency
- Phase

Likewise, the original signal can be **reconstructed** by adding all of these sinusoidal components together.

```text
Complex Signal
        │
        ▼
+---------------------------+
|  Sine Wave 1              |
|  Sine Wave 2              |
|  Sine Wave 3              |
|  Sine Wave 4              |
|  ...                      |
+---------------------------+
        │
        ▼
Original Signal
```

At first, this may seem like an unnecessary complication.

> Why replace one signal with many simpler signals?
> The reason is that **sinusoids are among the simplest signals to analyze**.

Over many decades, engineers have developed powerful mathematical tools for understanding how sinusoidal signals behave in electrical circuits, communication systems, filters, and many other engineering applications.

Instead of analyzing a complicated signal directly, we first express it as a collection of sinusoids. This often makes the analysis much easier.

---

## <font color='green'>7.2 Linear Time-Invariant (LTI) Systems</font>

The idea of decomposing a signal into sinusoids becomes especially powerful because **most systems studied in Digital Signal Processing are Linear Time-Invariant (LTI) systems**.

The most important property of an LTI system is the **superposition principle**.

> **The response to a sum of signals is equal to the sum of the responses to each individual signal.**

Suppose a signal is composed of three sinusoids.

```text
Input Signal

Signal = Sine₁ + Sine₂ + Sine₃
```

Instead of analyzing the complete signal at once, we can analyze each sinusoid independently.

```text
Sine₁ ───► System ───► Output₁

Sine₂ ───► System ───► Output₂

Sine₃ ───► System ───► Output₃
```

The final output is simply the sum of the individual outputs.

```text
Final Output

Output = Output₁ + Output₂ + Output₃
```

In other words,

```text
System(Sine₁ + Sine₂ + Sine₃)

          =

System(Sine₁)
+
System(Sine₂)
+
System(Sine₃)
```

This means that instead of solving one difficult problem, we solve many simple problems and combine the results.

This is one of the main reasons why **frequency-domain analysis** is so useful.

> <font color='red'><b>Note:</b> At this stage, we are only introducing the intuitive idea of an LTI system. We are not discussing the mathematical definitions of linearity or time invariance. Those topics will be covered later in the course.</font>

### Key Takeaway

Frequency-domain analysis is based on two powerful ideas:

- **Any signal can be represented as a combination of sinusoids.**
- **For LTI systems, the response to a combination of signals is equal to the combination of the individual responses.**

Together, these ideas allow complex signals to be analyzed using simple sinusoidal building blocks, making many signal processing problems much easier to solve.


---
## <font color='green'>7.3 Time Domain vs Frequency Domain</font>

A signal can be represented in more than one way.

The two most common representations are the **time domain** and the **frequency domain**.

### Time-Domain Representation

In the **time domain**, we store the **value of the signal at each instant of time**.

In other words, the question being answered is:

> **"What is the signal value at this instant?"**

A time-domain signal is therefore represented as:

```text
Amplitude
    ^
    |
    |      /\
    |     /  \__
    |____/__________> Time
```

The horizontal axis represents **time**, while the vertical axis represents the **signal amplitude**.

---

### Frequency-Domain Representation

Instead of asking **when** the signal changes, we ask a different question:

> **"How much of each frequency is present in the signal?"**

Recall that a sinusoid is described by

```text
x(t) = A sin(2πft + φ)
```

where

- **A** = Amplitude
- **f** = Frequency
- **φ** = Phase

Since **any signal can be represented as a combination of sinusoids**, the frequency-domain representation simply stores these parameters for every frequency component present in the signal.

Unlike the time domain, we no longer store values against **time**.

Instead, for every frequency (from **0 Hz** to higher frequencies), we store:

- **Amplitude**
- **Phase**

Therefore, a complete frequency-domain representation consists of **two plots**.

### Amplitude Spectrum

The first plot shows **how much of each frequency is present**.

```text
Amplitude
    ^
    |
    |          │
    |    │     │         │
    |____│_____│_________│____________> Frequency (Hz)
         f₁    f₂        f₃
```

---

### Phase Spectrum

The second plot shows the **phase shift associated with each frequency**.

```text
Phase
   ^
   |      ●
   |             ●
   |  ●
   +---------------------------------> Frequency (Hz)
       f₁    f₂        f₃
```

Together, the **Amplitude Spectrum** and the **Phase Spectrum** completely describe the signal in the frequency domain.

### Key Takeaway

| **Time Domain** | **Frequency Domain** |
|-----------------|----------------------|
| Signal value is stored against **time** | Amplitude and phase are stored against **frequency** |
| Answers: **What is the signal value at this instant?** | Answers: **How much of each frequency is present?** |
| One plot | Two plots (Amplitude Spectrum and Phase Spectrum) |

---
## <font color='green'>7.4 An Example</font>

The difference between the **time domain** and the **frequency domain** is best understood through a simple example.

Suppose we have the following signal:

```text
x(t) = 3 sin(2π10t)
     + 2 sin(2π25t)
     + 1 sin(2π40t)
```

In the **time domain**, we simply observe the resulting waveform.

```text
Amplitude
    ^
    |      /\__/\_/\/\__
    |   __/             \__
    |__/____________________> Time
```

From this waveform alone, it is difficult to tell exactly which frequencies are present.

However, in the **frequency domain**, the same signal is represented by listing the amplitude and phase of each sinusoidal component.

### Amplitude Spectrum

```text
Amplitude
    ^
  3 |      │
  2 |             │
  1 |                    │
    +---------------------------------> Frequency (Hz)
          10      25      40
```

### Phase Spectrum

If all three sinusoids have zero phase, then

```text
Phase
   ^
 0°|      ●             ●             ●
   +---------------------------------> Frequency (Hz)
          10      25      40
```

Instead of viewing a complicated waveform, we immediately know that the signal contains:

- A **10 Hz** sinusoid with amplitude **3**
- A **25 Hz** sinusoid with amplitude **2**
- A **40 Hz** sinusoid with amplitude **1**

This is the main advantage of the frequency domain—it reveals the building blocks of a signal directly.

### Key Takeaway

The **time domain** shows the overall waveform, while the **frequency domain** reveals the individual sinusoidal components that make up that waveform.

---
## <font color='green'> 7.5 Chapter Summary </font>

In this chapter, we introduced the idea of **frequency-domain thinking**, which provides a completely different way of looking at signals.

The key points are:

- A signal can be represented in more than one way.

- The **time domain** shows how a signal changes with time.

- According to Fourier's theory, any signal can be represented as a combination of sinusoids.

- Every sinusoid is completely described by three parameters:
```
	Amplitude
	Frequency
	Phase
```

- Most DSP systems are modeled as **Linear Time-Invariant (LTI)** systems.
- For an LTI system, the response to a combination of signals is equal to the combination of the individual responses (superposition principle).

- This allows us to:
```
  1. Decompose a complex signal into sinusoids.
  2. Analyze each sinusoid independently.
  3. Combine the individual results to obtain the final response.
- In the **time domain**, we store the signal value against time.
- In the **frequency domain**, we store the amplitude and phase of each frequency component.
- A complete frequency-domain representation consists of:
  - An **Amplitude Spectrum**
  - A **Phase Spectrum**
```

The frequency domain does not replace the time domain—it provides another representation of the same signal. Depending on the problem, one representation may be much more useful than the other.

---
## **Relevant Links**

[Back to DSP Undergrade Level](index.md)

[Back to DSP Courses (All)](../index.md)


