import requests
from bs4 import BeautifulSoup


def getStats(fullName: str):

    # Stats page
    response = requests.get(f'https://ufc.com/athlete/{"-".join(fullName.lower().split())}', cookies={'STYXKEY_region': 'RUSSIA.RU.en.Default'})
    page = BeautifulSoup(response.text, 'lxml')

    stats_list = {
        item.find('div', class_='c-bio__label').text.strip(): item.find('div', class_='c-bio__text').text.strip()
        for item in page.findAll('div', class_='c-bio__field') if
        item.find('div', class_='c-bio__label') and item.find('div', class_='c-bio__text')
    }

    # Formatting
    if stats_list:  # Correct Name Input

        if 'Place of Birth' in stats_list:
            stats_list['Country'] = stats_list['Place of Birth'].split(' ')[-1]
            stats_list['Country'] = stats_list['Country'].replace('States', 'USA')

        for param in ['Status', 'Place of Birth', 'Trains at', 'Fighting style', 'Octagon Debut', 'Leg reach']:
            stats_list.pop(param, None)

        stats_list['ok'] = True

    else:  # Incorrect Name Input
        stats_list['ok'] = False

    return stats_list


if __name__ == '__main__':

    import time

    test_list = ['Ciryl Gane', 'Alexander Volkov', 'Alexandre Pantoja', 'Julianna Pena', 'Merab Dvalishvili',
                 'Ilia Topuria', 'Alex Pereira', 'Jon Jones', 'Valentina Shevchenko', 'Thiago Moisés']

    # for fighter in test_list:
    #     print(getStats(fighter))
    #     time.sleep(0.25)

    print(getStats('Alexander Volkov'))
