pipeline {
  agent any
  environment {
    PATH = "/Users/jajulayashwanth/.pyenv/shims:/Users/jajulayashwanth/.pyenv/bin:${env.PATH}"
  }
  stages {
    stage('Set Up Python Virtual Environment') {
      steps {
        sh '''
          python -m venv venv
          source venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }
    stage('Run Flask App') {
      steps {
        sh '''
          source venv/bin/activate
          # Use curl to get the external IP address of the Jenkins server
          IP_ADDRESS=$(curl -s ifconfig.me)
          # Now, use the variable to print the dynamic URL
          echo "Flask app is running at http://${IP_ADDRESS}:5000"
          # Start the Flask app, binding it to all interfaces (0.0.0.0)
          nohup python app.py run --host=0.0.0.0 > app.log 2>&1 &
        '''
      }
    }
  }
