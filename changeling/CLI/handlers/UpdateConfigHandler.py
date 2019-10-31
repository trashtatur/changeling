import logging
import os

import yaml

from changeling.file_interactions.YMLConfigReader import YMLConfigReader
from changeling.file_interactions.YMLConfigWriter import YMLConfigWriter
from changeling.util import Util


class UpdateConfigHandler:

    def update_config(self):
        version_current = YMLConfigReader.get_current_version()
        version_local = YMLConfigReader.get_local_version()

        if version_current != version_local:
            with open(os.path.join(Util.get_root(), 'changeling', 'config', 'config.yml')) as current_conf, \
                 open(Util.get_config_file_location()) as local_conf:
                try:
                    current_yaml_conf = self.__open_config(current_conf)
                    local_yaml_conf = self.__open_config(local_conf)
                    soft_updated_conf = {**current_yaml_conf, **local_yaml_conf}
                    adjusted_version_soft_update = self.__adjust_version(soft_updated_conf, version_current)
                    self.__write_config_file(adjusted_version_soft_update)
                except yaml.YAMLError as exception:
                    logging.getLogger('debug').exception('')

    def __open_config(self, openedFile):
        try:
            return yaml.safe_load(openedFile)
        except yaml.YAMLError as exception:
            logging.getLogger('debug').exception('Could not load config file into yml. Is it valid?')

    def __write_config_file(self, data):
        with open(Util.get_config_file_location(), 'w') as new_config:
            yaml.dump(data, new_config, default_flow_style=False)

    def __adjust_version(self, data, new_version):
        data['version'] = new_version
        return data
