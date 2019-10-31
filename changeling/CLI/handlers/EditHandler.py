import logging
import os
import subprocess
import click
import yaml
from colorama import Fore

from changeling.file_interactions.YMLConfigReader import YMLConfigReader
from changeling.file_interactions.YMLConfigValidator import YMLConfigValidator
from changeling.pathfinder import Pathfinder


class EditHandler:

    def edit_profile(self, profilename: str):
        if profilename != 'all':
            executable_editor = YMLConfigReader.get_profile_editor_name()
            profiledir = Pathfinder.get_profile_directory()
            pre_edit_profile = self.__safe_profile_before_edit(profilename)
            if os.path.exists(os.path.join(profiledir, profilename+'.yml')):
                process = subprocess.run(
                    [
                        executable_editor,
                        os.path.join(profiledir, os.path.splitext(profilename)[0]+'.yml')
                    ],
                    check=True
                )
                if not process.check_returncode():
                    if self.__validate_profile_after_edit(profilename):
                        click.echo(
                            Fore.LIGHTMAGENTA_EX +
                            'Edit of profile '+Fore.GREEN+profilename+Fore.LIGHTMAGENTA_EX+' complete')
                    else:
                        click.echo(
                            Fore.LIGHTRED_EX +
                            'Edit of profile '+profilename+' invalid. Your changes invalidated the profile.'
                                                           ' Changeling will now reset the profile to its'
                                                           ' previous state!')
                        self.__revert_to_previous(profilename, pre_edit_profile)

            else:
                click.echo(Fore.LIGHTRED_EX+'This profile does not exist. Please provide an existing profilename')
        else:
            click.echo(Fore.LIGHTRED_EX+'You can\'t edit the "all" profile. It is restricted')

    def __safe_profile_before_edit(self, profilename) -> dict:
        with open(os.path.join(Pathfinder.get_profile_directory(), os.path.splitext(profilename)[0]+'.yml')) as profile:
            try:
                return yaml.safe_load(profile)
            except yaml.YAMLError as exception:
                logging.getLogger('debug')\
                    .exception('Could not load profile '+profilename+'before edit. Does it exist?')

    def __validate_profile_after_edit(self, profilename) -> bool:
        with open(os.path.join(Pathfinder.get_profile_directory(), os.path.splitext(profilename)[0]+'.yml')) as profile:
            try:
                loaded_profile = yaml.safe_load(profile)
                return YMLConfigValidator.validate_profile(loaded_profile)
            except yaml.YAMLError as exception:
                logging.getLogger('debug') \
                    .exception('Could not load profile ' + profilename + 'after edit. Did you delete it?')

    def __revert_to_previous(self, profilename, data):
        with open(os.path.join(Pathfinder.get_profile_directory(),
                               os.path.splitext(profilename)[0]+'.yml'), 'w') as to_revert:
            yaml.dump(data, to_revert, default_flow_style=False)
