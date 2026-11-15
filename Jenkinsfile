pipeline {
    agent any

    triggers {
        pollSCM('H/5 * * * *')
    }

    environment {
        HEADLESS = 'true'
        // Повний шлях до Python (служба Jenkins не бачить PATH користувача)
        PY = 'C:\\Users\\Pathetic_Box\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
        PYTHONUTF8 = '1'
        PATH = "C:\\Windows\\System32;C:\\Windows;C:\\Windows\\System32\\WindowsPowerShell\\v1.0;${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ВАШ_ЛОГІН/ВАШ_РЕПО.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PY%" -m venv venv'
                bat 'venv\\Scripts\\python -m pip install -r requirements.txt flake8'
            }
        }

        stage('Lint') {
            steps {
                bat 'venv\\Scripts\\python -m flake8 --max-line-length=120 conftest.py pages tests utils'
            }
        }

        stage('Run UI Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat 'venv\\Scripts\\python -m pytest'
                }
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'reports/allure-results']]
        }
    }
}
