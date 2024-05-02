pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage("checkout") {
            steps {
                echo 'checking out the application...'
                checkout scmGit(branches: [[name: '*/main'], [name: '*/dev']], extensions: [], userRemoteConfigs: [[credentialsId: '35aebad0-dc13-47a1-a6ae-025d5d402529', url: 'https://github.com/Liseon617/flask-pytest-docker-jenkins.git']])
            }
        }

        stage("build") {
            steps {
                echo 'building the application...'
                git branch: 'main', credentialsId: '35aebad0-dc13-47a1-a6ae-025d5d402529', url: 'https://github.com/Liseon617/flask-pytest-docker-jenkins.git'
                sh 'python3 -m venv venv' // Create a virtual environment
                sh 'source venv/bin/activate' // Activate the virtual environment
                sh 'pip install -r requirements.txt' // Install requirements within the virtual environment
                sh 'python3 main.py'
                script {
                    def test = 2 + 2 > 3 ? 'cool' : 'not cool'
                    echo test
                }
            }
        }

        stage("test") {
            steps {
                echo 'testing the application...'
            }
        }

        stage("deploy") {
            steps {
                echo 'deploying the application...'
            }
        }
    }
}
