from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session  

def test_db_connection(engine: Engine, session: Session):
    try:
        with engine.connect():
            result = session.execute(text("SELECT 1")).fetchall()
        print("Database connection successful.")
    except OperationalError as e:
        print(f"Database connection failed: {e}")
