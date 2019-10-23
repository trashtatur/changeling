import os

import click

from changeling.assetResolving.AssetMover import AssetMover
from changeling.assetResolving.ProfileResolver import ProfileResolver


class ActivateHandler:

    def activate(self, profilename, dryrun: bool):
        profile_resolver = ProfileResolver()
        asset_mover = AssetMover(profile_resolver)
        all_modules = asset_mover.determine_active_modules() + asset_mover.determine_inactive_modules()
        foldernames = [os.path.basename(folder) for folder in all_modules]
        modules_in_profile = [
            os.path.basename(assetfolder)
            for assetfolder in profile_resolver.resolve_profile(profilename)
        ]
        non_existing = (list(set(modules_in_profile) - set(foldernames)))
        if len(non_existing) == 0:
            asset_mover.activate_profile(profilename, dryrun)
        else:
            click.echo('Some asset folders in your profile do not seem to exist: ')
            click.echo(print(*non_existing, sep="\n"))
            if click.confirm("Do you want to activate this profile anyway and ignore the non existing ones?"):
                asset_mover.activate_profile(profilename, dryrun)
            else:
                pass
