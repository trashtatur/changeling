import logging

from schema import Schema, Optional, Or, SchemaError


class YMLConfigValidator:

    @staticmethod
    def validate_profile(content):
        try:
            return YMLConfigValidator.profile_schema().validate(content)
        except SchemaError as exception:
            logging.getLogger('debug').exception('YML file was not correctly formatted')

    @classmethod
    def profile_schema(cls):
        return Schema({
            'name': str,
            Optional('assets'): [str],
            Optional('brushes'): [str],
            Optional('themes'): [str]

        })
