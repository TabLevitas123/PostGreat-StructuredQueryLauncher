
# Deployment and Configuration Guide

## System Requirements

### Software
- **Python**: Version 3.8 or higher
- **PostgreSQL**: Version 12 or higher
- **pip**: Python package manager for installing dependencies

### Hardware
- **Memory**: Minimum 4 GB RAM recommended
- **Disk Space**: At least 500 MB for data storage and application files

## Installation Steps

### 1. Install Python and Dependencies
Ensure Python is installed, then install required packages:

```bash
# Install pip if necessary
sudo apt-get install python3-pip

# Install dependencies
pip install -r requirements.txt
```

### 2. Set Up PostgreSQL
Install PostgreSQL and create a new database for the application.

```bash
# Install PostgreSQL
sudo apt-get install postgresql

# Create a PostgreSQL user and database
sudo -u postgres psql -c "CREATE USER app_user WITH PASSWORD 'your_password';"
sudo -u postgres psql -c "CREATE DATABASE app_db OWNER app_user;"
```

## Configuration

### Environment Variables
Set environment variables in a `.env` file or directly in your shell:

```bash
export DB_NAME="app_db"
export DB_USER="app_user"
export DB_PASSWORD="your_password"
export DB_HOST="localhost"
export DB_PORT="5432"
```

### Sample `.env` file
You can create a `.env` file for easy configuration management:

```
DB_NAME=app_db
DB_USER=app_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 3. Cloud Deployment
- **AWS**: Set up an EC2 instance, install dependencies, and configure environment variables as above.
- **Heroku**: Configure a PostgreSQL add-on and set environment variables in the dashboard.

### 4. Containerization with Docker

#### Dockerfile Example
```dockerfile
# Use Python base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app code
COPY . .

# Set environment variables
ENV DB_NAME=app_db
ENV DB_USER=app_user
ENV DB_PASSWORD=your_password
ENV DB_HOST=localhost
ENV DB_PORT=5432

# Run the application
CMD ["python", "run.py"]
```

#### Build and Run Docker Container
```bash
# Build Docker image
docker build -t database_creation_wizard .

# Run Docker container
docker run -p 8000:8000 --env-file .env database_creation_wizard
```

## Running the Application Locally

1. **Start PostgreSQL**: Ensure PostgreSQL is running.
2. **Run Application**:

```bash
python run.py
```

The application will start and connect to the specified PostgreSQL database.
