# Job Portal

A full-stack Django web application designed to connect employers with job seekers.

## Features

- **User Authentication**: Secure sign up, log in, and log out functionality.
- **Role-Based Users**: Support for `Employer`, `Job Seeker`, and `Admin` roles using a custom user model.
- **Job Management for Employers**:
  - Post new job listings with titles, descriptions, locations, and salaries.
  - View, edit, and delete jobs they have posted.
- **Job Browsing for Seekers**:
  - View all available job listings.
  - View detailed information about specific jobs.
  - Apply to jobs with a single click.
  - Track jobs they have already applied to.
- **Responsive UI**: A clean, centralized layout using a unified `base.html` structure.

## Tech Stack

- **Backend**: Django 6.0
- **Database**: SQLite (Default)
- **Frontend**: HTML5, CSS3, Django Templates

## Project Structure

- `jobportal/`: Core Django project configuration and settings.
- `accounts/`: Application handling user authentication, custom user models, and login/signup views.
- `jobs/`: Application handling core business logic for jobs, applications, and their corresponding views and models.
- `templates/`: Global templates folder containing the `base.html` layout.

## Installation & Setup

1. **Navigate to the project directory**:
   ```bash
   cd "Job Portal"
   ```

2. **Activate the virtual environment**:
   ```bash
   .\venv_jobportal\Scripts\activate
   ```

3. **Install Dependencies**:
   If not already installed, make sure Django is installed in your environment:
   ```bash
   pip install django
   ```

4. **Apply Migrations**:
   Run the following commands to create the database schema:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1. Start by navigating to the home page to see available jobs.
2. Click **Sign Up** to create a new account. You can register as an `Employer` or a `Job Seeker`.
3. If you are an **Employer**, navigate to **Post a Job** to create a new listing. You can manage your listings under **My Posted Jobs**.
4. If you are a **Job Seeker**, browse the jobs, click on a job to view details, and hit **Apply Now** to submit an application. Track your progress under **My Applications**.
