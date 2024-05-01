# vendor-management-system-Django
## Overview
This is a Vendor Management System developed using Django and Django REST Framework. The system handles vendor profiles, purchase orders, and vendor performance metrics.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/allemkarthik/vendor-management-system-Django.git
    cd vendor-management-system
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Database Setup
1. Create a SQLite database:
    ```bash
    createdb vendor_management_system
    ```

2. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

## Running the Server
Start the development server:
```bash
python manage.py runserver
