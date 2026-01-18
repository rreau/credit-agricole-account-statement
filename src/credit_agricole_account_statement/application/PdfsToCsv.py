import logging
from pathlib import Path

from credit_agricole_account_statement.adapter.input.pdf.PdfDocument import PdfDocument
from credit_agricole_account_statement.application.CreditAgricoleMonthlyStatementFactory import CreditAgricoleMonthlyStatementFactory
from credit_agricole_account_statement.adapter.output.csv.OperationsCsvExporter import OperationsCsvExporter

from credit_agricole_account_statement.domain.Operations import Operations

logger = logging.getLogger(__name__)

class PdfsToCsv:

    @staticmethod
    def execute(pdf_directory: Path, csv_path:Path):
        logger.info("Starting multiples PDF to CSV aggregation")
        logger.debug("PDF directory: %s", pdf_directory)
        logger.debug("CSV output path: %s", csv_path)

        if not pdf_directory.is_dir():
            logger.error("Provided path is not a directory: %s", pdf_directory)
            return

        operations: Operations = []

        pdf_files = list(pdf_directory.rglob("*.pdf"))
        logger.info("Found %d PDF file(s)", len(pdf_files))

        for pdf_file in pdf_files:
            if not pdf_file.is_file():
                logger.warning("Skipping non-file path: %s", pdf_file)
                continue
            
            logger.info("Processing PDF: %s", pdf_file.name)
            parsing_context = PdfDocument(pdf_file).parse()
            statement = CreditAgricoleMonthlyStatementFactory.build(parsing_context)

            if not statement.operations:
                logger.warning("No operations found in PDF: %s", pdf_file.name)
            
            operations.extend(statement.operations)
            logger.debug("Extracted %d operation(s) from %s", len(statement.operations), pdf_file.name)
        
        OperationsCsvExporter.export(csv_path, operations)
        logger.info("CSV successfully generated: %s (%d operations)", csv_path, len(operations))