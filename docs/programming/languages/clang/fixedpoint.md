---
hide:
  - navigation
  
tags:
  - Fixed-Point
  - Fixed Point
  - Q15
  - Q31
  

---

# Fixed-Point Arithmetic in Embedded C

*This article is intended for intermediate and advanced C programmers. It explains how fixed-point arithmetic can be used as an efficient alternative to floating-point arithmetic on embedded systems that do not include a Floating-Point Unit (FPU).*

---
## <font color='green'>1. What Is Fixed-Point Arithmetic?</font>

Floating-point arithmetic is computationally intensive. To perform floating-point operations efficiently, many modern processors include a dedicated hardware unit known as the **Floating-Point Unit (FPU)**.

Most general-purpose processors, such as Intel x86 processors and many ARM processors, include an FPU that performs floating-point addition, subtraction, multiplication, and division directly in hardware. This significantly improves performance for applications that require floating-point calculations.

However, many low-cost microcontrollers used in embedded systems do **not** include an FPU. These devices are designed to minimize cost, power consumption, and silicon area, making dedicated floating-point hardware unnecessary for many applications.

On systems without an FPU, floating-point calculations can still be performed, but they are typically implemented entirely in software using compiler-provided libraries. Although this produces the correct results, software-emulated floating-point arithmetic is considerably slower than hardware execution and increases both code size and execution time.

**When developing applications for such systems, there are two common approaches:**

1. Perform all floating-point calculations in software.
2. Convert fractional values into scaled integers and perform all calculations using integer arithmetic. This technique is known as **fixed-point arithmetic**.

Fixed-point arithmetic represents fractional values using integers together with an implied scaling factor. **Since integer operations are directly supported by the processor, fixed-point calculations are generally much faster** and more predictable than software-emulated floating-point operations.

The following sections explain how fixed-point numbers are represented, how arithmetic is performed on them, and how formats such as **Q15** and **Q31** are commonly used in embedded systems.


---
## <font color='green'>2. Representing Fixed-Point Numbers</font>

A fixed-point number is simply an integer that is interpreted using a predefined scaling factor. The scaling factor determines how the stored integer is converted into its actual fractional value.

Unlike floating-point numbers, no exponent or fractional component is stored separately. Instead, the programmer agrees on a scaling factor, and every value is interpreted using that scale.

For example, suppose we wish to store values with **two decimal places** of precision.

Instead of storing

```
12.50
```

we store

```
1250
```

Similarly,

| Actual Value | Stored Integer |
|-------------:|---------------:|
| `12.50` | `1250` |
| `3.75` | `375` |
| `-8.25` | `-825` |
| `0.10` | `10` |

The scaling factor in this example is **100**, meaning that the stored integer is always interpreted by dividing it by 100.

```
Actual Value = Stored Integer / 100
```

For example,

```
1250 ÷ 100 = 12.50
375  ÷ 100 =  3.75
-825 ÷ 100 = -8.25
```

The processor never performs these divisions automatically. Internally, it only stores and manipulates the integer values.

For example,

```c
int value = 1250;
```

The processor simply stores the integer `1250`. It is the programmer who interprets this value as `12.50` by applying the scaling factor.

This approach allows ordinary integer instructions to be used for calculations while still representing fractional quantities.

### **Choosing a Scaling Factor**

The choice of scaling factor determines the precision of the representation.

For example,

| Scaling Factor | Smallest Step | Example |
|---------------:|--------------:|---------|
| `10` | `0.1` | `125` represents `12.5` |
| `100` | `0.01` | `1250` represents `12.50` |
| `1000` | `0.001` | `12500` represents `12.500` |

A larger scaling factor provides greater precision because more fractional digits can be represented. However, it also reduces the maximum value that can be stored in a fixed-size integer before overflow occurs.

For example, a 16-bit signed integer can store values from **−32768** to **32767**.

If a scaling factor of `100` is used, the largest representable value becomes

```
32767 / 100 = 327.67
```

Increasing the scaling factor to `1000` improves the precision to three decimal places, but reduces the maximum representable value to

```
32767 / 1000 = 32.767
```

Choosing an appropriate scaling factor therefore involves balancing two competing requirements:

- **Precision**, which determines the smallest representable increment.
- **Range**, which determines the largest and smallest values that can be represented without overflow.

Many embedded applications use **binary scaling** instead of decimal scaling because powers of two allow multiplication and division to be implemented efficiently using bit shifts. This leads to the widely used **Q-format** representation, which is discussed in the next section.


---
## <font color='green'>3. Q Format</font>

Although decimal scaling is easy to understand, embedded systems commonly use **binary scaling** because processors naturally operate on binary numbers.

Rather than using scaling factors such as 10, 100, or 1000, fixed-point values are typically scaled by a power of two. This representation is known as **Q format**.

In Q format, a fixed-point number is divided into an **integer part** and a **fractional part**. The number following the letter **Q** indicates how many bits are used to represent the fractional portion of the value.

For example:

- **Q7** uses 7 fractional bits.
- **Q15** uses 15 fractional bits.
- **Q31** uses 31 fractional bits.

The remaining bit is used as the sign bit because fixed-point values are normally stored as signed integers.

### **Q15 Format**

Q15 is one of the most commonly used fixed-point formats in embedded systems. It stores values in a signed 16-bit integer, with one sign bit and fifteen fractional bits.

```
 15               0
+---+---------------+
| S | Fraction (15) |
+---+---------------+
```

The value represented by a Q15 number is

```
Actual Value = Stored Integer / 2^15
```

Since

```
2^15 = 32768
```

the stored integer is divided by **32768** to obtain its actual value.

For example,

| Stored Integer | Actual Value |
|---------------:|-------------:|
| `32767` | `0.99997` |
| `16384` | `0.5` |
| `8192` | `0.25` |
| `0` | `0.0` |
| `-16384` | `-0.5` |
| `-32768` | `-1.0` |

Notice that the largest positive value is slightly less than **1.0** because one positive value is sacrificed to allow the representation of **-1.0**.

### **Q31 Format**

When greater precision is required, many embedded applications use **Q31**.

Q31 stores values in a signed 32-bit integer.

```
31                       0
+---+-----------------------+
| S | Fraction (31)         |
+---+-----------------------+
```

The represented value is

```
Actual Value = Stored Integer / 2^31
```

Q31 provides much finer resolution than Q15 while still using efficient integer arithmetic. It is widely used in digital signal processing, motor control, and control algorithms where additional precision is required.

### **Why Powers of Two?**

Binary scaling is particularly efficient because multiplication and division by powers of two correspond to simple bit-shift operations.

For example,

```
2^15 = 32768
2^31 = 2147483648
```

Scaling by these values aligns naturally with the processor's binary arithmetic, making fixed-point calculations efficient on processors without an FPU.

In practice, Q15 and Q31 have become the standard fixed-point formats for many embedded software libraries and DSP applications because they provide an excellent balance between precision, performance, and ease of implementation.

The next section explains how values are converted between floating-point and fixed-point representations.

---
## <font color='green'>Example 1: Using Decimal Scaling</font>

Suppose we want to represent temperatures with **two decimal places** of precision. Rather than storing floating-point values, we multiply each value by **100** and store the result as an integer.

For example,

| Actual Temperature | Stored Integer |
|-------------------:|---------------:|
| `25.75°C` | `2575` |
| `1.50°C` | `150` |

Adding **1.50°C** to **25.75°C** becomes simple integer addition.

```c
#include <stdio.h>

int main(void)
{
    /* Scale factor = 100 */

    int temperature = 2575;   // 25.75°C
    int offset      = 150;    // 1.50°C

    temperature += offset;

    printf("Temperature = %.2f°C\n", temperature / 100.0);

    return 0;
}
```

Output

```
Temperature = 27.25°C
```

Internally, the processor performs only integer arithmetic.

```
2575 + 150 = 2725
```

The application interprets the result using the scaling factor.

```
2725 → 27.25°C
```

Although simple, decimal scaling is mainly useful for understanding the concept of fixed-point arithmetic. Embedded systems typically use **binary scaling**, which is more efficient because it aligns naturally with the processor's binary arithmetic.

---

## **Example 2: Using Q15 Format**

Q15 stores fractional values in a signed 16-bit integer using a scaling factor of **2¹⁵ = 32768**.

The following example performs the same calculation using Q15.

```c
#include <stdio.h>
#include <stdint.h>

#define Q15_SHIFT 15
#define TO_Q15(x)   ((int16_t)((x) * (1 << Q15_SHIFT)))
#define FROM_Q15(x) ((double)(x) / (1 << Q15_SHIFT))

int main(void)
{
    int16_t temperature = TO_Q15(25.75);
    int16_t offset      = TO_Q15(1.50);

    int32_t result = (int32_t)temperature + offset;

    printf("Temperature = %.2f°C\n", FROM_Q15((int16_t)result));

    return 0;
}
```

Output

```
Temperature = 27.25°C
```

Although both examples produce the same result, Q15 uses a **power-of-two scaling factor**, making it the preferred representation for many embedded systems and digital signal processing applications.



---

## **Example 3: Using Q31 Format**

Q31 uses a signed 32-bit integer with **31 fractional bits**, providing much greater precision than Q15.

Suppose we want to multiply a normalized signal by a gain.

```
Signal = 0.80
Gain   = 0.75
```

The expected result is

```
0.80 × 0.75 = 0.60
```

Using Q31, the calculation is performed entirely with integer arithmetic.

```c
#include <stdio.h>
#include <stdint.h>

#define Q31_SHIFT 31
#define TO_Q31(x)   ((int32_t)((x) * (1LL << Q31_SHIFT)))
#define FROM_Q31(x) ((double)(x) / (1LL << Q31_SHIFT))

int main(void)
{
    int32_t signal = TO_Q31(0.80);
    int32_t gain   = TO_Q31(0.75);

    /* Q31 multiplication */
    int64_t result = (int64_t)signal * gain;
    result >>= Q31_SHIFT;

    printf("Signal : %.2f\n", FROM_Q31(signal));
    printf("Gain   : %.2f\n", FROM_Q31(gain));
    printf("Result : %.2f\n", FROM_Q31((int32_t)result));

    return 0;
}
```

Output

```
Signal : 0.80
Gain   : 0.75
Result : 0.60
```

Notice that the multiplication produces a 64-bit intermediate result. This is necessary because multiplying two 32-bit Q31 values can exceed the range of a 32-bit integer. After the multiplication, the result is shifted right by **31 bits** to restore the Q31 scaling.

Q31 is widely used in digital signal processing, motor control, and control algorithms because it provides much higher precision than Q15 while still avoiding floating-point arithmetic.


---
## <font color='green'>4. Choosing the Right Q Format</font>

There is no single fixed-point format that is suitable for every application. The choice of Q format depends on the required **range** and **precision** of the values being represented.

Using more fractional bits increases precision but reduces the range of values that can be represented. Conversely, allocating more bits to the integer portion increases the range but reduces the precision.

The following table compares some commonly used fixed-point formats.

| Format | Storage | Approximate Range | Typical Applications |
|--------|---------|-------------------|----------------------|
| Q7 | 8-bit | -1.0 to +0.992 | Audio samples, small lookup tables |
| Q15 | 16-bit | -1.0 to +0.99997 | Sensor data, DSP, motor control |
| Q31 | 32-bit | -1.0 to +1.0 | High-precision DSP, digital filters, control algorithms |

### **When to Use Q7**

Q7 uses only one byte of memory, making it suitable for memory-constrained systems where moderate precision is acceptable.

Typical uses include:

- Audio processing
- Small lookup tables
- Neural network inference on tiny microcontrollers

---

### **When to Use Q15**

Q15 is probably the most widely used fixed-point format in embedded systems.

It provides a good balance between memory usage, execution speed, and precision, making it suitable for many real-time applications.

Typical uses include:

- Sensor processing
- Motor control
- PID controllers
- Audio processing
- ARM CMSIS-DSP libraries

---

### **When to Use Q31**

Q31 offers significantly greater precision than Q15 while still avoiding floating-point arithmetic.

Because it uses 32-bit integers, calculations require more memory and, in some cases, wider intermediate variables such as `int64_t`.

Typical uses include:

- Digital filters
- Signal processing
- Precision control systems
- Navigation and estimation algorithms

---

### **Factors to Consider**

When selecting a Q format, consider the following:

- **Range**: Can the format represent the largest and smallest expected values?
- **Precision**: Does it provide sufficient fractional resolution?
- **Memory**: Larger formats consume more RAM and Flash.
- **Performance**: Smaller data types are generally processed more efficiently on low-end microcontrollers.
- **Overflow Risk**: Larger integer values increase the likelihood of overflow during multiplication.

Choosing the correct Q format is always a trade-off between **range**, **precision**, and **performance**. In practice, **Q15** is often the preferred choice for 16-bit embedded applications, while **Q31** is used when additional precision is required.

---
## <font color='green'>5. Overflow and Precision</font>

One of the primary challenges of fixed-point arithmetic is managing **overflow** and **precision**. Since fixed-point values are stored using integers of a fixed size, every calculation must remain within the representable range of the chosen format.

### **Overflow**

Overflow occurs when the result of an arithmetic operation exceeds the maximum or minimum value that can be represented by the underlying integer type.

For example, a Q15 value is stored in a signed 16-bit integer. The valid range is

```
-32768 to 32767
```

If an arithmetic operation produces a value outside this range, the result cannot be represented correctly. Depending on the processor and compiler, the value may wrap around, producing an incorrect result.

For this reason, many fixed-point algorithms perform intermediate calculations using a wider integer type. For example, multiplying two Q15 values typically uses a 32-bit intermediate result, while multiplying two Q31 values requires a 64-bit intermediate.

### **Precision Loss**

Although fixed-point arithmetic avoids the overhead of floating-point operations, it cannot represent every fractional value exactly.

The smallest change that can be represented depends on the number of fractional bits.

For example:

- Q15 has a resolution of **1 / 32768**
- Q31 has a resolution of **1 / 2³¹**

Increasing the number of fractional bits improves precision but reduces the range of values that can be represented.

### **Rounding and Truncation**

Some arithmetic operations, particularly multiplication and division, require the result to be rescaled. During this process, fractional bits may be discarded.

Simply discarding the extra bits truncates the result, introducing a small error. In applications where numerical accuracy is important, the result is often rounded before rescaling to reduce the accumulated error.

### **Saturation Arithmetic**

Many embedded processors and DSP libraries support **saturation arithmetic**.

Instead of allowing an overflow to wrap around, the result is clamped to the nearest representable value.

For example,

```
32767 + 100
```

becomes

```
32767
```

rather than wrapping to a negative value.

Saturation arithmetic is widely used in digital signal processing and motor control because it produces more predictable behaviour than integer wrap-around.

### **Best Practices**

When implementing fixed-point arithmetic:

- Choose a Q format that provides sufficient range and precision.
- Use wider intermediate types for multiplication.
- Be aware of precision loss during rescaling.
- Use saturation arithmetic when supported or when overflow must be prevented.
- Test calculations using boundary values to detect overflow conditions.

Careful management of overflow and precision is essential for producing reliable and predictable fixed-point software, especially in safety-critical and real-time embedded applications.


---
## <font color='green'>6. Implementing Fixed-Point Arithmetic in C</font>

Most embedded applications encapsulate fixed-point operations behind macros or functions. This improves code readability, reduces the likelihood of programming errors, and allows the underlying representation to be changed with minimal modifications to the application.

### **Converting Between Floating-Point and Q Format**

The following macros convert between floating-point values and Q15 or Q31 representations.

```c
#include <stdint.h>

#define Q15_SHIFT      15
#define Q31_SHIFT      31

#define TO_Q15(x)      ((int16_t)((x) * (1 << Q15_SHIFT)))
#define FROM_Q15(x)    ((float)(x) / (1 << Q15_SHIFT))

#define TO_Q31(x)      ((int32_t)((x) * (1LL << Q31_SHIFT)))
#define FROM_Q31(x)    ((double)(x) / (1LL << Q31_SHIFT))
```

These conversions are typically used during initialization, debugging, or when exchanging data with floating-point code.

---

### **Multiplying Q15 Values**

When multiplying two Q15 values, the intermediate result must be stored in a 32-bit integer before restoring the Q15 scaling.

```c
int16_t q15_mul(int16_t a, int16_t b)
{
    return (int16_t)(((int32_t)a * b) >> Q15_SHIFT);
}
```

---

### **Multiplying Q31 Values**

Q31 multiplication requires a 64-bit intermediate result because multiplying two 32-bit integers can overflow a 32-bit variable.

```c
int32_t q31_mul(int32_t a, int32_t b)
{
    return (int32_t)(((int64_t)a * b) >> Q31_SHIFT);
}
```

---

### **Encapsulating Fixed-Point Operations**

Rather than performing scaling and bit shifts throughout an application, it is good practice to encapsulate fixed-point operations in dedicated functions.

For example,

```c
int16_t q15_add(int16_t a, int16_t b);
int16_t q15_sub(int16_t a, int16_t b);
int16_t q15_mul(int16_t a, int16_t b);

int32_t q31_add(int32_t a, int32_t b);
int32_t q31_sub(int32_t a, int32_t b);
int32_t q31_mul(int32_t a, int32_t b);
```

Using these functions keeps application code simple and reduces the risk of incorrect scaling or overflow.

---

### **Use Existing Libraries When Available**

Many embedded software frameworks already provide optimized fixed-point arithmetic routines.

For example, the ARM CMSIS-DSP library includes functions such as:

- `arm_add_q15()`
- `arm_sub_q15()`
- `arm_mult_q15()`
- `arm_add_q31()`
- `arm_sub_q31()`
- `arm_mult_q31()`

These functions are highly optimized for ARM Cortex-M processors and often include saturation arithmetic, making them more efficient and reliable than custom implementations.

Whenever a suitable library is available, it is generally preferable to use the vendor-provided implementation rather than developing your own fixed-point routines.

---
## <font color='green'>7. Fixed-Point vs. Floating-Point</font>

Both fixed-point and floating-point arithmetic have their advantages. The choice depends on the capabilities of the target processor and the requirements of the application.

| Fixed-Point | Floating-Point |
|--------------|----------------|
| Uses integer arithmetic | Uses floating-point arithmetic |
| Fast on processors without an FPU | Fast on processors with a hardware FPU |
| Smaller code size | Larger code size on processors without an FPU |
| Predictable execution time | Execution time may vary depending on hardware support |
| Limited range and precision | Wide dynamic range and high precision |
| Requires careful scaling | Scaling is handled automatically |

### **When to Use Fixed-Point**

Fixed-point arithmetic is well suited for applications where:

- The processor does not include a hardware floating-point unit (FPU).
- Real-time performance is critical.
- Memory and code size are limited.
- Numerical ranges are well understood.
- Deterministic execution time is required.

Typical applications include:

- Motor control
- Digital signal processing
- Sensor processing
- Battery-powered embedded devices
- Low-cost microcontrollers

---

### **When to Use Floating-Point**

Floating-point arithmetic is generally the better choice when:

- The processor includes a hardware FPU.
- The application requires a very large dynamic range.
- High numerical precision is more important than execution speed.
- Ease of development and code readability are priorities.

Typical applications include:

- Scientific computing
- Machine learning
- Image processing
- Simulation and modelling
- Desktop and server applications




---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
