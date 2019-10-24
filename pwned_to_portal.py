#!/usr/bin/env python3
"""Converts the output from checkpwnedemails.py to CSV for pentest portal
or output of recon.sh to CSV for pentest portal
Usage:
  pwned_to_portal.py (-e -f FILE | -e -f FILE -o OUTPUT)
  pwned_to_portal.py (-r -f FILE | -r -f FILE -o OUTPUT | -r -d DIRECTORY | -r -d DIRECTORY -o OUTPUT)

Options:
  -h --help                             Show this help message and exit
  -e --email                            Parse for DNS Email records
  -r --recon                            Parse Recon DNS records
  -f FILE --file=FILE                   Name of FILE to parse
  -o OUTPUT --output=OUTPUT             Name of CSV output file
  -d DIRECTORY --directory=DIRECTORY    Will Parse a directory for all DNS files with -DomainSubnets.csv
"""
# Author: Kyle Evers
import csv
import re
import os
from enum import IntEnum
from docopt import docopt

# These classes of enums is to easily change the script if the data format changes
class EmailColumns(IntEnum):
    EMAIL_ADDRESS = 0
    IS_PWNED = 1
    DATA_CLASSES = 6                      # this is where the breach data came from

    def __int__(self):
        return self.value

class ReconColumns(IntEnum):
    IP_ADDRESS = 0
    DOMAIN_NAME = 1
    REGISTRANT = 3
    REGISTRANT_CONT = 4     # Because of lack of formatting consistancy the registrant can be on the 3rd or 4th column

    def __int__(self):
        return self.value

def parse_email(args):
    print(args)
    regex = re.compile('....-..-..')        # Search for date in row, periods are wildcards
    if(args['--output']):
        f = open(args['--output'], 'w')
        f.write('Email Address,Breach Information\n')
    else:
        print('Email Address,Breach Information')

    with open(args['--file']) as csv_file:
        for row in csv_file:
            # Split each row into columns based on tabs
            columns = row.split('\t')
            # If the email has been pwned process it
            if(columns[EmailColumns.IS_PWNED] == 'True'):
                # Find all occurences of dates, the first date is the breach date
                matches = re.findall(regex, row)
                if(args['--output']):
                    f.write(columns[EmailColumns.EMAIL_ADDRESS] + ',' +
                    columns[EmailColumns.DATA_CLASSES] + ' - ' + matches[0] +"\n")
                else:
                    print(columns[EmailColumns.EMAIL_ADDRESS] + ',' +
                    columns[EmailColumns.DATA_CLASSES] + ' - ' + matches[0])

def parse_recon_dns(args):
    if(args['--directory']):
        for file in os.listdir(args['--directory']):
            if file.endswith('-DomainSubnets.csv'):
                parse_recon_csv(args, file)
    else:
        parse_recon_csv(args, args['--file'])

def parse_recon_csv(args, filename):
     # Regex to check for an IP address
    regex = re.compile('''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)''')
    if(args['--output']):
        f = open(args['--output'], 'w')
        f.write('Network,Domain,Registrant\n')
    else:
        print('Network,Domain,Registrant')

    with open(filename) as csv_file:
        for row in csv_file:
            # Split each row into columns based on comma
            columns = row.split(',')
            matches = re.findall(regex, columns[ReconColumns.IP_ADDRESS])
            # If there is an IP address in the first column
            if(len(matches)):
                if(args['--output']):
                    f.write(columns[ReconColumns.IP_ADDRESS] + ',' +
                    columns[ReconColumns.DOMAIN_NAME] + ',' +
                    columns[ReconColumns.REGISTRANT] +
                    columns[ReconColumns.REGISTRANT_CONT].rstrip() + '\n')
                else:
                    print(columns[ReconColumns.IP_ADDRESS] + ',' +
                    columns[ReconColumns.DOMAIN_NAME] + ',' +
                    columns[ReconColumns.REGISTRANT] +
                    columns[ReconColumns.REGISTRANT_CONT].rstrip())


def main():
    arguements = docopt(__doc__, version='1.0.0rc2')
    if arguements['--email']:
        parse_email(arguements)
    if arguements['--recon']:
        parse_recon_dns(arguements)

if __name__ == '__main__':
    main()
