import csv
import json
import dotenv
import requests
from os import environ
from os.path import realpath
from pathlib import Path

base_path = Path(realpath(__file__)).parent / 'data_json_api'


def json_to_csv(in_path, out_path):
    with open(in_path, 'r') as f:
        data = json.loads(f.read())

    with open(out_path, 'w', newline='\n') as f:
        dw = csv.DictWriter(f, fieldnames=['depth', 'time', 'value'])
        dw.writeheader()

        for i_data in data:
            for result in i_data['results']:
                if not result['value'] or result['value'] < 0 or result['value'] > 50:
                    continue

                dw.writerow({
                    'depth': result['depth'],
                    'time': result['time'],
                    'value': result['value']
                })


if __name__ == '__main__':
    for json_path in (base_path / 'tempdata').glob('*.json'):
        json_to_csv(json_path, base_path / 'tempdata_csv' / (json_path.name.replace('.json', '')+'.csv'))
