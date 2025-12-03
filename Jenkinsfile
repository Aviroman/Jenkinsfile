pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME="amitksunbeam/python-test-app"
        DOCKER_USER_NAME="amitksunbeam"
        DOCKER_AUTH_TOKEN=credentials('DOCKER_AUTH_TOKEN')
    }

    stages {
        stage('build docker image') {
            steps {
                sh 'docker image build -t ${DOCKER_IMAGE_NAME} .'
            }
        }

        stage('docker login') {
            steps {
                sh 'echo ${DOCKER_AUTH_TOKEN} | docker login -u ${DOCKER_USER_NAME} --password-stdin'
            }
        }

        stage('push docker image') {
            steps {
                sh 'docker image push ${DOCKER_IMAGE_NAME}'
            }
        }

        stage('restart service') {
            steps {
                sh 'docker service update --force --image ${DOCKER_IMAGE_NAME} python-app'
            }
        }
    }
}
