import os
from databases import Database
from sqlalchemy import MetaData, Table, Column, create_engine
from sqlalchemy import Integer, String

DB_URL = f"sqlite:///{os.path.relpath(os.getcwd(), '../')}.db"
db = Database(DB_URL)

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32)),
    Column("email", String(128)),
    Column("password", String(128)),
)


engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
