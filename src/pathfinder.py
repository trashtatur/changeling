import os
import yaml

from src.util import Util


class Pathfinder:

    @staticmethod
    def get_profile_directory():
        return os.path.join(
            Util.get_root(),
            'profiles'
        )

    @staticmethod
    def get_deactivated_folder_path():
        return os.path.join(
            Pathfinder.get_wonderdraft_userfolder(),
            Pathfinder.get_deactivated_modules_folder_name()
        )

    @staticmethod
    def __appdata_path():
        return os.getenv('APPDATA')

    @staticmethod
    def get_wonderdraft_userfolder():
        return os.path.join(Pathfinder.__appdata_path(), 'Wonderdraft', 'assets')

    @staticmethod
    def create_deactivated_modules_folder():
        os.mkdir(
            os.path.join(Pathfinder.get_wonderdraft_userfolder(),
                         Pathfinder.get_deactivated_modules_folder_name()
                         )
        )

    @staticmethod
    def get_deactivated_modules_folder_name():
        config_file_location = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'config',
            'config.yml'
        )
        with open(config_file_location) as configfile:
            try:
                read_yml_config = yaml.safe_load(configfile)
                return read_yml_config['inactiveModulesFolder']
            except yaml.YAMLError as exception:
                # TODO Logger!
                print(exception)
