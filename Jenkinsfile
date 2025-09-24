pipeline {
    agent any
    environment {
        VENV = "venv"
    }
    stages {
        stage('Clone Application Repo') {
            steps {
                // Clones the application code into the current workspace
                git branch: 'main', credentialsId: 'github-https', 
                url: 'https://github.com/Phani2603/Pipelining_pythonApp.git' [cite: 1]
            }
        }
        stage('Set Up Python Virtual Environment') {
            steps {
                // Create and activate a Python virtual environment
                sh 'python3 -m venv ${VENV}' [cite: 2]
                // Upgrade pip and install dependencies
                sh """
                ./${VENV}/bin/pip install --upgrade pip
                ./${VENV}/bin/pip install pandas numpy tensorflow flask
                """ [cite: 3]
            }
        }
        stage('Run and Test Flask App') {
            steps {
                script {
                    // Start the Flask app in the background
                    // The 'nohup' command and '&' make sure the process doesn't terminate when the shell exits
                    sh 'nohup ./${VENV}/bin/python app.py > server.log 2>&1 &'

                    // Wait for a few seconds to ensure the server is up and running
                    sh 'sleep 5'

                    // Use curl to test if the server is accessible
                    // This command will fail the stage if the server doesn't respond
                    sh 'curl --fail http://localhost:5000'

                    // Find and kill the process to clean up
                    sh 'kill $(lsof -t -i:5000)'
                }
            }
        }
    }
}
