pipeline {
    agent any
    environment {
        VENV = "venv"
    }
    stages {
        stage('Clone Application Repo') {
            steps {
                // Correct way to clone the repo
                git(
                    branch: 'main', 
                    credentialsId: 'github-https', 
                    url: 'https://github.com/Phani2603/Pipelining_pythonApp.git'
                )
            }
        }
        stage('Set Up Python Virtual Environment') {
            steps {
                // Use double quotes for string interpolation
                sh "python3 -m venv ${VENV}"
                sh "./${VENV}/bin/pip install --upgrade pip"
                sh "./${VENV}/bin/pip install pandas numpy tensorflow flask"
            }
        }
        stage('Run and Test Flask App') {
            steps {
                script {
                    sh 'nohup ./${VENV}/bin/python app.py > server.log 2>&1 &'
                    sh 'sleep 5'
                    sh 'curl --fail http://localhost:5000'
                    // Correct way to kill the process to avoid Groovy Sandbox errors
                    sh 'kill $(lsof -t -i:5000)'
                }
            }
        }
    }
}
