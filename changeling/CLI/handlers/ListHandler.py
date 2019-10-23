import os

from changeling.pathfinder import Pathfinder


class ListHandler:

    def list_profiles(self):
        profiles = [
            os.path.splitext(profilename)[0]
            for profilename in os.listdir(Pathfinder.get_profile_directory())
            if os.path.splitext(profilename)[0] != 'all'
        ]

        return print(*profiles, sep="\n")
