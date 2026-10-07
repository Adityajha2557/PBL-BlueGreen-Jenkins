pipeline {
    agent any

    environment {
        IMAGE_NAME = "pbl-cicd-app"
        IMAGE_TAG = "v2"
        KUBECONFIG = "C:\\Users\\shrek\\.kube\\config"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out Blue-Green project...'
                checkout scm
            }
        }

        stage('Build Green Image') {
            steps {
                echo 'Building Docker V2 image...'
                bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
            }
        }

        stage('Load Green Image') {
            steps {
                echo 'Loading V2 image into Minikube...'
                bat 'minikube image load %IMAGE_NAME%:%IMAGE_TAG%'
            }
        }

        stage('Deploy Green') {
            steps {
                echo 'Deploying GREEN version...'
                bat 'kubectl apply -f k8s/green-deployment.yaml'
            }
        }

        stage('Verify Green') {
            steps {
                echo 'Waiting for GREEN deployment...'
                bat 'kubectl rollout status deployment/pbl-green --timeout=120s'
                bat 'kubectl get pods -l version=green'
            }
        }

        stage('Switch Traffic to Green') {
            steps {
                echo 'Switching traffic from BLUE to GREEN...'
                bat 'kubectl apply -f k8s/service.yaml'
            }
        }

        stage('Verify Service') {
            steps {
                echo 'Verifying Blue-Green service...'
                bat 'kubectl get service pbl-bluegreen-service'
                bat 'kubectl get pods --show-labels'
            }
        }
    }

    post {
        success {
            echo 'Blue-Green deployment completed successfully!'
        }

        failure {
            echo 'Blue-Green deployment failed!'
        }
    }
}