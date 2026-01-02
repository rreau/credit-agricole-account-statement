from dataclasses import dataclass
from decimal import Decimal
from datetime import date

from credit_agricole_account_statement.domain.Operations import Operations
from credit_agricole_account_statement.domain.Balances import Balances

@dataclass()
class CreditAgricoleMonthlyStatement:
    account_statement_number: Decimal
    effective_date: date
    operations: Operations
    balances: Balances
