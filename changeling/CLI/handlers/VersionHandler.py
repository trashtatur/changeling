from changeling.file_interactions.YMLConfigReader import YMLConfigReader


class VersionHandler:

    def version(self):
        return YMLConfigReader.get_local_version()