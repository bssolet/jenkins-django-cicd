
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Preparation') {
            steps {
                echo 'Starting Django CI Pipeline'
                echo "Job: ${env.JOB_NAME}"
                echo "Build number: ${env.BUILD_NUMBER}"
            }
        }

        stage('Verify Execution Environment') {
            steps {
                sh '''
                    set -e

                    echo "Current user:"
                    whoami

                    echo "Operating system:"
                    uname -s

                    echo "Current directory:"
                    pwd
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution finished'
        }

        success {
            echo 'Pipeline completed successfully'
        }

        failure {
            echo 'Pipeline failed'
        }
    }
}
