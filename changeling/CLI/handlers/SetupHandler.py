import logging
from colorama import Fore, Style
import os

import click

from changeling.file_interactions.YMLConfigReader import YMLConfigReader
from changeling.pathfinder import Pathfinder


class SetupHandler:

    def setup(self):
        if not self.is_setup():
            self.display_welcome_message()
        click.echo(Fore.LIGHTMAGENTA_EX+'Create changeling manager directory if it doesn\'t exist yet')
        if not self.__sanity_check_main_dir():
            self.__create_profile_manager_folderstructure()
        click.echo(Fore.LIGHTMAGENTA_EX+'Creating logging directory if it doesn\'t exist yet')
        if not self.__sanity__check_logger_dir():
            self.__create_logger_directory()
        click.echo(Fore.LIGHTMAGENTA_EX+'Creating inactive modules directory if it doesn\'t exist yet')
        if not self.__sanity_check_inactive_assets_dir():
            self.__create_deactivated_assets_folder()
        click.echo(Fore.LIGHTMAGENTA_EX+'Creating inactive themes directory if it doesn\'t exist yet')
        if not self.__sanity_check_inactive_themes_dir():
            self.__create_deactivated_themes_folder()
        click.echo(Fore.LIGHTMAGENTA_EX+'Creating inactive brushes directory if it doesn\'t exist yet')
        if not self.__sanity_check_inactive_brushes_dir():
            self.__create_deactivated_brushes_folder()
        if self.is_setup():
            logging.getLogger('debug').info('Setup completed')

    def __create_logger_directory(self):
        try:
            os.mkdir(
                os.path.join(
                    Pathfinder.get_wonderdraft_userfolder(),
                    YMLConfigReader.get_changeling_manager_directory_name(),
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
                    YMLConfigReader.get_changeling_manager_directory_name()
                )
            )
        except OSError as exception:
            logging.getLogger('debug').exception('You can\'t create the profile manager folder twice')

    def __create_deactivated_folder_generic(self, path_splitter, name):
        try:
            os.mkdir(
                os.path.join(Pathfinder.get_wonderdraft_userfolder(),
                             YMLConfigReader.get_changeling_manager_directory_name(),
                             path_splitter
                             )
            )
        except OSError as exception:
            logging.getLogger('debug').exception('You can\'t create the inactive ' + name + ' folder twice')

    def __create_deactivated_assets_folder(self):
        self.__create_deactivated_folder_generic(YMLConfigReader.get_deactivated_assets_folder_name(), 'assets')

    def __create_deactivated_themes_folder(self):
        self.__create_deactivated_folder_generic(YMLConfigReader.get_deactivated_themes_folder_name(), 'themes')

    def __create_deactivated_brushes_folder(self):
        self.__create_deactivated_folder_generic(YMLConfigReader.get_deactivated_brushes_folder_name(), 'brushes')

    def __sanity_check_main_dir(self):
        return os.path.exists(
            os.path.join(
                Pathfinder.get_wonderdraft_userfolder(),
                YMLConfigReader.get_changeling_manager_directory_name()
            )
        )

    def __sanity_check_inactive_assets_dir(self):
        return os.path.exists(
            os.path.join(
                Pathfinder.get_wonderdraft_userfolder(),
                YMLConfigReader.get_changeling_manager_directory_name(),
                YMLConfigReader.get_deactivated_assets_folder_name()
            )
        )

    def __sanity_check_inactive_themes_dir(self):
        return os.path.exists(
            os.path.join(
                Pathfinder.get_wonderdraft_userfolder(),
                YMLConfigReader.get_changeling_manager_directory_name(),
                YMLConfigReader.get_deactivated_themes_folder_name()
            )
        )

    def __sanity_check_inactive_brushes_dir(self):
        return os.path.exists(
            os.path.join(
                Pathfinder.get_wonderdraft_userfolder(),
                YMLConfigReader.get_changeling_manager_directory_name(),
                YMLConfigReader.get_deactivated_brushes_folder_name()
            )
        )

    def __sanity__check_logger_dir(self):
        return os.path.exists(
            os.path.join(
                Pathfinder.get_wonderdraft_userfolder(),
                YMLConfigReader.get_changeling_manager_directory_name(),
                YMLConfigReader.get_logger_directory_name()
            )
        )

    def is_setup(self):
        return self.__sanity_check_main_dir() \
               and self.__sanity_check_inactive_assets_dir() \
               and self.__sanity_check_inactive_brushes_dir() \
               and self.__sanity_check_inactive_brushes_dir() \
               and self.__sanity__check_logger_dir()

    def display_welcome_message(self):
        click.echo(Fore.CYAN + '-------------------------------------------------------------------')
        click.echo(Fore.CYAN + '---------------------WELCOME TO CHANGELING-------------------------')
        click.echo(Fore.CYAN + '-------------------------------------------------------------------')
        click.echo(Fore.LIGHTCYAN_EX + 'Since this is your initial (??) setup, here\'s a bit of help')
        click.echo(
            Fore.LIGHTCYAN_EX +
            'Assets, brushes and themes you disable wont disappear. They just get moved and can always be recovered!')
        click.echo(
            Fore.LIGHTCYAN_EX +
            'Profiles are fluid. If you don\'t provide a section, changeling will always keep '
            'all things from that section active.')
        click.echo(Fore.LIGHTCYAN_EX + 'With the activate command, you can use the'
                   + Fore.LIGHTGREEN_EX + ' --dryrun' + Fore.LIGHTCYAN_EX
                   + ' switch to just test things out')
        click.echo('\n')
        click.echo(Fore.LIGHTCYAN_EX + 'To see a list of all commands just type'
                   + Fore.LIGHTGREEN_EX + ' changeling'
                   + Fore.LIGHTCYAN_EX + ' without any command into the terminal')
        click.echo('\n')
        click.echo(Fore.LIGHTCYAN_EX + 'To get help on any command just type the command with the switch '
                   + Fore.LIGHTGREEN_EX + '--help')
        click.echo('\n')
        click.echo(Fore.LIGHTCYAN_EX + 'To activate all assets use the following command: '
                   + Fore.LIGHTGREEN_EX + 'changeling activate all')
        click.echo('\n')
        click.echo(Fore.LIGHTCYAN_EX + 'And now have fun with changeling, and with wonderdraft')
        click.echo(Fore.CYAN + '-------------------------------------------------------------------')
        click.echo(Style.RESET_ALL)
