from typing import List

from ca_account_statement.adapter.input.pdf.parser.table.interfaces.Handler import Handler
from ca_account_statement.adapter.input.pdf.parser.ParsingContext import ParsingContext

class ExtraDescriptionHandler(Handler):
    def can_handle(self, row: List[str]) -> bool:
        if row[:2] == ["", ""] and row[-3:] == ["", "", ""]:
            return True
        else:
            return False

    def handle(self, row: List[str], context: ParsingContext) -> None:
        extra_description = row[2]
        context.current_extra_description = extra_description