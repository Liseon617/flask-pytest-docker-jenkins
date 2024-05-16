pipeline {
    environment {
        registry = "liseon/python-jenkins"
        registryCredential = 'docker-creds'
        dockerImage = ''
    }
    agent any
    triggers {
        pollSCM 'H */2 * * *'
    }
    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github_credentials_personal', url: 'https://github.com/Liseon617/flask-pytest-docker-jenkins.git']])
            }
        }
        
        stage('Stop previous running container') {
            steps {
                sh returnStatus: true, script: 'docker stop $(docker ps -a | grep ${JOB_NAME} | awk \'{print $1}\')'
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

        stage('Run Pytest in Docker Container') {
            steps {
                script {
                    sh "docker-compose -f docker-compose.yaml up --abort-on-container-exit --exit-code-from test"
                } 
            }
        }

        stage("Publish Coverage Results") {
            steps {
                cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'coverage*.xml', conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
            }
        }

        // stage("Deploy") {
        //     steps {
        //         // copy content to deployment directory
        //         // sh 'cp * /var/www/html'
        //     }
        // }
    }
}
