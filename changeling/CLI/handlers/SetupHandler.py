import logging
import os

import click

from changeling.file_interactions.YMLConfigReader import YMLConfigReader
from changeling.pathfinder import Pathfinder


class SetupHandler:

    def setup(self):
        click.echo('Create changeling manager directory if it doesn\'t exist yet')
        if not self.__sanity_check_main_dir():
            self.__create_profile_manager_folderstructure()
        click.echo('Creating logging directory if it doesn\'t exist yet')
        if not self.__sanity__check_logger_dir():
            self.__create_logger_directory()
        click.echo('Creating inactive modules directory if it doesn\'t exist yet')
        if not self.__sanity_check_inactive_dir():
            self.__create_deactivated_modules_folder()
        if self.is_setup():
            logging.getLogger('debug').info('Setup completed')

    def __create_logger_directory(self):
        try:
            os.mkdir(
                os.path.join(
                    Pathfinder.get_wonderdraft_userfolder(),
                    YMLConfigReader.get_profile_manager_directory_name(),
                    YMLConfigReader.get_logger_directory_name()
                )
            )
        except OSError as exception:
            logging.getLogger('debug').exception('You can\'t create the logger folder twice')

    def __create_profile_manager_folderstructure(self):
        try:
            os.mkdir(
                os.path.join(
                    Pathfinder.get_wonderdraft_userfolder(),
                    YMLConfigReader.get_profile_manager_directory_name()
                )
            )
        except OSError as exception:
            logging.getLogger('debug').exception('You can\'t create the profile manager folder twice')

    def __create_deactivated_modules_folder(self):
        try:
            os.mkdir(
                os.path.join(Pathfinder.get_wonderdraft_userfolder(),
                             YMLConfigReader.get_profile_manager_directory_name(),
                             YMLConfigReader.get_deactivated_modules_folder_name()
                             )
            )
        except OSError as exception:
            logging.getLogger('debug').exception('You can\'t create the inactive assets folder twice')


    def __sanity_check_main_dir(self):
        return os.path.exists(
            os.path.join(
                Pathfinder.get_wonderdraft_userfolder(),
                YMLConfigReader.get_profile_manager_directory_name()
            )
        )

    def __sanity_check_inactive_dir(self):
        return os.path.exists(
            os.path.join(
                Pathfinder.get_wonderdraft_userfolder(),
                YMLConfigReader.get_profile_manager_directory_name(),
                YMLConfigReader.get_deactivated_modules_folder_name()
            )
        )

    def __sanity__check_logger_dir(self):
        return os.path.exists(
            os.path.join(
                Pathfinder.get_wonderdraft_userfolder(),
                YMLConfigReader.get_profile_manager_directory_name(),
                YMLConfigReader.get_logger_directory_name()
            )
        )

    def is_setup(self):
        return self.__sanity_check_main_dir() \
               and self.__sanity_check_inactive_dir() \
               and self.__sanity__check_logger_dir()
