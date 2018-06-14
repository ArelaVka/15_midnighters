import requests
import pytz


def load_attempts():
    main_url = 'https://devman.org/api/challenges/solution_attempts/'
    response_data = requests.get(main_url).json()
    count_of_pages = response_data['number_of_pages']
    for page in range(count_of_pages + 1):
        url = main_url + '?page=' + str(page)
        print(response_data['records'])
    #     response_data = requests.get(url).json()
    #     for data in response_data['records']:
    #         yield data


def get_midnighters():
    pass


if __name__ == '__main__':
    info = load_attempts()
