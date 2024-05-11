pipeline {
    agent any
    triggers {
        pollSCM 'H */2 * * *'
    }
    stages {
        stage("checkout") {
            steps {
                echo 'Checking out the application...'
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '3af2009d-e30c-4a0a-afaf-97914a2062c4', url: 'https://github.com/Liseon617/flask-pytest-docker-jenkins.git']])
            }
        }

        stage('Build') {
            agent {
                docker { image 'python:3.8-buster' }
            }
            steps {
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
