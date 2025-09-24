pipeline {
    agent any
    environment {
        VENV = "venv"
    }
    stages {
        stage('Clone Application Repo') {
            steps {
                git branch: 'main', credentialsId: 'github-https', url: 'https://github.com/your-username/Pipelining_pythonApp.git'
            }
        }
        stage('Set Up Python Virtual Environment') {
            steps {
                sh 'python3 -m venv ${VENV}'
                sh './${VENV}/bin/python -m pip install --upgrade pip'
                sh './${VENV}/bin/pip install -r requirements.txt'
            }
        }
        stage('Run and Test Flask App') {
            steps {
                script {
                    // Start the Flask app in the background
                    sh 'nohup ./${VENV}/bin/python app.py > server.log 2>&1 &'

                    // Wait for a few seconds to ensure the server is up and running
                    sh 'sleep 5'

                    // Use curl to perform a health check
                    sh 'curl --fail http://localhost:5000'

                    // Find and kill the process to clean up
                    sh 'kill $(lsof -t -i:5000)'
                }
            }
        }
    }
}
