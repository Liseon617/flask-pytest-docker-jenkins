pipeline {
    environment {
        registry = "liseon/python-jenkins" //To push an image to Docker Hub, you must first name your local image using your Docker Hub username and the repository name that you created through Docker Hub on the web.
        registryCredential = 'a8d55a13-bff7-4cb5-bb3c-7e718787f9fc'
        dockerImage = ''
    }
    agent any
    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '612cdbf6-7518-4129-ae40-cc188484a2bc', url: 'https://github.com/Liseon617/flask-pytest-docker-jenkins.giti']])
            }
        }
        stage ('Stop previous running container'){
            steps{
                sh returnStatus: true, script: 'docker stop $(docker ps -a | grep ${JOB_NAME} | awk \'{print $1}\')'
                sh returnStatus: true, script: 'docker rmi $(docker images | grep ${registry} | awk \'{print $3}\') --force' //this will delete all images
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
                sh script: "docker exec ${JOB_NAME} python -m pytest"
            }
        }
        stage('Push To DockerHub') {
            steps {
                script {
                    docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
        /*stage('Deploy to Test Server') {
            steps {
                script {
                    def stopcontainer = "docker stop ${JOB_NAME}"
                    def delcontName = "docker rm ${JOB_NAME}"
                    def delimages = 'docker image prune -a --force'
                    def drun = "docker run -d --name ${JOB_NAME} -p 5000:5000 ${img}"
                    println "${drun}"
                    sshagent(['docker-test']) {
                        sh returnStatus: true, script: "ssh -o StrictHostKeyChecking=no docker@192.168.1.16 ${stopcontainer} "
                        sh returnStatus: true, script: "ssh -o StrictHostKeyChecking=no docker@192.168.1.16 ${delcontName}"
                        sh returnStatus: true, script: "ssh -o StrictHostKeyChecking=no docker@192.168.1.16 ${delimages}"

                    // some block
                        sh "ssh -o StrictHostKeyChecking=no docker@192.168.1.16 ${drun}"
                    }
                }
            }
        }*/
    }
}