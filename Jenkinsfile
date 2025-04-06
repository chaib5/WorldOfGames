pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "worldofgames"
        CONTAINER_NAME = "worldofgames_container"
        HOST_SCORE_PATH = "C:\\Users\\chaib\\.jenkins\\workspace\\WorldOfGames\\Scores.txt"
        CONTAINER_SCORE_PATH = "/Scores.txt"
    }

    stages {
        stage('Build') {
            steps {
                bat "docker build -t %DOCKER_IMAGE% ."
            }
        }

        stage('Run') {
            steps {
                bat "docker run -d -p 8777:5000 --name %CONTAINER_NAME% -v \"%HOST_SCORE_PATH%\":\"%CONTAINER_SCORE_PATH%\" %DOCKER_IMAGE%"
            }
        }

        stage('Test') {
            steps {
                echo 'Tests would go here'
            }
        }

        stage('Finalize') {
            steps {
                echo 'Pipeline completed'
            }
        }
    }

    post {
        always {
            bat "docker stop %CONTAINER_NAME% || exit 0"
            bat "docker rm %CONTAINER_NAME% || exit 0"
        }
    }
}
