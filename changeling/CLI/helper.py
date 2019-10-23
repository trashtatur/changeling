import logging
import os

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
    if os.path.exists(os.path.join(Pathfinder.get_wonderdraft_userfolder(),
                                   YMLConfigReader.get_profile_manager_directory_name(),
                                   YMLConfigReader.get_logger_directory_name())):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=os.path.join(Pathfinder.get_logger_directory_path(), 'debug.log'))
    return func