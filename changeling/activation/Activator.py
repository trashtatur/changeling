import shutil

from changeling.pathfinder import Pathfinder


class Activator:

    @staticmethod
    def activate(folder_list: list):
        for folder in folder_list:
            shutil.move(folder, Pathfinder.get_wonderdraft_userfolder())