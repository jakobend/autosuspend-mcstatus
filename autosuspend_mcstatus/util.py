from typing import *
import configparser
from autosuspend.checks import ConfigurationError
from mcstatus import MinecraftServer

class MCStatusMixin:
    @classmethod
    def collect_init_args(cls, config: configparser.SectionProxy) -> Dict[str, Any]:
        args = {} # type: Dict[str, Any]
        try:
            address = config.get("server", fallback="localhost")
            args["server"] = MinecraftServer.lookup(address)
        except ValueError as error:
            raise ConfigurationError(
                "Unable to look up server: {}".format(error)
            ) from error
        
        try:
            args["retries"] = config.getint("retries", fallback=3)
        except ValueError as error:
            raise ConfigurationError("Retries must be integer") from error

        return args

    def __init__(self, server: MinecraftServer, retries: int):
        self._server = server
        self._retries = retries

    @property
    def _address(self):
        return "{}:{}".format(self._server.host, self._server.port)
