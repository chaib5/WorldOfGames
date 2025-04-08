pipeline {
    agent any

    environment {
        PATH = "C:\\Program Files\\Docker\\Docker\\resources\\bin;${env.PATH}"
        SCORE_FILE = "C:/Users/chaib/WorldOfGames/Scores.txt"
    }

    stages {
        stage('Build') {
            steps {
                bat 'where docker'
                bat 'docker build -t worldofgames .'
            }
        }

        stage('Run') {
            steps {
                bat 'docker run -d -p 8777:5000 --name worldofgames_container -v "%SCORE_FILE%":/Scores.txt worldofgames'
            }
        }

        stage('Test') {
            steps {
                bat 'curl http://localhost:8777'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat 'docker stop worldofgames_container || exit 0'
            bat 'docker rm worldofgames_container || exit 0'
        }
    }
}
