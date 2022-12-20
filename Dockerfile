#Dockerfile to build an image/container to host Newsletter Generator Application
#Pull python Image
FROM newsletter_automation/reloaded:latest
LABEL maintainer = "Qxf2 Services"

ADD .. /newsletter_automation

#Make port 5000 available to the container
EXPOSE 5000

#Execute command
ENTRYPOINT [ "/bin/bash" ]
CMD [ "newsletter_setup.sh" ]