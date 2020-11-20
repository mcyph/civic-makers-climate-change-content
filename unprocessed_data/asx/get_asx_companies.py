import pandas
from pathlib import Path
from os.path import realpath

base_path = Path(realpath(__file__)).parent
asx_companies_csv_path = next(base_path.glob('ASX_Listed_Companies*.csv'))


def get_asx_companies():
    """

    :return:
    """
    data = pandas.read_csv(asx_companies_csv_path)
    data.set_index('ASX code', verify_integrity=True)
    print(data)

    out = {}
    for idx, row in data.iterrows():
        out[row['Company name']] = row['GICs industry group']
    return out


if __name__ == '__main__':
    print(get_asx_companies())
