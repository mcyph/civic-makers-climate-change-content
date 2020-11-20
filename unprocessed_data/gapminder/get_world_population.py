import pycountry
import pandas
from pathlib import Path
from os.path import realpath

base_path = Path(realpath(__file__)).parent


ISO_OVERRIDES = {
    'cape verde': 'CV',
    'congo, dem. rep.': 'CD',
    'congo, rep.': 'CG',
    'micronesia, fed. sts.': 'FM',
    'north korea': 'KP',
    'south korea': 'KR',
    'st. kitts and nevis': 'KN',
    'st. lucia': 'LC',
    'st. vincent and the grenadines': 'VC',
}


def get_world_population():
    df = pandas.read_csv(base_path / 'data_csv' / 'population_total.csv')
    country_codes = [
        ISO_OVERRIDES.get(i.lower()) or
            pycountry.countries.search_fuzzy(i)[0].alpha_2
        for i in df['country']
    ]
    for col in df:
        if col.isdigit():
            df[col] = df[col].astype(int)
    df.index = country_codes
    return df


if __name__ == '__main__':
    print(get_world_population().loc['AU']['2010'])
