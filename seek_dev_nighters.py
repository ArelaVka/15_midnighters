import requests
import datetime
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
        return datetime.datetime.fromtimestamp(
            record['timestamp'],
            pytz.timezone(record['timezone'])).time()
        # upload_time = datetime.date.fromtimestamp(record['timestamp'])


if __name__ == '__main__':
    info = load_attempts()
    out = set()
    for info in load_attempts():
        print(get_midnighters(info))
        # out.add(info['username'])
        # print(out)
