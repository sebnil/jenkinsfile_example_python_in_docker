#!groovy

// virtual environment should be unique per project
def venvName = "paylando-automatic-system-tests"

pipeline {
    agent 
    {
        docker {
          image 'python:3'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install requirements') {
            steps {
                // install all requirements listed in requirements.txt
                sh "pip install -r requirements.txt"
            }
        }

        stage('Test') {
            steps {
                // run tests
                sh "nosetests -w tests --with-xunit --verbosity=2"

                // publish test results
                junit 'nosetests.xml'
            }
        }

        stage('Static Code Analysis') {
            steps {
                // flake8 code analysis
                sh "flake8 tests --exit-zero --output-file flake8.log"

                // pylint code analysis
                sh "pylint tests --rcfile=./pylintrc > pylint.log | EXIT 0"

                // publish analysis from both flake8 and pylint
                step([$class: 'WarningsPublisher',
                    parserConfigurations: [
                        [
                            parserName: 'Pep8',
                            pattern: 'flake8.log'
                        ],
                        [
                            parserName: 'pylint',
                            pattern: 'pylint.log'
                        ]
                    ],
                ])
            }
        }
    }
}