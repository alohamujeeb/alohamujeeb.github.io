---
hide:
  - navigation
  
search:
  exclude: true
  
---

# <font color='green'>My DSP Notes</font>

A collection of notes on DSP

---
## <font color='green'>Part I (Signals & Sampling)</font>

**Question:**
How does the real world become digital?

**Outcome:**
Students understand how physical signals are converted into digital data and the limitations introduced by sampling and quantization.

### [Chapter 1: What is a Signal?](ch1_whatissignal.md)

### [Chapter 2: Analog-to-Digital Conversion (ADC)](ch2_adc.md)

### [Chapter 3: Digital to Analog Conversion (DAC)](ch3_dac.md)


---
## <font color='green'>Part II (Frequency-Domain Thinking)</font>

Question:
What is inside a signal?

Outcome:
Students can interpret signals in the frequency domain, understand the Fourier family of transforms, and choose the appropriate Fourier tool for a given problem.


	Chapters
	Why Frequency Matters
	Sinusoids as Building Blocks
	Linear Systems and Superposition
	Fourier Series
	Fourier Transform
	The Fourier Family
	FS
	FT
	DTFT
	DFT
	FFT
	Which Fourier Tool Should I Use?
	Hands-on Frequency Analysis
	Frequency-Domain Interpretation


---
## <font color='green'>Part III (Digital Filtering)</font>

Question:
How do we modify a signal?

Outcome:
Students understand how digital filters work, when to use FIR or IIR filters, and how to design filters to achieve a desired frequency response.


	Chapters
	Why Filtering?
	Time-Domain vs Frequency-Domain Filtering
	Convolution (motivated by filtering, not introduced in isolation)
	FIR Filters
	IIR Filters
	Frequency Response
	Filter Design
	Choosing Between FIR and IIR
	Filter Design Examples

---
## <font color='green'>Part IV — Analysis Domains</font>
(Choosing the Right Mathematical Tool)

Question:
Which mathematical domain should I use to analyze a signal or system?

Outcome:
Students understand the purpose and relationship of the time domain, frequency domain, Z-domain, and S-domain, and can identify the most appropriate analysis framework for a given engineering problem.


	Why Change Domains?

		Time domain
		Frequency domain
		Complex domain
		
	Time Domain vs Frequency Domain

		When is time-domain analysis enough?
		When does frequency-domain analysis become easier?

	Fourier Domain

		Signal analysis
		Spectrum
		Frequency content

	Z-Domain

		Why digital systems need the Z-transform
		Poles and zeros (conceptual only)
		Stability
		Frequency response

	Laplace (S-Domain)

		Why analog engineers use the s-domain
		Transient response
		Stability
		Relationship to the Fourier Transform

	Putting It All Together

---
## <font color='green'>Part IV — Optimization-Based Filter Design</font>
*(Computer-Aided Filter Design)*

**Question:**  
How can a computer automatically design a digital filter that satisfies a given set of specifications?

**Outcome:**  
Students understand how numerical optimization techniques are used to design digital filters, how they differ from analytical methods, and when each approach is appropriate.

    Why Optimization?

        Limitations of analytical methods
        Filter specifications
        Optimization as a design tool

    Problem Formulation

        Objective (cost) function
        Design constraints
        Performance metrics

    Classical Optimization Methods

        Least-Squares Design
        Minimax Design
        Parks–McClellan (Remez Exchange)

    Modern Optimization Methods

        Convex Optimization
        Genetic Algorithms
        Particle Swarm Optimization (PSO)
        Simulated Annealing

    AI-Based Filter Design

        Machine Learning
        Neural Networks
        Future trends

    Putting It All Together

        Analytical vs Optimization-based design
        Choosing the appropriate design method
        Practical design workflow


---
## <font color='green'>Part V — DSP with Python</font>
*(Practical Digital Signal Processing)*

**Question:**  
How do we implement digital signal processing algorithms using Python?

**Outcome:**  
Students learn how to implement, visualize, and experiment with DSP concepts using Python and its scientific computing libraries.

    Python for DSP

        Python ecosystem
        NumPy
        SciPy
        Matplotlib

    Working with Signals

        Generating signals
        Loading real-world signals
        Plotting signals
        Signal operations

    Sampling and Quantization

        Sampling experiments
        Aliasing demonstrations
        Quantization experiments

    Frequency Analysis

        Fourier Series
        FFT
        Spectrum visualization
        Spectrograms

    Digital Filtering

        FIR filters
        IIR filters
        Frequency response
        Audio filtering

    Real-World DSP Projects

        Audio processing
        ECG signal analysis
        Image filtering
        Sensor data processing

    Putting It All Together

        Building complete DSP applications
        Best practices
        Performance considerations
        
---
## <font color='green'>Part VI — Advanced Topics in DSP</font>
*(Beyond Classical Signal Processing)*

**Question:**  
How are advanced DSP techniques used to estimate, detect, and track signals in real-world applications?

**Outcome:**  
Students gain an overview of advanced DSP topics and understand where they are used in modern engineering systems.

    Estimation Theory

        Parameter estimation
        Least-squares estimation
        Maximum likelihood estimation
        Bayesian estimation

    Detection Theory

        Signal detection
        Hypothesis testing
        Matched filter
        ROC curves

    Tracking

        State estimation
        Kalman Filter
        Extended Kalman Filter
        Particle Filter (Overview)

    Adaptive Signal Processing

        Adaptive filters
        LMS algorithm
        RLS algorithm

    Time-Frequency Analysis

        STFT
        Wavelets
        Spectrograms

    Statistical Signal Processing

        Random signals
        Correlation
        Power spectral density (PSD)

    Multirate Signal Processing

        Decimation
        Interpolation
        Polyphase filters

    Putting It All Together

        Radar
        Sonar
        Communications
        Biomedical signal processing
        Autonomous systems
        
        
        
