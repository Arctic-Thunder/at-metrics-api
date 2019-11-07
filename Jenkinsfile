pipeline {
  agent any
  stages {
    stage('Push to Heroku') {
      steps {
        echo 'Pushing to Heroku'
        git(url: 'https://git.heroku.com/at-metrics-api-stage.git', branch: 'master')
      }
    }

  }
}