import logging
import os
import shutil
import click

from colorama import Fore, Style
from changeling.file_interactions.YMLConfigReader import YMLConfigReader
from changeling.pathfinder import Pathfinder
from changeling.resolving.ResourceResolverInterface import ResourceResolverInterface


class AssetResourceResolver(ResourceResolverInterface):

    def activate(self, profilename, dryrun, assetlist, catchall: bool):
        active_modules = AssetResourceResolver.determine_active()
        inactive_modules = AssetResourceResolver.determine_inactive()
        to_activate = self.needs_activation(assetlist, inactive_modules)
        to_deactivate = self.needs_deactivation(assetlist, active_modules)
        self.__print_banner()
        if dryrun:
            self.dryrun(to_activate, to_deactivate, catchall)
        else:
            if profilename == 'all' or catchall:
                self.activate_all(inactive_modules)
            else:
                for module in to_deactivate:
                    self.deactivate_single(module)
                for module in to_activate:
                    self.activate_single(module)

    def needs_activation(self, profile_elements: list, inactive: list):
        return [os.path.join(Pathfinder.get_deactivated_assets_folder_path(), element)
                for element in profile_elements
                if os.path.join(Pathfinder.get_deactivated_assets_folder_path(), element) in inactive
                ]

    def needs_deactivation(self, profile_elements: list, active: list):
        return list(set(active) -
                    set([os.path.join(Pathfinder.get_wonderdraft_asset_folder(), element) for element in profile_elements])
                    )

    @staticmethod
    def determine_active():
        active_assets = [
            os.path.join(Pathfinder.get_wonderdraft_asset_folder(), root)
            for root in os.listdir(Pathfinder.get_wonderdraft_asset_folder())
            # To exclude Mythkeeper download folder
            if root != 'tempMKDownload'
            # To exclude any rogue files
            and os.path.isdir(os.path.join(Pathfinder.get_wonderdraft_asset_folder(), root))
        ]
        return active_assets

    @staticmethod
    def determine_inactive():
        inactive_assets = [
            os.path.join(Pathfinder.get_deactivated_assets_folder_path(), root)
            for root in os.listdir(Pathfinder.get_deactivated_assets_folder_path())
            # To exclude any rogue files
            if os.path.isdir(os.path.join(Pathfinder.get_deactivated_assets_folder_path(), root))
        ]
        return inactive_assets

    def deactivate_single(self, module):
        click.echo(Fore.MAGENTA + "deactivating asset module: " + Fore.LIGHTMAGENTA_EX + os.path.basename(module))
        shutil.move(
            module,
            Pathfinder.get_deactivated_assets_folder_path()
        )

    def activate_single(self, module):
        click.echo(Fore.MAGENTA + "activating asset module: " + Fore.LIGHTMAGENTA_EX + os.path.basename(module))
        shutil.move(
            module,
            Pathfinder.get_wonderdraft_asset_folder()
        )

    def activate_all(self, inactive_modules: list):
        click.echo(
            Fore.MAGENTA + "activating all assets")
        for module in inactive_modules:
            self.activate_single(module)

    def dryrun(self, to_activate, to_deactivate, catchall: bool):
        if catchall:
            click.echo(Fore.MAGENTA + 'This run would have activated these assets: ' + Fore.LIGHTMAGENTA_EX)
            click.echo(print(*[os.path.basename(folder) for folder in AssetResourceResolver.determine_inactive()],
                             sep="\n"))
            click.echo(Fore.MAGENTA + 'This run would have deactivated these assets: ' + Fore.LIGHTMAGENTA_EX)
        else:
            click.echo(Fore.MAGENTA + 'This run would have activated these assets: ' + Fore.LIGHTMAGENTA_EX)
            click.echo(print(*[os.path.basename(folder) for folder in to_activate], sep="\n"))
            click.echo(Fore.MAGENTA + 'This run would have deactivated these assets: ' + Fore.LIGHTMAGENTA_EX)
            click.echo(print(*[os.path.basename(folder) for folder in to_deactivate], sep="\n"))

    def __print_banner(self):
        click.echo(Fore.LIGHTBLUE_EX + '---------------------------------------------------')
        click.echo(Fore.LIGHTBLUE_EX + '------------------ASSETS---------------------------')
        click.echo(Fore.LIGHTBLUE_EX + '---------------------------------------------------')
