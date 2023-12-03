# Family Harmony Dashboard

## Overview
The Family Harmony Dashboard is a specialized app designed to help families manage complex schedules, finances, and household tasks efficiently. It's tailored for parents with different work shifts, childcare responsibilities, and financial management needs.

## Features

### Central Calendar & Scheduler
- Integrates work schedules and adapts to changes.
- Visual representation of daily routines.

### Financial Management
- YNAB integration for budget tracking.
- Dashboard for bills and automated financial management.

### Communication & Reminders
- Reminder setup from text messages.
- In-app communication and important notifications.

### Task & Cleaning Schedule
- Customizable chore lists and reminders.

### Time Management & Leisure Planning
- Suggests activities based on free time.
- Plans for family and individual relaxation time.

### Maintenance & Updates
- User-friendly interface with manual adjustment capabilities.

## Tech Stack

- **Frontend**: React
- **Backend**: Django
- **Database**: SQLite3
- **APIs**: YNAB, Twilio

## Project Structure
```plaintext
harmonydash/
├── app/                           # Main Django application
│   ├── migrations/                # Database migrations
│   ├── admin.py                   # Admin site configuration
│   ├── models.py                  # Database models
│   │   ├── user_profile.py        # Model for user profiles
│   │   ├── schedule.py            # Model for user schedules
│   │   ├── financial_info.py      # Model for financial information
│   │   └── task.py                # Model for tasks and chores
│   ├── serializers.py             # Serializers for models
│   ├── views.py                   # Views for the application
│   ├── tests.py                   # Test cases for the app
│   └── urls.py                    # URL configurations for the app
├── harmonydash/                   # Django project folder
│   ├── settings.py                # Project settings
│   ├── urls.py                    # Project URL declarations
│   ├── wsgi.py                    # WSGI configuration for deployment
│   └── views.py                   # Views for project-level URLs (like root redirect)
├── frontend/                      # React frontend application
│   ├── src/                       # Source files for React
│   │   ├── components/            # React components
│   │   ├── App.js                 # Main React component
│   │   └── index.js               # Entry point for React app
│   └── public/                    # Public assets for React app
├── venv/                          # Virtual environment for the project
├── manage.py                      # Django command-line utility script
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies
````

## Getting Started Checklist

### Set up Django Backend
- [x] Initialize Django project (`django-admin startproject harmonydash`).
- [x] Create Django app within the project (`python manage.py startapp app`).
- [x] Design and define database models in `app/models.py`.
- [x] Set up and configure a SQLite3 database (default for Django).
- [ ] Migrate to PostgreSQL if the project scales beyond personal use (Future Task).

### Prepare Backend for React Frontend
- [ ] Create RESTful APIs using Django REST Framework.
- [ ] Ensure proper CORS configuration for secure AJAX requests.
- [ ] Implement token-based authentication for API access.
- [ ] Test API endpoints for CRUD operations.

### Develop React Frontend
- [ ] Initialize React application (`npx create-react-app frontend`).
- [ ] Create basic React components for the user interface in the `src/components/` directory.

### Integrate APIs
- [ ] Connect to the YNAB API for financial data management.
- [ ] Implement the Twilio API for SMS reminders.

### Database Configuration
- [x] Connect Django to the SQLite3 database via the settings in `harmonydash/settings.py`.

### Create Views and URLs
- [x] Define views in `app/views.py`.
- [x] Set up URL patterns in `app/urls.py` and `harmonydash/urls.py`.

### Testing
- [ ] Write test cases for each Django app component in `app/tests.py`.
- [ ] Run tests to ensure stability and functionality.

### Deployment
- [ ] Deploy the Django backend and React frontend on a suitable platform (e.g., Heroku, AWS).

### Explore Mobile App Development (Future Step)
- [ ] Research mobile app development frameworks (e.g., React Native, Flutter).
- [ ] Evaluate the feasibility of converting the existing React app to a mobile app.
- [ ] Plan the user interface and experience for mobile.
- [ ] Determine additional features or adjustments needed for mobile usability.
- [ ] Consider the integration of mobile-specific features (e.g., push notifications, offline access).
- [ ] Assess the budget and resources required for mobile app development.

