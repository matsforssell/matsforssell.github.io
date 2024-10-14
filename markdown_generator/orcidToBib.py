orcid = '0000-0001-7811-6773' # Fill your orcid here

import requests

response = requests.get('https://pub.orcid.org/v3.0/{}/works'.format(orcid), headers={"Accept": "application/orcid+json" })
record = response.json()

put_codes = []
for work in record['group']:
    put_code = work['work-summary'][0]['put-code']
    put_codes.append(put_code)
put_code = put_codes[0]

citations = []
for put_code in put_codes:
    response = requests.get('https://pub.orcid.org/v3.0/{}/work/{}'.format(orcid, put_code),headers={"Accept": "application/orcid+json" })
    work = response.json()
    if work['citation'] is not None:
        citations.append(work['citation']['citation-value'])

with open('output.bib', 'w') as bibfile:
    for citation in citations:
        bibfile.write(citation)
        bibfile.write('\n')

