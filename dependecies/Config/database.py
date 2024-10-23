from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


# URL_DATABASE = f"mysql+pymysql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:3306/${DB_NAME}"

URL_DATABASE = "mysql+pymysql://admin:Graphic8012@busappdb.c9wo86eco8pm.eu-north-1.rds.amazonaws.com:3306/busdb"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit = False , autoflush=False , bind = engine)

Base = declarative_base()