import csv
from pathlib import Path

from ca_account_statement.domain.CreditAgricoleMonthlyStatement import CreditAgricoleMonthlyStatement

class OperationsCsvExporter():

    @staticmethod
    def export(filepath: Path, statement: CreditAgricoleMonthlyStatement, delimiter: str = ';') -> None:
        operations = statement.operations
        with open(filepath, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=delimiter)

            writer.writerow(["date", "description", "debit", "credit"])

            for op in operations:
                writer.writerow([
                    op.transaction_date,
                    op.description,
                    str(op.debit) if op.debit is not None else "",
                    str(op.credit) if op.credit is not None else "",
                ])