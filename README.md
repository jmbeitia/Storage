# File Manager - Python - Django - Javascript

# Solution:

- Web application that allows users to store, at later retrieve, files at a specified URL.

- Stores files of any type and name

- Stores files at any URL

- Does not allow interaction by non-authenticated users

- Does not allow a user to access files submitted by another user

- Allows users to store multiple revisions of the same file at  the same URL

- Allows users to fetch any revision of any file

# How to Run:

1. Create and activate a python3 virtualenv.

    `python -m venv env`

2. A `requirements.txt` is provided for a virtual enviroment:

    `pip install -r requirements.txt`

3. Open console an execute:

    `python manage.py makemigrations` and `python manage.py migrate`

4. Go to `http://127.0.0.1:8000/`


# Imporvements:

1. Error handling could be improved.

2. Add unit test scripts