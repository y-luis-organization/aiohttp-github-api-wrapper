import argparse
import asyncio
import logging
import sys

from aiohttp import web
from trafaret_config import commandline

from db import init_sqlite, close_sqlite
from organizations.utils import TRAFARET
from routes import setup_routes


def init(loop, argv):
    ap = argparse.ArgumentParser()
    commandline.standard_argparse_options(ap,
                                          default_config='./config/organizations.yaml')
    #
    # define your command-line arguments here
    #
    options = ap.parse_args(argv)

    config = commandline.config_from_options(options, TRAFARET)

    # setup application and extensions
    app = web.Application(loop=loop)

    # load config from yaml file in current dir
    app['config'] = config

    # create connection to the database
    app.on_startup.append(init_sqlite)

    app.on_cleanup.append(close_sqlite)

    # setup views and routes
    setup_routes(app)

    return app


def main(argv):
    # init logging
    logging.basicConfig(level=logging.DEBUG)

    loop = asyncio.get_event_loop()

    app = init(loop, argv)
    web.run_app(app,
                host=app['config']['host'],
                port=app['config']['port'])


if __name__ == '__main__':
    main(sys.argv[1:])
