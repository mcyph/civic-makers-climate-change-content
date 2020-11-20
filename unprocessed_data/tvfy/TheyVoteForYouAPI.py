import os
import dotenv
from requests import get

# a basic python class to allow using the api from
# https://theyvoteforyou.org.au/help/data

# Note: to use this script, create a ".env" file with the contents
# THEYVOTEFORYOU_APIKEY=(API Key)
# using the api key of your account from https://theyvoteforyou.org.au
dotenv.load_dotenv(override=True)

API_PREFIX = 'https://theyvoteforyou.org.au/api/v1'
GET_PARAMS = {
    'key': os.environ['THEYVOTEFORYOU_APIKEY']
}


class TheyVoteForYouAPI:
    def people(self):
        """

        :return:
        """
        return get(f'{API_PREFIX}/people.json', GET_PARAMS).json()

    def person(self, person_id: int):
        """

        :param person_id:
        :return:
        """
        return get(f'{API_PREFIX}/people/{person_id}.json', GET_PARAMS).json()

    def policies(self):
        """

        :return:
        """
        return get(f'{API_PREFIX}/policies.json', GET_PARAMS).json()

    def policy(self, policy_id: int):
        """

        :param policy_id:
        :return:
        """
        return get(f'{API_PREFIX}/policies/{policy_id}.json', GET_PARAMS).json()

    def divisions(self):
        """

        :return:
        """
        return get(f'{API_PREFIX}/divisions.json', GET_PARAMS).json()

    def division(self, division_id: int):
        """

        :param division_id:
        :return:
        """
        return get(f'{API_PREFIX}/divisions/{division_id}.json', GET_PARAMS).json()


if __name__ == '__main__':
    from pprint import pprint
    api = TheyVoteForYouAPI()

    pprint(api.policies())
    pprint(api.policy(228))

    pprint(api.people())
    pprint(api.divisions())
