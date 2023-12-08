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

## Current Progress
### Completed Features
- [x] Basic Django setup and configuration.
- [x] YNAB API integration for financial data.
- [x] Models for FinancialSettings and Transactions.
- [x] Basic financial data processing logic.
- [x] Celery and RabbitMQ setup for task processing.

### Work In Progress (WIP)
- [ ] Advanced financial analysis features.
- [ ] Frontend development with React.
- [ ] Additional Celery tasks for data synchronization.

### Planned Features
- [ ] Comprehensive testing suite.
- [ ] Dockerization for streamlined deployment.
- [ ] Implementation of user authentication and authorization.

## Makefile Main Commands
    make setup # Set up the project
    make test # Run tests
    make run # Run Django development server
    make celery # Run Celery worker
    make migrate # Apply database migrations
    ...other commands...