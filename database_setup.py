# database_setup.py
import mysql.connector
from credentials import db_credentials

def setup():
    db = mysql.connector.connect(**db_credentials)
    cursor = db.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarot_responses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            question VARCHAR(255) NOT NULL,
            date DATETIME NOT NULL,
            response TEXT NOT NULL,
            past_card VARCHAR(255) NOT NULL,
            present_card VARCHAR(255) NOT NULL,
            future_card VARCHAR(255) NOT NULL
        )
    ''')

    db.close()
