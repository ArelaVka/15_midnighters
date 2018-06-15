import requests
import datetime as dt
import pytz


def load_attempts():
    main_url = 'https://devman.org/api/challenges/solution_attempts/'
    response_data = requests.get(main_url).json()
    count_of_pages = response_data['number_of_pages']
    for page in range(1, count_of_pages + 1):
        url = main_url + '?page=' + str(page)
        page_records_data = requests.get(url).json()
        for record in page_records_data['records']:
            yield record


def get_midnighters(record):
    if record['timestamp']:
        upload_time = dt.datetime.fromtimestamp(
            record['timestamp'],
            pytz.timezone(record['timezone'])).time()
        if dt.time(0, 0) < upload_time < dt.time(12, 0):
            return True


if __name__ == '__main__':
    info = load_attempts()
    owls = set()
    for info in load_attempts():
        if get_midnighters(info):
            owls.add(info['username'])
    print(owls)
