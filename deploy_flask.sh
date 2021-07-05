#!/bin/bash
#Script to deploy flask app to EC2 instance
cd /home/ubuntu
pip3 install virtualenv
if [ -d "venv_newsletter" ]
then
        echo "Virtual environment already exists"
else
        echo "Virtual environment does not exists"
        virtualenv venv_newsletter
fi
source venv_newsletter/bin/activate
pip install -r requirements.txt
cp -R newsletter_automation-0.0.2/newsletter_automation venv_newsletter/lib/python3*/site-packages
cd venv_newsletter/lib/python3*/site-packages/newsletter_automation
ps -ef | grep python  | grep flask | awk {'print $2'} | xargs kill -9 2>/dev/null
export FLASK_APP=run
nohup flask run --host=0.0.0.0 --port=8080 2>/home/ubuntu/nohup.err 1>/home/ubuntu/nohup.out &

