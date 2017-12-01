pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh '''
                    COMPOSE_FLAGS="-f ${WORKSPACE}/ex2/apache/docker-compose.yml -p apache"

                    sudo docker-compose ${COMPOSE_FLAGS} stop
                    sudo docker-compose ${COMPOSE_FLAGS} rm --force -v

                    sudo docker-compose ${COMPOSE_FLAGS} build --no-cache
                    sudo docker-compose ${COMPOSE_FLAGS} up -d

                    sudo docker-compose ${COMPOSE_FLAGS} exec -T apache /app/tests.py
                    error=$?
                    sudo docker-compose ${COMPOSE_FLAGS} stop
                    sudo docker-compose ${COMPOSE_FLAGS} rm --force -v

                    if [[ $error != 0 ]]; then
                        echo "Problem testing, killing the container and exiting"
                        exit -1
                    fi

                    # Restart the container again. Here we'd deploy somewhere else.
                    sudo docker-compose ${COMPOSE_FLAGS} build --no-cache
                    sudo docker-compose ${COMPOSE_FLAGS} up -d

                    sudo docker image prune -f
                '''
            }
        }
    }
    post {
        success {
            sh 'echo Success!!!!!!!!!!!'
        }
        failure {
            sh 'echo Failure to build!'
            sh ''' 
                    COMPOSE_FLAGS="-f ${WORKSPACE}/ex2/apache/docker-compose.yml -p apache"
                    # Stop the container, it had some problems
                    sudo docker-compose ${COMPOSE_FLAGS} stop
                    sudo docker-compose ${COMPOSE_FLAGS} rm --force -v
                    sudo docker image prune -f
            '''
        }
    }
}
