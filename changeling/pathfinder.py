import os

from changeling.file_interactions.YMLConfigReader import YMLConfigReader
from changeling.init import Initial


class Pathfinder:

    @staticmethod
    def get_profile_directory():
        return Initial.CHANGELING_PROFILES_PATH

    @staticmethod
    def __appdata_path():
        return os.getenv('APPDATA')

    @staticmethod
    def get_wonderdraft_userfolder():
        return os.path.join(Pathfinder.__appdata_path(), 'Wonderdraft', 'assets')

    @staticmethod
    def get_deactivated_folder_path():
        return os.path.join(
            Pathfinder.get_wonderdraft_userfolder(),
            YMLConfigReader.get_changeling_manager_directory_name(),
            YMLConfigReader.get_deactivated_modules_folder_name()
        )

    @staticmethod
    def get_logger_directory_path():
        return os.path.join(
            Pathfinder.get_wonderdraft_userfolder(),
            YMLConfigReader.get_changeling_manager_directory_name(),
            YMLConfigReader.get_logger_directory_name()
        )

    @staticmethod
    def get_changeling_manager_directory_path():
        return os.path.join(
            Pathfinder.get_wonderdraft_userfolder(),
            YMLConfigReader.get_changeling_manager_directory_name(),
        )




