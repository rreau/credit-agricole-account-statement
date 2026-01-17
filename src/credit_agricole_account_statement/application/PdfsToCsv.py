from pathlib import Path

from credit_agricole_account_statement.adapter.input.pdf.PdfDocument import PdfDocument
from credit_agricole_account_statement.application.CreditAgricoleMonthlyStatementFactory import CreditAgricoleMonthlyStatementFactory
from credit_agricole_account_statement.adapter.output.csv.OperationsCsvExporter import OperationsCsvExporter

from credit_agricole_account_statement.domain.Operations import Operations

class PdfsToCsv:

    @staticmethod
    def execute(pdf_directory: Path, csv_path:Path):
        if not pdf_directory.is_dir():
            print(f"This path {pdf_directory.name} is not directory")
            return

        operations: Operations = []
        
        for pdf_file in pdf_directory.rglob("*.pdf"):
            if not pdf_file.is_file():
                continue
        
            parsing_context = PdfDocument(pdf_file).parse()
            statement = CreditAgricoleMonthlyStatementFactory.build(parsing_context)
            operations.extend(statement.operations)
        
        OperationsCsvExporter.export(csv_path, operations)