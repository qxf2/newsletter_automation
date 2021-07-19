#!/bin/env bash

sudo systemctl stop newsletter_automation_app
sudo source /home/ubuntu/venv/newsletter_app/bin/activate
cd /home/ubuntu/
sudo python -m pip install *.tar.gz
sudo systemctl start newsletter_automation_app
