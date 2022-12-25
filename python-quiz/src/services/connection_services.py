import os
import sqlite3


dir = os.path.dirname(__file__)  # pylint: disable=redefined-builtin


def get_db_connection():
    """Connects to SQL database

    Returns:
        Connection: database connection to questions db.
    """
    dbconnection = sqlite3.connect(os.path.join(dir, "..", "..", "data", "data.db"))
    return dbconnection
