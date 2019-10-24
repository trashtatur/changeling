import os
import shutil

from changeling.util import Util

CHANGELING_CONFIG_PATH = os.path.join(os.getenv('APPDATA'), 'changeling')
CHANGELING_PROFILES_PATH = os.path.join(CHANGELING_CONFIG_PATH, 'profiles')


def is_initialized():
    if os.path.exists(CHANGELING_CONFIG_PATH):
        return True
    return False


def initialize(func):
    if not is_initialized():
        print('INITIALIZING')
        os.mkdir(CHANGELING_CONFIG_PATH)
        os.mkdir(CHANGELING_PROFILES_PATH)
        shutil.copy(os.path.join(Util.get_root(), 'changeling', 'config', 'config.yml'), CHANGELING_CONFIG_PATH)
        shutil.copy(os.path.join(Util.get_root(), 'profiles', 'all.yml'), CHANGELING_PROFILES_PATH)
    return func