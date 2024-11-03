
import json
import os
from cryptography.fernet import Fernet

class Config:
    CONFIG_FILE = "config.json"
    ENCRYPTION_KEY_FILE = "encryption.key"

    def __init__(self):
        self.config = {
            "host": "",
            "port": 5432,
            "user": "",
            "password": "",
            "database": ""
        }
        self.key = self.load_encryption_key()
        self.load_config()

    def load_encryption_key(self):
        if not os.path.exists(self.ENCRYPTION_KEY_FILE):
            key = Fernet.generate_key()
            with open(self.ENCRYPTION_KEY_FILE, "wb") as key_file:
                key_file.write(key)
        else:
            with open(self.ENCRYPTION_KEY_FILE, "rb") as key_file:
                key = key_file.read()
        return Fernet(key)

    def encrypt_value(self, value):
        return self.key.encrypt(value.encode()).decode()

    def decrypt_value(self, encrypted_value):
        return self.key.decrypt(encrypted_value.encode()).decode()

    def load_config(self):
        if os.path.exists(self.CONFIG_FILE):
            with open(self.CONFIG_FILE, "r") as file:
                encrypted_config = json.load(file)
                self.config = {k: self.decrypt_value(v) for k, v in encrypted_config.items()}

    def save_config(self):
        encrypted_config = {k: self.encrypt_value(v) for k, v in self.config.items()}
        with open(self.CONFIG_FILE, "w") as file:
            json.dump(encrypted_config, file)

    def get(self, key):
        return self.config.get(key)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()

    def validate(self):
        required_keys = ["host", "port", "user", "password", "database"]
        for key in required_keys:
            if not self.config[key]:
                raise ValueError(f"Configuration for '{key}' is missing.")
