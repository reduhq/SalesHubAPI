from saleshubapi.db.session import SessionLocal

def get_connection():
    try:
        return SessionLocal()
    except Exception as e:
        print(e)