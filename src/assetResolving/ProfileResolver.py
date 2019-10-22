import logging
import os

import yaml

from src.pathfinder import Pathfinder


class ProfileResolver:

    def resolve_profile(self, profilename):
        profilename_cleaned = os.path.splitext(profilename)[0]
        profile_yml = self.__open_profile_by_name(profilename_cleaned)
        return self.__create_folder_list(profile_yml['modules'])

    def __create_folder_list(self, foldernamelist: list):

        return [self.__find_full_path_for_foldername(foldername) for foldername in foldernamelist]

    def __open_profile_by_name(self, profilename: str):

        try:
            with open(os.path.join(Pathfinder.get_profile_directory(), profilename + '.yml')) as profile:
                try:
                    return yaml.safe_load(profile)
                except yaml.YAMLError as exception:
                    logging.getLogger('debug').exception("YAML File seems to be tampered. Have you changed keys?")
        except OSError as exception:
            logging.getLogger('debug').exception(
                'Profile could not be opened. Was it the right name? Does it exist?')

    def __find_full_path_for_foldername(self, foldername):

        return os.path.join(Pathfinder.get_wonderdraft_userfolder(), foldername)
