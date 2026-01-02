from typing import List
import re

from ca_account_statement.adapter.input.pdf.parser.ParsingContext import ParsingContext
from ca_account_statement.adapter.input.pdf.parser.table.interfaces.Handler import Handler
from ca_account_statement.domain.Balances import Balance
from ca_account_statement.adapter.input.pdf.parser.utils.DateParser import DateParser
from ca_account_statement.adapter.input.pdf.parser.utils.DecimalParser import DecimalParser

class SoldeHandler(Handler):
    def can_handle(self, row: List[str]) -> bool:
        if row[0] is not None and "Solde au" in row[0]:
            return True
        else:
            return False

    def handle(self, row: List[str], context: ParsingContext) -> None:
        data = row[0]
        m = re.search(r"(\d{2}\.\d{2}\.\d{2}).(.+\,\d{2})$", data)
        if m is None:
            raise ValueError("DONT WORK")

        solde_date = DateParser.parse(m.group(1))
        amount = DecimalParser.parse(m.group(2))

        current_balance: Balance = Balance(
            as_of=solde_date,
            amount=amount
        )

        context.current_date = solde_date
        context.current_balance = current_balance
        context.balances.append(current_balance)