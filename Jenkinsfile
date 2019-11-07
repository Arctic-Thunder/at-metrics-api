pipeline {
  agent any
  stages {
    stage('Install Dependencies') {
      steps {
        echo 'Installing Dependencies'
        sh '''apt update 


&& apt install python3 python3-pip virtualenv libpq-dev



'''
      }
    }

  }
}