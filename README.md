# Image Processing With Docker
<img src="docker.webp" alt="Docker Image" width="300">

## What is Docker?

Docker is an open-source platform used to develop, deploy, and run applications quickly and reliably. Docker creates lightweight, portable packages called **containers** that allow applications to run independently of their environment. Containers include all dependencies, libraries, and files needed for the application to run. This way, an application can operate consistently on any system using the same container.

## Core Components of Docker

Docker consists of several key components that allow it to create, manage, and run containers efficiently. Here’s an overview of each:

---

### 1. Docker Engine
Docker Engine is the core service that enables the creation, execution, and management of Docker containers. It consists of two primary parts:
   - **Docker Daemon**: A background service that builds, runs, and manages Docker containers.
   - **Docker CLI (Command Line Interface)**: A command-line tool that allows users to interact with the Docker Daemon, enabling tasks like building images and managing containers.

---

### 2. Docker Images
A Docker image is a lightweight, standalone, and executable software package that includes everything needed to run a specific application, such as code, libraries, and dependencies. Images are the templates from which Docker containers are launched. Docker images are typically stored and shared through container registries, such as Docker Hub.

#### Key Commands:
   - `docker pull <image_name>`: Download an image from a registry.
   - `docker build -t <image_name> .`: Build an image from a Dockerfile.

---

### 3. Docker Containers
A Docker container is a runnable instance of a Docker image. Containers are isolated environments where applications run independently. Each container shares the host operating system’s kernel but maintains its own filesystem, network, and process space.

#### Key Commands:
   - `docker run <image_name>`: Create and start a container from an image.
   - `docker stop <container_name>`: Stop a running container.
   - `docker ps`: List all running containers.

---

### 4. Dockerfile
A Dockerfile is a text document that contains all the commands required to assemble an image. It provides instructions on setting up the environment for your application, installing dependencies, and configuring the application to run within a container.

#### Example Dockerfile:
```dockerfile
# Start with a base image
FROM python:3.8

# Set working directory
WORKDIR /app

# Copy files and install dependencies
COPY . .
RUN pip install -r requirements.txt

# Command to run the application
CMD ["python", "app.py"]

```

## Why We Use Docker

- **Consistent Environments**  
  Docker containers include all dependencies needed to run an application, ensuring it operates the same way on any system and eliminating "it works on my machine" issues.

- **Resource Efficiency**  
  Containers share the host OS kernel, making them lighter than VMs. This allows more containers to run on the same hardware, saving resources and boosting performance.

- **Rapid Deployment**  
  Docker packages applications with all dependencies into a single container, enabling quick and reliable deployment across different environments (development, testing, production).

- **Application Isolation**  
  Each container runs independently, allowing multiple applications on the same host without interference—ideal for microservices.

- **Easy Scalability**  
  Docker makes scaling easy by allowing you to adjust container instances as needed, while orchestration tools (like Kubernetes) simplify managing and scaling large deployments.

- **CI/CD Compatibility**  
  Docker integrates well with CI/CD pipelines, enabling reliable automated testing and deployment through consistent environments.

- **Portability**  
  Containers can run on any system with Docker, allowing easy transitions between local environments, cloud providers, and on-premises servers.

## Docker Installation Guide

This guide provides step-by-step instructions to install Docker on both Linux and Windows operating systems.

---

### Installation on Linux

### Step 1: Update Package Index
Begin by updating the package index on your Linux system:

```bash
sudo apt update
```

### Step 2: Install Required Packages
Install the necessary packages to allow apt to use repositories over HTTPS:
```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
### Step 3: Add Docker’s Official GPG Key
Add Docker’s official GPG key for verifying packages:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

### Step 4: Add Docker Repository
Add the Docker repository to your system’s repository list:
```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### Step 5: Install Docker Engine
Update the package index again and install Docker:
```bash
sudo apt update
sudo apt install docker-ce
```

### Step 6: Verify Installation
To confirm Docker is installed correctly, run:
```bash
sudo docker --version
```
**You should see the installed Docker version. If you are using a different operating system, please refer to the [official Docker website](https://docs.docker.com/get-started/get-docker/) for specific installation instructions.**

## Image Processing Projects

### Image Reading Project
- **Description**: This project reads and displays images using OpenCV.
- **Code**: [Image Reading Project File](Image_Reading)

---

### People Detection Project
- **Description**: Detects people in images or video streams using YOLOv8.
- **Code**: [People Detection Project Code](path/to/people_detection_code.py)
