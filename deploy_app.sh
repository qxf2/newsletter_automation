#!/bin/env bash

systemctl stop newsletter_automation_app
source /home/ubuntu/venv/newsletter_app/bin/activate
cd /home/ubuntu/
python -m pip install *.tar.gz
systemctl start newsletter_automation_app
