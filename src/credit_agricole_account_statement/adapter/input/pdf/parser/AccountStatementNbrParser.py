import re
from decimal import Decimal

class AccountStatementNbrParser():

    @staticmethod
    def parse(page_content: str):
        m = re.search(r"RELEVE DE COMPTES.+N\° (\d+)", page_content)
        if m is None:
            raise ValueError("Account statement number not found !")

        return Decimal(m.group(1))
