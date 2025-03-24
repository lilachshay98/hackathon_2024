In this directory you can find the data for both tasks presented in the hackathon. 

It includes the training data, and also the test data that you are expected to submit your predictions on.

  # Hackathon 2024 - Optimizing public Transportation

This project is a containerized application using Docker and Docker Compose to build and run an Nginx server and a test application. 
The test application is specifically designed to test the functionality of the Nginx server. The application is deployed using GitHub Actions and 
Docker Hub/GitHub Container Registry for the container images.

## Technologies Used

* Docker - For containerizing the application
* Docker Compose - For managing multi-container applications
* Docker Hub - For storing and managing public Docker images (used in the test and nginx containers).
* GitHub Actions - For continuous integration and deployment
* Nginx - As the web server
* GitHub Container Registry (GHCR) - For storing and managing Docker images

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Docker installed on your machine
* Docker Compose installed on your machine

### Getting Started

1. Clone the Repository
   
Clone this repository to your local machine using the following command:

  ```
  git clone https://github.com/lilachshay98/f5-assignment.git
  ```

2. Set up the Docker Images
   
The project already includes Docker images for the Nginx server and Test application in GitHub Container Registry. However, you can build them locally if needed:
  
  ```
  docker build -t ghcr.io/lilachshay98/nginx:2 ./nginx
  docker build -t ghcr.io/lilachshay98/test:2 ./test
  ```

3. Configuration Files

   * nginx.conf: The Nginx configuration file is located in the nginx/ directory. This file configures the Nginx server for proper operation.
   * requirements.txt: The requirements.txt file under the test/ directory contains the dependencies needed for the test application.
   * The test.py file is a Python script that sends HTTP requests to the Nginx server and verifies that it responds correctly. The test script is responsible for confirming that the Nginx server is functioning properly.


4. Start the Apllication with Docker Compose:

   Run the following command to start the containers using Docker Compose:

  ```
  docker-compose up -d
  ```


5. Verify the Nginx Server and Test Results

  * The Nginx server will be running on the ports:
    8080 
    8081 
    You can access the server by visiting http://localhost:8080 and http://localhost:8081 in your browser.

  * The Test application will run a series of tests against the Nginx server to ensure that it is functioning correctly. The results will be saved in the ./output directory and will be published to an artifact.


6. Stopping the Application

   To stop the application, run:
   
  ```
  docker-compose down
  ```

## Acknowledgments

* Docker and Docker Compose for containerization and orchestration.
* GitHub Actions for CI/CD automation.
* Nginx for serving the web application.


