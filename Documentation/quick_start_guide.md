
# Quick Start Guide

Welcome to the Quick Start Guide for the Database Creation Wizard. This guide will help you get the application up and running in just a few steps.

## 1. Prerequisites

- **Python** (version 3.8 or higher)
- **PostgreSQL** (version 12 or higher)
- **pip** (Python package installer)

## 2. Install the Database Creation Wizard

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/your-repo/database-creation-wizard.git
cd database-creation-wizard
```

## 3. Install Required Python Packages

Use pip to install all required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 4. Set Up PostgreSQL

1. Start your PostgreSQL service.
2. Create a new database and user with the following commands:

    ```bash
    sudo -u postgres psql -c "CREATE USER app_user WITH PASSWORD 'your_password';"
    sudo -u postgres psql -c "CREATE DATABASE app_db OWNER app_user;"
    ```

3. **Set Environment Variables**:

    You can set these in a `.env` file in the root directory:

    ```
    DB_NAME=app_db
    DB_USER=app_user
    DB_PASSWORD=your_password
    DB_HOST=localhost
    DB_PORT=5432
    ```

## 5. Run the Application

Simply execute the following command:

```bash
python run.py
```

The Database Creation Wizard will start and connect to PostgreSQL using the specified credentials.

## 6. Test the Setup

To test that everything is working, run the test suite:

```bash
python -m unittest discover tests/
```

## Next Steps

- Explore advanced usage in the [User Manual](user_manual.md).
- Check the [Error Handling Guide](error_handling_reference.md) for troubleshooting tips.

Enjoy using the Database Creation Wizard!
