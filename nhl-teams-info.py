import requests

# NHL API endpoint to get team information
url = "https://statsapi.web.nhl.com/api/v1/teams"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    nhl_teams = data["teams"]
    
    for team in nhl_teams:
        print(team["name"])
else:
    print("Failed to retrieve team data from the NHL API")
