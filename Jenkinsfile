// Declarative Jenkins Pipeline for devops-demo
// Works on both Linux (sh) and Windows (bat) Jenkins agents.
// >>> Replace gauriidhondge with your GitHub username before pushing <<<

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/gauriidhondge/devops-demo.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
                script {
                    if (isUnix()) {
                        sh 'ls -la'
                        sh 'python3 app.py'
                    } else {
                        bat 'dir'
                        bat 'python app.py'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                script {
                    if (isUnix()) {
                        sh 'python3 -m unittest discover -s tests -v'
                    } else {
                        bat 'python -m unittest discover -s tests -v'
                    }
                }
            }
        }
    }

    post {
        success { echo 'Pipeline completed successfully: code checked out, built and tested.' }
        failure { echo 'Pipeline failed. Check the Console Output for details.' }
    }
}
