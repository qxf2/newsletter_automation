# Newsletter automation
This project is to automate the process of creating the weekly Qxf2 newsletter. We take the URLs posted on the Skype channel as input and create a MailChimp campaign.

## Setup
  1. Clone the repository
  
  2. Setup and activate a virtual environment: </br>
    `virtualenv env` <br />
    `source env\Scripts\activate` <br />
 
  3. Install the dependencies </br>
    `pip install -r requirements.txt`
 
 ## Run the project locally
    export FLASK_APP=run.py
    flask run

