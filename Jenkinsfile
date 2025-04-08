pipeline {
    agent any

    environment {
        SCORE_FILE = "/c/Users/chaib/WorldOfGames/Scores.txt"
    }

    stages {
        stage('Build') {
            steps {
                bat 'docker build -t worldofgames .'
            }
        }

        stage('Run') {
            steps {
                // Stop + Remove existing container if it exists
                bat 'docker stop test_wog_container || exit 0'
                bat 'docker rm test_wog_container || exit 0'

                // Run new container
                bat 'docker run -d -p 8777:5000 --name test_wog_container -v "%SCORE_FILE%":/Scores.txt worldofgames'
            }
        }

        stage('Test') {
            steps {
                bat 'timeout /t 5 > NUL'  // Laisse à Flask le temps de démarrer
                bat 'curl http://localhost:8777'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat 'docker stop test_wog_container || exit 0'
            bat 'docker rm test_wog_container || exit 0'
        }
    }
}
