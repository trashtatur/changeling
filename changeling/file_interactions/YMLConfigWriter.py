import os
import yaml

from changeling.file_interactions.YMLConfigValidator import YMLConfigValidator
from changeling.pathfinder import Pathfinder


class YMLConfigWriter:

    @staticmethod
    def write_profile(data, filename):
        if YMLConfigValidator.validate_profile(data):
            with open(os.path.join(Pathfinder.get_profile_directory(), filename), 'w') as new_profile:
                yaml.dump(data, new_profile, default_flow_style=False)
