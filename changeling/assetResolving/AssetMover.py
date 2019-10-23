import os

from changeling.assetResolving.ProfileResolver import ProfileResolver
from changeling.file_interactions.YMLConfigReader import YMLConfigReader
from changeling.pathfinder import Pathfinder


class AssetMover:

    def __init__(self, profile_resolver: ProfileResolver):
        self.profile_resolver = profile_resolver

    def activate_profile(self, profilename):
        folderlist = self.profile_resolver.resolve_profile(profilename)

    @staticmethod
    def determine_active_modules():
        active_modules = [
            os.path.join(Pathfinder.get_wonderdraft_userfolder(), root)
            for root in os.listdir(Pathfinder.get_wonderdraft_userfolder())
            # To exclude Mythkeeper download folder and the inactive assets
            if root != 'tempMKDownload' and root != YMLConfigReader.get_profile_manager_directory_name()
        ]
        return active_modules

    @staticmethod
    def determine_inactive_modules():
        inactive_modules = [
            os.path.join(Pathfinder.get_deactivated_folder_path(), root)
            for root in os.listdir(Pathfinder.get_deactivated_folder_path())
        ]
        return inactive_modules

