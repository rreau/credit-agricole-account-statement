from datetime import datetime, date

from ca_account_statement.adapter.input.pdf.parser.utils.Parser import Parser

class DateParser(Parser[date]):
    @staticmethod
    def parse(raw: str) -> date:
        splitted_date = raw.split('.')
        if len(splitted_date[2]) == 2:
            parsed_datetime = datetime.strptime(raw, "%d.%m.%y")
        elif len(splitted_date[2]) == 4:
            parsed_datetime = datetime.strptime(raw, "%d.%m.%Y")
        else:
            raise ValueError(f"Dont parse this date : {raw}")

        return parsed_datetime.date()