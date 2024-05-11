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

        stage("build") {
            steps {
                echo 'Building the application...'
                sh 'pip3 install -r requirements.txt'
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
