import json
import dotenv
import requests
from os import environ
from os.path import realpath
from pathlib import Path

base_path = Path(realpath(__file__)).parent / 'data_json_api'
dotenv.load_dotenv(override=True)
API_KEY = environ['AIMS_DATAPLATFORM_API_KEY']


ENDPOINT_WIND = 'https://api.aims.gov.au/data/v1.0/10.25845/5c09bf93f315d/data'


def __download_all_data(use_endpoint, sites_path, output_dir):
    with open(sites_path, 'r') as f:
        site_names = json.loads(f.read())['results']

    for site_name in site_names:
        output_path = output_dir / f'{site_name}.json'
        if output_path.exists():
            print("Continuing:", output_path)
            continue

        data = None
        datas = []
        first_req = True

        while first_req or data.get('links', {}).get('next'):
            if first_req:
                first_req = False
                print(site_name)
                endpoint = use_endpoint  # "https://api.aims.gov.au/data/v1.0/10.25845/5b4eb0f9bb848/data"
                get_data = {'site-name': site_name}
                headers = {'x-api-key': API_KEY}
            else:
                endpoint = data['links']['next']
                print(endpoint)
                get_data = None
                headers = {'x-api-key': API_KEY}

            datas.append(requests.get(endpoint, get_data, headers=headers).json())
            data = datas[-1]

        with open(output_path, 'w') as f:
            f.write(json.dumps(datas, indent=4))


def download_weather_data():
    sites_path = base_path / 'weather_sites.json'
    output_dir = base_path / 'weatherdata'
    endpoint_weather = "https://api.aims.gov.au/data/v1.0/10.25845/5b4eb0f9bb848/data"
    __download_all_data(endpoint_weather, sites_path, output_dir)


def download_temperature_data():
    sites_path = base_path / 'temp_sites.json'
    output_dir = base_path / 'tempdata'
    endpoint_weather = "https://api.aims.gov.au/data/v1.0/10.25845/5b4eb0f9bb848/data"
    __download_all_data(endpoint_weather, sites_path, output_dir)


if __name__ == '__main__':
    #download_weather_data()
    download_temperature_data()
