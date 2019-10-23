import os

from changeling.file_interactions.YMLConfigWriter import YMLConfigWriter
from changeling.pathfinder import Pathfinder


class ConfigureHandler:

    def configure(self, changeling_manager_folder, inactive_modules_folder, logging_folder):
        YMLConfigWriter.write_config(changeling_manager_folder, inactive_modules_folder, logging_folder)

    def __rename_main_folder(self, changeling_manager_folder):
        os.rename(
            Pathfinder.get_deactivated_folder_path(),
            os.path.join(Pathfinder.get_wonderdraft_userfolder(), changeling_manager_folder)
        )

    def __rename_inactive_folder(self, inactive_modules_folder):
        os.rename(
            Pathfinder.get_profile_directory(),
            os.path.join(Pathfinder.get_wonderdraft_userfolder(), inactive_modules_folder)
        )

    def __rename_logging_folder(self, changeling_manager_folder):
        pass