pipeline {
    agent any
    environment {
        PATH = 'C:\\Program Files\\Docker\\Docker\\resources\\bin;%PATH%'
    }
    stages {
        stage('Build') {
            steps {
                bat 'docker build -t worldofgames .'
            }
        }
        stage('Run') {
            steps {
                bat 'docker run -d -p 8777:5000 --name worldofgames_container -v %cd%\\Scores.txt:/Scores.txt worldofgames'
            }
        }
        stage('Test') {
            steps {
                echo 'Tests go here'
            }
        }
    }
}

