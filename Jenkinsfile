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
          nohup python app.py > app.log 2>&1 &
          echo "Flask app is running at http://<your-jenkins-ip>:5000"
        '''
      }
    }
  }
}

