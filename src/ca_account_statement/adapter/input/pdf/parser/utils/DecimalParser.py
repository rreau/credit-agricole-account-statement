from decimal import Decimal, InvalidOperation

from ca_account_statement.adapter.input.pdf.parser.utils.Parser import Parser

class DecimalParser(Parser[Decimal]):
    @staticmethod
    def parse(raw: str) -> Decimal:
        if not raw:
            raise ValueError(f"Invalid decimal value for parser: '{raw}'")

        cleaned_value = raw.replace(" ", "").replace(",", ".")
        try:
            return Decimal(cleaned_value)
        except InvalidOperation as exc:
            raise InvalidOperation(
                f"Invalid decimal value: '{cleaned_value}'"
            ) from exc