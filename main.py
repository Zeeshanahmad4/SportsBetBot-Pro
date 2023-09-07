# main.py
from telegram import listener
from sportsbook import search, odds_verifier, placer
from utilities import stealth

def main():
    # Main logic to run the bot
    
    # 1. Listen to the Telegram group for new bet details
    bet_details = listener.listen_for_bets()
    
    # If no bet details are received, exit
    if not bet_details:
        print("No bet details received.")
        return
    
    # 2. Search for the bet on the sportsbook
    found_bet = search.search_bet(bet_details)
    
    # If the bet is not found, exit
    if not found_bet:
        print("Bet not found on the sportsbook.")
        return
    
    # 3. Verify the odds
    odds_are_valid = odds_verifier.verify_odds(found_bet['odds'])
    
    # If the odds don't meet the criteria, exit
    if not odds_are_valid:
        print("Odds do not meet the criteria.")
        return
    
    # 4. Disguise the bot's activity
    stealth.disguise_bot_activity()
    
    # 5. Place the bet
    confirmation = placer.place_bet(found_bet)
    print(confirmation)

if __name__ == "__main__":
    main()
