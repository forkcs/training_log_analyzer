import re
import gzip
import json
import argparse

from typing import Generator, Iterable

from string import Template


config = {
    'REPORT_SIZE': 1000,
    'REPORT_DIR': './reports',
    'LOG_DIR': './log'
}

with open('report.html', 'r') as report_template:
    REPORT_TEMPLATE = report_template.read()


def get_last_log_filename(logs_dir: str) -> str:
    pass


def generate_report_dict(log_file: Iterable) -> dict:
    for line in log_file:
        pass


def generate_report(report: dict) -> str:
    report_json = json.dumps(report)
    report_html_template = Template(REPORT_TEMPLATE).safe_substitute(table_json=report_json)
    return report_html_template


def open_log_file(filename: str) -> Generator:
    if filename.endswith('.bz2'):
        file = gzip.open(filename=filename, mode='r')
    else:
        file = open(file=filename, mode='r')
    for line in file:
        yield line
    file.close()


def main() -> None:
    pass


if __name__ == '__main__':
    pass
