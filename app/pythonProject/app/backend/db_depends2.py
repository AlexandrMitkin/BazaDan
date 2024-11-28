from app.backend.db2 import SessionLocal

async def get_db():
    db2 = SessionLocal()
    try:
        yield db2
    finally:
        db2.close()