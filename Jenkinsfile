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
  }
}

