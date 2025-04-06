pipeline {
    agent any

environment {
    PATH = "${env.PATH};C:\\Program Files\\Docker\\Docker\\resources\\bin"
}

    stages {
        stage('Build') {
            steps {
                bat'docker build -t worldofgames .'
            }
        }

        stage('Run') {
            steps {
                bat 'docker run -d -p 8777:5000 --name worldofgames_container -v $PWD/Scores.txt:/Scores.txt WorldOfGames'
            }
        }

        stage('Test') {
            steps {
                bat'python3 e2e.py'
            }
        }

        stage('Finalize') {
            steps {
                bat'docker stop worldofgames_container'
                bat'docker rm worldofgames_container'
                bat'docker tag WorldOfGames chaib5/worldofgames:latest'
                bat'docker push chaib5/worldofgames:latest'
            }
        }
    }
}

