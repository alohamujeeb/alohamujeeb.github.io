---
tags:
  - iterators
---
# **Iterators in Python**

---
## 1. What is an Iterator

- There are objects in Python that group multiple elements together, such as: lists, tuples, dictionaries, sets etc.

- These are called **iterables** because you can go through their elements.

- Iteration is the process of going through elements of a collection one by one and performing some operation on each element, usually exactly once per element.

- We can process all elements in these collections using loops like **for** or **while**.

- However, instead of using a loop directly, we can manually create an **iterator**.

--- 
### 2. Lazy processing
In lazy processing:

- We do not compute or load all data immediately.
- Instead, we compute each value only when it is needed.

**Iterators are a technique for lazy processing**, meaning values are produced and processed only when they are needed, not all at once.


---
## 3. What is Iterator Object

- **An iterator is an object** in Python that allows you to access elements of a collection one at a time, keeping track of its current position internally.


Example WITHOUT iterator (with loop):

```
my_list = [10, 20, 30]

for item in my_list:
    print(item)
```

Example WITH iterator:
<br>(This automatically goes through each element once, from start to end)


```
my_list = [10, 20, 30]

it = iter(my_list)   # create iterator

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
```

- A loop automatically handles iteration for us. 
<br>An iterator lets you control the process manually, step by step.

---
## 4. Why use iterators?

### i) **Memory efficiency** (big reason):
A loop over a list already works fine because the list is in memory. But iterators become powerful when data is not fully stored in memory at once.

e.g Reading a very big file; 
<br>The file is not loaded entirely into memory
<br>Only one line is processed at a time

```
file = open("big_file.txt")

record = iter(file)

print(next(record))  # reads one line
print(next(record))  # next line
```

### ii) **Working with infinite or very large data**: 
A list must store everything, but iterators can generate values one by one.


In the following example, we don’t need to store everything upfront.
```
import itertools

counter = iter(range(10**18))  # huge sequence (conceptually infinite-scale)

print(next(counter))
```

### iii) **More control over iteration**: 
With iterators, we manually control when to move forward.
```
it = iter([1, 2, 3])

print(next(it))  # you decide when to get next item
```

### iv) **4) Loops already use iterators:** 
A for loop is actually just a simplified version of iterators:

```
for item in my_list:
    print(item)
    
#is internally like following:

it = iter(my_list)
while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break
```

## 5. Some real-life examples

### Very large files
Imagine a 10GB log file

```
#BAD WAY
data = open("big.log").read()  # loads everything into memory 


#GOOD way (user iterators)
file = open("big.log")

for line in file:
    if "ERROR" in line:
        print(line)   
```

### Huge data sets
```
data_stream = iter(range(10**12))  # huge conceptual dataset

print(next(data_stream))  # process 1 item
print(next(data_stream))  # process next iteme
```

### Streaming Data
Example: live sensor data or stock prices

```
import time

def stream_data():
    yield "price: 100"
    time.sleep(1)
    yield "price: 101"
    time.sleep(1)
    yield "price: 102"

it = iter(stream_data())

print(next(it))  # price: 100
print(next(it))  # price: 101
```
### Paginated API responses

APIs don’t return everything at once; Data comes in chunks
<br>hence we need iterators

```
pages = iter([
    ["user1", "user2"],
    ["user3", "user4"],
    ["user5"]
])

print(next(pages))  # page 1
print(next(pages))  # page 2
```

