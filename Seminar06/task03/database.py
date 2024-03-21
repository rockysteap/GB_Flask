# Каждая задача должна содержать поля "название", "описание" и "статус" (выполнена/не выполнена).
import os
from databases import Database
from sqlalchemy import MetaData, Table, Column, create_engine
from sqlalchemy import Integer, String, Enum
from models import Status

DB_URL = f"sqlite:///{os.path.relpath(os.getcwd(), '../')}.db"
db = Database(DB_URL)

metadata = MetaData()

tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(128)),
    Column("description", String(64)),
    Column("status", Enum(Status)),
)

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
