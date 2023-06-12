pipeline {
    agent any
    stages {
        stage('Checkout Repositories:') {

                    steps {
                        deleteDir()
                        checkout_template_repo()
                        checkout_itops_repo()
                    }

        }
    stage('Copy template files:') {
      steps {
        sh '''
            echo "Info: Using node version: `node -v` and npm version: `npm -v` and yarn version: `yarn -v`"
            set -e

            # ENVJS as template - ITOPS-139662
            ENVJS_TEMPLATE="$WORKSPACE/itops/ansible/files/configs/spr-template-preview/$ENV/environment.j2"
            ENVJS_FILE="$WORKSPACE/itops/ansible/files/configs/spr-template-preview/$ENV/environment.js"
            ENVJS_DEST_FILE="$WORKSPACE/config/environment.js"
            if [[ -f "$ENVJS_TEMPLATE" ]]; then
            cd $WORKSPACE/itops/ansible
            ansible-playbook -i inventory/$ENV/hosts copy-template-file.yml -e "src_file=$ENVJS_TEMPLATE dest_file=$ENVJS_DEST_FILE"
            else
            cp $ENVJS_FILE $ENVJS_DEST_FILE
            fi
            '''
      }
    }
//     stage('Run Install and Upload Steps:') {
//        agent  { docker { image 'prod-nexus.sprinklr.com:8123/spr-rocky8-node10-18-1:node-10.18.1-npm-6.13.4-yarn-1.22.5' 
//                      reuseNode true 
//            args '-v /root/.npmrc:/root/.npmrc -v /etc/hosts:/etc/hosts'
//        } }
//         steps {
//             dir(env.WORKSPACE){
//             sh 'npm -v'
//             sh 'node -v'
//             sh 'yarn -v'
//             sh 'rm .npmrc'
//             sh 'cat /root/.npmrc'
//             sh 'time yarn install'
//             sh 'time npm run publish-previews'
//             }
            
//         }
//     }
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
