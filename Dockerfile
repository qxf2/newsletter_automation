#Dockerfile to build an image/container to host Newsletter Generator Application

#Pull an Image
FROM qxf2rohand/newsletter_automation:latest
LABEL maintainer = "Qxf2 Services"

#Mounting a code as volume into the container
ADD . /newsletter_automation

#Make port 5000 available to the container
EXPOSE 5000

#Execute command
ENTRYPOINT [ "/bin/bash" ]
CMD [ "newsletter_setup.sh" ]
