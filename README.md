# Employee Management System – Backend

A RESTful backend application for managing employees, attendance, leave management, authentication, and role-based access control. The system is built using **Django** and **Django REST Framework (DRF)** and provides structured APIs for managing employee-related operations.

## 🚀 Features

* 🔐 User authentication and authorization
* 👥 Employee management
* 🏢 Department and employee information management
* ⏰ Attendance management
* 📝 Leave management
* 🛡️ Role-based permissions and access control
* 🔄 RESTful API architecture
* 🗄️ Database-driven employee records
* ✅ API validation using Django REST Framework serializers
* 📦 Modular Django app structure

## 🛠️ Technologies Used

* **Python**
* **Django**
* **Django REST Framework**
* **SQLite**
* **REST API**
* **Git & GitHub**

## 📂 Project Structure

```text
Employee_Management_System/
│
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── employees/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── attendance/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── leave_management/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── .gitignore
```

## 🔑 Main Modules

### Accounts

Handles user-related functionality including authentication, authorization, and custom permissions.

### Employees

Provides APIs for managing employee information and employee-related records.

### Attendance

Handles employee attendance-related operations and records.

### Leave Management

Provides functionality for managing employee leave requests and related operations.

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/var-sha04/Employee_management_backend.git
```

### 2. Navigate to the project

```bash
cd Employee_management_backend
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

The backend will be available at:

```text
http://127.0.0.1:8000/
```

## 🔌 API Architecture

The application follows a RESTful architecture using Django REST Framework.

The API is organized into separate modules for:

```text
Authentication
     │
     ├── Accounts
     │
     ├── Employees
     │
     ├── Attendance
     │
     └── Leave Management
```

Each module uses Django REST Framework components such as:

* Models
* Serializers
* Views
* URL routing
* Permissions

## 🛡️ Security & Permissions

The backend implements permission-based access control to restrict operations according to the user's role and authorization level.

Sensitive configuration such as environment variables is excluded from version control using `.gitignore`.

## 🧪 Testing

The project includes Django test modules within the individual applications.

Tests can be executed using:

```bash
python manage.py test
```

## 📌 Development Practices

* Modular Django application structure
* Separation of models, serializers, views, and URLs
* RESTful API design
* Git-based version control
* Environment-specific configuration management
* Virtual environment isolation
* Sensitive files excluded using `.gitignore`

## 🔮 Future Enhancements

Potential improvements for the project include:

* API documentation using Swagger/OpenAPI
* Token/JWT-based authentication enhancements
* Advanced employee search and filtering
* Pagination and sorting
* Automated email notifications
* Production database integration
* Docker containerization
* CI/CD integration
* Automated API testing

## 👩‍💻 Author

**Varsha N**

MCA Graduate | Python & Django Developer

---

⭐ If you find this project useful, feel free to explore the repository and give it a star.
