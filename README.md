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
- `urls.py`
- `views.py`

### File Descriptions

- **`admin.py`**  
  Configures how models appear in the Django admin site. In this project, it displays the `Fitness` and `Book` models.

- **`__init__.py`**  
  Marks the folder as a Python package.

- **`apps.py`**  
  Contains app informations.
  
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
     - Fields:
      - fitness(ForeignKey of Fitness class)
      - client_name
      - client_email

- **`serializers.py`**  
  Contains serializers used for converting model instances to JSON and vice versa.

- **`urls.py`**  
  Maps URL paths to views

- **`views.py`**  
  Contains the business logic and API views.

---

- **`setting.py`**  
  It is the configuration file of the project. It tells Django how to run your app.


### Working

-  Fitness class creation using the required fields(name,type,date,instructor name,slots).here (name,type,instructor name and slot are character field),(date is datetime field) and(email is email field).POST API(**`FitnessAPIView`** ) is used for Fitness class creation.
-  GET API (**`FitnessAPIView`** ) class is used to get a list of all upcoming fitness classes (name, date/time, instructor, available slots).
-  Client Booking through POST API (**`BookingAPIView`**) using fields(fitness(class_id),client_name and client_email). once the booking is made then the slot is reduced.
-  GET API (**BookingAPIView**) Returns all bookings made by a specific email address, this email is passed as a params in the request. 
- in setting.py file Timezone management is done by changing  
    TIME_ZONE = 'Asia/Kolkata'
    USE_TZ = True

### API DOCUMENTATION LINK
- IN this documentation can view how the input is passed and its coresponding response with example.

   [my API DOCUMENTATION](https://documenter.getpostman.com/view/35960963/2sB34iiz95)




