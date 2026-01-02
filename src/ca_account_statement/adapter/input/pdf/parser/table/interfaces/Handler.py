from typing import Protocol, List

from ca_account_statement.adapter.input.pdf.parser.ParsingContext import ParsingContext

class Handler(Protocol):
    def can_handle(self, row: List[str]) -> bool:
        ...

    def handle(self, row: List[str], context: ParsingContext) -> None:
        ...