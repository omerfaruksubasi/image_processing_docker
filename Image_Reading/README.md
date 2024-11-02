# Image Reading and Processing with Docker

This project demonstrates a simple image processing task using Docker, Python, and OpenCV. The code reads an image, converts it to grayscale, displays the result, and saves the processed image. This guide will help you set up and run the project step-by-step.

---

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your system
- Basic command line knowledge

---

## Steps to Set Up and Run the Project

### Step 1: Create the Dockerfile

A Dockerfile is a configuration file that sets up the environment for your application. It tells Docker what base image to use, installs dependencies, and specifies how to run the app.

1. In your project directory, create a file named `Dockerfile` and add the following code:

   ```dockerfile
   # Use a Python 3.8 base image
   FROM python:3.8-slim

   # Set the working directory inside the container
   WORKDIR /app

   # Install necessary dependencies for OpenCV
   RUN apt-get update && apt-get install -y \
       python3-opencv \
       libgl1-mesa-glx \
       libglib2.0-0 libsm6 libxrender1 libxext6 \
       && rm -rf /var/lib/apt/lists/*

   # Copy the requirements file and install Python dependencies
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   # Copy the Python script into the container
   COPY app.py .

   # Set the default command to run the application
   CMD ["python", "app.py"]

#### Explanation of Each Command in Dockerfile:

- **FROM python:3.8-slim**: Starts with a lightweight Python 3.8 image.
- **WORKDIR /app**: Sets the working directory inside the container to `/app`.
- **RUN apt-get update...**: Installs OpenCV and necessary libraries.
- **COPY requirements.txt .**: Copies `requirements.txt` into the container.
- **RUN pip install...**: Installs Python dependencies specified in `requirements.txt`.
- **COPY app.py .**: Copies your main Python script (`app.py`) to the container.
- **CMD ["python", "app.py"]**: Runs `app.py` when the container starts.

### Step 2: Create `requirements.txt` 
In the same directory, create a `requirements.txt` file. This file lists the Python packages required for your project.

```plaintext
opencv-python-headless
```

This will install OpenCV when Docker builds the image.

### Step 3: Create the Python Script `app.py`
Create a file named `app.py` with the following code. This script reads an image, converts it to grayscale, displays both the original and grayscale images, and saves the grayscale image.

```bash
import cv2

# Load the image
image = cv2.imread('input.jpg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the original and grayscale images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray_image)

    # Save the grayscale image
    cv2.imwrite('output.jpg', gray_image)
    print("Grayscale image saved as 'output.jpg'")

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

### Step 4: Add an Input Image 
Place an image named `lenna.jpg` in the project directory. This will be the image the script processes.

## Building and Running the Docker Container

### Step 1: Build the Docker Image
Now that your Dockerfile and code files are ready, you can build the Docker image. Run this command in the project directory:
```bash
docker build -t image-processing .

```
- **`-t image-processing`**: Tags the image as `image-processing`.
- **`.`**: Refers to the current directory containing the Dockerfile.

### Step 2: Run the Docker Container

Run the container with the following command:

```bash
docker run --rm -v "$(pwd)":/app image-processing
```
- **`--rm`**: Automatically removes the container after it runs.
- **`-v "$(pwd)":/app`**: Mounts the current directory to the `/app` directory in the container. This allows the container to access `input.jpg` and save `output.jpg`.
- **`image-processing`**: The name of the Docker image we built.

After running, you’ll see `output.jpg` in the project directory—this is the grayscale version of your input image.









