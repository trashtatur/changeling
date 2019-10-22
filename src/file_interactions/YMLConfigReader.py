import logging
import os

import yaml

from src.util import Util


class YMLConfigReader:

    @staticmethod
    def get_profile_manager_directory_name():
        with open(YMLConfigReader.__get_config_file_location()) as configfile:
            try:
                read_yml_config = yaml.safe_load(configfile)
                return read_yml_config['profile_manager_folder']
            except yaml.YAMLError as exception:
                logging.getLogger('debug').exception("YAML File seems to be tampered. Have you changed keys?")

    @staticmethod
    def get_deactivated_modules_folder_name():
        with open(YMLConfigReader.__get_config_file_location()) as configfile:
            try:
                read_yml_config = yaml.safe_load(configfile)
                return read_yml_config['inactiveModulesFolder']
            except yaml.YAMLError as exception:
                logging.getLogger('debug').exception("YAML File seems to be tampered. Have you changed keys?")

    @staticmethod
    def get_logger_directory_name():
        with open(YMLConfigReader.__get_config_file_location()) as configfile:
            try:
                read_yml_config = yaml.safe_load(configfile)
                return read_yml_config['logging_folder']
            except yaml.YAMLError as exception:
                logging.getLogger('debug').exception("YAML File seems to be tampered. Have you changed keys?")

    @staticmethod
    def __get_config_file_location():
        return os.path.join(
            Util.get_root(),
            'src',
            'config',
            'config.yml'
        )
