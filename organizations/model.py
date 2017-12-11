from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Organization(Base):
    __tablename__ = 'organizations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    public_repos = Column(Integer, nullable=False)
    biggest_repo_name = Column(String(200), nullable=False)
    biggest_repo_size = Column(Integer, nullable=False)