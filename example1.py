import json
from typing import List, Dict, Union


JSONValueType = Union[str, int, float, List, Dict]
JSONType = Dict[str, JSONValueType]


class Model:
    base_url = None  # type: str

    def serialize(self) -> str:
        return json.dumps(self.get_json())

    def get_json(self) -> JSONType:
        raise NotImplementedError()


class ServerGroup(Model):

    def __init__(self, name: str) -> None:
        self.id = None  # type: int
        self.name = name

    def get_json(self) -> JSONType:
        return {'name': self.name}


class Server(Model):

    def __init__(self, fqdn: str, server_group: ServerGroup, name: str=None) -> None:
        self.id = None  # type: int
        self.fqdn = fqdn
        self.name = name
        self.server_group = server_group

    def get_json(self) -> JSONType:
        return {
            'name': self.name,
            'fqdn': self.fqdn,
            'server_group': self.server_group.get_json(),
        }


class AbstractService:

    def get_server_groups(self) -> List[ServerGroup]:
        raise NotImplementedError()

    def get_servers(self, server_group: ServerGroup) -> List[Server]:
        raise NotImplementedError()


class DummyService(AbstractService):

    def get_server_groups(self) -> List[ServerGroup]:
        return [ServerGroup('Sunscrapers'), ServerGroup('Startupworks')]

    def get_servers(self, server_group: ServerGroup) -> List[Server]:
        if server_group.name == 'Sunscrapers':
            return [Server('sunscrapers.com', server_group)]
        else:
            return [Server('startupworks.co', server_group)]


class DummyAPIClient:

    def post(self, model: Model) -> None:
        print('POST {0}'.format(model.serialize()))


class Consumer:

    def __init__(self, service: AbstractService, api_client) -> None:
        self.service = service
        self.api = api_client

    def migrate(self) -> None:
        for server_group in self.service.get_server_groups():
            self.api.post(server_group)
            for server in self.service.get_servers(server_group):
                self.api.post(server)


if __name__ == '__main__':
    consumer = Consumer(DummyService(), DummyAPIClient())
    consumer.migrate()
