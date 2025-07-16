# Omnify-Assignment

Build a simple Booking API for a fictional fitness studio using Python.  

In this project, I have used:

- Django web framework
- SQLite as the database
- Postman to test and debug APIs

I have uploaded my project folder (`omnifyPrj`) in the **master** branch.

---

## Project Contents

This project folder contains:

- `omnifyApp/`
- `omnifyPrj/`
- `db.sqlite3` (database)
- `manage.py`

---

## omnifyApp

The `omnifyApp` folder contains the following files:

- `__init__.py`
- `admin.py`
- `apps.py`
- `models.py`
- `serializers.py`
- `tests.py`
- `urls.py`
- `views.py`

### File Descriptions

- **`admin.py`**  
  Configures how models appear in the Django admin site. In this project, it displays the `Fitness` and `Book` models.

- **`__init__.py`**  
  Marks the folder as a Python package.

- **`apps.py`**  
  Contains app configuration and metadata.

- **`models.py`**  
  Defines the database models. In this project, two models are created:
  - **Fitness**  
    - Fields:
      - name
      - type (Zumba / Yoga / HIIT)
      - date
      - instructor name
      - available slots

  - **Book**  
    (Add description here if applicable.)

- **`serializers.py`**  
  Contains serializers used for converting model instances to JSON and vice versa.

- **`tests.py`**  
  Contains test cases for the application.

- **`urls.py`**  
  Maps URL paths to views.

- **`views.py`**  
  Contains the business logic and API views.

---




