from datetime import datetime
from sqlalchemy import create_engine, String, ForeignKey, BigInteger, Numeric, Text, SmallInteger, Enum, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, declared_attr, Session, sessionmaker
from enum import Enum as PyEnum
from os import getenv
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(f"postgresql+psycopg2://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@localhost:{getenv('DB_PORT')}/{getenv('DB_NAME')}")
session = Session(engine)
engine.connect()

class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        if cls.__name__[-1] in ['s']:
            return cls.__name__.lower() + "es"
        return cls.__name__.lower() + "s"

class User(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255))
    phone_number: Mapped[str] = mapped_column(String(50))

class Category(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    products: Mapped[list["Product"]] = relationship(back_populates="category")

class Product(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categorys.id", ondelete="NO ACTION"))
    name: Mapped[str] = mapped_column(String(100))
    photo: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[int] = mapped_column(Numeric(12, 0))
    quantity: Mapped[int] = mapped_column(SmallInteger)

    category: Mapped["Category"] = relationship(back_populates="products")


Base.metadata.create_all(engine)