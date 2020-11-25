import math
import numpy as np
import pandas as pd
from pathlib import Path
from os.path import realpath
from datetime import datetime
from unprocessed_data.aims.get_headered_csv_dataframe import get_headered_csv_dataframe

base_path = Path(realpath(__file__)).parent / 'data_csv_avgtemp'


def get_coral_bleaching_temperature_data():
    dfs = []
    metadatas = {}

    for csv_path in base_path.glob('*.csv'):
        metadata, df = get_headered_csv_dataframe(csv_path)

        out = {
            'date': [],
            'degc': []
        }
        for _, row in df.iterrows():
            row = row.to_dict()

            for key in row:
                if key.startswith('wtemp_LEVEL0_summer_') and not math.isnan(row[key]):
                    year = int(key.split('_')[-1])
                    #print(key, row['DATE'], year, row[key])

                    if row['DATE'].split('-')[-1] not in ('JAN', 'FEB', 'MAR', 'APR', 'MAY'):
                        # If not start months of year, then in summer of previous year
                        year -= 1
                    if year == -1:
                        year = 99

                    date = '%s-%02d' % (row['DATE'], year)
                    if date in ('29-FEB-03', '29-FEB-07', '29-FEB-11', '29-FEB-15', '29-FEB-19'):
                        continue # ???

                    #print(date)
                    date = datetime.strptime(date, '%d-%b-%y')
                    degc = row[key]
                    out['date'].append(date)
                    out['degc'].append(degc)

        df = pd.DataFrame({
            'degc': out['degc'],
            'station': [metadata['STATION']]*len(out['degc'])
        }, index=out['date'])
        df.sort_index(inplace=True)

        dfs.append(df)
        metadatas[metadata['STATION']] = metadata

    return metadatas, pd.concat(dfs)


if __name__ == '__main__':
    import json
    from pprint import pprint
    metadatas, df = get_coral_bleaching_temperature_data()

    df.to_csv('out.csv')
    with open('metadata.json', 'w') as f:
        f.write(json.dumps(metadatas))
