import requests

from typing import TypedDict, List, Optional
from datetime import datetime

class SplitTime(TypedDict):
    distance: int
    absolute_time: float
    relative_time: float
    delta_time: float

class Stroke(TypedDict):
    stroke: int
    distance: int
    power_act: int
    split_act: int
    rate: float

class Game(TypedDict):
    id: int
    calories: float
    distance: int
    elapsed_seconds: int
    extra_millies: int
    time: int
    p_ave: float
    stroke_count: int
    option: str
    option_distance: int
    option_time: int
    created: str
    account: int
    mod: str
    device_mac: str
    accessory_mac: str
    ave_bpm: int
    watt_per_beat: Optional[float]
    ave_power: Optional[float]
    watt_kg: float
    strava_id: str
    curve: str
    confirmed: bool
    public_id: str
    user_age: int
    user_max_hr: Optional[int]
    calc_ave_split: int
    calc_min_split: int
    calc_avg_stroke_work: int
    calc_avg_stroke_length: int
    calc_avg_stroke_time: Optional[int]
    calc_avg_stroke_rate: float
    calc_max_stroke_rate: float
    calc_max_power: int
    protocol_version: int
    calc_max_force: int
    calc_ave_hr: int
    calc_max_hr: int
    split_times: List[SplitTime]
    heart_rates: List
    strokes: List[Stroke]
    race_details: Optional[str]

class PublicGame(TypedDict):
    id: int
    calories: float
    distance: int
    elapsed_seconds: int
    extra_millies: int
    time: int
    p_ave: float
    stroke_count: int
    option: str
    option_distance: int
    option_time: int
    created: datetime
    account: int
    mod: datetime
    device_mac: str
    accessory_mac: str
    ave_bpm: int
    watt_per_beat: Optional[float]
    ave_power: Optional[float]
    watt_kg: float
    strava_id: str
    curve: str
    confirmed: bool
    race: Optional[None]  # Assuming 'race' can be None based on your data
    public_id: str
    user_age: int
    user_weight: int
    user_max_hr: Optional[int]
    protocol_version: int
    calc_ave_split: int
    calc_avg_stroke_work: int
    calc_avg_stroke_rate: float

def Profile(TypedDict):
    id: str
    avatar: str
    name: str
    country: int
    country_name: str
    gender: str
    age_class: str
    weight_class: str
    color: str



class SmartRow:
    base_url = "https://smartrow.fit/api"

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def get_game(self, id) -> Game:
        url = f"{self.base_url}/game/{id}"
        response = requests.get(url, auth=(self.username, self.password))
        return response.json()
    
    def get_games(self) -> List[PublicGame]:
        url = f"{self.base_url}/public-game"
        response = requests.get(url, auth=(self.username, self.password))
        return response.json()
    
    def get_profile(self) -> List[Profile]:
        url = f"{self.base_url}/profile"
        response = requests.get(url, auth=(self.username, self.password))
        return response.json()


