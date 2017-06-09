pipeline {
  agent any
  stages {
    stage('SayAWord') {
      steps {
        echo 'Meh'
      }
    }
    stage('Printing dir') {
      steps {
        sh 'pwd'
      }
    }
    stage('Last one') {
      steps {
        sleep 5
      }
    }
  }
}