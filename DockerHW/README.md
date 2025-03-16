### Docker Assignment (8%)

- **Objective:**  
  Run the webpage from the `DockerHW` directory using Docker Compose.

- **Instructions & Steps:**  
  1. **Dockerfile Creation:**  
     - Write a complete `Dockerfile` that builds the image for the webpage.
  2. **Docker Compose Setup:**  
     - Create a `docker-compose.yml` file to define and run the container.
  3. **Local Verification:**  
     - Run `docker-compose up` in the `DockerHW` directory to verify that the container is created successfully.
  4. **change code file everything to run command:**
    docker-compose up --build -d

- **Submission Requirements:**  
  Once the container runs locally, push both the `Dockerfile` and `docker-compose.yml` to your repository. CI testing will verify their correctness.