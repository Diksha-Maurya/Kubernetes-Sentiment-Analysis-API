# Kubernetes Sentiment Analysis API

[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-blue?style=for-the-badge)](https://huggingface.co/)

A hands-on project that demonstrates the end-to-end process of deploying a Python Flask API for sentiment analysis using a pre-trained Hugging Face model, containerized with Docker, and managed by Kubernetes.

This repository is a log of the development journey, including setup, deployment, debugging of common real-world errors, and scaling an ML model as a resilient, high-availability service.

---

## Project Architecture

This project follows a standard cloud-native microservice pattern:

```
User -> curl (API Request) -> NodePort -> Kubernetes Service -> Kubernetes Pod (Flask App + ML Model)
```
* The **Service** acts as a stable load balancer and entry point.
* The **Deployment** manages multiple replica **Pods** for scalability and resilience.
* Each **Pod** runs the Docker container with the Flask application, which performs model **inference**.

---

## Key Concepts and Learnings

This project served as a practical exercise in a wide range of modern software engineering and MLOps practices.

### Kubernetes & DevOps
* **Declarative Infrastructure:** Using `YAML` files (`Deployment`, `Service`) to define the desired state of the application.
* **Container Orchestration:** Managing the entire lifecycle of a containerized application automatically.
* **High Availability & Self-Healing:** Using a `Deployment` with multiple replicas to ensure the application automatically recovers from crashes.
* **Zero-Downtime Deployments:** Performing rolling updates to release new versions of the application without service interruption.
* **Service Discovery & Load Balancing:** Using a `Service` to provide a stable network endpoint for a set of ephemeral pods.

### MLOps (Machine Learning Operations)
* **Model Serving:** Deploying a trained ML model as a live, scalable API.
* **Inference Endpoint:** Creating a `/analyze` endpoint to perform real-time predictions using the model.
* **Containerizing ML Workloads:** Packaging a complex ML application with its heavy dependencies (`transformers`, `torch`) into a portable Docker image.
* **Domain Mismatch Analysis:** Discovering and understanding why a pre-trained model (trained on movie reviews) might perform poorly on out-of-domain data (technical sentences).

---

## Technology Stack

* **Language:** Python 3.9
* **Web Framework:** Flask
* **ML/AI Libraries:** Hugging Face `transformers`, PyTorch
* **Containerization:** Docker
* **Orchestration:** Kubernetes (via Docker Desktop)
* **API Testing:** curl

---

## Getting Started

### Prerequisites

* Docker Desktop installed and running.
* Kubernetes enabled within Docker Desktop's settings.
* `kubectl` command-line tool installed and configured.

### How to Run

1.  **Clone the repository:**
    ```bash
    git clone [URL_OF_YOUR_REPO]
    cd [REPO_NAME]
    ```

2.  **Build the Docker image:**
    ```bash
    docker build -t ml-api:v1 .
    ```

3.  **Deploy to Kubernetes:**
    ```bash
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    ```

4.  **Verify the deployment:**
    Wait for the pods to start (this can take a minute as the image is large). Check that the pods are `Running` and `1/1` ready.
    ```bash
    kubectl get pods
    ```

---

## API Usage

To test the API, find the `NodePort` assigned to the service by running `kubectl get service sentiment-api-service`. Then, use `curl` to send a `POST` request.

**Example Request:**

```bash
# Replace [YOUR_NODE_PORT] with the port from the 'get service' command
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"text": "Kubernetes is a powerful and essential tool for modern software."}' \
  http://localhost:[YOUR_NODE_PORT]/analyze
```

**Example Success Response:**

```json
[
  {
    "label": "POSITIVE",
    "score": 0.99988
  }
]
```

---

## License

This project is licensed under the MIT License.
