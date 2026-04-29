---
tags:
  - lambda functions
---
# **Lambda Functions in Python**

---
## 1. What is a Lamda function

- A lambda function is an anonymous function (no name) defined using lambda.
- It is used to write a small, single-expression function inline.
- It is often used when a function is needed temporarily as an argument, especially in places like map(), filter(), and sorted().
- A lambda function is not “better” than a normal function. **It’s just a short-hand** tool for a specific situation.
- Lambda is useful when the **logic is very small** (one expression).

---
## 2. Simple examples
**Example 1:**
```
add = lambda a, b: a + b  #a,b are parameters
print(add(3, 5))  # Output: 8
```
**add** is a variable holding the lambda functions; the variable is not used with "parameters"
	
**Example 2(two variables for same function):**
```
add = lambda x, y: x + y
add2 = lambda x, y: x + y

a = 10
b = 20

print(add(a, b))   # 30
print(add2(a, b))  # 30
```

---
## 3. Why NOT always use lambda?

- Lambda is bad if logic becomes more than one step:

```
lambda x: x * 2 + 5  # OK

#following is not very good use of lambda
#At that point, def is much clearer
lambda x: (x * 2 + 5 if x > 0 else (x * 3 + 10 if x < 0 else x)) 
```

- **Simple rule of thumb**
	<br> - Use lambda when the function is short, simple, and used temporarily.
	<br> - Use def when the function has meaningful logic or needs clarity and reuse.

---
## 4. A more practical example

Sorting a tuple WITHOUT lamda
```
students = [
    ("Mujeeb", 78),
    ("Chua", 92),
    ("Chong", 85)
]

def get_marks(student):
    return student[1]

sorted_students = sorted(students, key=get_marks)

print(sorted_students)
```

Following is same example WITH lamda
```
students = [
    ("Mujeeb", 78),
    ("Chua", 92),
    ("Chong", 85)
]

# Sort by marks (second item in tuple)
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)

Output: [('Mujeeb', 78), ('Chong', 85), ('Chua', 92)]
```
Note: The parameter is student; And the function code returns second index of students

