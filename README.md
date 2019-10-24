# pwned_to_portal #

Converts the output from checkpwnedemails.py to CSV for pentest portal or output of recon.sh to CSV for pentest portal

## Getting Started ##

'pwned_to_portal' uses python3

### pwned_to_portal Usage and Examples ###

```bash
python pwned_to_portal.py -e -f example_pwned_breaches.csv
python pwned_to_portal.py -e -f example_pwned_breaches.csv -o output.csv
python pwned_to_portal.py -r -f example.com-DomainSubnets.csv
python pwned_to_portal.py -r -f example.com-DomainSubnets.csv -o output.csv
python pwned_to_portal.py -r -d .
python pwned_to_portal.py -r -d example_dir -o example_outfile.csv
```

#### pwned_to_portal Options ####

```bash
Converts the output from checkpwnedemails.py to CSV for pentest portal or output of recon.sh to CSV for pentest portal
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

```

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.
