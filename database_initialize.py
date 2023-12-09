# Imports
import os
from database_interaction import sql_query

# Loading environment
import dotenv
dotenv.load_dotenv()


DATABASE_URI = os.getenv('DATABASE_URI')

# Initializing table
if __name__ == '__main__':
    sql_query(
        DATABASE_URI,
        ('''CREATE TABLE IF NOT EXISTS conversations (
    id SERIAL PRIMARY KEY,
    conversation JSON
);
TRUNCATE TABLE conversations;''',)
    )
