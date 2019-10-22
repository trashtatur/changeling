import os

from src.assetResolving.ProfileResolver import ProfileResolver
from src.pathfinder import Pathfinder


class AssetMover:

    def __init__(self, profile_resolver: ProfileResolver):
        self.profile_resolver = profile_resolver

    def activate_profile(self, profilename):
        folderlist = self.profile_resolver.resolve_profile(profilename)

    def determine_active_modules(self):
        active_modules = [
            os.path.join(Pathfinder.get_wonderdraft_userfolder(), root)
            for root in os.listdir(Pathfinder.get_wonderdraft_userfolder())
            # To exclude Mythkeeper download folder and the inactive assets
            if root != 'tempMKDownload' and root != Pathfinder.get_deactivated_modules_folder_name()
        ]
        return active_modules


