from pybtex.database import parse_file
import pprint
import os

dir = '/Users/uum209/GitHub/search-design-journals/'
bibtex = 'bibtex/savedrecs.bib'

dd = parse_file(dir+bibtex)

for entry in dd.entries:
    title = dd.entries[entry].fields.values
    print(title)
    # title = dd.entries[entry].fields["Title"]
    # print(title)
    # authors = dd.entries[entry].persons
    # venue = dd.entries[entry].fields["Journal"]
    # abstract = dd.entries[entry].fields["Abstract"]
    # print("\t"+abstract)
    # doi = dd.entries[entry].fields["DOI"]
    # year = dd.entries[entry].fields["Year"]



# for i in bibtex:
#     with file as open()