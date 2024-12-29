import requests
from bs4 import BeautifulSoup


def getStats(fullName: str):

    response = requests.get(f'https://ufc.com/athlete/{"-".join(fullName.lower().split())}', cookies={'STYXKEY_region': 'RUSSIA.RU.en.Default'})
    page = BeautifulSoup(response.text, 'lxml')

    stats_list = {
        item.find('div', class_='c-bio__label').text.strip(): item.find('div', class_='c-bio__text').text.strip()
        for item in page.findAll('div', class_='c-bio__field')[1:] if item.find('div', class_='c-bio__label') and item.find('div', class_='c-bio__text')
    }

    return stats_list


if __name__ == '__main__':

    import time

    test_list = ['Ciryl Gane', 'Alexander Volkov', 'Alexandre Pantoja', 'Julianna Pena', 'Merab Dvalishvili', 'Ilia Topuria', 'Alex Pereira', 'Jon Jones', 'Valentina Shevchenko']

    for fighter in test_list:
        print(getStats(fighter))
        time.sleep(0.25)
