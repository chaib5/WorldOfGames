pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t WorldOfGames .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:5000 --name worldofgames_container -v $PWD/Scores.txt:/Scores.txt WorldOfGames'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 e2e.py'
            }
        }

        stage('Finalize') {
            steps {
                sh 'docker stop worldofgames_container'
                sh 'docker rm worldofgames_container'
                sh 'docker tag WorldOfGames chaib5/worldofgames:latest'
                sh 'docker push chaib5/worldofgames:latest'
            }
        }
    }
}
