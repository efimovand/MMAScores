from pydantic import BaseModel
from typing import List


# ---------- Classes of data ----------

# Judges / Media
class ScoreCard(BaseModel):
    name: str
    score: List[str]


# Match
class Match(BaseModel):
    names: List[str]
    pics: List[str]
    judges: List[ScoreCard]
    media: List[ScoreCard]
    stats: List[dict]


# Event
class Event(BaseModel):
    title: str
    timestamp: str
    matches: List[Match]


# All Events
class Events(BaseModel):
    future: List[Event]
    present: List[Event]
    past: List[Event]
