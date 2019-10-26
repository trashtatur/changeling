import logging
import os
from colorama import init

import click

from changeling.CLI.handlers.SetupHandler import SetupHandler
from changeling.file_interactions.YMLConfigReader import YMLConfigReader
from changeling.pathfinder import Pathfinder


def is_setup(func):
    handler = SetupHandler()

    @click.command(hidden=True)
    def is_not_setup():
        click.echo('You need to call setup command first')

    if handler.is_setup():
        return func
    else:
        return is_not_setup


def setup_logging(func):
    if os.path.exists(os.path.join(Pathfinder.get_logger_directory_path())):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=os.path.join(Pathfinder.get_logger_directory_path(), 'debug.log'))
    return func


def init_colorama(func):
    init()
    return func
