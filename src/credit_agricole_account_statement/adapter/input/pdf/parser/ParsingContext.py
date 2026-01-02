from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from typing import Optional

from credit_agricole_account_statement.domain.Operations import Operations, Operation
from credit_agricole_account_statement.domain.Balances import Balances, Balance
from credit_agricole_account_statement.domain.CreditAgricoleMonthlyStatement import CreditAgricoleMonthlyStatement

@dataclass()
class ParsingContext:
    account_statement_number: Optional[Decimal] = None
    effective_date: Optional[date] = None
    operations: Operations = field(default_factory=list)
    balances: Balances = field(default_factory=list)

    current_date: Optional[date] = None
    current_balance: Optional[Balance] = None
    current_operation: Optional[Operation] = None
    current_extra_description: Optional[str] = None

    def build_statement(self) -> CreditAgricoleMonthlyStatement:
        if self.account_statement_number is None:
            raise ValueError("Missing account_statement_number")
        if self.effective_date is None:
            raise ValueError("Missing effective_date")
        if self.operations is None:
            raise ValueError("Missing operations")
        if self.balances is None:
            raise ValueError("Missing balances")

        return CreditAgricoleMonthlyStatement(
            account_statement_number=self.account_statement_number,
            effective_date=self.effective_date,
            operations=self.operations,
            balances=self.balances,
        )

    def __str__(self):
        return (
            "ParsingContext(\n"
            f"  account_statement_number={self.account_statement_number}\n"
            f"  effective_date={self.effective_date}\n"
            f"  operations_count={len(self.operations)}\n"
            f"  balances_count={len(self.balances)}\n"
            f"  current_date={self.current_date}\n"
            f"  current_balance={self.current_balance}\n"
            f"  current_operation={self.current_operation}\n"
            f"  current_extra_description={self.current_extra_description!r}\n"
            ")"
        )