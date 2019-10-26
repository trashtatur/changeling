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
        return os.path.join(Pathfinder.__appdata_path(), 'Wonderdraft')

    @staticmethod
    def get_wonderdraft_asset_folder():
        return os.path.join(Pathfinder.get_wonderdraft_userfolder(), 'assets')

    @staticmethod
    def get_wonderdraft_themes_folder():
        return os.path.join(Pathfinder.get_wonderdraft_userfolder(), 'themes')

    @staticmethod
    def get_wonderdraft_brushes_folder():
        return os.path.join(Pathfinder.get_wonderdraft_userfolder(), 'brushes')

    @staticmethod
    def get_deactivated_assets_folder_path():
        return os.path.join(
            Pathfinder.get_wonderdraft_userfolder(),
            YMLConfigReader.get_changeling_manager_directory_name(),
            YMLConfigReader.get_deactivated_assets_folder_name()
        )

    @staticmethod
    def get_deactivated_brushes_folder_path():
        return os.path.join(
            Pathfinder.get_wonderdraft_userfolder(),
            YMLConfigReader.get_changeling_manager_directory_name(),
            YMLConfigReader.get_deactivated_brushes_folder_name()
        )

    @staticmethod
    def get_deactivated_themes_folder_path():
        return os.path.join(
            Pathfinder.get_wonderdraft_userfolder(),
            YMLConfigReader.get_changeling_manager_directory_name(),
            YMLConfigReader.get_deactivated_themes_folder_name()
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




