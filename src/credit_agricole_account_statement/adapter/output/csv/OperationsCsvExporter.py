import csv
from pathlib import Path

from credit_agricole_account_statement.domain.Operations import Operations

class OperationsCsvExporter():

    @staticmethod
    def export(filepath: Path, operations: Operations, delimiter: str = ';') -> None:
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