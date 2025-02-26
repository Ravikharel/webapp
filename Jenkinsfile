pipeline{ 
    agent any
    stages{ 
        stage('Creating the Images'){ 
            steps{ 
                echo "Building the docker images..."
                sh 'docker build -t webapp:v1 .'
            }
        }
        stage('Running the container'){ 
            steps{ 
                echo " Building the docker container"
                sh 'docker container run -d -p 8000:8000 webapp:v1'
            }
        }
    }
}