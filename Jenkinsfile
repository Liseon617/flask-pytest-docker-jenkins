pipeline {
    agent {
    docker {
        label 'docker'
        image 'python:3.10'
        }
    }
    triggers {
        pollSCM 'H */2 * * *'
    }
    stages {
        stage("checkout") {
            steps {
                echo 'checking out the application...'
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '743a5bc4-53c9-44f1-a813-3049691463ac', url: 'https://github.com/Liseon617/flask-pytest-docker-jenkins.git']])
            }
        }

        stage("build") {
            steps {
                echo 'building the application...'
                git branch: 'main', credentialsId: '743a5bc4-53c9-44f1-a813-3049691463ac', url: 'https://github.com/Liseon617/flask-pytest-docker-jenkins.git'
                sh 'pip install -r requirements.txt' // Install requirements within the virtual environment
            }
        }

        stage("test") {
            steps {
                echo 'testing the application...'
                sh 'python3 -m pytest ./tests'
            }
        }

        stage("deploy") {
            steps {
                echo 'deploying the application...'
            }
        }
    }
}
