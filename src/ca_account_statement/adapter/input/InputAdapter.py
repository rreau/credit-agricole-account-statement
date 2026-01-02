from typing import Protocol
from ca_account_statement.domain.CreditAgricoleMonthlyStatement import CreditAgricoleMonthlyStatement

class InputAdapter(Protocol):
    def parse(self) -> CreditAgricoleMonthlyStatement:
        ...