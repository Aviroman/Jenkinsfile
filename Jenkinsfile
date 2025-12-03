pipeline {
    agent any

    stages {
        stage('scm') {
            steps {
                echo "already taken care by jenkins"
            }
        }

        stage('prepare the environment') {
            steps {
                sh 'pip3 install --break-system-package -r requirements'
            }
        }

        stage('test the application') {
            steps {
                sh 'pytest test_app.py'
            }
        }

    }
}