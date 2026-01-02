from typing import Protocol, TypeVar

T_co = TypeVar("T_co", covariant = True)

class Parser(Protocol[T_co]):
    @staticmethod
    def parse(raw: str) -> T_co:
        ...