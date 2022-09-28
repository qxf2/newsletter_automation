# Newsletter automation
This project is to automate the process of creating the weekly Qxf2 newsletter. We take the URLs posted on the Skype channel as input and create a MailChimp campaign.

## Setup
  1. Clone the repository

  2. Setup and activate a virtual environment: </br>
    `virtualenv env` <br />
    `source env\Scripts\activate` <br />

  3. Install the dependencies </br>
    `pip install -r requirements.txt`

  4. Setup the following environment variables<br>
    `export FLASK_APP=run.py`<br>
    `export CLIENT_ID="Your Google Client ID"`<br>
    `export CLIENT_SECRET="Your Google Secret"`<br>
    `export SERVER_PREFIX="Your Server Prefix"`<br>
    `export SUBSCRIBER_LIST_ID="Your Mailchimp subscriber list"`<br>
    `export MAILCHIMP_API_KEY="Your Mailchimp API key"`<br>
    `export MYSQL_USERNAME="Your MYSQL username"`<br>
    `export MYSQL_PASSWORD="Your MYSQL password"`<br>
    `export API_KEY="API KEY OF YOUR CHOICE"`<br>
    *NOTE:* For Qxf2 employees, please ask a colleague to share the right vault with you for these values

  5. Run <br>
    `cd newsletter_automation`<br>
    `flask db stamp head`<br>
    `flask db migrate`<br>

  6. Manually insert data into article_category using below query: <br>
     `"insert into article_category (category_name) values ('comic'),('pastweek'),('currentweek'),('automation corner'),('uncategorized');"`<br>

At this point, you are ready to run the app locally.

 ## Run the project locally
Once you are setup, from the next time onwards, all you need to do is<br>
    `flask run`

This assumes you have set the right environment variables in step 4 of the setup. To test that your setup works, please visit http://localhost:5000 and login. Then, try to add a single article via the form in the /articles page.

## Provided support for flask-migrate
  To track migrations, migrations folder have been added now, Next time onwards following steps needs to be followed:
  1. Update the `model.py` file to make the changes.
  2. Run `flask db migrate`
  3. Run `flask db upgrade`

## Add articles through api endpoint
  To add articles using POST method use the following:
  1. Set your api key in environment variable as `'API_KEY': '<YOURAPIKEY>'`
  2. Use the same api key for Request headers `'x-api-key': '<YOURAPIKEY>'`
  3. API Endpoint: POST `<base_url>/api/articles`
  4. Example curl command ` curl -X POST http://localhost:5000/api/articles -H 'X-API-KEY: <YOUR_API_KEY>' -F 'url=http://exampleURL.com' -F 'category_id=2 `

## How to run Great Expectations test locally:
Great Expectations is an open-source Python library to test data pipelines. It helps in validating and documenting data and thus maintaining data quality.

1. Install great_expectations:
   `pip install great_expectations`

2. Set the environment variables prefixed with `DB_`, mentioned in great_expectations.yml

3. Navigate to tests > data_validation > great_expectations directory:
   `cd tests/data_validation/great_expectations`

4. Run the checkpoint script.
   Navigate to newsletter_automation directory and run:

   `pytest tests/data_validation/great_expectations/utils/ -s -v -m checkpoint10am`

   This will trigger the Checkpoint and run the Expectation Suite against the MySQL table data as configured in the datasource. Please use the correct pytest marker to trigger the relevant checkpoint.


5. Results are stored in `great_expectations/uncommitted/data_docs/local_site` folder.
  Navigate to the above directory using File Explorer.
  Open index.html, go to Validations tab and select your recent run.
  It will show details of what expectations have run, how many have passed/failed, failure details etc.
