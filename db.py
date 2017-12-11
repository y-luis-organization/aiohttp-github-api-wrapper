from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from organizations.model import Organization, Base


async def init_sqlite(app):
    """
    Initialize connection to database
    :param app:
    :return:
    """
    conf = app['config']
    engine = create_engine(conf['sqlite']['database'])
    Session = sessionmaker(bind=engine)
    app['session'] = Session()
    Base.metadata.create_all(engine)


async def close_sqlite(app):
    """
    Closes connection to database, flushing all changes
    :param app:
    :return:
    """
    app['session'].commit()
    app['session'].close()


def get_organization(session, organization_name):
    """
    Get an organization by its name
    :param session:
    :param organization_name:
    :return:
    """
    return session.query(Organization).filter_by(name=organization_name).first()


def save_organization(session, organization_name, repos):
    """
    Save an organization
    :param session:
    :param organization_name:
    :param repos:
    :return:
    """
    organization = Organization(name=organization_name, public_repos=repos['public_repos'],
                     biggest_repo_name=repos['biggest_repo']['name'], biggest_repo_size=repos['biggest_repo']['size'])
    session.add(organization)


class RecordNotFound(Exception):
    """Requested record in database was not found"""
