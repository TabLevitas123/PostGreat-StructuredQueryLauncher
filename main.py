
import sys
from database_creation_wizard import DatabaseCreationWizard
from data_ingestion_manager import DataIngestionManager

def run_wizard():
    # Initialize and start the database creation wizard interface
    wizard = DatabaseCreationWizard()
    wizard.run()

def run_data_ingestion():
    manager = DataIngestionManager()
    print("Choose data ingestion type:")
    print("1. CSV")
    print("2. JSON")
    print("3. XML")
    print("4. SQL Dump")
    print("5. Excel")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        table_name = input("Enter table name: ")
        csv_file_path = input("Enter CSV file path: ")
        columns = input("Enter column names (comma-separated): ").split(",")
        manager.ingest_csv(table_name, csv_file_path, columns)

    elif choice == "2":
        table_name = input("Enter table name: ")
        json_file_path = input("Enter JSON file path: ")
        columns = input("Enter column names (comma-separated): ").split(",")
        manager.ingest_json(table_name, json_file_path, columns)

    elif choice == "3":
        table_name = input("Enter table name: ")
        xml_file_path = input("Enter XML file path: ")
        columns = input("Enter column names (comma-separated): ").split(",")
        root_tag = input("Enter root tag name: ")
        row_tag = input("Enter row tag name: ")
        manager.ingest_xml(table_name, xml_file_path, columns, root_tag, row_tag)

    elif choice == "4":
        sql_file_path = input("Enter SQL dump file path: ")
        manager.ingest_sql(sql_file_path)

    elif choice == "5":
        table_name = input("Enter table name: ")
        excel_file_path = input("Enter Excel file path: ")
        sheet_name = input("Enter sheet name: ")
        columns = input("Enter column names (comma-separated): ").split(",")
        manager.ingest_excel(table_name, excel_file_path, sheet_name, columns)

    else:
        print("Invalid choice. Exiting data ingestion.")

if __name__ == "__main__":
    print("Database Creation Wizard")
    print("1. Run Wizard")
    print("2. Run Data Ingestion")

    option = input("Enter option (1-2): ")

    if option == "1":
        run_wizard()
    elif option == "2":
        run_data_ingestion()
    else:
        print("Invalid option. Exiting program.")
