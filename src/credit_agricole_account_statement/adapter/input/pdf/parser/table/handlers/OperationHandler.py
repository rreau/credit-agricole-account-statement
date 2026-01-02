from typing import List
import re

from credit_agricole_account_statement.adapter.input.pdf.parser.table.interfaces.Handler import Handler
from credit_agricole_account_statement.adapter.input.pdf.parser.ParsingContext import ParsingContext
from credit_agricole_account_statement.domain.Operations import Operation

from credit_agricole_account_statement.adapter.input.pdf.parser.utils.DateParser import DateParser
from credit_agricole_account_statement.adapter.input.pdf.parser.utils.DecimalParser import DecimalParser

class OperationHandler(Handler):
    def can_handle(self, row: List[str]) -> bool:
        if row[0] is None or row[1] is None:
            return False

        return self._is_date(row[0]) and self._is_date(row[1])

    def handle(self, row: List[str], context: ParsingContext) -> None:

        if context.current_date is None:
            print(context)
            raise RuntimeError(
                "OperationHandler called before date was set (SoldeHandler missing?)"
            )

        full_date = f"{row[0]}.{context.current_date.year}"
        transaction_date = DateParser.parse(full_date)

        full_date = f"{row[1]}.{context.current_date.year}"
        value_date = DateParser.parse(full_date)

        description = row[2].replace("\n", " ")

        if context.current_extra_description:
            description += " " + context.current_extra_description.replace("\n", " ")
            context.current_extra_description = None

        debit = DecimalParser.parse(row[3]) if row[3] else None
        credit = DecimalParser.parse(row[4]) if row[4] else None

        operation = Operation(
            transaction_date=transaction_date,
            value_date=value_date,
            description=description,
            debit=debit,
            credit=credit
        )

        context.current_operation = operation
        context.operations.append(operation)

    def _is_date(self, raw: str) -> bool:
        if re.match(r"^\d{2}\.\d{2}$", raw):
            return True
        else:
            return False