import logging
import os

import click

from changeling.resolving.assetResolving.AssetResourceResolver import AssetResourceResolver
from changeling.resolving.ProfileResolver import ProfileResolver
from changeling.resolving.brushesResolving.BrushesResourceResolver import BrushesResourceResolver
from changeling.resolving.themesResolving.ThemesResourceResolver import ThemesResourceResolver


class ActivateHandler:

    def activate(self, profilename, dryrun: bool):
        profile_resolver = ProfileResolver()
        profile = profile_resolver.resolve_profile(profilename)
        self.__activate_assets(profilename, dryrun, profile.assets)
        self.__activate_brushes(profilename, dryrun, profile.brushes)
        self.__activate_themes(profilename, dryrun, profile.themes)
        if not dryrun:
            logging.getLogger('debug').info('Activated profile: '+profilename)

    def __activate_assets(self, profilename, dryrun, assetlist):
        asset_resolver = AssetResourceResolver()
        if profilename == 'all':
            asset_resolver.activate(profilename, dryrun, assetlist, True)
        else:
            all_assets = asset_resolver.determine_active() + asset_resolver.determine_inactive()
            foldernames = [os.path.basename(folder) for folder in all_assets]
            assets_in_profile = [
                os.path.basename(assetfolder)
                for assetfolder in assetlist
            ]
            if len(assets_in_profile) == 0:
                asset_resolver.activate(profilename, dryrun, assetlist, True)
            else:
                non_existing = (list(set(assets_in_profile) - set(foldernames)))
                if len(non_existing) == 0:
                    asset_resolver.activate(profilename, dryrun, assetlist, False)
                else:
                    click.echo('Some asset folders in your profile do not seem to exist: ')
                    click.echo(print(*non_existing, sep="\n"))
                    if click.confirm("Do you want to activate this profile anyway and ignore the non existing ones?"):
                        asset_resolver.activate(profilename, dryrun, assetlist, False)

    def __activate_brushes(self, profilename, dryrun, brusheslist):
        brushes_resolver = BrushesResourceResolver()
        if profilename == 'all':
            brushes_resolver.activate(profilename, dryrun, brusheslist, True)
        else:
            all_brushes = brushes_resolver.determine_active() + brushes_resolver.determine_inactive()
            foldernames = [os.path.basename(folder) for folder in all_brushes]
            brushes_in_profile = [
                os.path.basename(brushes_folder)
                for brushes_folder in brusheslist
            ]
            if len(brushes_in_profile) == 0:
                brushes_resolver.activate(profilename, dryrun, brusheslist, True)
            else:
                non_existing = (list(set(brushes_in_profile) - set(foldernames)))
                if len(non_existing) == 0:
                    brushes_resolver.activate(profilename, dryrun, brusheslist, False)
                else:
                    click.echo('Some brushes folders in your profile do not seem to exist: ')
                    click.echo(print(*non_existing, sep="\n"))
                    if click.confirm("Do you want to activate this profile anyway and ignore the non existing ones?"):
                        brushes_resolver.activate(profilename, dryrun, brusheslist, False)

    def __activate_themes(self, profilename, dryrun, themeslist):
        themes_resolver = ThemesResourceResolver()
        if profilename == 'all':
            themes_resolver.activate(profilename, dryrun, themeslist, True)
        else:
            all_themes = themes_resolver.determine_active() + themes_resolver.determine_inactive()
            filenames = [os.path.splitext(os.path.basename(file))[0] for file in all_themes]
            themes_in_profile = [
                os.path.basename(themes_folder)
                for themes_folder in themeslist
            ]
            if len(themes_in_profile) == 0:
                themes_resolver.activate(profilename, dryrun, themeslist, True)
            else:
                non_existing = (list(set(themes_in_profile) - set(filenames)))
                if len(non_existing) == 0:
                    themes_resolver.activate(profilename, dryrun, themeslist, False)
                else:
                    click.echo('Some themes in your profile do not seem to exist: ')
                    click.echo(print(*non_existing, sep="\n"))
                    if click.confirm("Do you want to activate this profile anyway and ignore the non existing ones?"):
                        themes_resolver.activate(profilename, dryrun, themeslist, False)
