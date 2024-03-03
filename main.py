import os
import csv

from tqdm import tqdm
from smartrow import SmartRow
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    if not os.getenv("SMARTROW_USER") or not os.getenv("SMARTROW_PASSWORD"):
        print("Please set the environment variables SMARTROW_USER and SMARTROW_PASSWORD")
        exit(1)

    smartrow = SmartRow(os.getenv("SMARTROW_USER"), os.getenv("SMARTROW_PASSWORD"))

    games = smartrow.get_games()
    with open('smartrow.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Game ID', 'Distance (m)', 'Time (s)', 'Calories (kcal)', 'Peak Power (W)'])
        for game in tqdm(games):
            game_details = smartrow.get_game(game["id"])
            writer.writerow([game_details['id'], game_details['distance'], game_details['time'], game_details['calories'], game_details['calc_max_power']])

    

