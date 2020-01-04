import os
import sys

os.system('sudo apr-get install pip3')
os.system('pip3 install termcolor')

from termcolor import colored

commands = {
            apt_update0: 'sudo apt-get update',
            docker_in0: 'sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common',
            docker_in1: 'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -',
            docker_in2: 'sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"',
            apt_update1: 'sudo apt-get update',
            docker_in3: 'sudo apt-get install docker-ce docker-ce-cli containerd.io',
            dockerC_i0: 'sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose',
            dockerC_i1: 'sudo chmod +x /usr/local/bin/docker-compose',
            apt_update2: 'sudo apt-get update',
            ansible_in: 'sudo apt-get install ansible'
            }

for key in commands.keys():
    cmd = os.system(key)
    if cmd == 0:
        print(colored('Operation status: OK', 'green'))
    else:
        print(colored('Operation status: ERROR', 'red'))
        sys.exit()
