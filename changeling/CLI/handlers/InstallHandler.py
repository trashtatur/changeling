import logging
import os
import shutil

import click
import yaml

from changeling.file_interactions.YMLConfigValidator import YMLConfigValidator
from changeling.pathfinder import Pathfinder


class InstallHandler:

    def install(self, profilepath, force):
        opened_profile = self.open_file(profilepath)
        if YMLConfigValidator.validate_profile(opened_profile):
            if os.path.splitext(profilepath)[1] == '.yml':
                click.echo('Installing profile: '+os.path.splitext(profilepath)[0])
                shutil.copy(profilepath, Pathfinder.get_profile_directory())
                # TODO look for force parameter and respect it
                # TODO Change file ending to YML
        else:
            click.echo('Profile is not correctly formatted. Make sure to write it properly')

    def open_file(self, path):
        if os.path.isfile(path):
            try:
                conf = yaml.safe_load(open(path))
                return conf
            except yaml.YAMLError as error:
                logging.getLogger('debug').exception('YML File could not be opened')
