import abc


class ResourceResolverInterface(abc.ABC):

    @abc.abstractmethod
    def activate(self, profilename: str, dryrun: bool, elements: list, catchall: bool):
        pass

    @staticmethod
    @abc.abstractmethod
    def determine_active() -> list:
        pass

    @staticmethod
    @abc.abstractmethod
    def determine_inactive() -> list:
        pass

    @abc.abstractmethod
    def activate_single(self, element: str):
        pass

    @abc.abstractmethod
    def deactivate_single(self, element: str):
        pass

    @abc.abstractmethod
    def needs_deactivation(self, profile_modules: list, active: list) -> list:
        pass

    @abc.abstractmethod
    def needs_activation(self, profile_modules: list, inactive: list) -> list:
        pass

    @abc.abstractmethod
    def activate_all(self, elements: list):
        pass

    @abc.abstractmethod
    def dryrun(self, to_activate: list, to_deactivate: list, catchall: bool):
        pass
