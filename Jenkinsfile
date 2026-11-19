// Кейс 5: многоэтапный пайплайн Jenkins — lint, юнит-тесты, сборка, развертывание
pipeline {
    agent any

    triggers {
        // Jenkins работает локально, вебхук GitHub до него не достучится,
        // поэтому проверяем репозиторий на новые коммиты каждые 2 минуты
        pollSCM('H/2 * * * *')
    }

    environment {
        IMAGE = "ci-cd-practice:${env.BUILD_NUMBER}"
        APP_CONTAINER = 'ci-cd-practice-staging'
        APP_PORT = '5001'
    }

    stages {
        stage('Install') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -q -r requirements-dev.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '. .venv/bin/activate && flake8 .'
            }
        }

        stage('Unit tests') {
            steps {
                sh '. .venv/bin/activate && pytest -v'
            }
        }

        stage('Build') {
            steps {
                sh '. .venv/bin/activate && python -m build'
                sh 'docker build -t $IMAGE .'
                archiveArtifacts artifacts: 'dist/*', fingerprint: true
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f $APP_CONTAINER || true
                    docker run -d --name $APP_CONTAINER -p $APP_PORT:5000 \
                        -e APP_VERSION=build-$BUILD_NUMBER $IMAGE
                    for i in $(seq 1 15); do
                        if curl -fsS http://host.docker.internal:$APP_PORT/health; then
                            echo; echo "Deployed: http://localhost:$APP_PORT"; exit 0
                        fi
                        sleep 2
                    done
                    echo "Health check failed"; exit 1
                '''
            }
        }
    }

    post {
        success { echo 'Pipeline finished successfully' }
        failure { echo 'Pipeline failed' }
    }
}
