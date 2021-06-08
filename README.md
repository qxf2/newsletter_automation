# newsletter_automation
This project is to automate the process of creating the weekly Qxf2 newsletter. We take the URLs posted on the Skype channel as input and create a MailChimp campaign.

## Setup
<li>
  1. Clone the repository
  
  2. Setup and activate a virtual environment
    `virtualenv env` <br />
    `env\Scripts\activate` <br />
 
  3. Install the dependencies 
    `pip install -r requirements.txt`
 </li>
 
 ## Run the project locally
 <li>
    `export FLASK_APP=run.py`
    `flask run`
