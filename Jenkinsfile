
pipeline {
    agent any
    environment {
        // docker image name
        DOCKER_IMAGE_NAME="amitksunbeam/python-test-app"

        // docker user name
        DOCKER_USER_NAME="amitksunbeam"
    }

    stages {
        stage('scm') {
            steps {
                echo "already taken care by Jenkins"
            }
        }

        stage('prepare env') {
            steps {
                // execute a shell command
                sh 'pip3 install --break-system-package -r requirements.txt '
            }
        }

        stage('test the application') {
            steps {
                sh 'pytest test_app.py'
            }
        }

        stage('prepare docker image') {
            steps {
                sh 'echo $DOCKER_IMAGE_NAME'
                sh 'echo $DOCKER_USER_NAME'
                // sh 'docker image build -t ${DOCKER_IMAGE_NAME} .'
            }
        }

        stage('docker login') {
            steps {
                // sh 'docker login -u '
            }
        }
    }
}
