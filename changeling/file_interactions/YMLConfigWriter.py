import os
import yaml

from changeling.file_interactions.YMLConfigValidator import YMLConfigValidator
from changeling.pathfinder import Pathfinder
from changeling.util import Util


class YMLConfigWriter:

    @staticmethod
    def write_profile(data, filename):
        if YMLConfigValidator.validate_profile(data):
            with open(os.path.join(Pathfinder.get_profile_directory(), filename), 'w') as new_profile:
                yaml.dump(data, new_profile, default_flow_style=False)

    @staticmethod
    def write_config(changeling_manager_folder, inactive_modules_folder, logging_folder):
        data = {
            'changeling_manager_folder': changeling_manager_folder,
            'inactive_modules_folder': inactive_modules_folder,
            'logging_folder': logging_folder
        }
        with open(Util.get_config_file_location(), 'w') as new_config:
            yaml.dump(data, new_config, default_flow_style=False)
