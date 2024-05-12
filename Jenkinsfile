pipeline {
    environment {
        registry = "liseon/python-jenkins"
        registryCredential = 'a8d55a13-bff7-4cb5-bb3c-7e718787f9fc'
        dockerImage = ''
    }
    agent any
    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '612cdbf6-7518-4129-ae40-cc188484a2bc', url: 'https://github.com/Liseon617/flask-pytest-docker-jenkins.git']])
            }
        }
        stage('Stop previous running container') {
            steps {
                sh returnStatus: true, script: 'docker stop $(docker ps -a | grep ${JOB_NAME} | awk \'{print $1}\')'
                sh returnStatus: true, script: 'docker rmi $(docker images | grep ${registry} | awk \'{print $3}\') --force'
                sh returnStatus: true, script: 'docker rm ${JOB_NAME}'
            }
        }
        stage('Build Image') {
            steps {
                script {
                    img = registry + ":${env.BUILD_ID}"
                    println ("${img}")
                    dockerImage = docker.build("${img}")
                }
            }
        }
        stage('Test - Run Docker Container on Jenkins') {
            steps {
                sh label: '', script: "docker run -d --name ${JOB_NAME} -p 5000:5000 ${img}"
            }
        }
        stage('Run Pytest in Docker Container') {
            steps {
                sh 'docker-compose -f docker-compose.yaml up --abort-on-container-exit --exit-code-from test'
            }
        }
        stage('Push To DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
