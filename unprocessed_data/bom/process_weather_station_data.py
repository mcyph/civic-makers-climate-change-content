import csv
import json
import numpy as np
import pandas as pd
from pathlib import Path
from os.path import realpath


# Data from http://www.bom.gov.au/climate/data/acorn-sat/#tabs=Data-and-networks
# under Creative Commons Attribution Australia Licence

base_path = Path(realpath(__file__)).parent
base_tmin_path = base_path / 'acorn_sat_v2_daily_tmin'
base_tmax_path = base_path / 'acorn_sat_v2_daily_tmax'

TYPE_MAXIMUM = 'maximum temperature (degC)'
TYPE_MINIMUM = 'minimum temperature (degC)'


def get_stations_dict():
    """

    :return:
    """
    stations = {}

    with open(base_tmax_path / 'acorn_sat_v2_stations.txt', 'r') as f:
        for item in csv.DictReader(f, delimiter='\t'):
            stations[int(item['stnnum'])] = {
                'lat': float(item['lat.']),
                'long': float(item['long.']),
                'name': item['name'].title(),
                'stnum': int(item['stnnum'])
            }

    return stations


def get_time_series(path, key):
    """

    :param path:
    :param key:
    :return:
    """

    # Read the ACORN weather data
    df = pd.read_csv(path,
                     index_col='date',
                     parse_dates=['date'],
                     skiprows=[1],
                     converters={key: lambda x: float(x) if x else np.nan})

    # We'll remove the site number+name, as we're
    # only interested in the date and degrees celcius
    df = df.drop('site number', 1)
    df = df.drop('site name', 1)

    # Get the average of a year
    df = df.groupby(pd.Grouper(freq='1Y')).mean()

    # Fill in blanks
    df = df.fillna(df.mean())

    # Make it so the values are in a column called "value"
    # rather than 'maximum/minimum temperature (degC)'
    df = df.rename(columns={key: 'value'})

    # Make the values a rolling average over
    # 10 years, to smooth the results
    df = df.rolling(window=10).mean()

    # Remove month and day from the index,
    # as we're only interested in the year
    df.index = pd.DatetimeIndex(df.index).year

    return df


if __name__ == '__main__':
    out = None
    stations = get_stations_dict()

    for path in base_tmax_path.glob('*.csv'):
        df = get_time_series(path, key=TYPE_MAXIMUM)
        df = df.rename(columns={'value': str(int(path.name.split('.')[1]))+'_max'})

        if out is not None:
            out = pd.merge(out, df, left_index=True, right_index=True, how='outer')
        else:
            out = df

    for path in base_tmin_path.glob('*.csv'):
        df = get_time_series(path, key=TYPE_MINIMUM)
        df = df.rename(columns={'value': str(int(path.name.split('.')[1]))+'_min'})
        out = pd.merge(out, df, left_index=True, right_index=True, how='outer')

    with open('weatherdata.csv', 'w', encoding='utf-8', newline='\n') as f:
        out.to_csv(f, float_format='%.1f', line_terminator='\n', encoding='utf-8')

    with open('weatherdata.json', 'w', encoding='utf-8') as f:
        if False:
            f.write(json.dumps(stations, separators=(',',':')))
        else:
            f.write(json.dumps(stations, indent=4))
