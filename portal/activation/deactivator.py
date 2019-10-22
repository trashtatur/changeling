import shutil

from portal.pathfinder import Pathfinder


class Deactivator:

    @staticmethod
    def deactivate(folder_list: list):

        for folder in folder_list:
            shutil.move(folder, Pathfinder.get_deactivated_folder_path())


