---
hide:
  - navigation
  
tags:
  - venv
  - conda
---
# **Python and Conda Virtual Environments**

---
## <font color='green'> 1. What is a Python venv </font>
To isolate various Python projects, we create separate Python **virtual environments (venv)**.
Each venv acts like a lightweight virtual machine, running independently with its own:

- Python interpreter
- Packages and libraries
- Configuration settings

This ensures that:

- Projects do not interfere with each other’s dependencies
- Different projects can use different versions of the same package
- The development setup is clean, consistent, and easy to reproduce

---
## <font color='green'>2. Similar concept to dockers </font>
It is similar to the concept of Docker containers, but limited to the context of Python.
While Docker isolates entire applications and their environments at the system level, Python virtual environments isolate Python-specific dependencies and configurations at the project level.

---
## <font color='green'> 3. Python venv commands </font>

### Create a venv
Geheral syntax:  ```python3 -m venv <venv-name>```

Example:
```console
python3 -m venv venv-proj1/
```

This command creates a new virtual environment in a directory called ```venv-proj1```

- ```venv-proj1``` is not the actual project folder; it only contains the Python environment (i.e. Python interpreter, installed modules, configuration settings, etc.).

- The actual project files (i.e. your Python code) are usually placed in the same parent folder as the virtual environment. (such as ```src```, ```tests```, and other files)

For example:

```
my-project/
├── venv-proj1/
├── src/
├── tests/
└─── <other files/folders for the project>
```


### Activate a venv
General syntax: ```source <venv-name>/bin/activate```

```
source venv-proj1/bin/activate
```

### Deactivate a venv
```
deactivate
```


### Deletes a venv
General syntax: ```rm -rf <venv-name>```

```
rm -rf venv-proj1
```

---
## <font color='green'> 4. Conda environment reference </font>

### Create, clone and edit a conda environment
Note: --name can be replaced with -n (as short form)

```
conda create --name myenv python=3.10
or
conda create -n myenv python=3.10
or
conda create -n dataenv python=3.10 numpy pandas matplotlib
or
conda create --name newenv --clone myenv

```

### Using yml files

```
conda env create -f environment.yml

type following in environment.yml:

name: myenv
dependencies:
  - python=3.11
  - numpy
  - pandas
```

### Activate or deactivate

```
conda activate myenv
conda activate myenv
```

###View
```
conda env list
```

### Delete 
```
conda remove -n myenv --all
```


---
## <font color='green'> 5. Some useful links </font>
[Python Virtual Environments](https://docs.python.org/3/library/venv.html)

[Anaconda Environments](https://www.anaconda.com/docs/getting-started/working-with-conda/environments)
