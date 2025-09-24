 pipeline {
    agent any
    stages {
        stage('Set Up Python Virtual Environment') {
            steps {
                // Use 'sh' instead of 'bat' for Linux/macOS
                sh '''
                   python3 -m venv venv
                   source venv/bin/activate
                   pip install -r requirements.txt
                '''
            }
        }
        stage('Run Flask App') {
            steps {
                sh '''
                   source venv/bin/activate
                   python app.py
                '''
            }
        }
    }
}


