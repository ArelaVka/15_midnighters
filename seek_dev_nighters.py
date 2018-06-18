import requests
import datetime as dt
import pytz


def load_attempts():
    url = 'https://devman.org/api/challenges/solution_attempts/'
    page = 0
    while True:
        page += 1
        page_param = {'page': page}
        one_page_records = requests.get(url, params=page_param).json()
        count_of_pages = one_page_records['number_of_pages']
        for record in one_page_records['records']:
            yield record
        if page == count_of_pages:
            break


def is_midnighter(record):
    if record['timestamp']:
        attempt_time = dt.datetime.fromtimestamp(
            record['timestamp'],
            pytz.timezone(record['timezone'])).time()
        return 0 < attempt_time.hour < 9


def print_owls(set_of_owls):
    print('List of owls:\n')
    for owl in set_of_owls:
        print('Username -', owl)


if __name__ == '__main__':
    owls = set()
    for record in load_attempts():
        if is_midnighter(record):
            owls.add(record['username'])
    print_owls(owls)
