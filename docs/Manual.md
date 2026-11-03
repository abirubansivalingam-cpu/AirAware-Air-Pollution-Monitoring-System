Using Windows Command Prompt (CMD)

    :: 1. Create a virtual environment
    py -m venv .venv

    :: 2. Upgrade pip and install requirements
    .venv\Scripts\python.exe -m pip install --upgrade pip
    .venv\Scripts\python.exe -m pip install -r requirements.txt

    :: 3. Apply database migrations
    .venv\Scripts\python.exe manage.py migrate

    :: 4. Populate illustrative demo data
    .venv\Scripts\python.exe manage.py load_demo_data

    :: 5. (Optional) Create superuser admin account
    .venv\Scripts\python.exe manage.py createsuperuser

    :: 6. (Optional) Run unit tests
    .venv\Scripts\python.exe manage.py test

    :: 7. Start the local server
    .venv\Scripts\python.exe manage.py runserver 8080
    or
    .venv\Scripts\python.exe manage.py runserver 0.0.0.0:8080
