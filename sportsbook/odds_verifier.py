# sportsbook/odds_verifier.py
from config import settings

def verify_odds(odds):
    # Compare the provided odds with the set criteria from settings
    if odds >= settings.MINIMUM_ODDS:
        return True  # The odds meet the criteria
    else:
        return False
