FROM ubuntu

WORKDIR /code
ADD . /code/

RUN apt update
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install python3.8 -y
RUN apt install python3-pip -y

RUN python3.8 -m pip install -r /code/requirements.txt
RUN python3.8 -m pip install cryptography

ENTRYPOINT  python3.8 /code/create_db.py && python3.8 /code/newsletter_automation/run.py
