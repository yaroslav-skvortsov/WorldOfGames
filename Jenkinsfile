pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout from GitHub repository
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/yaroslav-skvortsov/WorldOfGames.git']]])
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build('skvyaroslav/worldofgames:latest')
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    docker.image('skvyaroslav/worldofgames:latest').run('-p 8777:80 -v $PWD/Scores.txt:/Scores.txt')
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    try {
                        sh 'python3 tests/e2e.py'
                    } catch (Exception e) {
                        error "Tests failed"
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh 'docker stop $(docker ps -q --filter ancestor=skvyaroslav/worldofgames:latest)'
                    sh 'docker push skvyaroslav/worldofgames:latest'
                }
            }
        }
    }
}