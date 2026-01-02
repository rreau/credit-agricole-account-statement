from pdfplumber.page import Page

class PdfTextExtractor():
    def __init__(self):
        pass

    def extract(self, page: Page) -> str:
        text = page.extract_text_simple()
        return text