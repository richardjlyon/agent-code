"""Agent UID generator.

Generates a unique Agent Code (UID) for an email passed on the command line and
writes it back to the CSV file.

Usage:
    app.py <email>
    app.py -h | --help
"""
import csv

from docopt import docopt

from agent_code.utils import uid_from_email

CSV_FILE_IN = "/Users/richardlyon/Downloads/export.csv"

def make_uid():
    arguments = docopt(__doc__, version='Uid 1.0')
    email = arguments.get("<email>")

    uid = uid_from_email(email, CSV_FILE_IN)

    with open(CSV_FILE_IN, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([email, '', '', uid])
        print(f'Wrote {email} / {uid} to {CSV_FILE_IN}')

if __name__ == "__main__":
    # email = "richlyon@gmail.com"
    # uid = uid_from_email(email, CSV_FILE_IN)
    make_uid()



