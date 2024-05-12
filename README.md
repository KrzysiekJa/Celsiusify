# Celsiusify

### DevOps (MLOps) benchmark project

### *(DEMO Readme)*

**DevOps** (Development and Operations) work on tasks that bridge the gap between software development and IT operations teams.

## Step 1. Backend Web Application

**Project Initialization**:

* A new directory is created for the project, and within it, a Python virtual environment is set up.
* FastAPI and Uvicorn are installed using pip to facilitate the creation of the web app.

**API Endpoint Development**:

* A FastAPI application is developed, featuring an endpoint designed to convert temperatures from Fahrenheit to Celsius.
* The TensorFlow model (`saved_model.pb`) is integrated into the app to handle temperature conversion.

**App Initialization and Identification**:

* During the initialization phase of the FastAPI app, a unique identifier is generated, which persists throughout the application's runtime.

## Step 2. Docker Image

**Dockerfile Composition**:

* A Dockerfile is authored to encapsulate the FastAPI application within a Docker image.
* This Dockerfile includes instructions for installing dependencies, copying necessary files, and exposing the required port.

**Build and Verification**:

* Locally, the Docker image is constructed and validated to ensure proper functionality and adherence to expectations.

## Step 3. Helm Chart for FastAPI

**Chart Structure Setup**:

* A directory structure is established for the Helm chart, incorporating essential templates and values files.

**Configuration of Deployment and Service**:

* Configuration files for deployment (`deployment.yaml`) and service (`service.yaml`) are tailored to meet the app's requirements.
* Auto-scaling based on CPU usage metrics is implemented to dynamically adjust app replicas.

## Step 4. Locust for Performance Testing

**Locust Dockerization**:

* A Dockerfile is crafted to define the Locust testing environment and scenarios.

**Helm Chart for Locust Deployment**:

* A Helm chart is created to streamline the deployment of Locust on Kubernetes, facilitating efficient testing.

**Execution of Performance Tests**:

* The Locust Helm chart is deployed, initiating performance tests against the FastAPI application.

## Step 5. CI Pipeline implementation

**Pipeline Configuration**:

* A CI pipeline is established utilizing tools like GitHub Actions or Jenkins.
* Stages within the pipeline are configured to encompass linting, testing, Docker image building, Docker Hub pushing, and Helm chart syntax validation.

## Step 6. TensorFlow Model with TensorFlow Serving

**TensorFlow Serving Docker Image Creation**:

* A Dockerfile is authored to bundle TensorFlow Serving alongside the TensorFlow model files.

**Helm Chart Adjustment**:

* The Helm chart is updated to facilitate the deployment of the TensorFlow Serving image.

**Performance Testing Incorporation**:

* The performance tests conducted with Locust are replicated with the TensorFlow Serving deployment to gauge its efficiency.

## Step 7. Statistics Files and Report

**Evaluation of Performance Metrics**:

* Performance metrics obtained from testing are meticulously analyzed to discern trends and patterns.

**`results` Folder Establishment**:

* Within the repository, a designated `results` folder is established to house statistical files in CSV format.
* A concise report, comparing the performance of the FastAPI solution against TensorFlow Serving, is meticulously crafted.
* This report is transformed into a PDF format and uploaded to the `results` folder within the repository for easy access and reference.
