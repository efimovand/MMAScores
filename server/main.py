import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


# Classes of data
class Match(BaseModel):
    names: List[str]
    pics: List[str]
    judges: List[dict]
    media: List[dict]
    stats: List[dict]

class Event(BaseModel):
    title: str
    date: str
    matches: List[Match]

class Events(BaseModel):
    events: List[Event]


# FastAPI settings
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Data from the DB
memory_db = {
    "events" : [

        # UFC on ESPN 65
        {
            'title': 'UFC on ESPN 65 - Covington vs. Buckley',
            'date': '14-12-2024',

            'matches': [
                {
                    'names': ["Marcos", "Yanez"],
                    'pics': ['marcos_img', 'yanez_img'],
                    'judges': [
                        { 'name': "Derek Cleary", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Eric Colon", 'score': ["10 - 9", "9 - 10", "10 - 9"] },
                        { 'name': "Chris Lee", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                    ],
                    'media': [
                        { 'name': "Tyler Treese", 'score': ["29 - 28"] },
                        { 'name': "Tristen Critchfield", 'score': ["10 - 9", "9 - 10", "10 - 9"] },
                        { 'name': "Patrick McCorry", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                    ],
                    'stats': [
                        { 'param': 'age', 'values': [31, 31] },
                        { 'param': 'height', 'values': [5.7, 5.7] },
                        { 'param': 'weight', 'values': [136, 136] },
                        { 'param': 'reach', 'values': [70, 69] },
                        { 'param': 'state', 'values': ["USA", "Peru"] },
                    ]
                },

                {
                    'names': ["Stirling", "Tokkos"],
                    'pics': ['stirling_img', 'tokkos_img'],
                    'judges': [
                        { 'name': "Derek Cleary", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Eric Colon", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Jason Grenier", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    ],
                    'media': [
                        { 'name': "Zane Simon", 'score': ["30 - 26"] },
                        { 'name': "Tyler Treese", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Tristen Critchfield", 'score': ["30 - 27"] },
                    ],
                    'stats': [
                        { 'param': 'height', 'values': [6.4, 6.3] },
                        { 'param': 'weight', 'values': [206, 206] },
                        { 'param': 'reach', 'values': [79, 76] },
                    ]
                },

                {
                    'names': ["Lima", "Johns"],
                    'pics': ['lima_img', 'johns_img'],
                    'judges': [
                        { 'name': "Sal D'Amato", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Chris Lee", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Troy Wincapaw", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    ],
                    'media': [
                        { 'name': "Tyler Treese", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Patrick McCorry", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Matthew Wells", 'score': ["29 - 28"] },
                    ],
                    'stats': [
                        { 'param': 'age', 'values': [30, 26] },
                        { 'param': 'height', 'values': [5.7, 5.6] },
                        { 'param': 'weight', 'values': [146, 146] },
                        { 'param': 'reach', 'values': [66, 68] },
                        { 'param': 'state', 'values': ["USA", "Sweden"] },
                    ]
                },

                {
                    'names': ["Maverick", "Horth"],
                    'pics': ['maverick_img', 'horth_img'],
                    'judges': [
                        { 'name': "Derek Cleary", 'score': ["10 - 9", "9 - 10", "10 - 9"] },
                        { 'name': "Sal D'Amato", 'score': ["10 - 9", "9 - 10", "10 - 9"] },
                        { 'name': "Solimar Miranda", 'score': ["10 - 9", "9 - 10", "10 - 9"] },
                    ],
                    'media': [
                        { 'name': "Tyler Treese", 'score': ["10 - 9", "9 - 10", "10 - 9"] },
                        { 'name': "Tristen Critchfield", 'score': ["10 - 9", "9 - 10", "10 - 9"] },
                        { 'name': "Steve Duncan", 'score': ["29 - 28"] },
                    ],
                    'stats': [
                        { 'param': 'age', 'values': [27, 34] },
                        { 'param': 'height', 'values': [5.4, 5.7] },
                        { 'param': 'weight', 'values': [126, 126] },
                        { 'param': 'reach', 'values': [65, 66] },
                        { 'param': 'state', 'values': ["USA", "Canada"] },
                    ]
                },

                {
                    'names': ["Grant", "Taveras"],
                    'pics': ['grant_img', 'taveras_img'],
                    'judges': [
                        { 'name': "Derek Cleary", 'score': ["10 - 9", "9 - 10", "10 - 9"] },
                        { 'name': "Eric Colon", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Christopher Edgehill", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    ],
                    'media': [
                        { 'name': "Tyler Treese", 'score': ["30 - 27"] },
                        { 'name': "Chris De Santiago", 'score': ["29 - 28"] },
                    ],
                    'stats': [
                        { 'param': 'age', 'values': [38, 30] },
                        { 'param': 'height', 'values': [5.8, 5.8] },
                        { 'param': 'weight', 'values': [136, 136] },
                        { 'param': 'reach', 'values': [69, 70] },
                        { 'param': 'state', 'values': ["England", "USA"] },
                    ]
                },

                {
                    'names': ["Rodriguez", "Knutsson"],
                    'pics': ['rodriguez_img', 'knutsson_img'],
                    'judges': [
                        { 'name': "Eric Colon", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Sal D'Amato", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Jason Grenier", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    ],
                    'media': [
                        { 'name': "Tyler Treese", 'score': ["30 - 27"] },
                        { 'name': "Tristen Critchfield", 'score': ["30 - 27"] },
                        { 'name': "Brian Knapp", 'score': ["30 - 27"] },
                        { 'name': "Chris De Santiago", 'score': ["30 - 27"] },
                        { 'name': "Matthew Wells", 'score': ["30 - 27"] },
                    ],
                    'stats': [
                        { 'param': 'age', 'values': [28, 32] },
                        { 'param': 'height', 'values': [5.3, 5.3] },
                        { 'param': 'weight', 'values': [116, 116] },
                        { 'param': 'reach', 'values': [60, 63.5] },
                        { 'param': 'state', 'values': ["Sweden", "Venezuela"] },
                    ]
                },
            ]
        },

        {
            'title': 'UFC on ESPN 65 - Covington vs. Buckley - 2',
            'date': '14-12-2024',

            'matches': [
                {
                    'names': ["Marcos", "Yanez"],
                    'pics': ['marcos_img', 'yanez_img'],
                    'judges': [
                        { 'name': "Derek Cleary", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Eric Colon", 'score': ["10 - 9", "9 - 10", "10 - 9"] },
                        { 'name': "Chris Lee", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                    ],
                    'media': [
                        { 'name': "Tyler Treese", 'score': ["29 - 28"] },
                        { 'name': "Tristen Critchfield", 'score': ["10 - 9", "9 - 10", "10 - 9"] },
                        { 'name': "Patrick McCorry", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                    ],
                    'stats': [
                        { 'param': 'age', 'values': [31, 31] },
                        { 'param': 'height', 'values': [5.7, 5.7] },
                        { 'param': 'weight', 'values': [136, 136] },
                        { 'param': 'reach', 'values': [70, 69] },
                        { 'param': 'state', 'values': ["USA", "Peru"] },
                    ]
                },

                {
                    'names': ["Stirling", "Tokkos"],
                    'pics': ['stirling_img', 'tokkos_img'],
                    'judges': [
                        { 'name': "Derek Cleary", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Eric Colon", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Jason Grenier", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    ],
                    'media': [
                        { 'name': "Zane Simon", 'score': ["30 - 26"] },
                        { 'name': "Tyler Treese", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Tristen Critchfield", 'score': ["30 - 27"] },
                    ],
                    'stats': [
                        { 'param': 'height', 'values': [6.4, 6.3] },
                        { 'param': 'weight', 'values': [206, 206] },
                        { 'param': 'reach', 'values': [79, 76] },
                    ]
                },

                {
                    'names': ["Lima", "Johns"],
                    'pics': ['lima_img', 'johns_img'],
                    'judges': [
                        { 'name': "Sal D'Amato", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Chris Lee", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Troy Wincapaw", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    ],
                    'media': [
                        { 'name': "Tyler Treese", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Patrick McCorry", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Matthew Wells", 'score': ["29 - 28"] },
                    ],
                    'stats': [
                        { 'param': 'age', 'values': [30, 26] },
                        { 'param': 'height', 'values': [5.7, 5.6] },
                        { 'param': 'weight', 'values': [146, 146] },
                        { 'param': 'reach', 'values': [66, 68] },
                        { 'param': 'state', 'values': ["USA", "Sweden"] },
                    ]
                },
            ]
        },

        {
            'title': 'UFC on ESPN 65 - Covington vs. Buckley - 3',
            'date': '14-12-2024',

            'matches': [
                {
                    'names': ["Marcos", "Yanez"],
                    'pics': ['marcos_img', 'yanez_img'],
                    'judges': [
                        { 'name': "Derek Cleary", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                        { 'name': "Eric Colon", 'score': ["10 - 9", "9 - 10", "10 - 9"] },
                        { 'name': "Chris Lee", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                    ],
                    'media': [
                        { 'name': "Tyler Treese", 'score': ["29 - 28"] },
                        { 'name': "Tristen Critchfield", 'score': ["10 - 9", "9 - 10", "10 - 9"] },
                        { 'name': "Patrick McCorry", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                    ],
                    'stats': [
                        { 'param': 'age', 'values': [31, 31] },
                        { 'param': 'height', 'values': [5.7, 5.7] },
                        { 'param': 'weight', 'values': [136, 136] },
                        { 'param': 'reach', 'values': [70, 69] },
                        { 'param': 'state', 'values': ["USA", "Peru"] },
                    ]
                },

                {
                    'names': ["Stirling", "Tokkos"],
                    'pics': ['stirling_img', 'tokkos_img'],
                    'judges': [
                    { 'name': "Derek Cleary", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    { 'name': "Eric Colon", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    { 'name': "Jason Grenier", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    ],
                    'media': [
                    { 'name': "Zane Simon", 'score': ["30 - 26"] },
                    { 'name': "Tyler Treese", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    { 'name': "Tristen Critchfield", 'score': ["30 - 27"] },
                    ],
                    'stats': [
                    { 'param': 'height', 'values': [6.4, 6.3] },
                    { 'param': 'weight', 'values': [206, 206] },
                    { 'param': 'reach', 'values': [79, 76] },
                    ]
                },

                {
                    'names': ["Lima", "Johns"],
                    'pics': ['lima_img', 'johns_img'],
                    'judges': [
                    { 'name': "Sal D'Amato", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    { 'name': "Chris Lee", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    { 'name': "Troy Wincapaw", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    ],
                    'media': [
                    { 'name': "Tyler Treese", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    { 'name': "Patrick McCorry", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    { 'name': "Matthew Wells", 'score': ["29 - 28"] },
                    ],
                    'stats': [
                    { 'param': 'age', 'values': [30, 26] },
                    { 'param': 'height', 'values': [5.7, 5.6] },
                    { 'param': 'weight', 'values': [146, 146] },
                    { 'param': 'reach', 'values': [66, 68] },
                    { 'param': 'state', 'values': ["USA", "Sweden"] },
                    ]
                },
            ]
        },

        {
            'title': 'UFC on ESPN 65 - Covington vs. Buckley - 4',
            'date': '14-12-2024',

            'matches': [
                {
                    'names': ["Marcos", "Yanez"],
                    'pics': ['marcos_img', 'yanez_img'],
                    'judges': [
                    { 'name': "Derek Cleary", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    { 'name': "Eric Colon", 'score': ["10 - 9", "9 - 10", "10 - 9"] },
                    { 'name': "Chris Lee", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                    ],
                    'media': [
                    { 'name': "Tyler Treese", 'score': ["29 - 28"] },
                    { 'name': "Tristen Critchfield", 'score': ["10 - 9", "9 - 10", "10 - 9"] },
                    { 'name': "Patrick McCorry", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                    ],
                    'stats': [
                    { 'param': 'age', 'values': [31, 31] },
                    { 'param': 'height', 'values': [5.7, 5.7] },
                    { 'param': 'weight', 'values': [136, 136] },
                    { 'param': 'reach', 'values': [70, 69] },
                    { 'param': 'state', 'values': ["USA", "Peru"] },
                    ]
                },

                {
                    'names': ["Stirling", "Tokkos"],
                    'pics': ['stirling_img', 'tokkos_img'],
                    'judges': [
                    { 'name': "Derek Cleary", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    { 'name': "Eric Colon", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    { 'name': "Jason Grenier", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    ],
                    'media': [
                    { 'name': "Zane Simon", 'score': ["30 - 26"] },
                    { 'name': "Tyler Treese", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    { 'name': "Tristen Critchfield", 'score': ["30 - 27"] },
                    ],
                    'stats': [
                    { 'param': 'height', 'values': [6.4, 6.3] },
                    { 'param': 'weight', 'values': [206, 206] },
                    { 'param': 'reach', 'values': [79, 76] },
                    ]
                },

                {
                    'names': ["Lima", "Johns"],
                    'pics': ['lima_img', 'johns_img'],
                    'judges': [
                    { 'name': "Sal D'Amato", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    { 'name': "Chris Lee", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    { 'name': "Troy Wincapaw", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    ],
                    'media': [
                    { 'name': "Tyler Treese", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    { 'name': "Patrick McCorry", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    { 'name': "Matthew Wells", 'score': ["29 - 28"] },
                    ],
                    'stats': [
                    { 'param': 'age', 'values': [30, 26] },
                    { 'param': 'height', 'values': [5.7, 5.6] },
                    { 'param': 'weight', 'values': [146, 146] },
                    { 'param': 'reach', 'values': [66, 68] },
                    { 'param': 'state', 'values': ["USA", "Sweden"] },
                    ]
                },
            ]
        },

        # UFC 310
        {
            'title': 'UFC 310 - Pantoja vs. Asakura',
            'date': '07-12-2024',

            'matches': [
                {
                    'names': ["Rakhmonov", "Garry"],
                    'pics': ['rakh_img', 'garry_img'],
                    'judges': [
                        { 'name': "Michael Bell", 'score': ["10 - 9", "10 - 9", "9 - 10", "10 - 9", "9 - 10"] },
                        { 'name': "Chris Lee", 'score': ["10 - 9", "10 - 9", "9 - 10", "10 - 9", "9 - 10"] },
                        { 'name': "Ron McCarthy", 'score': ["10 - 9", "10 - 9", "9 - 10", "10 - 9", "9 - 10"] },
                    ],
                    'media': [
                        { 'name': "Jake Noecker", 'score': ["10 - 9", "10 - 9", "10 - 9", "10 - 9", "9 - 10"] },
                        { 'name': "Ryan Frederick", 'score': ["10 - 9", "10 - 9", "9 - 10", "9 - 10", "10 - 9"] },
                    ],
                    'stats': [
                        { 'param': 'age', 'values': [30, 27] },
                        { 'param': 'height', 'values': [6.1, 6.3] },
                        { 'param': 'weight', 'values': [171, 171] },
                        { 'param': 'reach', 'values': [77, 74.5] },
                        { 'param': 'state', 'values': ["Kazakhstan", "Ireland"] },
                    ]
                },

                {
                    'names': ["Gane", "Volkov"],
                    'pics': ['gane_img', 'volkov_img'],
                    'judges': [
                        { 'name': "Adalaide Byrd", 'score': ["10 - 9", "10 - 9", "9 - 10"] },
                        { 'name': "Eric Colon", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                        { 'name': "Junichiro Kamijo", 'score': ["10 - 9", "10 - 9", "9 - 10"] },
                    ],
                    'media': [
                        { 'name': "Danny Segura", 'score': ["10 - 9", "10 - 9", "9 - 10"] },
                        { 'name': "Tristen Critchfield", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                        { 'name': "CombatPress.com", 'score': ["28 - 29"] },
                        { 'name': "Dan Levi", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                        { 'name': "Keith Shillah", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                    ],
                    'stats': [
                        { 'param': 'age', 'values': [34, 36] },
                        { 'param': 'height', 'values': [193, 201] },
                        { 'param': 'weight', 'values': [245.5, 254.5] },
                        { 'param': 'reach', 'values': [206, 200] },
                        { 'param': 'state', 'values': ["France", "Russia"] },
                    ]
                },

                {
                    'names': ["Evloev", "Sterling"],
                    'pics': ['evloev_img', 'sterling_img'],
                    'judges': [
                        { 'name': "Ben Cartlidge", 'score': ["9 - 10", "10 - 9", "10 - 9"] },
                        { 'name': "Derek Cleary", 'score': ["9 - 10", "10 - 9", "10 - 9"] },
                        { 'name': "Sal D'Amato", 'score': ["9 - 10", "10 - 9", "10 - 9"] },
                    ],
                    'media': [
                        { 'name': "Jay Pettry", 'score': ["9 - 10", "10 - 9", "10 - 9"] },
                        { 'name': "Tristen Critchfield", 'score': ["9 - 10", "10 - 9", "10 - 9"] },
                        { 'name': "CombatPress.com", 'score': ["29 - 28"] },
                        { 'name': "Dan Levi", 'score': ["29 - 28"] },
                        { 'name': "Keith Shillah", 'score': ["29 - 28"] },
                        { 'name': "CombatPress.com", 'score': ["29 - 28"] },
                        { 'name': "Dan Levi", 'score': ["29 - 28"] },
                        { 'name': "Keith Shillah", 'score': ["29 - 28"] },
                        { 'name': "Damien Bartonek", 'score': ["28 - 29"] },
                        { 'name': "Ryan Frederick", 'score': ["28 - 29"] },
                        { 'name': "Daniel Yanofsky", 'score': ["28 - 29"] },
                        { 'name': "Val Dewar", 'score': ["28 - 29"] },
                    ],
                    'stats': [
                        { 'param': 'age', 'values': [30, 35] },
                        { 'param': 'height', 'values': [5.7, 5.7] },
                        { 'param': 'weight', 'values': [145.5, 145.5] },
                        { 'param': 'reach', 'values': [72.5, 71] },
                        { 'param': 'state', 'values': ["Russia", "USA"] },
                    ]
                },

                {
                    'names': ["Battle", "Brown"],
                    'pics': ['battle_img', 'brown_img'],
                    'judges': [
                        { 'name': "Michael Bell", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                        { 'name': "Adalaide Byrd", 'score': ["10 - 9", "9 - 10", "10 - 9"] },
                        { 'name': "Ron McCarthy", 'score': ["10 - 9", "9 - 10", "10 - 9"] },
                    ],
                    'media': [
                        { 'name': "Jay Pettry", 'score': ["10 - 9", "10 - 9", "9 - 10"] },
                        { 'name': "Ryan Frederick", 'score': ["9 - 10", "10 - 9", "9 - 10"] },
                    ],
                    'stats': [
                        { 'param': 'age', 'values': [34, 30] },
                        { 'param': 'height', 'values': [6.3, 6.1] },
                        { 'param': 'weight', 'values': [171, 175] },
                        { 'param': 'reach', 'values': [78, 77] },
                        { 'param': 'state', 'values': ['Jamaica', 'USA'] },
                    ]
                },

                {
                    'names': ["Van", "Durden"],
                    'pics': ['van_img', 'durden_img'],
                    'judges': [
                        { 'name': "Michael Bell", 'score': ["9 - 10", "10 - 9", "10 - 9"] },
                        { 'name': "Eric Colon", 'score': ["10 - 9", "10 - 9", "10 - 8"] },
                        { 'name': "Ron McCarthy", 'score': ["10 - 9", "10 - 9", "10 - 9"] },
                    ],
                    'media': [

                    ],
                    'stats': [
                        { 'param': 'age', 'values': [33, 23] },
                        { 'param': 'height', 'values': [5.7, 5.5] },
                        { 'param': 'weight', 'values': [126, 126] },
                    ]
                },
            ]
        },

        # PFL 10 - 2024
        {
            'title': 'PFL 10 - 2024 Season',
            'date': '29-11-2024',

            'matches': [
                {
                    'names': ["Rakhmonov", "Garry"],
                    'pics': ['rakh_img', 'garry_img'],
                    'judges': [
                        { 'name': "Michael Bell", 'score': ["10 - 9", "10 - 9", "9 - 10", "10 - 9", "9 - 10"] },
                        { 'name': "Chris Lee", 'score': ["10 - 9", "10 - 9", "9 - 10", "10 - 9", "9 - 10"] },
                        { 'name': "Ron McCarthy", 'score': ["10 - 9", "10 - 9", "9 - 10", "10 - 9", "9 - 10"] },
                    ],
                    'media': [
                        { 'name': "Jake Noecker", 'score': ["10 - 9", "10 - 9", "10 - 9", "10 - 9", "9 - 10"] },
                        { 'name': "Ryan Frederick", 'score': ["10 - 9", "10 - 9", "9 - 10", "9 - 10", "10 - 9"] },
                    ],
                    'stats': [
                        { 'param': 'age', 'values': [30, 27] },
                        { 'param': 'height', 'values': [6.1, 6.3] },
                        { 'param': 'weight', 'values': [171, 171] },
                        { 'param': 'reach', 'values': [77, 74.5] },
                        { 'param': 'state', 'values': ["Kazakhstan", "Ireland"] },
                    ]
                },

                {
                    'names': ["Gane", "Volkov"],
                    'pics': ['gane_img', 'volkov_img'],
                    'judges': [
                        { 'name': "Adalaide Byrd", 'score': ["10 - 9", "10 - 9", "9 - 10"] },
                        { 'name': "Eric Colon", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                        { 'name': "Junichiro Kamijo", 'score': ["10 - 9", "10 - 9", "9 - 10"] },
                    ],
                    'media': [
                        { 'name': "Danny Segura", 'score': ["10 - 9", "10 - 9", "9 - 10"] },
                        { 'name': "Tristen Critchfield", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                        { 'name': "CombatPress.com", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                        { 'name': "Dan Levi", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                        { 'name': "Keith Shillah", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                    ],
                    'stats': [
                        { 'param': 'age', 'values': [34, 36] },
                        { 'param': 'height', 'values': [193, 201] },
                        { 'param': 'weight', 'values': [245.5, 254.5] },
                        { 'param': 'reach', 'values': [206, 200] },
                        { 'param': 'state', 'values': ["France", "Russia"] },
                    ]
                },

                {
                    'names': ["Gane", "Volkov"],
                    'pics': ['gane_img', 'volkov_img'],
                    'judges': [
                        { 'name': "Adalaide Byrd", 'score': ["10 - 9", "10 - 9", "9 - 10"] },
                        { 'name': "Eric Colon", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                        { 'name': "Junichiro Kamijo", 'score': ["10 - 9", "10 - 9", "9 - 10"] },
                    ],
                    'media': [
                        { 'name': "Danny Segura", 'score': ["10 - 9", "10 - 9", "9 - 10"] },
                        { 'name': "Tristen Critchfield", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                        { 'name': "CombatPress.com", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                        { 'name': "Dan Levi", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                        { 'name': "Keith Shillah", 'score': ["10 - 9", "9 - 10", "9 - 10"] },
                    ],
                    'stats': [
                        { 'param': 'age', 'values': [34, 36] },
                        { 'param': 'height', 'values': [193, 201] },
                        { 'param': 'weight', 'values': [245.5, 254.5] },
                        { 'param': 'reach', 'values': [206, 200] },
                        { 'param': 'state', 'values': ["France", "Russia"] },
                    ]
                },
            ]
        },

    ]
}


# Routes
@app.get("/events", response_model=Events)
def get_events():
    return Events(events=memory_db["events"])


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
