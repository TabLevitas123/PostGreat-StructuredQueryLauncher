
# Database Creation Wizard - Project Overview

## Purpose
The Database Creation Wizard is a comprehensive tool designed to simplify PostgreSQL database management. This wizard enables users to create databases, schemas, tables, indexes, constraints, and roles with a user-friendly interface. Additionally, the tool supports data ingestion from multiple formats, including CSV, JSON, XML, SQL dumps, and Excel files, automating the process of populating database tables.

## Key Features
1. **Database Creation Wizard**: Step-by-step interface for creating and configuring PostgreSQL databases, schemas, and tables.
2. **Data Ingestion**: Automated ingestion of data from CSV, JSON, XML, SQL, and Excel files.
3. **Testing Suite**: Comprehensive suite of tests for each module, ensuring code reliability and integrity.
4. **Test Runner Interface**: User-friendly interface for running all tests and viewing results.

## Architecture
The project is organized into modular components:
- **Database Management Modules**: Responsible for database structure creation (tables, indexes, constraints, etc.)
- **Data Ingestion Modules**: Scripts for handling and inserting data from different file types.
- **Testing Suite**: Separate tests for each module, ensuring error-free operation.
- **Main Program**: Includes CLI and interface for launching the wizard or data ingestion functionality.

## Project Modules
- **main.py**: Main entry point, providing an interactive CLI to choose between running the wizard or data ingestion.
- **Database Modules**: Separate files for each type of database operation (table creation, index management, etc.).
- **Data Ingestion Manager**: Manages the ingestion process and routes files to appropriate ingestion scripts.
- **Test Runner**: Runs all tests with a UI interface for easy monitoring.

## Dependencies
- **PostgreSQL**: Database backend.
- **Python Libraries**: psycopg2, pandas, unittest, tkinter (UI library).
- **Data Ingestion Libraries**: pandas (for Excel), xml.etree.ElementTree (for XML).

## Workflow Summary
1. **Launch Main Program**: Choose to create database structures or ingest data.
2. **Data Structure Setup**: Use the wizard interface to configure database schemas, tables, and other components.
3. **Data Ingestion**: Ingest data from files into specified tables, utilizing automated scripts.
4. **Run Tests**: Verify functionality and detect issues using the test runner.

For further details, refer to individual module documentation.
