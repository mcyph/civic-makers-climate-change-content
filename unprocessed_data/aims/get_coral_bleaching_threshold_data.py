import pandas as pd
from pathlib import Path
from os.path import realpath
from collections import Counter
from unprocessed_data.aims.get_headered_csv_dataframe import get_headered_csv_dataframe

base_path = Path(realpath(__file__)).parent / 'data_csv_days'


def get_coral_bleaching_threshold_data():
    dfs = {}
    metadatas = {}
    breached_thresholds = {}
    breached_thresholds_all = {}
    breached_thresholds_all_days = Counter()

    for csv_path in base_path.glob('*.csv'):
        metadata, df = get_headered_csv_dataframe(csv_path)
        df['SUMMER-START-YEAR'] = pd.DatetimeIndex(df['SUMMER-BEGINNING']).year
        df = df.drop(columns=['SUMMER-BEGINNING'])
        df = df.set_index(['SUMMER-START-YEAR', 'TEMPERATURE'])
        df['DAYS-OVER-THRESHOLD'] = df['ACTUAL-DAYS'] - df['THRESHOLD-DAYS']
        df[df['DAYS-OVER-THRESHOLD'] < 0] = 0
        dfs[metadata['STATION']] = df
        metadatas[metadata['STATION']] = metadata

        # Get how many times this reef breached thresholds by year
        i_breached_thresholds = {}
        i_breached_thresholds_days = Counter()
        for (year, temperature), item in df.iterrows():
            i_breached_thresholds.setdefault(year, False)
            i_breached_thresholds_days[year] += 0

            if item['DAYS-OVER-THRESHOLD'] and not i_breached_thresholds_days[year]:
                i_breached_thresholds[year] = True
                i_breached_thresholds_days[year] += item['DAYS-OVER-THRESHOLD']

        breached_thresholds_all_days += i_breached_thresholds_days
        for i in i_breached_thresholds_days:
            breached_thresholds_all_days[i] += 0

        # Get how many of all reefs breached thresholds by year
        for year in i_breached_thresholds:
            breached_thresholds_all.setdefault(year, 0)
            if i_breached_thresholds[year]:
                breached_thresholds_all[year] += 1

        breached_thresholds[metadata['STATION']] = tuple(i_breached_thresholds.items())

    return (
        metadatas,
        dfs,
        breached_thresholds,
        tuple(breached_thresholds_all.items()),
        tuple(sorted(breached_thresholds_all_days.items()))
    )


if __name__ == '__main__':
    from pprint import pprint

    metadatas, dfs, breached_thresholds, breached_thresholds_all, breached_thresholds_all_days = \
        get_coral_bleaching_threshold_data()

    for year, val in breached_thresholds_all:
        print(f'{year}\t{val}')

    print()

    for year, val in breached_thresholds_all_days:
        print(f'{year}\t{val}')

    import json
    print(json.dumps(breached_thresholds_all))
