from __future__ import annotations
from abc import ABC, abstractmethod
import json
from datetime import datetime


class StatusServiceAbstract(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.__default_error_result = {
            "status": False,
            "error_message": "unidentified error",
            "error_code": 1
        }

        self.__default_success_result = {
            "status": True,
            "error_message": "",
            "error_code": 0
        }

    @abstractmethod
    def heart_beat(self):
        pass

    @property
    def default_error_result(self):
        default = self.__default_error_result.copy()
        default['heartbeat_time'] = datetime.now(tz=None)
        return default

    @property
    def default_success_result(self):
        default = self.__default_success_result.copy()
        default['heartbeat_time'] = datetime.now(tz=None)
        return default

    def health_check(self) -> dict:
        return self.heart_beat()
        pass
