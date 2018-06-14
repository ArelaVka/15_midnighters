import requests
import pytz


def load_attempts():
    url = 'https://devman.org/api/challenges/solution_attempts/?page=1'
    for page in range(2):
        response_data = requests.get(url).json()
        for data in response_data['records']:
            yield data


def get_midnighters():
    pass


if __name__ == '__main__':
    info = load_attempts()
    print(info)
