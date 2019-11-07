pipeline {
  agent any
  stages {
    stage('Install Dependencies') {
      steps {
        echo 'Installing Dependencies'
        sh '''sudo apt update && sudo apt install python3 python3-pip virtualenv libpq-dev



'''
      }
    }

  }
}