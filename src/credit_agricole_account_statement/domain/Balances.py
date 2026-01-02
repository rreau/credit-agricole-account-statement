from dataclasses import dataclass
from typing import NewType, List
from decimal import Decimal
from datetime import date

@dataclass(frozen=True, slots=True)
class Balance:
    as_of: date
    amount: Decimal

Balances = List[Balance]