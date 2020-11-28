import json
import pandas as pd
from pathlib import Path
from os.path import realpath
from unprocessed_data.tvfy.TheyVoteForYouAPI import TheyVoteForYouAPI

base_path = Path(realpath(__file__)).parent


def get_climate_change_policies():
    """
    Get the climate change policies as a pandas DataFrame object
    :return:
    """
    return pd.read_csv(base_path / 'data_csv' / 'tvfy_policies.csv',
                       delimiter='\t')


def write_policy(api, policy_id):
    """
    Download a given policy by ID, in turn getting
    any divisions associated with this policy

    :param api:
    :param policy_id:
    :return:
    """
    policy_dict = api.policy(policy_id)

    with open(base_path / 'data_json' / 'policies' / f'{policy_id}.json',
              'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(policy_dict, ensure_ascii=False, indent=4))

    for policy_division in policy_dict['policy_divisions']:
        write_division(api, policy_division['division']['id'])


def write_division(api, division_id):
    """
    Download a given division by ID

    :param api:
    :param division_id:
    :return:
    """
    division_dict = api.division(division_id)

    with open(base_path / 'data_json' / 'divisions' / f'{division_id}.json',
              'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(division_dict, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    policy_ids = set(get_climate_change_policies().id)
    api = TheyVoteForYouAPI()

    for policy_id in policy_ids:
        try:
            write_policy(api, policy_id)
        except json.decoder.JSONDecodeError:
            pass
