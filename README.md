# Newsletter automation
The **Newsletter automation** project helps automate the Newsletter creation process at [Qxf2 Services](https://qxf2.com/)

## Setup
  1. Clone the repository

  2. Run *docker-compose up*

  3. Access the Newsletter app in the browser on *http://127.0.0.1:5000*

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
