# Invoice Management System

A robust Django-based API for managing invoices and their associated details, providing comprehensive functionality for creating, updating, and validating invoice records.

## 🚀 Features

- **Invoice Management**
  - Create new invoices with or without details
  - Update existing invoice information
  - Delete invoices and their associated details
  - Retrieve invoice information with filtering options

- **Detail Management**
  - Add multiple details to invoices
  - Automatic line total calculation
  - Validation of quantity and price values
  - Bulk update capabilities

- **Data Validation**
  - Comprehensive input validation
  - Business rule enforcement
  - Error handling with detailed messages

## 📋 Requirements

- Python 3.x
- Django 4.x+
- Django REST Framework 3.x+
- SQLite (default) or any supported database

## 🔧 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/invoice-management-system.git
   cd invoice-management-system
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Database Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

### API Endpoints

- `GET /api/invoices/` - List all invoices
- `POST /api/invoices/` - Create new invoice
- `GET /api/invoices/{id}/` - Retrieve specific invoice
- `PUT /api/invoices/{id}/` - Update invoice
- `DELETE /api/invoices/{id}/` - Delete invoice
- `GET /api/invoices/{id}/details/` - List invoice details
- `POST /api/invoices/{id}/details/` - Add invoice detail

## 📚 Documentation

Detailed API documentation is available at:
- Swagger UI:  `http://localhost:8000/api/docs/`
