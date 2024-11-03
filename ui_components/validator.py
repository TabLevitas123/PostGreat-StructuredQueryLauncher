
class Validator:
    @staticmethod
    def validate_not_empty(value, field_name=""):
        if not value.strip():
            raise ValueError(f"{field_name} cannot be empty.")
        return value

    @staticmethod
    def validate_integer(value, field_name=""):
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"{field_name} must be an integer.")

    @staticmethod
    def validate_positive(value, field_name=""):
        integer_value = Validator.validate_integer(value, field_name)
        if integer_value <= 0:
            raise ValueError(f"{field_name} must be a positive integer.")
        return integer_value

    @staticmethod
    def validate_columns(columns_str):
        columns = columns_str.split(",")
        if not all(columns):
            raise ValueError("Each column name must be non-empty.")
        return [col.strip() for col in columns]
