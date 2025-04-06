pipeline {
    agent any
    environment {
        DOCKER_PATH = 'C:\\Program Files\\Docker\\Docker\\resources\\bin;%PATH%'
    }
    stages {
        stage('Build') {
            steps {
                withEnv(["PATH=env.DOCKER_PATH"]) 
                    bat 'docker build -t worldofgames .'
                
        stage('Run') 
            steps 
                withEnv(["PATH={env.DOCKER_PATH}"]) {
                    bat 'docker run -d -p 8777:5000 --name worldofgames_container -v %cd%\\Scores.txt:/Scores.txt worldofgames'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Tests go here'
            }
        }
    }
}