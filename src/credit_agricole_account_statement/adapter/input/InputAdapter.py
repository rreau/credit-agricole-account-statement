from typing import Protocol
from credit_agricole_account_statement.domain.CreditAgricoleMonthlyStatement import CreditAgricoleMonthlyStatement

class InputAdapter(Protocol):
    def parse(self) -> CreditAgricoleMonthlyStatement:
        ...