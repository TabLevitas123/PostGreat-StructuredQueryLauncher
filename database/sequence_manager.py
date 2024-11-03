
from connection_manager import ConnectionManager
from constants import ERROR_MESSAGES

class SequenceManager:
    def __init__(self):
        self.connection_manager = ConnectionManager()

    def create_sequence(self, sequence_name, start=1, increment=1, min_value=None, max_value=None, cycle=False):
        if not sequence_name:
            raise ValueError("Sequence name cannot be empty.")
        
        sequence_options = f"START {start} INCREMENT {increment}"
        if min_value is not None:
            sequence_options += f" MINVALUE {min_value}"
        if max_value is not None:
            sequence_options += f" MAXVALUE {max_value}"
        if cycle:
            sequence_options += " CYCLE"
        else:
            sequence_options += " NO CYCLE"

        create_sequence_query = f"CREATE SEQUENCE {sequence_name} {sequence_options};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(create_sequence_query)
                print(f"Sequence '{sequence_name}' created successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def drop_sequence(self, sequence_name, cascade=False):
        drop_query = f"DROP SEQUENCE {sequence_name}"
        drop_query += " CASCADE;" if cascade else ";"

        try:
            with self.connection_manager as cursor:
                cursor.execute(drop_query)
                print(f"Sequence '{sequence_name}' dropped successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def alter_sequence(self, sequence_name, **options):
        if not sequence_name:
            raise ValueError("Sequence name is required to alter sequence.")
        
        alteration_clauses = []
        for option, value in options.items():
            if option in ["increment", "min_value", "max_value", "restart"]:
                alteration_clauses.append(f"{option.upper()} {value}")
        
        alter_sequence_query = f"ALTER SEQUENCE {sequence_name} " + " ".join(alteration_clauses) + ";"

        try:
            with self.connection_manager as cursor:
                cursor.execute(alter_sequence_query)
                print(f"Sequence '{sequence_name}' altered successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)
