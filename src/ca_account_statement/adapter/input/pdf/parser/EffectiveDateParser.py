import re
from ca_account_statement.adapter.input.pdf.parser.utils.DateParser import DateParser

class EffectiveDateParser():

    MONTHS_FR = {
        "janvier": "01",
        "février": "02",
        "mars": "03",
        "avril": "04",
        "mai": "05",
        "juin": "06",
        "juillet": "07",
        "août": "08",
        "septembre": "09",
        "octobre": "10",
        "novembre": "11",
        "décembre": "12"
    }

    @staticmethod
    def parse(page_content: str):
        m = re.search(r"Date d'arrêté :.+(\d{2}) (\w+) (\d{4})", page_content)
        if m is None:
            raise ValueError("Effective date not found !")
        day = m.group(1)
        month = EffectiveDateParser.MONTHS_FR[str(m.group(2)).lower()]
        year = m.group(3)
        effective_date = DateParser.parse(f"{day}.{month}.{year}")
        return effective_date
