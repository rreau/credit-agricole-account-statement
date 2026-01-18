import logging
from pathlib import Path

from credit_agricole_account_statement.adapter.input.pdf.PdfDocument import PdfDocument
from credit_agricole_account_statement.application.CreditAgricoleMonthlyStatementFactory import CreditAgricoleMonthlyStatementFactory
from credit_agricole_account_statement.adapter.output.csv.OperationsCsvExporter import OperationsCsvExporter

logger = logging.getLogger(__name__)

class PdfToCsv:
    
    @staticmethod
    def execute(pdf_path: Path, csv_path: Path) -> None:
        if not pdf_path.exists():
            logger.error("Input file does not exist: %s", pdf_path)
            return

        if not pdf_path.is_file():
            logger.error("Input path is not a file: %s", pdf_path)
            return

        if pdf_path.suffix.lower() != ".pdf":
            logger.error("Input file is not a PDF: %s", pdf_path)
            return

        logger.info("Starting PDF → CSV conversion for '%s'", pdf_path.name)

        parsing_context = PdfDocument(pdf_path).parse()
        statement = CreditAgricoleMonthlyStatementFactory.build(parsing_context)

        logger.info("Exporting %d operations", len(statement.operations))
        OperationsCsvExporter.export(csv_path, statement.operations)

        logger.info("CSV generated: %s", csv_path)

