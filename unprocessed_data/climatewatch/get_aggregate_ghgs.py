import pandas
import pycountry
from pathlib import Path
from os.path import realpath

base_path = Path(realpath(__file__)).parent


def get_aggregate_ghgs():
    df = pandas.read_csv(
        base_path / 'data_csv' / 'CW_UNFCCC_GHG_Emissions.csv',
        delimiter='\t',
        thousands=","
    )
    df = df[df.country != 'ANNEXI']
    df = df[df.country != 'EU28']
    df = df[df.gas == 'Aggregate GHGs']
    df = df.drop(['gas'], axis='columns')

    country_codes = [pycountry.countries.get(alpha_3=i).alpha_2 for i in df['country']]
    df.index = country_codes

    df = df.drop(['country'], axis='columns')

    for col in df:
        if col.isdigit():
            print(col, df[col])
            df[col] = df[col].astype(float)
            print('CONVERTED:', df[col])

    return df


def get_lulucf():
    df = get_aggregate_ghgs()
    #df = df[df.sector == 'Total GHG emissions excluding LULUCF/LUCF'].append(
    #    df[df.sector == 'Total GHG emissions without LULUCF']
    #)
    df = df[df.sector == 'Total GHG emissions including LULUCF/LUCF'].append(
        df[df.sector == 'Total GHG emissions with LULUCF']
    )
    df = df.drop(['sector'], axis='columns')
    return df


if __name__ == '__main__':
    #print(get_aggregate_ghgs())
    #print()
    #print(get_lulucf())

    #print(get_aggregate_ghgs().loc['AU'])
    print(get_lulucf().loc['AU'])
