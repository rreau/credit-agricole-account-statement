# Crédit Agricole Account Statement Parser

This library allows you to **extract transactions from Crédit Agricole PDF account statements** downloaded **from their website**. It converts PDF statements into structured data that can be exported to CSV or processed directly in Python.  

> ⚠️ Note: This library does **not** support scanned PDFs or image-based statements. OCR is not available at the moment, but may be added in a future release.

## Command Line Interface

```bash
root@root:~$ ca-statement --help
usage: ca-statement [-h] [-v] {pdf2csv,pdfs2csv} ...

Convert Crédit Agricole PDF statements to CSV

positional arguments:
  {pdf2csv,pdfs2csv}
    pdf2csv           Convert a single PDF statement to CSV
    pdfs2csv          Convert all PDF statements in a directory to a single CSV

options:
  -h, --help          show this help message and exit
  -v, --verbose       Increase verbosity (-v: INFO, -vv: DEBUG)

```
