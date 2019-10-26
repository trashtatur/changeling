import logging
import os
import shutil

import click
from colorama import Fore

from changeling.pathfinder import Pathfinder
from changeling.resolving.ResourceResolverInterface import ResourceResolverInterface


class BrushesResourceResolver(ResourceResolverInterface):

    def activate(self, profilename: str, dryrun: bool, elements: list, catchall: bool):
        active_brushes = BrushesResourceResolver.determine_active()
        inactive_brushes = BrushesResourceResolver.determine_inactive()
        to_activate = self.needs_activation(elements, inactive_brushes)
        to_deactivate = self.needs_deactivation(elements, active_brushes)
        self.__print_banner()
        if dryrun:
            self.dryrun(to_activate, to_deactivate, catchall)
        else:
            if profilename == 'all' or catchall:
                self.activate_all(inactive_brushes)
            else:
                for module in to_deactivate:
                    self.deactivate_single(module)
                for module in to_activate:
                    self.activate_single(module)

    @staticmethod
    def determine_active() -> list:
        active_brushes = [
            os.path.join(Pathfinder.get_wonderdraft_brushes_folder(), root)
            for root in os.listdir(Pathfinder.get_wonderdraft_brushes_folder())
            # To exclude any rogue files
            if root != os.path.isdir(os.path.join(Pathfinder.get_wonderdraft_brushes_folder(), root))
        ]
        return active_brushes

    @staticmethod
    def determine_inactive() -> list:
        inactive_brushes = [
            os.path.join(Pathfinder.get_deactivated_brushes_folder_path(), root)
            for root in os.listdir(Pathfinder.get_deactivated_brushes_folder_path())
            # To exclude any rogue files
            if os.path.isdir(os.path.join(Pathfinder.get_deactivated_brushes_folder_path(), root))
        ]
        return inactive_brushes

    def activate_single(self, element: str):
        click.echo(Fore.MAGENTA + "activating brush set: " + Fore.LIGHTMAGENTA_EX + os.path.basename(element))
        shutil.move(
            element,
            Pathfinder.get_wonderdraft_brushes_folder()
        )

    def deactivate_single(self, element: str):
        click.echo(Fore.MAGENTA + "deactivating brush set: " + Fore.LIGHTMAGENTA_EX + os.path.basename(element))
        shutil.move(
            element,
            Pathfinder.get_deactivated_brushes_folder_path()
        )

    def activate_all(self, elements: list):
        click.echo(
            Fore.MAGENTA + "activating all brushes")
        for element in elements:
            self.activate_single(element)

    def needs_deactivation(self, profile_elements: list, active: list) -> list:
        return list(set(active) -
                    set([os.path.join(Pathfinder.get_wonderdraft_brushes_folder(), element)
                         for element in profile_elements])
                    )

    def needs_activation(self, profile_elements: list, inactive: list) -> list:
        return [os.path.join(Pathfinder.get_deactivated_brushes_folder_path(), element)
                for element in profile_elements
                if os.path.join(Pathfinder.get_deactivated_brushes_folder_path(), element) in inactive
                ]

    def dryrun(self, to_activate: list, to_deactivate: list, catchall: bool):
        if catchall:
            click.echo(Fore.MAGENTA + 'This run would have activated these brushes: ' + Fore.LIGHTMAGENTA_EX)
            click.echo(print(*[os.path.basename(folder) for folder in BrushesResourceResolver.determine_inactive()],
                             sep="\n"))
            click.echo(Fore.MAGENTA + 'This run would have deactivated these brushes: ' + Fore.LIGHTMAGENTA_EX)
        else:
            click.echo(Fore.MAGENTA + 'This run would have activated these brushes: ' + Fore.LIGHTMAGENTA_EX)
            click.echo(print(*[os.path.basename(folder) for folder in to_activate], sep="\n"))
            click.echo(Fore.MAGENTA + 'This run would have deactivated these brushes: ' + Fore.LIGHTMAGENTA_EX)
            click.echo(print(*[os.path.basename(folder) for folder in to_deactivate], sep="\n"))

    def __print_banner(self):
        click.echo(Fore.LIGHTBLUE_EX + '---------------------------------------------------')
        click.echo(Fore.LIGHTBLUE_EX + '------------------BRUSHES--------------------------')
        click.echo(Fore.LIGHTBLUE_EX + '---------------------------------------------------')
