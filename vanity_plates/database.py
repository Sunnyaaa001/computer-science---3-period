from dotenv import load_dotenv
import os
from flask import Flask
from sqlalchemy import create_engine
from model import Base
from sqlalchemy.orm import sessionmaker

load_dotenv()

load_dotenv()
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(BASE_DIR, os.environ.get("DB_PATH", "vanity_plate.db"))
DATABASE_URL = f"sqlite:///{db_file}"

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

app = Flask(__name__)


Base.metadata.create_all(engine)
   