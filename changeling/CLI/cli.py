import os

import click
from colorama import Fore

from changeling.CLI.handlers.ActivateHandler import ActivateHandler
from changeling.CLI.handlers.ConfigureHandler import ConfigureHandler
from changeling.CLI.handlers.InstallHandler import InstallHandler
from changeling.CLI.handlers.ListHandler import ListHandler
from changeling.CLI.handlers.SetupHandler import SetupHandler
from changeling.CLI.handlers.ShowProfileHandler import ShowProfileHandler
from changeling.CLI.helper import is_setup, setup_logging, init_colorama
from changeling.file_interactions.YMLConfigReader import YMLConfigReader
from changeling.init.Initial import initialize, reset_conf

setuphandler = SetupHandler()
installhandler = InstallHandler()
listhandler = ListHandler()
show_profile_handler = ShowProfileHandler()
activatehandler = ActivateHandler()
configurehandler = ConfigureHandler()


@setup_logging
@initialize
@init_colorama
@click.group()
def cli():
    pass


@click.command()
def setup():
    setuphandler.setup()


@click.command()
def reset_config():
    if click.confirm(Fore.RED + 'This will reset your config file. Do you want to proceed?'):
        reset_conf()


@is_setup
@click.command()
@click.argument('filename')
@click.option('--force/--gentle', default=False, help='Force overwrite of existing profile or not. Gentle is default')
@click.option('--from-current/--normal', default=False,
              help='Lets you install from the current setup. Default is --normal')
def install_profile(filename, force, from_current):
    if os.path.splitext(filename)[0] == 'all':
        click.echo(
            Fore.LIGHTRED_EX + 'You can\'t name your profile "all". It is a reserved name. Pick something different')
    else:
        if from_current:
            if click.confirm(Fore.LIGHTBLUE_EX +
                             'Will install from current setup. Filename provided will be used as profile name. Is that ok?',
                             default=True):
                installhandler.install_from_current(filename, force)
            else:
                filename_new = click.prompt('Please provide a name for the profile to be created')
                installhandler.install_from_current(filename_new, force)
        else:
            installhandler.install(filename, force)


@is_setup
@click.command()
def list_profiles():
    click.echo(Fore.LIGHTMAGENTA_EX)
    click.echo(listhandler.list_profiles())


@is_setup
@click.command()
@click.argument('profilename')
def show_profile(profilename):
    click.echo(Fore.LIGHTMAGENTA_EX)
    click.echo(show_profile_handler.show_profile(profilename))


@is_setup
@click.command()
@click.option('--changelingfolder', default=YMLConfigReader.get_changeling_manager_directory_name(),
              help='Rename main changeling folder folder')
@click.option('--loggingfolder', default=YMLConfigReader.get_logger_directory_name(), help='Rename logging folder')
@click.option('--inactivefolder', default=YMLConfigReader.get_deactivated_assets_folder_name(),
              help='Rename inactive modules folder')
def configure(changelingfolder, loggingfolder, inactivefolder):
    click.echo(
        Fore.LIGHTMAGENTA_EX + 'Renaming the folders with a command will be implemented in a later release. Stay tuned')
    # configurehandler.configure(changelingfolder, inactivefolder, loggingfolder)


@is_setup
@click.command()
@click.argument('profilename')
@click.option('--dryrun/--actual', default=False,
              help='Lets you simulate what would be activated and what not. Default is --actual')
def activate(profilename, dryrun):
    activatehandler.activate(profilename, dryrun)


cli.add_command(setup)
cli.add_command(reset_config)
cli.add_command(install_profile)
cli.add_command(activate)
cli.add_command(configure)
cli.add_command(list_profiles)
cli.add_command(show_profile)

if __name__ == '__main__':
    cli()
