from abc import ABC
from typing import Any
from datetime import datetime


class EventInterface(ABC):

    def __init__(
        self,
        datetime_ocurred: datetime,
        event_data: Any
    ) -> None:

        self.datetime_ocurred = datetime_ocurred
        self.event_data = event_data
