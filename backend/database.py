from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 🔴 CHANGE USERNAME + PASSWORD
DATABASE_URL = "mysql+pymysql://root:sql_pass@localhost/crm_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# 📊 TABLE
class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    doctor = Column(String(100))
    topic = Column(String(255))
    outcome = Column(String(255))

# CREATE TABLE
Base.metadata.create_all(bind=engine)