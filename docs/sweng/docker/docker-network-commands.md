---
tags:
  - Linux
  - docker
---
# Docker command reference


## 1. Docker network commands

### Create networks
???+ "Create networks"
	|command|description|Example|
	|---|---|---|
	|```docker network create <network_name>```|Create a custom bridge network|```docker network create my_network-A```|
	|```docker network create --driver <driver> <network_name>```|Specify a network driver (e.g., bridge, overlay, macvlan)|```docker network create --driver overlay my_overlay_net-A```|
	|```docker network create -d bridge my-bridge-net```|Same as above using -d shorthand|```docker network create -d bridge my-bridge-net-A```|
	|```docker network create --subnet=192.168.100.0/24 custom_net```|Create a network with a custom subnet|```docker network create --subnet=192.168.100.0/24 my_subnet_net-A```|


###  Inspect & list networks
???+ "Inspect & List Networks"
	|command|description|Example|
	|---|---|---|
	|```docker network ls```|List all Docker networks|```docker network ls```|
	|```docker network inspect <network_name>```|Show detailed info (subnets, containers, etc.)|```docker network inspect bridge```|
	
###  Remove networks
???+ "Remove"
	|command|description|Example|
	|---|---|---|
	|```docker network rm <network_name>```|Remove a network by name|```docker network rm my_custom_net```|
	|```docker network rm net1 net2```|Remove multiple networks|```docker network rm net1 net2```|
	|```docker network prune```|Remove all unused (dangling) networks|```docker network prune```|
	
	
###  Connect and disconnect containers
???+ "Remove"
	|command|description|Example|
	|---|---|---|
	|```docker network connect <network_name> <container_name>```|Attach a container to an existing network|```docker network connect my_custom_net my_container```|
	|```docker network disconnect <network_name> <container_name>```|Detach a container from a network|```docker network disconnect my_custom_net my_container```|

###  Gateways
???+ "Gateways"
	|command|description|
	|---|---|
	|docker network create --subnet=192.168.50.0/24 --gateway=192.168.50.1 my_advanced_net|Create a network with a specific IP range and gateway|

## 2. Container commands
???+ "Container commands"
	|command|description|Example|
	|---|---|---|
	|docker run [options] <image>|Create and start a new container|docker run -d --name myapp nginx|
	|docker ps|List running containers|docker ps|
	|docker ps -a|List all containers (including stopped)|docker ps -a|
	|docker stop <container>|Stop a running container|docker stop myapp|
	|docker start <container>|Start a stopped container|docker start myapp|
	|docker restart <container>|Restart a container|docker restart myapp|
	|docker rm <container>|Remove a container (must be stopped)|docker rm myapp|
	|docker logs <container>|Show logs of a container|docker logs myapp|
	|docker exec -it <container> <command>|Run a command inside a running container|docker exec -it myapp bash|
	|docker inspect <container>|Show detailed info about container|docker inspect myapp|
	|docker commit <container> <new_image>|Create new image from container changes|docker commit myapp myapp_image|
	|docker top <container>|Show running processes inside container|docker top myapp|
	|docker stats|Show live resource usage of containers|docker stats|
	|docker pause <container>|Pause container processes|docker pause myapp|
	|docker unpause <container>|Unpause container|docker unpause myapp|
	
### ```docker run``` command options
???+ "run command options"
	|option|description|Example|
	|---|---|---|
	|```-d```|Run container in detached (background) mode|```docker run -d nginx```|
	|```--name```|Give the container a custom name|```docker run --name web nginx```|
	|```-p <host>:<container>```|Map ports from host to container|```docker run -p 8080:80 nginx```|
	|```-v <host>:<container>```|Mount a volume (host → container)|```docker run -v /my/html:/usr/share/nginx/html nginx```|
	|```-e <key>=<value>```Set environment variables|```docker run -e MYSQL_ROOT_PASSWORD=secret mysql```|
	|```--network <network>```|Connect to a specific Docker network|```docker run --network=my_net nginx```|
	|```--rm```|Automatically remove container when it exits|```docker run --rm alpine echo "Hello"```|
	|```--it```|Run in interactive mode (tty)|```docker run -it ubuntu bash```|
	|```--restart <policy>```|Set restart policy (no, always, on-failure)|```docker run --restart=always nginx```|
	|
	
### Full ```docker run``` command options
``` bash
docker run -d \
  --name web \
  -p 8080:80 \
  -v /my/html:/usr/share/nginx/html \
  --network my_custom_net \
  nginx
```

This runs an ```nginx``` container:

- in detached mode
- named ```web```
- with port 8080 mapped to 80
- serving files from ```/my/html```
- on a custom network ```my_custom_net```


## 3. Run prebuilt images without custom source code
???+ "Run prebuilt images"
	|Image|Description|Example|
	|---|---|---|
	|nginx|High-performance HTTP server & reverse proxy|docker run -d --name web -p 8080:80 nginx|
	|redis|In-memory data structure |docker run -d --name redis -p 6379:6379 redis|
	|postgres|Open-source relational database|docker run -d --name pg -e POSTGRES_PASSWORD=secret -p 5432:5432 postgres|
	|mysql|Popular relational database system|docker run -d --name mysql -e MYSQL_ROOT_PASSWORD=secret -p 3306:3306 mysql|
	|mongo|	NoSQL document database|docker run -d --name mongo -p 27017:27017 mongo|
	|traefik|Modern reverse proxy/load balancer|docker run -d --name traefik -p 80:80 traefik (needs config)|
	|consul|Service discovery and configuration|docker run -d --name consul -p 8500:8500 consul|
	|etcd|Distributed reliable key-value store|docker run -d --name etcd quay.io/coreos/etcd|
	|vault|	Secrets and encryption management|docker run -d --name vault -p 8200:8200 vault|
	|haproxy|High performance TCP/HTTP load balancer|docker run -d --name haproxy -p 80:80 haproxy (needs config)|
	|minio/minio|S3-compatible object storage|docker run -d --name minio -p 9000:9000 -e MINIO_ACCESS_KEY=minio -e MINIO_SECRET_KEY=minio123 minio/minio server /data|
	|rabbitmq|Robust message broker supporting AMQP|docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management|
	|grafana/grafana|Analytics and monitoring dashboard|docker run -d --name grafana -p 3000:3000 grafana/grafana|
	|prom/prometheus|Monitoring & alerting toolkit|docker run -d --name prometheus -p 9090:9090 prom/prometheus|

## 4. Popular basic images for custom docker buils
???+ "Basic images"
	|Image|Description|Example|
	|---|---|---|
	|python|Python runtime (with pip)|```FROM python:3.11```|
	|node|Node.js runtime (with npm/yarn)|```FROM node:20```|
	|golang|Go compiler & runtime|Run go apps|```FROM golang:1.22```|
	|openjdk / eclipse-temurin |Java runtime & JDK|```FROM eclipse-temurin:21```|
	|gcc|GNU C/C++ compiler|```FROM gcc:13```|
	|rust|Rust compiler & cargo|```FROM rust:1.74```|
	|php|PHP runtime|```FROM php:8.3-apache```|
	|ruby|Ruby & gem environment|```FROM ruby:3.3```|
	|alpine|Lightweight Linux distro|```FROM alpine```|
	|debian|Full Linux OS base|```FROM debian:bookworm```|
	|ubuntu|Popular Linux distro base|```FROM ubuntu:24.04```|
	|busybox|Tiny Unix utilities|```FROM busybox```|
	|dotnet|.NET SDK & runtime|```FROM mcr.microsoft.com/dotnet/sdk:8.0```|
	|tensorflow/tensorflow|Python + TensorFlow|```FROM tensorflow/tensorflow:latest```|
	|pytorch/pytorch + TensorFlow|Python + PyTorch|```FROM pytorch/pytorch:latest```|
	

### How to find Base OS of a base container
Option 1:
``` bash 
docker image inspect python:3.11-slim
```

Option 2: Run a shell in the container
``` bash
docker run -it --rm python:3.11-slim bash
cat /etc/os-release
```
This will show,
``` text
PRETTY_NAME="Debian GNU/Linux 11 (bullseye)"
```



## 5. Dockerfile template
``` Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

Here, the base image (python:3.11-slim) includes:

- OS base (Debian/Alpine)
- Python interpreter
- pip

Note: In ```FROM python:3.11-slim```, you are using an image named python:3.11-slim, but it inherits from an underlying OS base — typically Debian.

