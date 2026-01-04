# BoraCredit
Dynamic Interest Based on Repayment Timing
The app as at now supports user registration, authentication, loan requests, loan approvals, and repayments with progressive interest logic.


## Features
- User registration, login, and logout
- Borrower loan requests
- Admin loan approvals (with max interest rate assignment)
- Progressive interest calculation (Day N = N% interest, capped at max interest rate)
- Repayment tracking with automatic loan status updates (`active`, `overdue`, `defaulted`, `paid`)
- Loan repayment history endpoint

---

## Authentication
All endpoints require authentication using **DRF Token Authentication**.

Include the token in the request header: **Authorization: Token <your_token>**

---

## Endpoints

### User Endpoints
- `POST /users/register/` - Register a new user
- `POST /users/login/` - Login and receive token
- `POST /users/logout/` - Logout (invalidate token)

---

### Loan Endpoints
- `POST /loans/request/` - Borrower requests a loan.  
  
---

## SetUp

`
git clone https://github.com/Elly-otieno/boracredit.git
cd boracredit

`
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
django-admin startproject my_project

python manage.py startapp loans

python manage.py startapp repayment

python manage.py startapp users


## Deployment

Deployed on PythonAnywhere

pip install whitenoise