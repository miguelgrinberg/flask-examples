Example 5
=========

This example shows a scalable application structure.

Running the application
-----------------------

To run this example follow these steps:

- Activate a virtual environment that contains the packages in `../requirements.txt`
- Set a `FLASK_CONFIG` environment variable to `development` or `production` to select the proper configuration. If this variable is not set `development` is used by default.
- Set a `MONGO_DEV_URI` (development) or `MONGO_URI` (production) environment variable to the MongoDB database for the application.
- To start the application run the following command:

        (venv) $ python manage.py runserver

Running the test suite
----------------------

This application contains unit tests, which can be executed with the following steps:

- Set a `MONGO_TEST_URI` environment variable to the MongoDB database used for testing. Do not use the development or production databases here, as the tests will destroy their contents.
- Run the tests with the following command:

        (venv) $ python manage.py test
