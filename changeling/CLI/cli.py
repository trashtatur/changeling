import click

from changeling.CLI.handlers.InstallHandler import InstallHandler
from changeling.CLI.handlers.ListHandler import ListHandler
from changeling.CLI.handlers.SetupHandler import SetupHandler
from changeling.CLI.handlers.ShowProfileHandler import ShowProfileHandler
from changeling.CLI.helper import is_setup, setup_logging
from changeling.file_interactions.YMLConfigReader import YMLConfigReader


setuphandler = SetupHandler()
installhandler = InstallHandler()
listhandler = ListHandler()
show_profile_handler = ShowProfileHandler()


@setup_logging
@click.group()
def cli():
    pass


@click.command()
def setup():
    setuphandler.setup()


@is_setup
@click.command()
@click.argument('filename')
@click.option('--force/--gentle', default=False, help='Force overwrite of existing profile or not. Gentle is default')
@click.option('--from-current/--normal', default=False,
              help='Lets you install from the current setup. Default is --normal')
def install_profile(filename, force, from_current):
    if from_current:
        if click.confirm('Will install from current setup. Filename provided will be used as profile name. Is that ok?'):
            installhandler.install_from_current(filename, force)
        else:
            filename_new = click.prompt('Please provide a name for the profile to be created')
            installhandler.install_from_current(filename_new, force)
    else:
        installhandler.install(filename, force)


@is_setup
@click.command()
def list_profiles():
    click.echo(listhandler.list_profiles())

@is_setup
@click.command()
@click.argument('profilename')
def show_profile(profilename):
    show_profile_handler.show_profile(profilename)


@is_setup
@click.command()
@click.option('--loggingfolder', default=YMLConfigReader.get_logger_directory_name(), help='Rename logging folder')
@click.option('--inactivefolder', default=YMLConfigReader.get_deactivated_modules_folder_name(),
              help='Rename inactive modules folder')
def configure(loggingfolder, inactivefolder):
    click.echo('configured ' + loggingfolder)


@is_setup
@click.command()
@click.argument('profilename')
def activate(profilename):
    click.echo('activate')




cli.add_command(setup)
cli.add_command(install_profile)
cli.add_command(activate)
cli.add_command(configure)
cli.add_command(list_profiles)
cli.add_command(show_profile)

if __name__ == '__main__':
    cli()
