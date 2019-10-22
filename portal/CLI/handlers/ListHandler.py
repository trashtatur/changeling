import os

from portal.pathfinder import Pathfinder


class ListHandler:

    def list_profiles(self):
        profiles = [os.path.splitext(profilename)[0] for profilename in os.listdir(Pathfinder.get_profile_directory())]
        return print(*profiles, sep = "\n")
