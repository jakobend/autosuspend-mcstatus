from typing import *
import configparser
import socket
from mcstatus import MinecraftServer
from autosuspend.checks import Activity, ConfigurationError
from .util import MCStatusMixin

class ServerOnline(Activity, MCStatusMixin):
    @classmethod
    def create(cls, name: str, config: configparser.SectionProxy) -> "ServerOnline":
        return cls(name, **cls.collect_init_args(config))
    
    def __init__(self, name: str, **kwargs) -> None:
        MCStatusMixin.__init__(self, **kwargs)
        Activity.__init__(self, name)
    
    def check(self) -> Optional[str]:
        self.logger.debug("Sending SLP to {}".format(self._address))

        try:
            self._server.ping(tries=self._retries)
            return "Server is online"
        except socket.timeout as error:
            pass
        except ConnectionError as error:
            pass


class PlayersOnline(Activity, MCStatusMixin):
    @classmethod
    def create(cls, name: str, config: configparser.SectionProxy) -> "PlayersOnline":
        try:
            treshold = config.getint("treshold", fallback=0)
        except ValueError as error:
            raise ConfigurationError("Treshold must be integer") from error
        
        return cls(name, treshold, **cls.collect_init_args(config))

    def __init__(self, name: str, treshold: int, **kwargs) -> None:
        MCStatusMixin.__init__(self, **kwargs)
        Activity.__init__(self, name)
        self._treshold = treshold

    def check(self) -> Optional[str]:
        self.logger.debug("Sending SLP to {}".format(self._address))

        try:
            status = self._server.status(tries=self._retries)
            if status.players.online > self._treshold:
                return "{} players online on {}".format(
                    status.players.online,
                    self._address
                )
        except socket.timeout as error:
            self.logger.warning("SLP timed out, server is probably down")
        except ConnectionError as error:
            self.logger.warning("Connection error: {}".format(error))
