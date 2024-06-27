pipeline {
    environment {
        REMOTE_SERVER = credentials('brian-vlsdemo-vm-ip')
    }
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs:
                                [[credentialsId: 'hiverlab-dillonloh', url: 'git@github.com/Hiverlab-Brian/flask_docker_jenkins_example.git']])
            }
        }

        stage('Build') {
            steps {
                withCredentials([file(credentialsId: 'auto-datahandler-env', variable: 'SECRET_ENV_FILE')]) {
                    script {
                        // Read the secret file and write its contents to .env file
                        sh 'cat $SECRET_ENV_FILE > .env'
                        
                        script {
                            def containers = sh(script: 'docker ps -a | grep ${JOB_NAME} | awk \'{print $1}\'', returnStdout: true).trim()
                            if (containers) {
                                sh "docker stop ${containers} || true"
                                sh "docker rm ${containers} || true"
                            }
                        }

                        // Ensure docker-compose.yml is present
                        if (!fileExists('docker-compose.yml')) {
                            error "docker-compose.yml not found"
                        }
                        sh "docker compose -f docker-compose.yaml up --abort-on-container-exit --exit-code-from test"
                    }
                }
            }
        }

        stage("Test") {
            steps {
                junit keepProperties: true, skipMarkingBuildUnstable: true, stdioRetention: '', testResults: 'xmlReport/output.xml'
                cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'coverage.xml', 
                conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', 
                maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying to test/test-application @ vlsdemo, /home/dillon/test/test-application"
                withCredentials([
                    sshUserPrivateKey(credentialsId: 'vlsdemo-ssh-key', keyFileVariable: 'SSH_KEY'),
                    file(credentialsId: 'auto-datahandler-env', variable: 'SECRET_ENV_FILE'),
                    file(credentialsId: 'brian-vlsdemo-vm-ip', variable: 'REMOTE_SERVER'),
                    ]) {
                    sshagent(['hiverlab-dillonloh']) {
                        sh '''
                            ssh dillon@$REMOTE_SERVER "
                            if [ ! -d "/home/dillon/test/test-application/.git" ]; then
                                git clone git@github.com/Hiverlab-Brian/flask_docker_jenkins_example.git /home/dillon/test/test-application;
                            fi &&
                            cd /home/dillon/test/test-application/ && 
                            git pull origin main && 

                            cat ${SECRET_ENV_FILE} > .env &&

                            docker-compose down && 
                            docker-compose up -d --build"
                        '''
                    }
               }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            echo 'Pipeline completed.'
        }
    }
}
