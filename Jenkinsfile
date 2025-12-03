
pipeline {
    agent any
    environment {
        // docker image name
        DOCKER_IMAGE_NAME="avii9172951423/python-test-app"

        // docker user name
        DOCKER_USER_NAME="avii9172951423"
    }

    stages {
        stage('scm') {
            steps {
                echo "already taken care by Jenkins"
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
                sh 'docker image build -t ${DOCKER_IMAGE_NAME} .'
            }
        }
    }
}
