# CivicNode

CivicNode is a web application built with Django that empowers community members to report and track local civic issues. Users can raise issues based on specific categories (e.g., emergency, infrastructure), upvote existing issues, and track their resolution status. Administrators and staff can manage, assign, and update the status of these issues to keep the community informed.

## Features

- **User Authentication**: Secure login and registration system with role-based access control (User, Staff, Admin).
- **Issue Reporting**: Users can easily raise issues by providing a title, description, location, and selecting a category.
- **Issue Tracking**: A centralized dashboard to view active and resolved community issues.
- **Upvoting**: Community members can upvote issues to increase their visibility and prioritization.
- **Staff Assignment & Management**: Admins can assign specific issues to staff members who can update their status (Pending, In Progress, Resolved) and provide remarks.

## Technology Stack

- **Backend Framework**: Django
- **Database**: PostgreSQL
- **Frontend**: HTML/CSS/JS (Django Templates)

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd CivicNode
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows use: venv\Scripts\activate
   # On macOS/Linux use: source venv/bin/activate
   ```

3. **Install the dependencies:**
   Make sure to install the required packages (e.g., Django, python-dotenv).
   ```bash
   pip install django python-dotenv
   # Or using requirements.txt if available: pip install -r requirements.txt
   ```

4. **Environment Variables:**
   - Copy the `.env.example` file to a new file named `.env`.
   - Update the variables inside the `.env` file, such as `SECRET_KEY`.
   ```bash
   cp .env.example .env
   ```

5. **Apply Database Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser:**
   To access the admin panel, create a superuser account:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
   The application will be accessible at `http://127.0.0.1:8000/`.

## Project Structure

- `accounts/`: Handles user authentication, registration, and profiles.
- `dashboard/`: Manages the landing page and user-specific dashboards based on roles.
- `issues/`: Core application for raising, viewing, upvoting, and managing civic issues.
- `CivicNode/`: Project configuration, settings, and root URL routing.
- `templates/`: Contains all HTML templates for the frontend.
- `static/`: Contains static assets like CSS, JavaScript, and images.

## Usage

- **Regular Users**: Can register, log in, view the dashboard, raise new issues, upvote existing issues, and track community problems.
- **Staff**: Can log in, view their assigned issues, and update the status of issues they are working on (with remarks).
- **Admins (Superuser)**: Have full control over the platform. They can access the Django admin panel, manage users, categories, and assign issues to specific staff members.
