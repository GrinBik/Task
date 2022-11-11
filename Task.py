from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps

def get_score(game_stamps, offset):
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    '''
    # return home, away

    # Check for correct input offset
    if type(offset) is not int:
        try:
            offset = int(offset)
        except:
            return "Inputed offset is incorrect!"

    # Check for correct input game_stamps 
    if type(game_stamps) is not list:
        return "Input correct list of game's stamps!"
    if isinstance(game_stamps[0].get('offset', 'offset is not exists'), str):
        return "Input correct list of game's stamps!"
    if not isinstance(game_stamps[0].get('score', 'score is not exists'), dict):
        return "Input correct list of game's stamps!"
    if not isinstance(game_stamps[0]['score'].get('home', 'home is not exists'), int):
        return "Input correct list of game's stamps!"
    if not isinstance(game_stamps[0]['score'].get('away', 'away is not exists'), int):
        return "Input correct list of game's stamps!"

    # Search inputed offset in game_stamps list
    low = 0
    high = len(game_stamps) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = game_stamps[mid]['offset']
        if guess == offset:
            return game_stamps[mid]['score']['home'], game_stamps[mid]['score']['away']
        if guess > offset:
            high = mid -1
        else:
            low = mid + 1
    # If inputed offset is not in game_stamps list
    return "List not contain scores for current offset!"

if __name__ == "__main__":
    game_stamps = generate_game()
    pprint(game_stamps)
    pprint(get_score(game_stamps, 45))