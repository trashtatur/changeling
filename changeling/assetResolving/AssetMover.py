import logging
import os
import shutil
import click

from changeling.assetResolving.ProfileResolver import ProfileResolver
from changeling.file_interactions.YMLConfigReader import YMLConfigReader
from changeling.pathfinder import Pathfinder


class AssetMover:

    def __init__(self, profile_resolver: ProfileResolver):
        self.profile_resolver = profile_resolver

    def activate_profile(self, profilename, dryrun):
        modulelist = self.profile_resolver.resolve_profile(profilename)
        active_modules = AssetMover.determine_active_modules()
        inactive_modules = AssetMover.determine_inactive_modules()
        to_activate = []
        for modulename in modulelist:
            if self.__needs_activation(modulename, inactive_modules):
                to_activate.append(os.path.join(Pathfinder.get_deactivated_folder_path(), modulename))
        to_deactivate = self.__needs_deactivation(modulelist, active_modules)
        if dryrun:
            click.echo('This run would have activated: ')
            click.echo(print(*[os.path.basename(folder) for folder in to_activate], sep="\n"))
            click.echo('This run would have deactivated: ')
            click.echo(print(*[os.path.basename(folder) for folder in to_deactivate], sep="\n"))
        else:
            for module in to_deactivate:
                click.echo("deactivating asset module: "+os.path.basename(module))
                self.__deactivate_module(module)
            for module in to_activate:
                click.echo("activating asset module: "+os.path.basename(module))
                self.__activate_module(module)
            logging.getLogger('debug').info('Activated profile: '+profilename)

    def __needs_activation(self, modulename: str, inactive: list):
        if os.path.join(Pathfinder.get_deactivated_folder_path(), modulename) in inactive:
            return True
        return False

    def __needs_deactivation(self, modules: list, active: list):
        return list(set(active) -
                    set([os.path.join(Pathfinder.get_wonderdraft_userfolder(), module) for module in modules]))

    @staticmethod
    def determine_active_modules():
        active_modules = [
            os.path.join(Pathfinder.get_wonderdraft_userfolder(), root)
            for root in os.listdir(Pathfinder.get_wonderdraft_userfolder())
            # To exclude Mythkeeper download folder and the inactive assets
            if root != 'tempMKDownload'
            and root != YMLConfigReader.get_profile_manager_directory_name()
            # To exclude any rogue files
            and os.path.isdir(os.path.join(Pathfinder.get_wonderdraft_userfolder(),root))
        ]
        return active_modules

    @staticmethod
    def determine_inactive_modules():
        inactive_modules = [
            os.path.join(Pathfinder.get_deactivated_folder_path(), root)
            for root in os.listdir(Pathfinder.get_deactivated_folder_path())
            # To exclude any rogue files
            if os.path.isdir(os.path.join(Pathfinder.get_deactivated_folder_path(), root))
        ]
        return inactive_modules

    def __deactivate_module(self, module):
        shutil.move(
            module,
            Pathfinder.get_deactivated_folder_path()
        )

    def __activate_module(self, module):
        shutil.move(
            module,
            Pathfinder.get_wonderdraft_userfolder()
        )
