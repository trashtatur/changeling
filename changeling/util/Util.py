import os
from pathlib import Path


def get_root():
    return Path(__file__).parent.parent.parent


def get_config_file_location():
    return os.path.join(
        get_root(),
        'changeling',
        'config',
        'config.yml'
    )
