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
    Column("firstname", String(32)),
    Column("lastname", String(64)),
    Column("birthday", String(10)),
    Column("email", String(128)),
    Column("address", String(128)),
)

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
