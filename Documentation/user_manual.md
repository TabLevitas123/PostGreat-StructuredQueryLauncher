
# User Manual for Database Creation Wizard

## Quick Start Guide

### Overview
The Database Creation Wizard is a tool for setting up and managing a PostgreSQL database, including schema creation, data ingestion, and access control.

### Quick Setup and Run
1. **Install Dependencies**: Ensure Python, PostgreSQL, and required Python packages are installed.
    ```bash
    pip install -r requirements.txt
    ```
2. **Set Up Database**: Configure PostgreSQL with a new user and database.
3. **Configure Environment**: Set environment variables for database credentials.

4. **Run the Application**:
    ```bash
    python run.py
    ```
   The application will start and connect to PostgreSQL using the specified credentials.

### Sample Commands
- **Create Schema**: `schema_creator.create_schema("my_schema")`
- **Ingest Data**: `data_ingestion_manager.ingest_csv("file.csv", "my_table")`


## High-Level Guide for Novices

### Purpose
The Database Creation Wizard simplifies database management. Its main components help you set up schemas, create tables, and import data from files.

### Core Features
1. **Schema Creation**: Organize your data by creating schemas within the database.
2. **Table Management**: Create and delete tables within your schemas.
3. **Data Ingestion**: Import data from common file types (CSV, JSON, etc.) into your tables.
4. **Index and Constraint Management**: Improve search speed and maintain data integrity.
5. **User Roles and Privileges**: Manage database access with role-based permissions.
6. **Testing and Validation**: Run built-in tests to ensure data accuracy.

### Common Tasks
1. **Setting Up a Schema**: Organize data with schemas.
    ```python
    schema_creator.create_schema("analytics")
    ```

2. **Creating a Table**: Define tables within a schema to store data.
    ```python
    table_manager.create_table("analytics", "sales_data", {"id": "SERIAL PRIMARY KEY", "name": "VARCHAR(100)", "amount": "FLOAT"})
    ```

3. **Ingesting Data**: Import data from a CSV or JSON file.
    ```python
    data_ingestion_manager.ingest_csv("sales.csv", "analytics.sales_data")
    ```

4. **Managing Access**: Assign roles to control access.
    ```python
    role_manager.create_role("analyst")
    privilege_manager.grant_privilege("analyst", "SELECT", "analytics.sales_data")
    ```

### Error Handling Basics
- **Database Connection Issues**: Check if PostgreSQL is running and your credentials are correct.
- **Schema/Table Not Found**: Verify that you created the schema/table before trying to access it.


## Low-Level Technical Guide for Professionals

### Detailed Module Descriptions

1. **Connection Manager**: Manages database connections.
    - **connect()**: Establishes a connection to PostgreSQL.
    - **get_cursor()**: Retrieves a cursor for executing commands.
    - **close_connection()**: Safely closes the connection.

2. **Schema Creator**: Handles schema creation and deletion.
    - **create_schema(schema_name)**: Creates a new schema.
    - **drop_schema(schema_name, cascade)**: Deletes a schema with an optional cascade.

3. **Table Manager**: Manages table setup.
    - **create_table(schema_name, table_name, columns)**: Creates a table with columns.
    - **drop_table(schema_name, table_name, cascade)**: Deletes a table.

4. **Data Ingestion Manager**: Imports data from files.
    - **ingest_csv(file_path, table_name)**: Loads CSV data.
    - **ingest_json(file_path, table_name)**: Loads JSON data.
    - **ingest_xml(file_path, table_name)**: Loads XML data.

5. **Index Manager**: Manages indexes for faster search.
    - **create_index(table_name, index_name, columns)**: Adds an index.
    - **drop_index(index_name)**: Removes an index.

### Advanced Configurations
- **Environment Variables**: Store credentials securely in `.env`.
- **Custom Schema Configurations**: Adjust schema and table setup dynamically.

### Workflow Details
1. **Data Ingestion Process**
    - Verify the file format and load data based on the table schema.
    - Data is validated for consistency and inserted into the table.
2. **Schema and Table Management**
    - Each schema/table is defined by attributes and constraints to ensure data integrity.
3. **Testing Suite Execution**
    - Runs tests, logs results, and highlights issues with data integrity and role permissions.

### Error Handling
- **Common Exceptions**:
    - **ConnectionError**: Raised if the database is unreachable.
    - **DataValidationError**: Occurs if file data doesn't match table schema.
    - **SchemaExistsError**: Raised if attempting to create an existing schema.

- **Debugging Tips**:
    - Check PostgreSQL logs for connection issues.
    - Validate environment variables and ensure correct permissions.

### Example Usage for Developers
To create an automated workflow:

```python
# Import modules
from connection_manager import ConnectionManager
from schema_creator import SchemaCreator
from data_ingestion_manager import DataIngestionManager

# Initialize components
conn_manager = ConnectionManager()
schema_creator = SchemaCreator()
data_manager = DataIngestionManager()

# Workflow
conn = conn_manager.connect()
schema_creator.create_schema("analytics")
data_manager.ingest_csv("data.csv", "analytics.sales_data")
conn_manager.close_connection(conn)
```

This guide provides a complete reference for setting up, using, and troubleshooting the Database Creation Wizard.
