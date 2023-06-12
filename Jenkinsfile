pipeline {
    agent any
    stages {
        stage('code checkout') {
            parallel {
                stage('checkout charts repo') {
                    steps {
                        checkout_charts_repo()
                    }
                }
                stage('checkout itops repo') {
                    steps {
                        checkout_itops_repo()
                    }
                }
            }
        }
//         stage('Checkout Repositories:') {
//                    agent  { docker { image 'prod-nexus.sprinklr.com:8123/spr-centos7-node16:node-16.18.0-npm-8.1.0-yarn-3.2.4' 
//                      reuseNode true 
//        } }


//                     steps {
//                         echo "Hello"
//                         sh '''#!/usr/bin/env bash
//                         # run build
//                         echo "Info: Using node version: `node -v` and npm version: `npm -v` and yarn version: `yarn -v`"
//                         set -e
//                         SERVICE_DIR='packages/web'

//                         cd $WORKSPACE
//                         rm -rf .npmrc
//                         cd $WORKSPACE/$SERVICE_DIR
//                         time yarn install'''
//                     }

//         }
    
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
def checkout_charts_repo() {
    checkout([
                    $class: 'GitSCM',
                    branches: [[name: params.CHART_REPO_BRANCH]],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [
                        [$class: 'RelativeTargetDirectory', relativeTargetDir: 'apps-charts']
                    ],
                    submoduleCfg: [],
                    userRemoteConfigs: [[url: 'git@prod-gitlab.sprinklr.com:sprinklr-k8s/helm-charts.git']]
                ])
}

