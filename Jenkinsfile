pipeline {
    agent any

    environment {
        // Spécifie le chemin absolu directement dans le Jenkinsfile
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
                // Utilise un chemin absolu pour le fichier dans Docker run
                bat 'docker run -d -p 8777:5000 --name test_wog_container -v "C:/Users/chaib/WorldOfGames/Scores.txt:/Scores.txt" worldofgames'
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
            bat 'docker stop test_wog_container || exit 0'
            bat 'docker rm test_wog_container || exit 0'
        }
    }
}
