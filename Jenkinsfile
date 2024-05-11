pipeline {
    agent {
        docker {
            image 'python:3.10.4-slim'
            args '-u root' // This allows running commands as root user
        }
    }
    triggers {
        pollSCM 'H */2 * * *'
    }
    stages {
        stage("checkout") {
            steps {
                echo 'Checking out the application...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'python -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing the application...'
                sh 'source venv/bin/activate && python3 -m pytest'
            }
        }
        // Add other stages as needed
        stage("deploy") {
            steps {
                echo 'Deploying the application...'
            }
        }
    }
}
