import pandas


def get_headered_csv_dataframe(path):
    with open(path, 'r') as f:
        metadata = {}

        for line in f:
            line = line.strip()

            if not line:
                continue
            elif line in ('Long term averages', 'BLEACH THRESHOLDS'):
                break
            elif line.startswith('STATION,'):
                value = line.partition(',')[-1]
                try:
                    # HACK: It seems the longitude is listed
                    # under STATION for the thresholds data!
                    float(value)
                    metadata['LONGITUDE'] = value
                except ValueError:
                    metadata['STATION'] = value
            elif line.startswith('LATITUDE,'):
                metadata['LATITUDE'] = line.partition(',')[-1]
            elif line.isupper():
                key = line
            elif line:
                if key in metadata:
                    metadata[key] += '\n'+line
                else:
                    metadata[key] = line

        return metadata, pandas.read_csv(f)


if __name__ == '__main__':
    print(get_headered_csv_dataframe('data_csv_days/1_days.csv'))
    print()
    print(get_headered_csv_dataframe('data_csv_avgtemp/1_avgtemp.csv'))
