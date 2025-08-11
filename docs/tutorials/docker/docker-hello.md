---
tags:
  - Linux
  - docker
---
# Hello Docker (Create Your First Docker)

In this section, we build a simple Docker application that displays a message on the screen. While it's not a very useful app, it serves to demonstrate the basic concept clearly.


## 1. Create a directory structure

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

## 2. Create file contents

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
 

## 3. Build the docker and run

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

## 4. Copy and run onto another machine
Once docker image is ready, you can export it to a file, so that it can be trasferred to any machine where it can be executed.

``` bash
sudo docker save -o my_first_docker.tar my_first_docker
```

## 5. Run the docker image on target machine

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

## 6. Run multiple instances of a docker app
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

















