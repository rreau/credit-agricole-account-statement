from typing import Optional, Any, List
from pdfplumber.page import Page
import re

class PdfTableExtractor():

    DEFAULT_TABLE_SETTINGS: dict[str, str | int | List[int]]= {
        "vertical_strategy": "lines",
        "horizontal_strategy": "lines",
        "explicit_vertical_lines": [],
        "explicit_horizontal_lines": [],   # CHANGED
        "snap_tolerance": 4,               # CHANGED
        "snap_x_tolerance": 3,
        "snap_y_tolerance": 4,             # CHANGED
        "join_tolerance": 3,
        "join_x_tolerance": 3,
        "join_y_tolerance": 3,
        "edge_min_length": 3,
        "edge_min_length_prefilter": 1,
        "min_words_vertical": 3,
        "min_words_horizontal": 1,
        "intersection_tolerance": 3,
        "intersection_x_tolerance": 3,
        "intersection_y_tolerance": 3,
        "text_tolerance": 3,
        "text_x_tolerance": 3,
        "text_y_tolerance": 3
    }

    @staticmethod
    def extract(page: Page, table_setting: Optional[Any] = None) -> Any:
        _table_setting = PdfTableExtractor.DEFAULT_TABLE_SETTINGS
        if table_setting:
            _table_setting.update(table_setting)
        table = page.extract_table(table_settings=_table_setting)
        return table

    @staticmethod
    def get_row_boundaries(words: Any) -> List[int]:
        predicted_lines = []
        last_top, last_bottom = 0, 0
        for word in words:
            if re.match(r"^\d{2}\.\d{2}$", word["text"]) and (word["top"] != last_top and word["bottom"] != last_bottom):
                predicted_lines.append(word["top"])
                predicted_lines.append(word["bottom"])

                last_top = word["top"]
                last_bottom = word["bottom"]

        return predicted_lines