pipeline {
    agent any

    environment {
        // Selenoid настройки
        SELENOID_URL = 'ru.selenoid.autotests.cloud/wd/hub'
        SELENOID_USER = 'user1'
        SELENOID_PASSWORD = '1234'

        // Тестовые данные
        BASE_URL = 'https://demoqa.com'
        API_BASE_URL = 'https://reqres.in/api'
        BROWSER = 'chrome'
        BROWSER_VERSION = '128.0'
        WINDOW_SIZE = '1920,1080'
        TIMEOUT = '30'

        // Telegram уведомления (через Jenkins credentials)
        TELEGRAM_TOKEN = credentials('telegram-token')
        TELEGRAM_CHAT_ID = credentials('telegram-chat-id')
    }

    tools {
        python 'Python-3.12'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo '✅ Код склонирован'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    python -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
                echo '✅ Виртуальное окружение настроено'
            }
        }

        stage('Run All Tests') {
            steps {
                sh '''
                    . .venv/bin/activate
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
            script {
                def duration = currentBuild.durationString
                sendTelegramNotification(
                    "✅ JOB SUCCESSFUL\n" +
                    "📦 Проект: ${env.JOB_NAME}\n" +
                    "🔢 Номер сборки: ${env.BUILD_NUMBER}\n" +
                    "🕐 Длительность: ${duration}\n" +
                    "📊 Статус: Все тесты прошли успешно!\n" +
                    "🔗 Отчёт Allure: ${env.BUILD_URL}allure/"
                )
            }
        }
        failure {
            script {
                def duration = currentBuild.durationString
                sendTelegramNotification(
                    "❌ JOB FAILED\n" +
                    "📦 Проект: ${env.JOB_NAME}\n" +
                    "🔢 Номер сборки: ${env.BUILD_NUMBER}\n" +
                    "🕐 Длительность: ${duration}\n" +
                    "📊 Статус: Тесты упали\n" +
                    "🔗 Ссылка: ${env.BUILD_URL}"
                )
            }
        }
        always {
            echo '🏁 Сборка завершена'
        }
    }
}

def sendTelegramNotification(String message) {
    sh """
        curl -s -X POST https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage \
        -d chat_id=${TELEGRAM_CHAT_ID} \
        -d text="${message}"
    """
}