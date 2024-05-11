pipeline {
    agent any
    triggers {
        pollSCM 'H */2 * * *'
    }
    stages {
        stage("checkout") {
            steps {
                echo 'Checking out the application...'
                git branch: 'main', credentialsId: '743a5bc4-53c9-44f1-a813-3049691463ac', url: 'https://github.com/Liseon617/flask-pytest-docker-jenkins.git'
            }
        }

        stage("build") {
            steps {
                echo 'Building the application...'
                sh 'python3 main.py' // Install requirements within the virtual environment
            }
        }

        stage("test") {
            steps {
                echo 'Testing the application...'
                sh 'python3 -m pytest ./tests'
            }
        }

        stage("deploy") {
            steps {
                echo 'Deploying the application...'
            }
        }
    }
}
