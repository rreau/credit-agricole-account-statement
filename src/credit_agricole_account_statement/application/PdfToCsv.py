from pathlib import Path

from credit_agricole_account_statement.adapter.input.pdf.PdfDocument import PdfDocument
from credit_agricole_account_statement.application.CreditAgricoleMonthlyStatementFactory import CreditAgricoleMonthlyStatementFactory
from credit_agricole_account_statement.adapter.output.csv.OperationsCsvExporter import OperationsCsvExporter

class PdfToCsv:
    @staticmethod
    def execute(pdf_path: Path, csv_path:Path):
        parsing_context = PdfDocument(pdf_path).parse()
        statement = CreditAgricoleMonthlyStatementFactory.build(parsing_context)
        OperationsCsvExporter.export(csv_path, statement)