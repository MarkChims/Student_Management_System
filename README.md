# Student Management System

## Overview

This Student Management System is a simple web application developed to streamline the management of students, subjects, hostels, and user authentication within an educational institution.

The project uses **Plain HTML, CSS, and JavaScript** for the frontend and **Django with Django REST Framework** for the backend API. Authentication is secured using **JWT (JSON Web Tokens)**.

---

## Core Modules

1. **Subject Management and Registration (CRUD)**  
   Create, read, update, and delete subjects offered by the institution.

2. **Student Management**  
   Staff members can add, update, and manage student profiles.

3. **Hostel Management**  
   Manage dormitories, rooms, and allocate students to residences.

4. **Secure Login Functionality**  
   Authentication and authorization implemented via JWT tokens and Django REST Framework.

---

## Key Features

- Staff members are responsible for adding students.
- Staff accounts are created via Django admin by creating a superuser.
- RESTful APIs to manage and retrieve data.
- Frontend communicates with backend APIs using JavaScript fetch calls.
- Dashboard and statistics endpoints for aggregated data insights.
  
---

## Important URLs (API Endpoints & Pages)

| URL                       | Description                       |
|---------------------------|---------------------------------|
| `/staff/add-student`       | Add a new student (staff only)  |
| `/staff/edit-student/<id>` | Edit an existing student         |
| `/staff/add-subject`       | Add a new subject                |
| `/staff/add-dorm`          | Add dormitory details            |
| `/staff/add-room`          | Add a room to dormitory          |
| `/staff/studentsstats`     | View student gender stats        |
| `/staff/dashboardstats`    | View overall dashboard statistics|

*Note: Staff members must login using JWT tokens to access protected routes.*

---

## Technologies Used

- **Frontend:**  
  - Plain HTML  
  - CSS  
  - JavaScript (Vanilla)

- **Backend:**  
  - Python 3.x  
  - Django  
  - Django REST Framework (DRF)  
  - JWT for Authentication  

---

## Getting Started

### Prerequisites

- Python 3.x  
- pip  
- Virtualenv or any virtual environment manager  
- Git  
- Visual Studio Code (for frontend development with Live Server)

### Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/student-management-system.git
    cd student-management-system
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser (to manage staff accounts via Django Admin):
    ```bash
    python manage.py createsuperuser
    ```

6. Run the backend development server:
    ```bash
    python manage.py runserver
    ```

7. Access the backend admin panel at:
    ```
    http://localhost:8000/admin
    ```

---

### Running Frontend with Live Server (VS Code)

To preview and develop the frontend with live reload:

1. Install the **Live Server** extension in Visual Studio Code:  
   - Open VS Code.  
   - Go to Extensions (`Ctrl+Shift+X` or `Cmd+Shift+X` on Mac).  
   - Search for **Live Server** by *Ritwick Dey* and install it.

2. Open your project folder in VS Code and navigate to the frontend folder (where your HTML files are).

3. Right-click the main HTML file (e.g., `index.html`) and select **"Open with Live Server"**.

4. Your browser will open the frontend locally. Any changes you make to HTML, CSS, or JavaScript files will automatically reload the page.

5. Ensure the Django backend server is running (see step 6 above) so frontend API calls to endpoints like `http://localhost:8000/staff/add-student` will work correctly.

---

## Usage Notes

- Staff members **must be created via the Django admin panel** (superuser creates staff users).
- Only authenticated staff users can add or edit student records.
- Frontend uses JavaScript to call backend APIs securely with JWT tokens.
- Include JWT tokens in request headers for protected endpoints.
- Make sure CORS is configured properly if frontend and backend run on different ports.

---

## Project Structure


