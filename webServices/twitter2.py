import urllib.request, urllib.parse, urllib.error
import json
import twurl  # Twitter URL library

TWITTER_URL = "https://api.twitter.com/1.1/friends/list.json"

while True:
    print("")
    acct = input("Enter Twitter Account:")
    if len(acct) < 1:
        break
    url = twurl.augment(TWITTER_URL, {"screen_name": acct, "count": "5"})

    print("Retrieving", url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
