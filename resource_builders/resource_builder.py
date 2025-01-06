from abc import ABC, abstractmethod


class ResourcesBuilder(ABC):
    @abstractmethod
    def create_identity(self, *args):
        raise NotImplementedError

    @abstractmethod
    def create_role(self, *args):
        raise NotImplementedError

    @abstractmethod
    def create_identity_role_binding(self, *args):
        raise NotImplementedError

    @abstractmethod
    def create_resource(self, *args):
        raise NotImplementedError

    @abstractmethod
    def create_resource_relation(self, *args):
        raise NotImplementedError
