from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>PBL CI/CD Pipeline | Jenkins + Docker + Kubernetes</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: Inter, Arial, sans-serif;
            background: #0b1020;
            color: #e8edf7;
            line-height: 1.6;
        }

        /* NAVBAR */

        nav {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(11, 16, 32, 0.92);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid #202a44;
        }

        .nav-container {
            max-width: 1200px;
            margin: auto;
            padding: 18px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 20px;
            font-weight: 800;
            color: #ffffff;
        }

        .logo span {
            color: #60a5fa;
        }

        .nav-links {
            display: flex;
            gap: 24px;
            list-style: none;
        }

        .nav-links a {
            color: #aab5ca;
            text-decoration: none;
            font-size: 14px;
            transition: 0.2s;
        }

        .nav-links a:hover {
            color: #60a5fa;
        }

        /* HERO */

        .hero {
            max-width: 1200px;
            margin: auto;
            padding: 90px 24px 70px;
            text-align: center;
        }

        .badge {
            display: inline-block;
            padding: 7px 14px;
            border: 1px solid #31558b;
            border-radius: 30px;
            color: #8ec5ff;
            background: #101d35;
            font-size: 13px;
            margin-bottom: 22px;
        }

        .hero h1 {
            font-size: clamp(38px, 6vw, 70px);
            line-height: 1.05;
            margin-bottom: 20px;
            letter-spacing: -2px;
        }

        .gradient {
            background: linear-gradient(90deg, #60a5fa, #a78bfa, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero p {
            max-width: 760px;
            margin: auto;
            color: #9da9bf;
            font-size: 18px;
        }

        .hero-buttons {
            margin-top: 30px;
            display: flex;
            justify-content: center;
            gap: 14px;
            flex-wrap: wrap;
        }

        .btn {
            padding: 12px 22px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            font-size: 14px;
        }

        .btn-primary {
            background: #3b82f6;
            color: white;
        }

        .btn-secondary {
            border: 1px solid #34415d;
            color: #dbe5f5;
        }

        /* GENERAL */

        .container {
            max-width: 1200px;
            margin: auto;
            padding: 30px 24px 80px;
        }

        .section-title {
            font-size: 30px;
            margin-bottom: 10px;
        }

        .section-subtitle {
            color: #8793aa;
            margin-bottom: 30px;
        }

        /* PIPELINE */

        .pipeline {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin-top: 35px;
        }

        .pipeline-card {
            background: #11182b;
            border: 1px solid #26324c;
            padding: 25px;
            border-radius: 14px;
            text-align: center;
            position: relative;
        }

        .pipeline-card:not(:last-child)::after {
            content: "→";
            position: absolute;
            right: -22px;
            top: 50%;
            color: #4f76ad;
            font-size: 24px;
        }

        .icon {
            font-size: 34px;
            margin-bottom: 10px;
        }

        .pipeline-card h3 {
            margin-bottom: 5px;
        }

        .pipeline-card p {
            color: #8290a9;
            font-size: 13px;
        }

        /* OVERVIEW CARDS */

        .cards {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 18px;
        }

        .card {
            background: #11182b;
            border: 1px solid #26324c;
            border-radius: 14px;
            padding: 25px;
        }

        .card h3 {
            margin-bottom: 10px;
        }

        .card p {
            color: #909bb0;
            font-size: 14px;
        }

        /* STEPS */

        .steps {
            display: grid;
            gap: 16px;
        }

        .step {
            display: grid;
            grid-template-columns: 70px 1fr;
            gap: 20px;
            background: #11182b;
            border: 1px solid #26324c;
            border-radius: 14px;
            padding: 22px;
        }

        .step-number {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            background: #172a4b;
            color: #60a5fa;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
        }

        .step h3 {
            margin-bottom: 5px;
        }

        .step p {
            color: #929db1;
            font-size: 14px;
        }

        /* CODE */

        .code {
            margin-top: 15px;
            background: #080d18;
            border: 1px solid #202b40;
            border-radius: 9px;
            padding: 16px;
            overflow-x: auto;
            color: #b9c8df;
            font-family: Consolas, monospace;
            font-size: 13px;
        }

        /* STATUS */

        .status-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 18px;
        }

        .status {
            background: #11182b;
            border: 1px solid #26324c;
            border-radius: 14px;
            padding: 25px;
        }

        .status-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }

        .green {
            color: #34d399;
        }

        .status-value {
            font-size: 27px;
            font-weight: 800;
        }

        .status-label {
            color: #8490a7;
            font-size: 13px;
        }

        /* TECHNOLOGIES */

        .tech {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .tech span {
            background: #172038;
            border: 1px solid #2a3958;
            padding: 9px 15px;
            border-radius: 20px;
            font-size: 13px;
            color: #b9c8df;
        }

        /* RESULT */

        .result {
            text-align: center;
            padding: 50px 25px;
            border: 1px solid #31558b;
            background: linear-gradient(145deg, #111d35, #10172a);
            border-radius: 18px;
        }

        .result h2 {
            font-size: 34px;
            margin-bottom: 12px;
        }

        .result p {
            color: #96a4bb;
            max-width: 650px;
            margin: auto;
        }

        .success {
            display: inline-block;
            margin-top: 22px;
            padding: 10px 18px;
            border-radius: 30px;
            background: #10372d;
            color: #4ade80;
            border: 1px solid #21634e;
            font-weight: 700;
        }

        /* FOOTER */

        footer {
            border-top: 1px solid #202a44;
            text-align: center;
            padding: 30px;
            color: #66748c;
            font-size: 13px;
        }

        /* RESPONSIVE */

        @media (max-width: 800px) {

            .nav-links {
                display: none;
            }

            .pipeline {
                grid-template-columns: 1fr;
            }

            .pipeline-card:not(:last-child)::after {
                content: "↓";
                right: 50%;
                top: auto;
                bottom: -32px;
            }

            .cards,
            .status-grid {
                grid-template-columns: 1fr;
            }

            .hero {
                padding-top: 60px;
            }

            .hero h1 {
                font-size: 42px;
            }
        }
    </style>
</head>

<body>

<!-- NAVIGATION -->

<nav>
    <div class="nav-container">
        <div class="logo">PBL<span> DevOps</span></div>

        <ul class="nav-links">
            <li><a href="#overview">Overview</a></li>
            <li><a href="#pipeline">Pipeline</a></li>
            <li><a href="#steps">Steps</a></li>
            <li><a href="#kubernetes">Kubernetes</a></li>
            <li><a href="#result">Result</a></li>
        </ul>
    </div>
</nav>


<!-- HERO -->

<section class="hero">

    <div class="badge">PBL-III • CI/CD & Cloud Native Deployment</div>

    <h1>
        CI/CD Pipeline to Deploy
        <span class="gradient">Dockerized Applications</span>
        on Kubernetes
    </h1>

    <p>
        A complete hands-on implementation using GitHub, Jenkins,
        Docker and Kubernetes to automate application build and deployment.
    </p>

    <div class="hero-buttons">
        <a href="#pipeline" class="btn btn-primary">
            Explore Pipeline
        </a>

        <a href="#steps" class="btn btn-secondary">
            View Implementation
        </a>
    </div>

</section>


<!-- OVERVIEW -->

<section id="overview" class="container">

    <h2 class="section-title">Project Overview</h2>

    <p class="section-subtitle">
        What was implemented in this PBL exercise?
    </p>

    <div class="cards">

        <div class="card">
            <h3>🎯 Objective</h3>

            <p>
                Build a CI/CD pipeline that automatically takes application
                source code from GitHub, builds a Docker image and deploys
                the containerized application to Kubernetes.
            </p>
        </div>

        <div class="card">
            <h3>⚙️ Automation</h3>

            <p>
                Jenkins is used as the automation server. A Jenkinsfile
                defines the complete pipeline including Docker build,
                Kubernetes deployment and verification.
            </p>
        </div>

        <div class="card">
            <h3>☸️ Deployment</h3>

            <p>
                Kubernetes manages two replicas of the application and
                exposes the application through a NodePort service.
            </p>
        </div>

    </div>

</section>


<!-- PIPELINE -->

<section id="pipeline" class="container">

    <h2 class="section-title">CI/CD Pipeline</h2>

    <p class="section-subtitle">
        The complete flow implemented in this project.
    </p>

    <div class="pipeline">

        <div class="pipeline-card">
            <div class="icon">🐙</div>
            <h3>GitHub</h3>
            <p>Source Code Repository</p>
        </div>

        <div class="pipeline-card">
            <div class="icon">🔨</div>
            <h3>Jenkins</h3>
            <p>CI/CD Automation</p>
        </div>

        <div class="pipeline-card">
            <div class="icon">🐳</div>
            <h3>Docker</h3>
            <p>Containerization</p>
        </div>

        <div class="pipeline-card">
            <div class="icon">☸️</div>
            <h3>Kubernetes</h3>
            <p>Container Deployment</p>
        </div>

    </div>

</section>


<!-- TECHNOLOGIES -->

<section class="container">

    <h2 class="section-title">Technologies Used</h2>

    <p class="section-subtitle">
        Tools and technologies used during implementation.
    </p>

    <div class="tech">

        <span>Python</span>
        <span>Flask</span>
        <span>Git</span>
        <span>GitHub</span>
        <span>Jenkins</span>
        <span>Docker</span>
        <span>Kubernetes</span>
        <span>Minikube</span>
        <span>kubectl</span>
        <span>PowerShell</span>
        <span>YAML</span>

    </div>

</section>


<!-- STEPS -->

<section id="steps" class="container">

    <h2 class="section-title">Implementation Steps</h2>

    <p class="section-subtitle">
        How the complete CI/CD environment was created.
    </p>

    <div class="steps">

        <div class="step">

            <div class="step-number">01</div>

            <div>
                <h3>Create the Flask Application</h3>

                <p>
                    A lightweight Flask application was created as the
                    application to be containerized and deployed.
                </p>

                <div class="code">
                    from flask import Flask<br><br>
                    app = Flask(__name__)<br><br>
                    @app.route("/")<br>
                    def home():<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;return "CI/CD Application"
                </div>

            </div>

        </div>


        <div class="step">

            <div class="step-number">02</div>

            <div>

                <h3>Dockerize the Application</h3>

                <p>
                    A Dockerfile was created to package the Flask application
                    together with Python and its dependencies.
                </p>

                <div class="code">
                    docker build -t pbl-cicd-app:latest .
                </div>

            </div>

        </div>


        <div class="step">

            <div class="step-number">03</div>

            <div>

                <h3>Test the Docker Container</h3>

                <p>
                    The Docker image was executed locally to verify that the
                    application worked correctly inside a container.
                </p>

                <div class="code">
                    docker run -d -p 5000:5000 pbl-cicd-app:latest
                </div>

            </div>

        </div>


        <div class="step">

            <div class="step-number">04</div>

            <div>

                <h3>Set Up Kubernetes</h3>

                <p>
                    Minikube was used to create a local Kubernetes cluster.
                    kubectl was used to communicate with the cluster.
                </p>

                <div class="code">
                    minikube start --driver=docker<br><br>
                    kubectl get nodes
                </div>

            </div>

        </div>


        <div class="step">

            <div class="step-number">05</div>

            <div>

                <h3>Create Kubernetes Deployment</h3>

                <p>
                    A Kubernetes Deployment was configured with two replicas
                    of the Dockerized application.
                </p>

                <div class="code">
                    kubectl apply -f k8s/deployment.yaml
                </div>

            </div>

        </div>


        <div class="step">

            <div class="step-number">06</div>

            <div>

                <h3>Create Kubernetes Service</h3>

                <p>
                    A NodePort service was configured to expose the
                    application outside the Kubernetes cluster.
                </p>

                <div class="code">
                    kubectl apply -f k8s/service.yaml
                </div>

            </div>

        </div>


        <div class="step">

            <div class="step-number">07</div>

            <div>

                <h3>Configure Jenkins</h3>

                <p>
                    Jenkins was configured as a Pipeline from SCM and linked
                    with the GitHub repository containing the Jenkinsfile.
                </p>

                <div class="code">
                    GitHub → Jenkins → Jenkinsfile
                </div>

            </div>

        </div>


        <div class="step">

            <div class="step-number">08</div>

            <div>

                <h3>Automate the Deployment</h3>

                <p>
                    The Jenkins pipeline automatically builds the Docker
                    image, applies Kubernetes manifests and verifies the
                    deployed pods and services.
                </p>

                <div class="code">
                    docker build -t pbl-cicd-app:latest .<br>
                    kubectl apply -f k8s/deployment.yaml<br>
                    kubectl apply -f k8s/service.yaml<br>
                    kubectl get pods<br>
                    kubectl get services
                </div>

            </div>

        </div>

    </div>

</section>


<!-- KUBERNETES -->

<section id="kubernetes" class="container">

    <h2 class="section-title">Kubernetes Deployment Status</h2>

    <p class="section-subtitle">
        Final deployment state observed during the successful Jenkins build.
    </p>

    <div class="status-grid">

        <div class="status">

            <div class="status-top">
                <h3>Pods</h3>
                <span class="green">● Running</span>
            </div>

            <div class="status-value">2 / 2</div>

            <div class="status-label">
                Application replicas running successfully
            </div>

        </div>


        <div class="status">

            <div class="status-top">
                <h3>Service</h3>
                <span class="green">● Active</span>
            </div>

            <div class="status-value">NodePort</div>

            <div class="status-label">
                Port 5000 → NodePort 30080
            </div>

        </div>


        <div class="status">

            <div class="status-top">
                <h3>Jenkins</h3>
                <span class="green">● Success</span>
            </div>

            <div class="status-value">SUCCESS</div>

            <div class="status-label">
                CI/CD pipeline completed successfully
            </div>

        </div>

    </div>

</section>


<!-- ARCHITECTURE -->

<section class="container">

    <h2 class="section-title">Deployment Architecture</h2>

    <p class="section-subtitle">
        How the components work together.
    </p>

    <div class="card">

        <div class="code" style="font-size:15px; line-height:2.1;">

            Developer<br>
            &nbsp;&nbsp;↓<br>
            GitHub Repository<br>
            &nbsp;&nbsp;↓<br>
            Jenkins Pipeline<br>
            &nbsp;&nbsp;↓<br>
            Docker Image: pbl-cicd-app:latest<br>
            &nbsp;&nbsp;↓<br>
            Kubernetes / Minikube<br>
            &nbsp;&nbsp;├── Pod 1<br>
            &nbsp;&nbsp;├── Pod 2<br>
            &nbsp;&nbsp;↓<br>
            Kubernetes NodePort Service<br>
            &nbsp;&nbsp;↓<br>
            Browser / User

        </div>

    </div>

</section>


<!-- JENKINS -->

<section class="container">

    <h2 class="section-title">Jenkins Pipeline Stages</h2>

    <p class="section-subtitle">
        Stages executed automatically by Jenkins.
    </p>

    <div class="cards">

        <div class="card">
            <h3>1. Checkout</h3>
            <p>
                Jenkins retrieves the latest source code from the GitHub
                repository.
            </p>
        </div>

        <div class="card">
            <h3>2. Build Docker Image</h3>
            <p>
                Jenkins executes Docker build and creates the latest
                application image.
            </p>
        </div>

        <div class="card">
            <h3>3. Deploy to Kubernetes</h3>
            <p>
                Jenkins applies the Kubernetes Deployment and Service
                manifests.
            </p>
        </div>

        <div class="card">
            <h3>4. Verify Deployment</h3>
            <p>
                Jenkins checks the running pods and Kubernetes services to
                confirm successful deployment.
            </p>
        </div>

        <div class="card">
            <h3>5. Post Action</h3>
            <p>
                Jenkins reports whether the complete CI/CD pipeline finished
                successfully or failed.
            </p>
        </div>

        <div class="card">
            <h3>6. Automated Delivery</h3>
            <p>
                Source code changes can trigger the same automated build and
                deployment workflow.
            </p>
        </div>

    </div>

</section>


<!-- RESULT -->

<section id="result" class="container">

    <div class="result">

        <h2>🚀 CI/CD Pipeline Successfully Deployed</h2>

        <p>
            The application was successfully containerized with Docker,
            automated using Jenkins and deployed with two replicas on
            Kubernetes using Minikube.
        </p>

        <div class="success">
            ✓ PIPELINE STATUS: SUCCESS
        </div>

    </div>

</section>


<!-- FOOTER -->

<footer>

    PBL-III • CI/CD Pipeline Implementation<br>
    Docker + Jenkins + Kubernetes

</footer>


</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)