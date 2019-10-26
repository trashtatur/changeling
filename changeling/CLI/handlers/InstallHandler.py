import logging
import os
import shutil

import click
import yaml

from changeling.resolving.assetResolving.AssetResourceResolver import AssetResourceResolver
from changeling.file_interactions.YMLConfigValidator import YMLConfigValidator
from changeling.file_interactions.YMLConfigWriter import YMLConfigWriter
from changeling.pathfinder import Pathfinder
from changeling.resolving.brushesResolving.BrushesResourceResolver import BrushesResourceResolver
from changeling.resolving.themesResolving.ThemesResourceResolver import ThemesResourceResolver


class InstallHandler:

    def install(self, profilepath, force):
        opened_profile = self.open_file(profilepath)
        if YMLConfigValidator.validate_profile(opened_profile):
            if os.path.splitext(profilepath)[1] == '.yml':
                self.__act_according_to_mode(profilepath, force)
            elif os.path.splitext(profilepath)[1] == '.yaml':
                new_path = self.__change_file_ending(profilepath)
                self.__act_according_to_mode(new_path, force)

        else:
            click.echo('Profile is not correctly formatted. Make sure to write it properly')

    def install_from_current(self, profilename, force):
        cleaned_profilename = os.path.splitext(profilename)[0] + '.yml'
        asset_folder_names = [os.path.basename(folder) for folder in AssetResourceResolver.determine_active()]
        brushes_folder_names = [os.path.basename(folder) for folder in BrushesResourceResolver.determine_active()]
        themes_file_names = [os.path.basename(file) for file in ThemesResourceResolver.determine_active()]
        yml_data = {'name': profilename}
        if len(asset_folder_names) > 0:
            yml_data['assets'] = asset_folder_names
        if len(brushes_folder_names) > 0:
            yml_data['brushes'] = brushes_folder_names
        if len(themes_file_names) > 0:
            yml_data['themes'] = themes_file_names
        if not force and self.__check_if_profile_exists(cleaned_profilename):
            click.echo('Not installing profile: ' + profilename)
            click.echo('to do so anyway, exectute again with option --force')
        else:
            YMLConfigWriter.write_profile(yml_data, cleaned_profilename)

    def open_file(self, path):
        if os.path.isfile(path):
            try:
                conf = yaml.safe_load(open(path))
                return conf
            except yaml.YAMLError as error:
                logging.getLogger('debug').exception('YML File could not be opened')

    def __act_according_to_mode(self, profilepath, mode):
        all_profiles = os.listdir(Pathfinder.get_profile_directory())
        if not mode and self.__check_if_profile_exists(profilepath):
            click.echo('Not installing profile: ' + os.path.splitext(profilepath)[0])
            click.echo('to do so anyway, exectute again with option --force')
            pass
        else:
            click.echo('Installing profile: ' + os.path.splitext(profilepath)[0])
            shutil.copy(profilepath, Pathfinder.get_profile_directory())

    def __change_file_ending(self, profilepath):

        new_name = profilepath[:-5] + '.yml'
        shutil.move(profilepath, new_name)
        return new_name

    def __check_if_profile_exists(self, profilepath):
        all_profiles = os.listdir(Pathfinder.get_profile_directory())
        if os.path.basename(profilepath) in all_profiles:
            return True
        return False
