<div align="center">
  <h1>🏙️ CivicNode</h1>
  <p><em>Empowering communities to report, track, and resolve local civic issues.</em></p>
  
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
  ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
  ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
  ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
</div>

---

## 📖 About The Project

**CivicNode** is a robust, role-based community issue tracking platform built with the Django web framework. 

Its primary goal is to empower local citizens to report problems in their area—such as infrastructure damage, sanitation issues, or emergencies—while giving local authorities and staff the tools they need to track, manage, and resolve them efficiently.

This project was built to demonstrate full-stack development capabilities, relational database design, user authentication, and role-based access control (RBAC).

---

## ✨ Key Features

- **🛡️ Role-Based Access Control (RBAC):** Three distinct user roles with specific permissions:
  - **Citizens:** Can register, report issues, upvote existing ones, and track progress on a personalized dashboard.
  - **Staff Members:** Have a dedicated dashboard for assigned issues, allowing them to update statuses (Pending, In Progress, Resolved) and leave public remarks.
  - **Administrators:** Full system control via the Django Admin Panel to manage users, categories, and delegate issues to staff.
- **📍 Comprehensive Issue Reporting:** Users can submit detailed reports including title, description, categorized tags, and specific locations.
- **👍 Community Upvoting:** Allows the community to prioritize urgent issues by upvoting them, pushing them higher up the queue.
- **🔔 Real-Time Notifications:** Provides immediate user feedback for actions (success, error, warning) via a custom notification system.

---

## 🛠️ Technology Stack

- **Backend:** Python, Django
- **Database:** PostgreSQL (Production) / SQLite (Development)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript, Django Templates

---

## 🚀 Getting Started

Follow these instructions to get a local copy up and running.

### Prerequisites

- Python 3.x
- PostgreSQL (if running in production mode) or SQLite (built-in)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/CivicNode.git
   cd CivicNode
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install django python-dotenv psycopg2
   # Or via requirements.txt if present
   # pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the root directory and add your secret key and database credentials:
   ```env
   SECRET_KEY=your_secure_secret_key_here
   ```

5. **Apply Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser (Admin Account)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   *Visit `http://127.0.0.1:8000/` in your browser.*

---

## 🗺️ Application Architecture & Site Map

The application is structured into modular Django apps: `accounts`, `dashboard`, and `issues`.

### Site Map Breakdown:
- **Public & User Dashboard**
  - `/` - Landing Page
  - `/dashboard/` - User Dashboard
- **Accounts & Authentication**
  - `/accounts/register/` - Create a new account
  - `/accounts/login/` - User login
  - `/accounts/logout/` - User logout
  - `/accounts/profile/` - View/Edit user profile
  - `/accounts/password-change/` - Change account password
- **Issue Management**
  - `/issues/` - Browse all community issues
  - `/issues/raise/` - Report a new issue
  - `/issues/assigned/` - View assigned issues *(Staff only)*
  - `/issues/<id>/update/` - Update issue status and remarks *(Staff only)*
  - `/issues/<id>/assign/` - Delegate issue to staff *(Admin only)*
  - `/issues/<id>/upvote/` - Upvote an issue
- **Administration**
  - `/admin/` - Secure Django Admin Panel

---
