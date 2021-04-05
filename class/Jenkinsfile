pipeline {
    agent any
    tools{
        maven 'local_MVN'
    }
    stages{
        stage('Build'){
            steps {
                sh 'mvn clean package'
            }
            post {
                success {
                    echo '开始...'
                    archiveArtifacts artifacts: '**/target/*.war'
                }
            }
        }
        stage('deploy_local'){
            steps{
                build job: 'deploy-to-local'
            }
        }
    }
}
