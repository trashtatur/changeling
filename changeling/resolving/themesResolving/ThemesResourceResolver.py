import os
import shutil

import click
from colorama import Fore

from changeling.pathfinder import Pathfinder
from changeling.resolving.ResourceResolverInterface import ResourceResolverInterface


class ThemesResourceResolver(ResourceResolverInterface):

    WONDERDRAFT_THEME_EXTENSION = '.wonderdraft_theme'

    def activate(self, profilename: str, dryrun: bool, elements: list, catchall: bool):
        active_themes = ThemesResourceResolver.determine_active()
        inactive_themes = ThemesResourceResolver.determine_inactive()
        to_activate = self.needs_activation(elements, inactive_themes)
        to_deactivate = self.needs_deactivation(elements, active_themes)
        self.__print_banner()
        if dryrun:
            self.dryrun(to_activate, to_deactivate, catchall)
        else:
            if profilename == 'all' or catchall:
                self.activate_all(inactive_themes)
            else:
                for module in to_deactivate:
                    self.deactivate_single(module)
                for module in to_activate:
                    self.activate_single(module)

    @staticmethod
    def determine_active():
        active_themes = [
            os.path.join(Pathfinder.get_wonderdraft_themes_folder(), root)
            for root in os.listdir(Pathfinder.get_wonderdraft_themes_folder())
            # To exclude folders
            if os.path.isfile(os.path.join(Pathfinder.get_wonderdraft_themes_folder(), root))
            # Only get wonderdraft themes
            and os.path.splitext(root)[1] == ThemesResourceResolver.WONDERDRAFT_THEME_EXTENSION
        ]
        return active_themes

    @staticmethod
    def determine_inactive():
        inactive_themes = [
            os.path.join(Pathfinder.get_deactivated_themes_folder_path(), root)
            for root in os.listdir(Pathfinder.get_deactivated_themes_folder_path())
            # To exclude any rogue files
            if os.path.isfile(os.path.join(Pathfinder.get_deactivated_themes_folder_path(), root))
            # Only get wonderdraft themes
            and os.path.splitext(root)[1] == ThemesResourceResolver.WONDERDRAFT_THEME_EXTENSION
        ]
        return inactive_themes

    def activate_single(self, element: str):
        click.echo(
            Fore.MAGENTA + "activating theme: " + Fore.LIGHTMAGENTA_EX + os.path.basename(element))
        shutil.move(
            element,
            Pathfinder.get_wonderdraft_themes_folder()
        )

    def deactivate_single(self, element: str):
        click.echo(
            Fore.MAGENTA + "deactivating theme: " + Fore.LIGHTMAGENTA_EX + os.path.basename(element))
        shutil.move(
            element,
            Pathfinder.get_deactivated_themes_folder_path()
        )

    def activate_all(self, elements: list):
        click.echo(
            Fore.MAGENTA + "activating all themes")
        for element in elements:
            self.activate_single(element)

    def needs_deactivation(self, profile_elements: list, active: list) -> list:
        return list(set(active) -
                    set([os.path.join(Pathfinder.get_wonderdraft_themes_folder(),
                                      element+ThemesResourceResolver.WONDERDRAFT_THEME_EXTENSION)
                         for element in profile_elements])
                    )

    def needs_activation(self, profile_elements: list, inactive: list) -> list:
        return [os.path.join(Pathfinder.get_deactivated_themes_folder_path(),
                             element+ThemesResourceResolver.WONDERDRAFT_THEME_EXTENSION)
                for element in profile_elements
                if os.path.join(Pathfinder.get_deactivated_themes_folder_path(),
                                element+ThemesResourceResolver.WONDERDRAFT_THEME_EXTENSION) in inactive
                ]

    def dryrun(self, to_activate: list, to_deactivate: list, catchall: bool):
        if catchall:
            click.echo(Fore.MAGENTA + 'This run would have activated these themes: ' + Fore.LIGHTMAGENTA_EX)
            click.echo(print(*[os.path.basename(os.path.splitext(file)[0])
                               for file in ThemesResourceResolver.determine_inactive()], sep="\n"))
            click.echo(Fore.MAGENTA + 'This run would have deactivated these themes: ' + Fore.LIGHTMAGENTA_EX)
        else:
            click.echo(Fore.MAGENTA + 'This run would have activated these themes: ' + Fore.LIGHTMAGENTA_EX)
            click.echo(print(*[os.path.basename(os.path.splitext(file)[0]) for file in to_activate], sep="\n"))
            click.echo(Fore.MAGENTA + 'This run would have deactivated these themes: ' + Fore.LIGHTMAGENTA_EX)
            click.echo(print(*[os.path.basename(os.path.splitext(file)[0]) for file in to_deactivate], sep="\n"))

    def __print_banner(self):
        click.echo(Fore.LIGHTBLUE_EX + '---------------------------------------------------')
        click.echo(Fore.LIGHTBLUE_EX + '------------------THEMES---------------------------')
        click.echo(Fore.LIGHTBLUE_EX + '---------------------------------------------------')