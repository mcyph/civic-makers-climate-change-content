from heapq import nsmallest
from editdistance import distance
from unprocessed_data.aec.get_donations_made import get_donations_made
from unprocessed_data.asx.get_asx_companies import get_asx_companies


donations_made = get_donations_made()
asx_companies = get_asx_companies()


def process_company(company):
    # nl, co, ag
    company = company.lower().replace(' co.', '')
    company = company.replace(',', '') \
                     .replace('.', '')
    company = company.replace('pty', '') \
                     .replace('ltd', '') \
                     .replace('limited', '') \
                     .replace('corporation', '') \
                     .replace('corp', '')
    while '  ' in company:
        company = company.replace('  ', ' ')
    return company


if __name__ == '__main__':
    out = []
    for donor in donations_made['Donor Name'].unique():
        closest_asx_company = [
            (distance(process_company(donor), process_company(company)), donor, company)
            for company in asx_companies
        ]

        closest_asx_company = sorted(closest_asx_company)[0]
        if closest_asx_company[0] > 3:
            closest_asx_company = (None, donor, None)
        else:
            closest_asx_company = closest_asx_company

        closest_asx_company += (
            donations_made.loc[donations_made['Donor Name'] == donor,
            ['Donor Name', 'Value']].sum()['Value'],
        )
        out.append(closest_asx_company)

    out.sort(key=lambda x: (-x[-1], x[1]))
    #from pprint import pprint
    #pprint(out)

    for closest_asx_company in out:
        print('\t'.join(str(i) for i in closest_asx_company))
