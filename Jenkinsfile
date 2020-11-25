pipeline{
    agent any
    stages{
        stage('Install Docker'){
            steps{
                sh './scripts/install_docker.sh'
            }
        }
        stage('Deploy Docker'){
            steps{
                sh './scripts/deploy.sh'
            }
        }
    }
