
pipeline {
    agent {
        label 'python'
    }

    options {
        skipDefaultCheckout(true)
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out Django source code'

                checkout scm

                sh '''
                    set -eu

                    test -f manage.py
                    test -f requirements.txt
                    test -f core/tests.py
                    test -f config/settings.py

                    echo "Django source files verified"
                    git rev-parse --short HEAD
                '''
            }
        }

        stage('Verify Python') {
            steps {
                sh '''
                    set -eu

                    echo "Execution user:"
                    whoami

                    echo "Python version:"
                    python --version

                    echo "Workspace:"
                    pwd
                '''
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                    set -eu

                    python -m venv .venv

                    .venv/bin/python --version
                    .venv/bin/python -m pip --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    set -eu

                    .venv/bin/python -m pip install -r requirements.txt

                    .venv/bin/python -m pip check
                '''
            }
        }

        stage('Django System Checks') {
            steps {
                sh '''
                    set -eu

                    .venv/bin/python manage.py check
                '''
            }
        }

        stage('Django Automated Tests') {
            steps {
                sh '''
                    set -eu

                    .venv/bin/python manage.py test -v 2
                '''
            }
        }
    }

    post {
        always {
            echo 'Django CI pipeline execution finished'
        }

        success {
            echo 'Django CI pipeline completed successfully'
        }

        failure {
            echo 'Django CI pipeline failed'
        }
    }
}
