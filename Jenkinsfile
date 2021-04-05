pipeline {
    agent {
        docker { 
            image 'python:3.8'
            args '-u root:root'
            }
    }
    options { 
        timestamps ()
        ansiColor('xterm')
    }
    stages {
        stage('python- install requirement') {
            steps {
                sh """
                python -V
                pip install pylint
                pip install pymysql
            """
            }
        }
        stage('python- check code') {
            steps {
                sh "pylint --output-format=parseable exampl.py > pylint.xml || exit 0"
            }
        }
        stage('python- genarate report') {
            steps {
                recordIssues(tools: [pyLint(pattern: 'pylint.xml')])
            }
        }
    }
}
