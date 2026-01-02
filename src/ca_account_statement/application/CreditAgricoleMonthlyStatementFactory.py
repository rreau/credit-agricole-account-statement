from ca_account_statement.adapter.input.pdf.parser.ParsingContext import ParsingContext
from ca_account_statement.domain.CreditAgricoleMonthlyStatement import CreditAgricoleMonthlyStatement

class CreditAgricoleMonthlyStatementFactory:

    @staticmethod
    def build(context: ParsingContext) -> CreditAgricoleMonthlyStatement:
        if context.account_statement_number is None:
            raise ValueError("Missing account_statement_number")

        if context.effective_date is None:
            raise ValueError("Missing effective_date")

        if context.operations is None:
            raise ValueError("Missing operations")

        if context.balances is None:
            raise ValueError("Missing balances")

        return CreditAgricoleMonthlyStatement(
            account_statement_number=context.account_statement_number,
            effective_date=context.effective_date,
            operations=context.operations,
            balances=context.balances,
        )