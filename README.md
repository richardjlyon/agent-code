# Agent UID

A python command line utility to create a unique Agent ID from an
email address. The utility expects a CSV file in `"/Users/richardlyon/Downloads/export.csv"
` in email/first/last/agent code format.

Utilty will create an Agent code in the form AG-XYZ from the random letters of the domain name, guaranteeing it to 
be unique, and write it back to the CSV file.

Utility will also report if an email from that domain has already been registered.

## Usage:
```commandline
> make_uid someone@somewhere.co.uk
Wrote someone@somewhere.co.uk / AG-SWE to /Users/richardlyon/Downloads/export.csv

```