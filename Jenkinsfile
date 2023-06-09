pipeline {
    agent any
    stages {
        stage('Checkout Repositories:') {

                    steps {
                        echo "Hello"
                        sh 'python3 --version'
                        sh '''#!/usr/bin/env bash
                        # run build
                        echo "Info: Using node version: `node -v` and npm version: `npm -v` and yarn version: `yarn -v`"
                        set -e
                        SERVICE_DIR='packages/web'

                        cd $WORKSPACE
                        rm -rf .npmrc
                        cd $WORKSPACE/$SERVICE_DIR
                        time yarn install'''
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
