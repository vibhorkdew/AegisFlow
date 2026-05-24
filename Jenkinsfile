pipeline {

    agent any

    stages {

        stage('Build Docker Image') {

            steps {

                sh 'docker build -t aegisflow-aegisflow .'

            }
        }

        stage('Bandit Security Scan') {

            steps {

                sh 'python3 -m bandit -r . || true'

            }
        }

        stage('Dependency Vulnerability Scan') {

            steps {

                sh 'python3 -m pip_audit || true'

            }
        }

        stage('Deploy Container') {

            steps {

                sh 'docker rm -f aegisflow_container || true'

                sh 'docker run -d --name aegisflow_container -p 7000:7000 aegisflow-aegisflow'

            }
        }

    }

}
