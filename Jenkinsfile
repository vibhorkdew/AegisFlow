pipeline {

    agent any

    stages {

        stage('Build Docker Image') {

            steps {

                sh 'docker build -t aegisflow-aegisflow .'

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