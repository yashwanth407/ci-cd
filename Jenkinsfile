pipeline {
    agent any

    environment {
        VENV = "venv"
        PYTHON_VERSION = "python3"
        JENKINS_ADMIN = "true"
    }

    options {
        timeout(time: 10, unit: 'MINUTES')
        retry(2)
    }

    stages {
        stage('Clone GitHub Repo') {
            steps {
                // IMPORTANT: Replace yashwanth407 with your actual GitHub username
                // Example: https://github.com/johndoe/Pipelining_pythonApp.git
                git branch: 'main', 
                    credentialsId: 'github-https', 
                    url: 'https://github.com/yashwanth407/Pipelining_pythonApp.git'
            }
        }

        stage('Set Up Python Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/python -m pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                    # Test if the app can be imported
                    ./venv/bin/python -c "import app; print('App import successful')"
                    
                    # Test if model can be loaded
                    ./venv/bin/python -c "from model import train_model; model = train_model(); print('Model loaded successfully')"
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                script {
                    // Start the Flask app in background
                    sh './venv/bin/python app.py &'
                    
                    // Wait a moment for the app to start
                    sleep 5
                    
                    // Test if the app is responding
                    sh 'curl -f http://localhost:5001 || exit 1'
                    
                    echo "Flask application is running successfully on port 5001"
                }
            }
        }
    }

    post {
        always {
            // Clean up background processes
            sh 'pkill -f "python.*app.py" || true'
            echo "Pipeline completed"
        }
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed. Check the logs for details."
        }
    }
}
