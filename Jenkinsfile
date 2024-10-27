pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Use the SCM configuration set in Jenkins
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image for Django project
                    bat "docker build -t recipe-app:%BUILD_NUMBER% ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Remove existing container if it exists
                    bat "docker rm -f recipe-app-conntainer || echo 'No existing container to remove.'"
                    // Run the Docker container with the new image
                    bat "docker run -d --name recipe-app-container -p 8000:8000 recipe-app:%BUILD_NUMBER%"
                }
            }
        }
    }

    post {
        success {
            echo "Build and deployment successful!"
        }
        failure {
            echo "Build failed. Check logs for details."
        }
    }
}
