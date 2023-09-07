# sportsbook/search.py
import requests
from config import settings

def search_bet(bet_details):
    # Connect to SPORTSBOOK_URL using SPORTSBOOK_API_KEY
    headers = {
        "Authorization": f"Bearer {settings.SPORTSBOOK_API_KEY}",
        "Content-Type": "application/json"
    }

    # Construct the search URL. For this demonstration, we'll assume `bet_details` contains a team name.
    # The actual structure of the URL would depend on the sportsbook's API documentation.
    search_url = f"{settings.SPORTSBOOK_URL}/search?team={bet_details['team_name']}"
    
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Check if the desired bet details are present in the response
        # For this demonstration, we're assuming the response contains a list of matches.
        for match in data.get("matches", []):
            # This is a basic condition; in reality, you'd match against more criteria from bet_details.
            if match["team_name"] == bet_details["team_name"]:
                return match  # Return the matched bet details from the sportsbook

    except requests.RequestException as e:
        print(f"Error searching for the bet: {e}")

    return None  # Return None if no match is found or in case of an error
