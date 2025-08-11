---
tags:
  - Linux
  - docker
---
# Getting Started with Docker

---
## What is a docker
Docker is a tool (primarily a linux-based) that lets you package your application and everything it needs to run into a single container, so it works the same on any computer.

**Consider a scenario**:

There is a linux machine with following configuration.

- Ubuntu Linux 22.04
- Python 3.10
- OpenCV version 4.4


Now you wnat to run an application about **robotic vision** which required different set of tools as follows:

- Ubuntu Linux 22.04
- Python 3.12
- OpenCV version 4.2 (4.4 is not compatible with our robotic application)

![Current vs Required Tools](images/docker_1.png)


---
## We create an **ISOLATED** container
The ubunutu machine is not only running many other applications besides this new application **robotic vision**. By changing the python verion and OpenCV version may break other applications.

**So what to do in this case?**
We create an **ISOLATED** space in which we run new application alongwith all necessary tools and configuration settings.

This new isolated space is called a container (or docker).

![Docker Inside a Physical Machine](images/docker_2.png)

---
## Multiple docker containers
This idea can be extended to include many dockers containers in a single machine, as shown below. In each case, we can chose different tools, version and configurations.

![Multiple Dockers](images/docker_3.png)

---

##  Docker installation
Docker is an application that enables the creation of isolated environments called containers. If Docker is not installed on your system, follow these steps to install it:

You can check if docker is installed or not:
``` bash
docker --version
```
if you see an out like **docker command not found**, then following the steps below.


### Step 1: Install dependencies

```
sudo apt update
sudo apt install \
	ca-certificates \
	curl \
	gnupg \
	lsb-release -y
```

### Step 2:  Add Docker’s official GPG key
``` bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | \
    sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

### Step 3: Add Docker's repository

- Find debian codename by ``` lsb_release -c ```
(code name can be "bookwork" or "buster", or "bullseye" etc.) 
- $(lsb_release -cs) is replaced with your Debian codename (e.g., bullseye, bookworm):

=== "General Command"
	``` bash
	echo \
	  "deb [arch=$(dpkg --print-architecture) \
	  signed-by=/etc/apt/keyrings/docker.gpg] \
	  https://download.docker.com/linux/debian \
	  $(lsb_release -cs) stable" | \
	  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	```

=== "Debian (Bookwork) Command"
	
	``` bash
	echo \
	  "deb [arch=$(dpkg --print-architecture) \
	  signed-by=/etc/apt/keyrings/docker.gpg] \
	  https://download.docker.com/linux/debian \
	  $(bookworm -cs) stable" | \
	  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	```

### Step 4: Install docker 
``` bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
```

### Step 4: Verify installation
``` bash
docker --version

```
You should see an output like:
```
Docker version 28.3.3, build 980b856
```

---
## Creating a "Hello World" docker
In this section, we build a simple Docker application that displays a message on the screen. While it's not a very useful app, it serves to demonstrate the basic concept clearly.


### Create a folder with following files in it

We create a folder structure like this
```
hello-python-docker/
├── Dockerfile
├── hello_world.py
└── requirements.txt

```


``` bash
mkdir hello_python_docker	#create a folder

cd hello_python_docker		#python file that prints a message

touch hello_world.py

touch Dockerfile			#docker build instructions

touch requirements.txt 		# (optional) dependencies such as required python modules
```

### Create file contents

```hello_world.py```
``` python
import time

for i in range(1, 101):
    print(f"hello world - from a docker app-{i}")
    time.sleep(1)  # wait for 1 second
	
```

```Dockerfile```
``` Dockerfile
# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR .

# Copy source code
COPY hello_world.py .
COPY requirements.txt ./

# Install dependencies (if any)
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["python", "./hello_world.py"]
```

Following is some brief desritpoin:

- FROM python:3.11-slim  
(this sets the base image for the container. Your code and configuration are added on top of it as in the next steps)


- COPY main.py .   
(include this code file inside the Docker image)
	Note: If there are more files and folders, all need to be included

- WORKDIR . (This is the directory where the application starts)

- RUN pip install --no-cache-dir -r requirements.txt
(Installs the Python packages listed in requirements.txt inside the container using pip)
	
- CMD ["python", "./hello_world.py"]
 Defines the default command that will run when the container starts.
 

## Build and run

- **Change directory**
Make sure that you are in the folder "hello_python_docker"
``` bash 
cd ~/hello-python-docker
```
	
- **Build the docker (container)**
``` bash
sudo docker build -t my_first_docker .
```
The resulting Docker image is saved locally on your system — not as a file but inside Docker’s internal storage.
``` bash
sudo docker images
```
Output is:
```
REPOSITORY        TAG       IMAGE ID       CREATED         SIZE
my_first_docker   latest    d4f0787c8afb   2 minutes ago   141MB
```

- **Run the docker** (the flag -it is important here... more on this later)
``` bash 
sudo docker run -it my_first_docker
```
Output:
```
hello world - from a docker app-1
hello world - from a docker app-2
hello world - from a docker app-3
......
```

## Copy and run onto another machine
Once docker image is ready, you can export it to a file, so that it can be trasferred to any machine where it can be executed.

``` bash
sudo docker save -o my_first_docker.tar my_first_docker
```

## Run the docker image on target machine

- Create a docker image file (see the above section "exporting the docker image")
- Transfer to another machine (via network, usb, etc.)
- load the image into the target machine
``` bash
sudo docker load -i my_first_docker.tar
```
- verify that the image is properly imported.
``` bash
sudo docker images
```

- Run the docker application.
``` bash
sudo docker run -it my_first_docker
```

## Run multiple instances of a docker app
As mentioned earlier, that a docker is an indepdent container. 

Once created, a docker can run many instances. Following instructions show how to run a docker multiple (twice) in the same machine.

``` Open Terminal 1```
``` bash
sudo docker -it run my_first_docker
```

``` Open Terminal 2```
``` bash
sudo docker -it run my_first_docker
```

Both will be running the same program and each will be displaying their own message count.

















