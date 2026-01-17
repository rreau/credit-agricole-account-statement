import argparse
import logging
from pathlib import Path

from credit_agricole_account_statement.application.PdfToCsv import PdfToCsv
from credit_agricole_account_statement.application.PdfsToCsv import PdfsToCsv

APP_LOGGER_NAME = "credit_agricole_account_statement"
logger = logging.getLogger(APP_LOGGER_NAME)

def ensure_output_dir(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)

def silence_third_party_logs() -> None:
    noisy_loggers = ["pdfminer"]

    for name in noisy_loggers:
        logging.getLogger(name).setLevel(logging.WARNING)

def configure_logging(verbosity: int) -> None:
    level = logging.WARNING
    if verbosity == 1:
        level = logging.INFO
    elif verbosity >= 2:
        level = logging.DEBUG

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    logging.getLogger(APP_LOGGER_NAME).setLevel(level)


def main():
    parser = argparse.ArgumentParser(
        prog="ca-statement",
        description="Convert Crédit Agricole PDF statements to CSV",
    )

    parser.add_argument(
        "-v", "--verbose",
        action="count",
        default=0,
        help="Increase verbosity (-v: INFO, -vv: DEBUG)",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # pdf-to-csv
    pdf_to_csv = subparsers.add_parser("pdf2csv")
    pdf_to_csv.add_argument("input", type=Path)
    pdf_to_csv.add_argument("-o", "--output", type=Path, required=True)

    # pdfs-to-csv
    pdfs_to_csv = subparsers.add_parser("pdfs2csv")
    pdfs_to_csv.add_argument("input_dir", type=Path)
    pdfs_to_csv.add_argument("-o", "--output", type=Path, required=True)

    args = parser.parse_args()

    configure_logging(args.verbose)
    silence_third_party_logs()

    if args.command == "pdf2csv":
        logger.info("Converting PDF to CSV: %s", args.input)
        ensure_output_dir(args.output)
        PdfToCsv.execute(args.input, args.output)

    elif args.command == "pdfs2csv":
        logger.info("Converting PDFs in directory: %s", args.input_dir)
        ensure_output_dir(args.output)
        PdfsToCsv.execute(args.input_dir, args.output)
