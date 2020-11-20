import pandas
from pathlib import Path
from os.path import realpath

base_path = Path(realpath(__file__)).parent
donations_made_csv_path = base_path / 'all_annual_data' / 'Donations Made.csv'


def get_donations_made():
    """

    :return:
    """
    data = pandas.read_csv(donations_made_csv_path)
    return data


if __name__ == '__main__':
    print(get_donations_made())
