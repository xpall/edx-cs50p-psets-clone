import requests
import json
import sys

data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = json.dumps(data.json(),indent=2)
data = json.loads(data)
rate_in_USD = float(data["bpi"]["USD"]["rate_float"])

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
        price = rate_in_USD * (float(sys.argv[1]))
        print(f"${round(price, 4):,}")
    else:
        raise ValueError

except (requests.RequestException, ValueError):
    sys.exit("Command-line argument is not a number")
