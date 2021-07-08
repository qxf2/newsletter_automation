#!/bin/bash
#Script to deploy flask app to EC2 instance
cd /home/ubuntu
pip3 install virtualenv
#check if the virtualenvironment exists
if [ -d "venv_newsletter" ]
then
        echo "Virtual environment already exists"
else
        echo "Virtual environment does not exist"
        virtualenv venv_newsletter
fi
source venv_newsletter/bin/activate
pip install -r requirements.txt
#place the newsletter folder inside the virutalenv. Will not be required once it is available as pip installable
cp -R newsletter_automation-0.0.2/newsletter_automation venv_newsletter/lib/python3*/site-packages
cd venv_newsletter/lib/python3*/site-packages/newsletter_automation
#terminate existing flask process
ps -ef | grep python  | grep flask | awk {'print $2'} | xargs kill -9 2>/dev/null
#deploy the flask app
export FLASK_APP=run
nohup flask run --host=0.0.0.0 --port=8080 2>/home/ubuntu/nohup.err 1>/home/ubuntu/nohup.out &

