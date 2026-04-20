pipeline {
    agent {
        label 'python3'
    }

    environment {
        SELENOID_URL = 'ru.selenoid.autotests.cloud/wd/hub'
        SELENOID_USER = 'user1'
        SELENOID_PASSWORD = '1234'
        BASE_URL = 'https://demoqa.com'
        API_BASE_URL = 'https://reqres.in/api'
        BROWSER = 'chrome'
        BROWSER_VERSION = '128.0'
        WINDOW_SIZE = '1920,1080'
        TIMEOUT = '30'
        TELEGRAM_TOKEN = credentials('telegram-token')
        TELEGRAM_CHAT_ID = credentials('telegram-chat-id')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo '✅ Код склонирован'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
                echo '✅ Зависимости установлены'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    pytest --alluredir=allure-results -v
                '''
            }
            post {
                always {
                    allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
                }
            }
        }
    }

    post {
        success {
            sh """
                curl -s -X POST https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage \
                -d chat_id=${TELEGRAM_CHAT_ID} \
                -d text="✅ Тесты прошли успешно!%0AПроект: ${JOB_NAME}%0AСборка: ${BUILD_NUMBER}"
            """
        }
        failure {
            sh """
                curl -s -X POST https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage \
                -d chat_id=${TELEGRAM_CHAT_ID} \
                -d text="❌ Тесты упали!%0AПроект: ${JOB_NAME}%0AСборка: ${BUILD_NUMBER}%0AСсылка: ${BUILD_URL}"
            """
        }
    }
}