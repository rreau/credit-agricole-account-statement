from pathlib import Path

import pdfplumber

from ca_account_statement.adapter.input.pdf.PdfTableExtractor import PdfTableExtractor
from ca_account_statement.adapter.input.pdf.PdfTextExtractor  import PdfTextExtractor
from ca_account_statement.adapter.input.pdf.PdfWordsExtractor import PdfWordsExtractor

from ca_account_statement.adapter.input.pdf.parser.EffectiveDateParser import EffectiveDateParser
from ca_account_statement.adapter.input.pdf.parser.AccountStatementNbrParser import AccountStatementNbrParser
from ca_account_statement.adapter.input.pdf.parser.table.RowProcessor import RowProcessor
from ca_account_statement.adapter.input.pdf.parser.ParsingContext import ParsingContext

from ca_account_statement.domain.CreditAgricoleMonthlyStatement import CreditAgricoleMonthlyStatement
from ca_account_statement.application.CreditAgricoleMonthlyStatementFactory import CreditAgricoleMonthlyStatementFactory

class PdfDocument:

    def __init__(self, path: Path):
        self.path: Path = path
        self.text_extractor: PdfTextExtractor = PdfTextExtractor()
        self.words_extractor: PdfWordsExtractor = PdfWordsExtractor()
        self.row_processor: RowProcessor = RowProcessor()

    def parse(self) -> ParsingContext:
        """Parse the PDF and build a complete domain statement."""
        parsing_context: ParsingContext = ParsingContext()

        with pdfplumber.open(self.path) as pdf:
            first_page_content = self.text_extractor.extract(pdf.pages[0])
            parsing_context.account_statement_number = AccountStatementNbrParser.parse(first_page_content)
            parsing_context.effective_date = EffectiveDateParser.parse(first_page_content)

            pdf_table = []

            for page in pdf.pages:
                current_table = self._process_page(page)
                pdf_table.extend(current_table)

            pdf_table.reverse()
            RowProcessor.process(pdf_table, parsing_context)

        return parsing_context

    def _process_page(self, page):
        """
        Extract words, detect row boundaries, extract tables,
        and process each row into the parsing context.
        """
        words = self.words_extractor.extract(page)
        row_boundaries = PdfTableExtractor.get_row_boundaries(words)
        table_settings = {"explicit_horizontal_lines": row_boundaries}
        table = PdfTableExtractor.extract(page, table_settings)
        return table
