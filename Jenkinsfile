pipeline {
    agent any
    environment {
        VENV = "venv"
        FLASK_PID = ""
    }
    stages {
        stage('Clone Application Repo') {
            steps {
                git(
                    branch: 'main', 
                    credentialsId: 'github-https', 
                    url: 'https://github.com/Phani2603/Pipelining_pythonApp.git'
                )
            }
        }
        
        stage('Set Up Python Virtual Environment') {
            steps {
                sh "python3 -m venv ${VENV}"
                sh "./${VENV}/bin/pip install --upgrade pip"
                sh "./${VENV}/bin/pip install pandas numpy tensorflow flask"
            }
        }
        
        stage('Run and Test Flask App') {
            steps {
                script {
                    // Start Flask app and capture PID
                    sh """
                        ./${VENV}/bin/python app.py > server.log 2>&1 &
                        echo \$! > flask.pid
                    """
                    
                    // Wait for app to start
                    sh 'sleep 10'
                    
                    // Test the application
                    sh 'curl --fail http://localhost:5000 || (cat server.log && exit 1)'
                }
            }
            post {
                always {
                    script {
                        // Gracefully stop the Flask app
                        sh '''
                            if [ -f flask.pid ]; then
                                kill $(cat flask.pid) 2>/dev/null || true
                                rm -f flask.pid
                            fi
                            # Force kill any process on port 5000 if needed
                            pkill -f "python app.py" 2>/dev/null || true
                        '''
                    }
                }
            }
        }
    }
}
