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
- Regular maintenance features ensuring the system remains up-to-date and functional.

## Setup and Installation
### Installation Steps

## Prerequisites
- **Python**: 3.9.6
- **RabbitMQ**: (for Celery)
- **Frontend**: React
- **Backend**: Django
- **Database**: SQLite3
- **APIs**: YNAB, Twilio

## Quick Start
    git clone <repository_url>
    cd your_project_directory
    make setup
    cp .env.example .env
    make run # Starts the Django development server
    make celery # Starts the Celery worker
    


## Project Structure
```plaintext
harmonydash/
├── app
│   ├── migrations
│   ├── models
│   ├── tests
│   └── utils
├── frontend
│   ├── public
│   └── src
│       ├── components
│       └── hooks
````

# Project Checklist

## Completed Tasks

- [x] Set up Django backend with RESTful API.
- [x] Create models and views for handling financial data.
- [x] Integrate React frontend with Django backend.
- [x] Install and configure `react-bootstrap` for UI styling.
- [x] Resolve React and `react-bootstrap` integration issues.
- [x] Implement functional components with hooks for dynamic data fetching.
- [x] Ensure error handling and loading states in React components.
- [x] Update `.gitignore` to include `node_modules` and standard JavaScript and Python ignores.
- [x] Remove `node_modules` directory from Git tracking.

## Current Focus

- [ ] Finalize styling and layout adjustments using `react-bootstrap`.
- [ ] Conduct comprehensive testing of frontend components.
- [ ] Optimize responsiveness of the UI for different screen sizes.
- [ ] Review and enhance error handling and data validation in the backend.
- [ ] Implement additional frontend features as per project requirements.
- [ ] Document frontend component usage and best practices.

## Upcoming Tasks

- [ ] Set up a testing framework for the backend (e.g., pytest for Django).
- [ ] Write unit tests for backend models and API views.
- [ ] Develop a continuous integration/continuous deployment (CI/CD) pipeline.
- [ ] Perform user acceptance testing (UAT) with a focus group.
- [ ] Refine and update the project documentation.
- [ ] Plan for scalability and potential deployment strategies.

## Optional Enhancements

- [ ] Integrate additional third-party services as needed (e.g., payment gateway, external APIs).
- [ ] Explore options for advanced data visualization.
- [ ] Consider implementing internationalization (i18n) and localization (l10n).
- [ ] Evaluate and potentially implement state management solutions (e.g., Redux).

## Makefile Main Commands
    make setup # Set up the project
    make test # Run tests
    make run # Run Django development server
    make celery # Run Celery worker
    make migrate # Apply database migrations
    ...other commands...