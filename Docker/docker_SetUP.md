# 1. Create a Dockerfile for Your NestJS App
The first step is to create a Dockerfile that specifies how to build your NestJS app into a Docker container. Here's a sample Dockerfile for a NestJS app:

Dockerfile

```
  # Use an official Node.js runtime as a parent image
  FROM node:18 AS build
  
  # Set the working directory inside the container
  WORKDIR /app
  
  # Copy package.json and package-lock.json
  COPY package*.json ./
  
  # Install dependencies
  RUN npm install
  
  # Copy the rest of the app's source code
  COPY . .
  
  # Build the NestJS app
  RUN npm run build
  
  # Expose the port the app will run on
  EXPOSE 3000
  
  # Command to run the app
  CMD ["npm", "run", "start:prod"]
```
# 2. Create .dockerignore File
Next, you should add a .dockerignore file to prevent unnecessary files from being copied into the Docker image. Here's a basic .dockerignore for a NestJS project:

```
node_modules
dist
*.log
.git
```
# 3. Build Your Docker Image
Navigate to your NestJS project’s root directory in your terminal, and then run the following Docker command to build the image:
```
docker build -t my-nestjs-app .
```
Replace my-nestjs-app with a name you prefer for your Docker image.

# 4. Test Your Docker Image Locally
Once the image is built, you can run it locally with the following command:
```
docker run -p 3000:3000 my-nestjs-app
```
This tells Docker to map port 3000 inside the container to port 3000 on your local machine. You can visit your app at http://localhost:3000 on your browser.

# 5. Push Your Docker Image to a Public Repository (Docker Hub)
To push your Docker image to a public repository like Docker Hub, you need to first log in to Docker Hub (or any other container registry you're using):
```
docker login
```
Then, tag your Docker image with your Docker Hub username and repository name. For example:
```
docker tag my-nestjs-app yourusername/my-nestjs-app:latest
```

Now, push the image to your public repository:

```
docker push yourusername/my-nestjs-app:latest
```
This will upload your Docker image to Docker Hub.

# 6. Run Your Docker Image Locally (after pushing)
Once the image is pushed to the repository, you can pull it to any other machine (or re-pull it on your local machine) and run it.

First, pull the image:
```
docker pull yourusername/my-nestjs-app:latest
```
Then, run it:

```
docker run -p 3000:3000 yourusername/my-nestjs-app:latest
```

# 7. Accessing the Application
Now, you can access your app by visiting http://localhost:3000.

Summary of Commands:
Build Docker image:
```
docker build -t my-nestjs-app .
```
Run Docker container locally:

```
docker run -p 3000:3000 my-nestjs-app
```
Login to Docker Hub:

```
docker login
```
Tag image:

```
docker tag my-nestjs-app yourusername/my-nestjs-app:latest
```
Push image to Docker Hub:

```
docker push yourusername/my-nestjs-app:latest
```
Pull image from Docker Hub (on any machine):
```
docker pull yourusername/my-nestjs-app:latest
```
Run pulled image locally:

```
docker run -p 3000:3000 yourusername/my-nestjs-app:latest
```
That’s it! Let me know if you need any further clarification.
