pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {
        stage('Clone GitHub Repo') {
            steps {
                git branch: 'main', credentialsId: 'github-https', url: 'https://github.com/your-username/Pipelining_pythonApp.git'
            }
        }

        stage('Set Up Python Virtual Environment') {
            steps {
                bat '"C:\\Users\\your-username\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m venv %VENV%'
                bat '%VENV%\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '%VENV%\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                // Run Flask app binding to all interfaces, in a separate process (optional: use start /B)
                bat 'start /B %VENV%\\Scripts\\python.exe app.py'
            }
        }
    }
}
