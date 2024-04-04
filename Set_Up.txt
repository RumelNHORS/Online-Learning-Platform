To set up the Online Learning Platform project, you'll need to follow these steps:

1. Clone the Project:
    Clone the project repository from your version control system (e.g., Git) to your local machine.
        git Clone https://github.com/RumelNHORS/Online-Learning-Platform.git

2. Set Up a Virtual Environment:
    It's recommended to use a virtual environment to isolate project dependencies. You can create a virtual environment using venv or virtualenv:
        python -m venv env

3. Activate the Virtual Environment:
    Activate the virtual environment:
        On Windows:
            .\env\Scripts\activate
        On macOS and Linux:
            source env/bin/activate

4. Install Dependencies:
    Navigate to the project directory and install the required dependencies using pip:
        pip install -r requirements.txt

5. Set Up Database:
    Configure your database settings in the settings.py file. By default, the project uses SQLite, but used the PostgreSQL for this project.

6. Apply Migrations:
    Apply database migrations to create the necessary database tables:
        python manage.py makemigrations
        python manage.py migrate

7. Run the Development Server:
    Start the development server to run the Django application:
        python manage.py runserver

