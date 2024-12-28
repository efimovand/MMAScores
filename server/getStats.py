import requests
from bs4 import BeautifulSoup


def getStats(fullName: str):

    page = requests.get(f'https://ufc.com/athlete/{"-".join(fullName.lower().split())}')
    soup = BeautifulSoup(page.text, 'lxml')

    stats_list = {
        item.find('div', class_='c-bio__label').text.strip(): item.find('div', class_='c-bio__text').text.strip()
        for item in soup.findAll('div', class_='c-bio__field')[1:] if item.find('div', class_='c-bio__label') and item.find('div', class_='c-bio__text')
    }

    return stats_list


if __name__ == '__main__':

    fightersList = ['Alexander Volkov', 'Islam Makhachev', 'Tom Aspinall', 'Shavkat Rakhmonov']

    for fighter in fightersList:
        print(getStats(fighter))
