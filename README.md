Invoice Management System
This project provides an API to manage invoices and their associated details, including the creation, updating, and validation of invoice records.

Features
Create Invoice: Allows creating a new invoice with or without details.
Update Invoice: Allows updating invoice information and its details.
Validate Details: Ensures that each invoice detail includes valid quantity and price values.
Line Total Calculation: Automatically calculates the line_total based on the quantity and price of the invoice details.
Requirements
Python 3.x
Django 4.x+
Django REST Framework 3.x+
SQLite (or any database of your choice)
Installation
Clone this repository:

git clone https://github.com/your-username/invoice-management-system.git
cd invoice-management-system
Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the dependencies:

pip install -r requirements.txt
Apply migrations to set up the database:

python manage.py migrate
Create a superuser to access the admin panel (optional):

python manage.py createsuperuser
Run the development server:

python manage.py runserver
Your API should now be running at http://127.0.0.1:8000.
