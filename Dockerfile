FROM shivaharip/qxf2_newsletter_packages_pre_installed

WORKDIR /code
ADD . /code

RUN pip3 install -r requirements.txt

ENTRYPOINT  python3 create_db.py && python3 newsletter_automation/run.py
