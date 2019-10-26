import logging
import yaml

from changeling.util import Util


class YMLConfigReader:

    MANAGER_FOLDER_KEY = 'changeling_manager_folder'
    INACTIVE_ASSETS_FOLDER_KEY = 'inactive_assets_folder'
    INACTIVE_THEMES_FOLDER_KEY = 'inactive_themes_folder'
    INACTIVE_BRUSHES_FOLDER_KEY = 'inactive_brushes_folder'
    LOGGER_FOLDER_KEY = 'logging_folder'

    @staticmethod
    def get_changeling_manager_directory_name():
        return YMLConfigReader.__get_entry_from_config_yml(YMLConfigReader.MANAGER_FOLDER_KEY)

    @staticmethod
    def get_logger_directory_name():
        return YMLConfigReader.__get_entry_from_config_yml(YMLConfigReader.LOGGER_FOLDER_KEY)

    @staticmethod
    def get_deactivated_brushes_folder_name():
        return YMLConfigReader.__get_entry_from_config_yml(YMLConfigReader.INACTIVE_BRUSHES_FOLDER_KEY)

    @staticmethod
    def get_deactivated_themes_folder_name():
        return YMLConfigReader.__get_entry_from_config_yml(YMLConfigReader.INACTIVE_THEMES_FOLDER_KEY)

    @staticmethod
    def get_deactivated_assets_folder_name():
        return YMLConfigReader.__get_entry_from_config_yml(YMLConfigReader.INACTIVE_ASSETS_FOLDER_KEY)

    @staticmethod
    def __get_entry_from_config_yml(key: str):
        with open(Util.get_config_file_location()) as configfile:
            try:
                read_yml_config = yaml.safe_load(configfile)
                return read_yml_config.get(key, 'NONE')
            except yaml.YAMLError or KeyError as exception:
                logging\
                    .getLogger('debug')\
                    .exception("YAML File seems to be tampered. Have you changed keys? Could not retrieve " + key)

