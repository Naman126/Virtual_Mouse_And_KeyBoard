# Virtual Mouse and Keyboard Using Hand Gestures

A computer vision project that allows users to control their computer's mouse and keyboard using hand gestures captured through a webcam. The project uses Python, OpenCV, and MediaPipe to detect hand landmarks and translate gestures into computer actions.

## Features

- Virtual mouse movement using the index finger.
- Left-click, right-click, and double-click gestures.
- Virtual keyboard controlled by finger movements.
- Screenshot capture using hand gestures.
- Real-time hand tracking and visual feedback.

## Technologies Used

- **Python** — Core programming language.
- **OpenCV** — Webcam access and image processing.
- **MediaPipe** — Real-time hand landmark detection.
- **NumPy** — Mathematical calculations.
- **PyAutoGUI and pynput** — Mouse and keyboard automation.

## Project Structure

- `hand.py`, `track.py` — Original gesture-control application.
- `app.py` — Web status page and health endpoint for deployment verification.
- `tests/` — Automated tests.
- `Dockerfile` — Defines the container image.
- `Jenkinsfile` — Defines the CI/CD pipeline.
- `k8s/deployment.yaml` — Kubernetes Deployment configuration.
- `k8s/service.yaml` — Kubernetes Service configuration.

## Run the Original Application

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the desktop dependencies:

```bash
python -m pip install -r requirements-desktop.txt
```

Run the gesture-control application:

```bash
python hand.py
```

A working webcam and the appropriate camera and accessibility permissions are required. The original application uses desktop GUI and input-control features.

## CI/CD Deployment Using Jenkins, Docker and Kubernetes

This repository also includes a CI/CD deployment demonstration for the project.

### Pipeline Workflow

1. Jenkins checks out the latest code from GitHub.
2. Python syntax checks and automated tests run.
3. Docker builds a container image.
4. Jenkins pushes the image to Docker Hub using stored Jenkins credentials.
5. Kubernetes Deployment and Service manifests are applied to Minikube.
6. Jenkins checks deployment rollout and application health.

### Prerequisites

- A GitHub repository containing this project.
- Jenkins with Pipeline, Git and Credentials Binding plugins.
- Docker Engine or Docker Desktop.
- A Docker Hub repository.
- `kubectl` and Minikube configured for the deployment environment.
- Python 3 and the project dependencies.

### Docker Hub Configuration

The Docker Hub repository used for this demonstration is:

`namanagarwal123/virtual-mouse-keyboard`

In Jenkins, create a **Username with password** credential with the ID:

`dockerhub-creds`

Use your Docker Hub username and a Docker Hub access token as the password. Never commit access tokens or other secrets to GitHub.

If using a different Docker Hub account, update `DOCKERHUB_REPO` in the `Jenkinsfile` and the image reference in `k8s/deployment.yaml`.

### Configure the Jenkins Pipeline

1. Create a Jenkins Pipeline job.
2. Select **Pipeline script from SCM**.
3. Choose Git and enter your GitHub repository URL.
4. Set the branch to `*/main`.
5. Set the script path to `Jenkinsfile`.
6. Ensure the Jenkins execution environment has Docker, `kubectl`, and access to the intended Kubernetes cluster.

**Important:** Jenkins must have a valid kubeconfig and network access to the Kubernetes API. A Minikube cluster running on a Mac is not automatically accessible to Jenkins running on an AWS EC2 instance. Configure the deployment environment before running the deployment stage.

### Verify the Deployment

After a successful pipeline run, use the same Kubernetes context that Jenkins uses:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
kubectl rollout status deployment/virtual-mouse-keyboard
```

To open the application locally when using Minikube:

```bash
minikube service virtual-mouse-keyboard --url
```

Open the URL returned by the command. The `/health` endpoint reports the web service status.

### Demonstrate a Second Deployment

After the first successful pipeline run:

1. Change a visible message in `app.py`.
2. Commit and push the change to GitHub.
3. Run the Jenkins pipeline again.
4. Verify the updated image, Kubernetes rollout, and changed page.

Example commands:

```bash
git add app.py
git commit -m "Update deployment status page"
git push origin main
```

Capture screenshots of the Jenkins stages, Docker Hub image, Kubernetes resources, and updated page for the assignment report.

## Deployment Limitation

The Kubernetes deployment runs the web status and health-check application; it does **not** remotely operate the host computer's webcam, mouse, or keyboard. The original interactive gesture-control application remains available through `python hand.py` on a supported desktop.

## Future Improvements

- Add more keyboard keys and special characters.
- Improve gesture accuracy and reduce accidental clicks.
- Add adjustable sensitivity and customizable gestures.
- Support additional gestures and multi-hand interactions.
- Develop a graphical settings interface.

## Academic Project

Developed as an academic project focused on computer vision, human-computer interaction, gesture-based automation, and CI/CD deployment.

## License

No license has been specified. Add an appropriate open-source license if you intend to permit others to reuse or modify this project.