pipeline {
    agent any
    stages {
        stage('Checkout Repositories:') {

                    steps {
                        echo "Hello"
                        sh 'python3 --version'
                        sh 'python3 install.py'
                    }

        }
    
    }
}

def checkout_itops_repo() {
    checkout([
                    $class: 'GitSCM',
                    branches: [[name: params.ITOPS_REPO_BRANCH]],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [
                        [$class: 'CloneOption', timeout: 20, depth: 1, shallow: true],
                        [$class: 'RelativeTargetDirectory', relativeTargetDir: 'itops']
                    ],
                    submoduleCfg: [],
                    userRemoteConfigs: [[url: env.ITOPS_MASTER_URL]]
                ])
}

def checkout_template_repo() {
    checkout([
                    $class: 'GitSCM',
                    branches: [[name: params.ANY_BRANCH]],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [
                        [$class: 'CloneOption', timeout: 20 ]
                    ],
                    submoduleCfg: [],
                    userRemoteConfigs: [[url: env.PREVIEW_TEMPLATE_MASTER_URL]]
                ])
}
