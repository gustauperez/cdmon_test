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
                    errorVar=$?

					# Before stopping the container, push it to the docker hub repo (or somewhere else). Here we'd push
					# it to our private repo and deploy it using that repo. For the sake of simplicity
					# I'll deploy using the same build process (pulling the base image from the Apache
					# project) 

                    echo "!!!!!!!!!! error: ${errorVar}"
                    if [ "${errorVar}" = "0" ]; then
                        
                        IMAGE_ID=$(docker ps | grep "httpd:latest" | sort -k 4 | cut -f 1  -d " ")
                        HASH=$(git rev-parse --short HEAD)

                        echo sudo docker login -u gustauperez -p cdmon_test

                        sudo docker login -u gustauperez -p cdmon_test

                        sudo docker tag httpd:latest gustauperez/cdmon_test:${HASH}
                        sudo docker tag httpd:latest gustauperez/cdmon_test:newest

                        sudo docker push gustauperez/cdmon_test:${HASH}
                        sudo docker push gustauperez/cdmon_test:newest

                        # Remove the tags

                        sudo docker rmi gustauperez/httpd:${HASH}
                        sudo docker rmi gustauperez/httpd:newest
                    else    
                        echo "Error was 1"
                    fi    

                    sudo docker-compose ${COMPOSE_FLAGS} stop
                    sudo docker-compose ${COMPOSE_FLAGS} rm --force -v

                    if [ "$error" = "0" ]; then
                        echo "Problem testing, killing the container and exiting"
                        exit -1
                    fi

                    # Restart the container again. Here we'd deploy somewhere else.
                    sudo docker-compose ${COMPOSE_FLAGS} build --no-cache
                    sudo docker-compose ${COMPOSE_FLAGS} up -d

                    sudo docker image prune -a -f
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
