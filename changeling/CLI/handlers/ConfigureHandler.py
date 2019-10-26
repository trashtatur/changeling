import os

from changeling.file_interactions.YMLConfigWriter import YMLConfigWriter
from changeling.pathfinder import Pathfinder


class ConfigureHandler:

    def configure(self, changeling_manager_folder, inactive_modules_folder, logging_folder):
        YMLConfigWriter.write_config(changeling_manager_folder, inactive_modules_folder, logging_folder)

    def __rename_main_folder(self, changeling_manager_folder):
        pass

    def __rename_inactive_folder(self, inactive_modules_folder):
        pass

    def __rename_logging_folder(self, changeling_manager_folder):
        pass
