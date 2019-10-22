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
@click.argument('filename', type=click.Path(exists=True))
@click.option('--force/--gentle', default=False, help='Force overwrite of existing profile or not. Gentle is default')
def install_profile(filename, force):
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


@is_setup
@click.command()
@click.argument('profilename')
def deactivate(profilename):
    click.echo('deactivate')


cli.add_command(setup)
cli.add_command(install_profile)
cli.add_command(activate)
cli.add_command(deactivate)
cli.add_command(configure)
cli.add_command(list_profiles)
cli.add_command(show_profile)

if __name__ == '__main__':
    cli()
