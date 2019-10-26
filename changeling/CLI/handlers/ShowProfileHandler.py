import logging
import os
import click


from changeling.pathfinder import Pathfinder


class ShowProfileHandler:

    def show_profile(self, profile):
        try:
            with open(os.path.join(Pathfinder.get_profile_directory(),profile+'.yml')) as profile:
                return profile.read()
        except FileNotFoundError as exception:
            click.echo('This profile is not installed into changeling')
            logging.getLogger('debug').exception('Could not show profile '+profile+' because it is not installed')