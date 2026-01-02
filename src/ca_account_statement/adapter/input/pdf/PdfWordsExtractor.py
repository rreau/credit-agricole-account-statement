from typing import Any
from pdfplumber.page import Page

class PdfWordsExtractor():
    def __init__(self):
        pass

    def extract(self, page: Page) -> Any:
        words = page.extract_words()
        return words