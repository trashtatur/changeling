import logging
import yaml

from changeling.util import Util


class YMLConfigReader:

    @staticmethod
    def get_changeling_manager_directory_name():
        with open(Util.get_config_file_location()) as configfile:
            try:
                read_yml_config = yaml.safe_load(configfile)
                return read_yml_config['changeling_manager_folder']
            except yaml.YAMLError as exception:
                logging.getLogger('debug').exception("YAML File seems to be tampered. Have you changed keys?")

    @staticmethod
    def get_deactivated_modules_folder_name():
        with open(Util.get_config_file_location()) as configfile:
            try:
                read_yml_config = yaml.safe_load(configfile)
                return read_yml_config['inactive_modules_folder']
            except yaml.YAMLError as exception:
                logging.getLogger('debug').exception("YAML File seems to be tampered. Have you changed keys?")

    @staticmethod
    def get_logger_directory_name():
        with open(Util.get_config_file_location()) as configfile:
            try:
                read_yml_config = yaml.safe_load(configfile)
                return read_yml_config['logging_folder']
            except yaml.YAMLError as exception:
                logging.getLogger('debug').exception("YAML File seems to be tampered. Have you changed keys?")
