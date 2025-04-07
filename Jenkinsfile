pipeline {
    agent any

    environment {
        SCORE_FILE = "C:/Users/chaib/WorldOfGames/Scores.txt"
    }

    stages {
        stage('Build') {
            steps {
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