from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar("T")


class RepositoryInterface(Generic[T], ABC):

    @abstractmethod
    def create(self, entity: T) -> Optional[T]:
        raise NotImplementedError

    @abstractmethod
    def update(self, entity: T) -> Optional[T]:
        raise NotImplementedError

    @abstractmethod
    def find(self, id: str) -> T:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[T]:
        raise NotImplementedError
