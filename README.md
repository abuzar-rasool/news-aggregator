# News Aggregator API

The **News Aggregator API** is a Django-based project designed to gather data from multiple sources such as Reddit and News API. The project follows the SOLID principles, which ensure that it is maintainable, scalable, and extensible.

The architecture of the application allows for the easy addition of new API sources without modifying the existing code. Each API source is encapsulated in a separate class, which is responsible for gathering data from its respective source. Moreover the business logic is extracted out from the views via services!


## Prerequisites

The project uses:
1. Python Version 3.11.1
2. Django Version 4.2
3. pip (Python package manager)
4. virtualenv (optional, but recommended)

## Installation



### Step 1: Clone the repository

Clone the repository to your local machine:


    git clone https://github.com/abuzar-rasool/news-aggregator.git
    cd news-aggregator
### Step 2: Create a virtual environment (optional)

It's a good practice to use a virtual environment for each Python project. This isolates the dependencies for each project and keeps your system clean.

`python3 -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'`

### Step 3: Install dependencies

Use pip to install the required packages from the `requirements.txt` file:

`pip install -r requirements.txt`

### Step 4: Configure the database

Migrate the database:

`python manage.py migrate`

### Step 5: Create a superuser

Create a superuser to access the Django admin panel:

`python manage.py createsuperuser`


### Step 6: Start the development server

Run the development server:

`python manage.py runserver`

The project should now be available at

http://127.0.0.1:8000/


![Swagger UI on the index page of the app](https://github.com/abuzar-rasool/news-aggregator/blob/main/images/index.PNG?raw=true)

## Documentation
In order to effiececintly make documentations i have added swagger UI for this project. Detailed API docs for are present there.

## Obtaining Tokens for requests
As the assignment asks us to implement token authentication, therefore you will have to generate tokens and then use it swagger ui to authorize yourself.

### Step 1: Log in to the Django admin dashboard

Open your web browser and navigate to the Django admin dashboard URL. The default URL is:

`http://127.0.0.1:8000/admin` 

Log in with your superuser credentials.


### Step 2: Create a token for a user

1.  Click on the "Tokens" section in the Django admin dashboard.
2.  Click on the "Add token" button in the top right corner.
3.  Select the user for whom you want to generate a token from the "User" dropdown.
4.  (Optional) Enter a custom token key or leave it blank to auto-generate one.
5.  Click "Save" to create the token.
6. Copy the token created


### Step 2: Using token in Swagger ui

1. Click on **Authorize**  in http://127.0.0.1:8000/.
2. Add your token in the value box and click **Authorize**

## Documentation
In order to effiececintly make documentations i have added swagger UI for this project. Detailed API docs for are present there. Hoever i will be going over the archiectecture of the app in this section.


## Testing
For the scope of this assignment i have written test for the dervices that are being used by the API Views!
All the tests are present in 

> news-aggregator/core/tests

In order to run the tests please run the following command.

    python manage.py test core.tests


