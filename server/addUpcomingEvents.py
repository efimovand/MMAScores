from models import ScoreCard, Event, Match
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
from getStats import getStats


# Convert date from String to UTC Timestamp
def standardizeDate(date: str):

    # Format date to the UTC Timestamp
    local_time = datetime.strptime(date, "%A, %B %d, %I:%M %p ET")

    # Set year
    current_year = datetime.now().year
    local_time = local_time.replace(year=current_year + 1) if local_time.replace(year=current_year) < datetime.now() else local_time.replace(year=current_year)

    # Convert to UTC Timestamp
    local_time = pytz.timezone("US/Eastern").localize(local_time)  # Set original timezone (ET)
    utc_time = local_time.astimezone(pytz.utc)  # Convert to UTC
    utc_timestamp = int(utc_time.timestamp())  # Convert to Timestamp

    return utc_timestamp


def addUpcomingEvents():

    upcoming_events = []

    # Get X upcoming events
    response = requests.get('https://www.tapology.com/fightcenter?group=ufc&schedule=upcoming')  # Only UFC events (group=ufc)
    events = BeautifulSoup(response.text, 'lxml').findAll('div', class_='promotion flex flex-wrap items-center leading-6 whitespace-nowrap overflow-hidden')[:3]

    # Extract { title, date, matches (names, pics, stats) } for every event
    for event in events:

        # Get { title, date }
        label = event.find('a', class_='border-b border-tap_3 border-dotted hover:border-solid')
        title, link = label.text, label.get('href')
        date = event.find('span', class_='hidden md:inline').text.replace('  ', ' ')
        date_utc_timestamp = standardizeDate(date)
        print(f'Title: {title}\nDate: {date_utc_timestamp} ({date})\nLink: https://www.tapology.com{link}\n')

        # Get { matches }
        event_response = requests.get(f'https://www.tapology.com{link}', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'})
        event_matches_lxml = BeautifulSoup(event_response.text, 'lxml').find('div', class_='eventQuickCardSidebar').findAll('span', class_='left')
        matches = []

        # Extract { match.names, match.stats } for every match
        for match in event_matches_lxml:

            names, stats = [], {}
            names_lxml = match.find_all('a', href=True)

            # Extract { match.names }
            for name_lxml in names_lxml:
                name = name_lxml.text.strip()
                if name[1] == '.':  # If name is short ('A. Volkov')
                    name = f"{name_lxml['href'].split('-')[1].capitalize()} {name[3:]}"
                names.append(name)

            # Extract { match.stats }
            stats_1, stats_2 = getStats(names[0]), getStats(names[1])
            if stats_1['ok'] and stats_2['ok']:
                for param in ['Age', 'Height', 'Weight', 'Reach', 'Country']:
                    if param in stats_1 and param in stats_2:
                        stats[param] = [stats_1[param], stats_2[param]]

            print(names, ':', stats)

            # Add MATCH to the event's matches' list
            matches.append(
                {
                    'names': names,
                    'stats': stats
                }
            )

        # Add EVENT to the upcoming events' list
        upcoming_events.append(
            {
                'title': title,
                'date': date_utc_timestamp,
                'matches': matches,
            }
        )

        print()

    # print('\nUpcoming events:\n')
    # for ue in upcoming_events:
    #     for param, value in ue.items():
    #         print(param, ':', value)
    #     print()


if __name__ == '__main__':
    addUpcomingEvents()
