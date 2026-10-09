
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out Django source code from GitHub'

                checkout scm

                echo 'Verifying checked-out repository files'

                sh '''
                    set -e

                    echo "Current workspace:"
                    pwd

                    echo "Repository files:"
                    ls -la

                    echo "Checking required Django files"

                    test -f manage.py
                    test -f requirements.txt
                    test -f core/tests.py
                    test -f config/settings.py

                    echo "All required Django files are present"
                '''
            }
        }

        stage('Verify Execution Environment') {
            steps {
                echo 'Checking Jenkins execution environment'

                sh '''
                    set -e

                    echo "Current user:"
                    whoami

                    echo "Operating system:"
                    uname -s

                    echo "Jenkins job:"
                    echo "$JOB_NAME"

                    echo "Build number:"
                    echo "$BUILD_NUMBER"
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
