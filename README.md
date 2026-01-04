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

Include the token in the request header: **Authorization: Token <token>**

---

## Endpoints

### User Endpoints
- `POST /users/api/register/` - Register a new user
- `POST /users/api/login/` - Login and receive token
- `POST /users/api/profile/` - Display user profile
- `POST /users/api/logout/` - Logout (invalidate token)

---

### Loan Endpoints
- `POST /loans/request/` - Borrower requests a loan.  
- `POST /loans/loan/<int:pk>/approve/` - Admin approves a loan request.

---

### Repayments Endpoints
- `POST /repayment/repayments/` - Make payments.
- `POST /repayment/loans/<int:pk>/repayments/` - Repayment history.

---

## SetUp

<!-- `
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
git clone https://github.com/Elly-otieno/BoraCredit.git
mkvirtualenv env
pip install -r requirements.txt -->