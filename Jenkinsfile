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
          # Start the Flask app, binding it only to the local machine (127.0.0.1)
          nohup python app.py run --host=127.0.0.1 > app.log 2>&1 &
        '''
      }
    }
  }
}
