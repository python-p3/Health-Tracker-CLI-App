# Health and Fitness Tracker CLI

## Overview

The Health and Fitness Tracker CLI is a command-line interface application that allows users to log their daily activities, meals, and health metrics for effective health tracking and analysis.

## Features

- User registration
- Logging of activities (type, duration)
- Logging of meals (food items, nutritional information)
- Logging of health metrics (weight, sleep duration)
- Viewing daily summaries of activities, meals, and health metrics

## Getting Started

### Prerequisites

- Python (version 3.9 recommended)
- Pipenv (for virtual environment and package management)
- SqlAlchemy

### Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:python-p3/Health-Tracker-CLI-App.git
   ```
2. Navigate to the project
    ```
    cd HEALTH CLI
    ```

3. Install dependencies 
    ``` 
    pipenv install 
    ```

## Database Setup
1. Initialize the database:

    ```
    pipenv run python -m alembic init alembic
    ```
2. Apply initial migrations:
    ```
    pipenv run python -m alembic upgrade head 
## Usage
1. Register User 
    ```
    pipenv run python3 cli.py register-user 
    ```
2. Log an activity
    ```
    pipenv run python cli.py add-activity
    ```
3. Log a meal 
    ```
    pipenv run python cli.py add-meal
    ```
4. Log health metrics
    ```
    pipenv run python cli.py add-health-metric 
    ```
5. Viewing summary 
    ```
    pipenv run python cli.py view-summary
    ```

## Author & License 
Michael Kiptoo & [MIT LICENSE](LICENSE)