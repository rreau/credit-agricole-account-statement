from dataclasses import dataclass
from typing import Optional, NewType
from decimal import Decimal
from datetime import date

@dataclass(frozen=True, slots=True)
class Operation:
    transaction_date: date
    value_date: date
    description: str
    credit: Optional[Decimal] = None
    debit: Optional[Decimal] = None

Operations = list[Operation]