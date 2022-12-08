#Dockerfile to build an image/container to host Newsletter Generator Application
#Pull python Image
FROM python
LABEL maintainer = "Qxf2 Services"

#Clone cars-api repository for Docker Image creation
RUN git clone https://github.com/qxf2/newsletter_automation.git

#Set working directory
WORKDIR /newsletter_automation

#Install packages listed in requirements.txt file
RUN python -m pip install -r requirements.txt
RUN export TURN_OFF_NEWSLETTER_SSO=true
RUN cd newsletter_automation

#Make port 5000 available to the container
EXPOSE 5000

#Execute command
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]