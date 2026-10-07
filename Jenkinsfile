pipeline {
    agent any

    environment {
        IMAGE_NAME = "healthcare-devsecops"
        IMAGE_TAG = "v1"

        KUBECONFIG = "C:\\Users\\shrek\\.kube\\config"
        MINIKUBE_HOME = "C:\\Users\\shrek\\.minikube"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out healthcare DevSecOps project...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building healthcare application Docker image...'

                bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
            }
        }

        stage('Security Scan') {
            steps {
                echo 'Scanning Docker image for vulnerabilities using Trivy...'

                bat 'trivy image --severity HIGH,CRITICAL %IMAGE_NAME%:%IMAGE_TAG%'
            }
        }

        stage('Load Image into Minikube') {
            steps {
                echo 'Loading secure image into Minikube...'

                bat 'minikube image load %IMAGE_NAME%:%IMAGE_TAG%'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying healthcare application to Kubernetes...'

                bat 'kubectl apply -f k8s/deployment.yaml'
                bat 'kubectl apply -f k8s/service.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Verifying healthcare deployment...'

                bat 'kubectl rollout status deployment/healthcare-app --timeout=120s'
                bat 'kubectl get pods'
                bat 'kubectl get service healthcare-service'
            }
        }
    }

    post {
        success {
            echo 'DevSecOps pipeline completed successfully!'
        }

        failure {
            echo 'DevSecOps pipeline failed!'
        }
    }
}