# Imports
import psycopg2
from psycopg2.extensions import connection as Database, cursor as Cursor
from typing import Any


class OpenDatabase(object):
    def __init__(self, database_uri: str):
        self.__database_url = database_uri

    def __enter__(self):
        self.__database: Database = psycopg2.connect(self.__database_url)
        return self.__database

    def __exit__(self, exc_type, exc_value, traceback):
        self.__database.close()


class OpenCursor(object):
    def __init__(self, database: Database):
        self.__database = database

    def __enter__(self):
        self.__cursor: Cursor = self.__database.cursor()
        return self.__cursor

    def __exit__(self, exc_type, exc_value, traceback):
        self.__cursor.close()


def sql_query(database_uri: str, query: tuple[str] | tuple[str, tuple[Any, ...]]) -> None:
    with OpenDatabase(database_uri) as database:
        with OpenCursor(database) as cursor:
            cursor.execute(*query)
            database.commit()
