
# Setup Guide (Detailed, Beginner-Friendly)

Welcome to the Setup Guide! This guide will walk you through each step of setting up the Database Creation Wizard. Every instruction is explained in simple terms so that anyone, even with no technical experience, can follow along.

## Step 1: Install Python

### What is Python?
Python is the programming language the Database Creation Wizard is written in. We need to install it first.

1. Go to [python.org](https://www.python.org/downloads/).
2. Download the latest version of Python (3.8 or newer).
3. Follow the installation steps provided by the installer.
4. **IMPORTANT**: During installation, make sure you check the box that says "Add Python to PATH".

## Step 2: Install PostgreSQL

### What is PostgreSQL?
PostgreSQL is the database system that will store all your data.

1. Go to [postgresql.org](https://www.postgresql.org/download/).
2. Download and install PostgreSQL. Follow the instructions in the installer.
3. During installation, set a password for the "postgres" user – this is the main account.

## Step 3: Install pip

### What is pip?
Pip is a tool to help us install the extra software needed by Python.

1. Open a terminal or command prompt.
2. Type `python -m ensurepip --upgrade` and press Enter.
3. Pip should now be installed.

## Step 4: Clone the Repository

### What does "clone the repository" mean?
It means copying all the files from the internet to your computer.

1. Open a terminal or command prompt.
2. Type:

    ```bash
    git clone https://github.com/your-repo/database-creation-wizard.git
    ```

3. Go into the project folder by typing:

    ```bash
    cd database-creation-wizard
    ```

## Step 5: Install Required Packages

### What are packages?
Packages are extra tools that the Database Creation Wizard needs to work.

1. Type:

    ```bash
    pip install -r requirements.txt
    ```

2. Wait until all packages finish installing.

## Step 6: Set Up the Database in PostgreSQL

1. Open PostgreSQL (you may need to use pgAdmin or the command line).
2. Create a new user and database:

    ```bash
    sudo -u postgres psql -c "CREATE USER app_user WITH PASSWORD 'your_password';"
    sudo -u postgres psql -c "CREATE DATABASE app_db OWNER app_user;"
    ```

### Step 7: Configure Environment Variables

1. **What are Environment Variables?** They are special settings the application needs to connect to the database.

2. Create a file named `.env` in the project folder.

3. Add the following information to it (replace `your_password` with your database password):

    ```
    DB_NAME=app_db
    DB_USER=app_user
    DB_PASSWORD=your_password
    DB_HOST=localhost
    DB_PORT=5432
    ```

## Step 8: Start the Application

1. To start the application, type:

    ```bash
    python run.py
    ```

2. If everything is set up, the application will connect to your database.

## Step 9: Testing

To check if the setup is complete and everything works:

1. Type the following to run the tests:

    ```bash
    python -m unittest discover tests/
    ```

2. If tests pass, your setup is complete!

Congratulations on setting up the Database Creation Wizard!
