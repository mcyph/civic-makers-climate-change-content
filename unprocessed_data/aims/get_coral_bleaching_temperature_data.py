from pathlib import Path
from os.path import realpath
from unprocessed_data.aims.get_headered_csv_dataframe import get_headered_csv_dataframe

base_path = Path(realpath(__file__)).parent / 'data_csv_avgtemp'


def get_coral_bleaching_temperature_data():
    dfs = {}
    metadatas = {}

    for csv_path in base_path.glob('*.csv'):
        metadata, df = get_headered_csv_dataframe(csv_path)
        dfs[metadata['STATION']] = (metadata, df)
        metadatas[metadata['STATION']] = metadata

    return metadatas, dfs


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_coral_bleaching_temperature_data())
