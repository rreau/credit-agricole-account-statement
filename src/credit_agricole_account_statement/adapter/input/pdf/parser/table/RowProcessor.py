from typing import List

from credit_agricole_account_statement.adapter.input.pdf.parser.table.interfaces.Handler import Handler
from credit_agricole_account_statement.adapter.input.pdf.parser.table.handlers.OperationHandler import OperationHandler
from credit_agricole_account_statement.adapter.input.pdf.parser.table.handlers.ExtraDescriptionHandler import ExtraDescriptionHandler
from credit_agricole_account_statement.adapter.input.pdf.parser.table.handlers.SoldeHandler import SoldeHandler
from credit_agricole_account_statement.adapter.input.pdf.parser.ParsingContext import ParsingContext

class RowProcessor():

    HANDLERS: List[Handler] = [
        SoldeHandler(),
        ExtraDescriptionHandler(),
        OperationHandler()
    ]

    @staticmethod
    def process(rows: List[List[str]], context: ParsingContext):
        for row in rows:
            for handler in RowProcessor.HANDLERS:
                if handler.can_handle(row):
                    handler.handle(row, context)
                    break
