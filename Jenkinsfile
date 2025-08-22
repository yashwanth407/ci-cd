pipeline {
    agent any
    environment {
        VENV = "venv"
    }
    stages {
        stage('Clone GitHub Repo') {
            steps {
                git branch: 'main', credentialsId: 'github-https', 
                url: 'https://github.com/Phani2603/Pipelining_pythonApp.git'
            }
        }
        stage('Set Up Python Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/python -m pip install --upgrade pip'
                sh './venv/bin/pip install pandas numpy tensorflow flask'
            }
        }
        stage('Run Flask App') {
            steps {
                sh './venv/bin/python app.py'
            }
        }
    }
}

