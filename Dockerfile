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

# Change the value of API_KEY in the script using sed
RUN sed -i 's|export MAILCHIMP_VIRTUALIZATION="https://v08eq.mocklab.io"|export MAILCHIMP_VIRTUALIZATION="https://v55dj.wiremockapi.cloud"|' newsletter_setup.sh

CMD [ "newsletter_setup.sh" ]
