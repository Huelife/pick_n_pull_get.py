#check_inventory.py: Check PicknPull for car stock in different lots

import webbrowser

import requests
from requests.exceptions import HTTPError

#figure out link 
link = ("")
chrome_loc = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

for url in [link]:
  try:
    response = requests.get(url)
    response.raise_for_status()
  except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
  except Exception as err:
    print(f"Other error occurred: {err}")
  else:
    print("Success!")
    webbrowser.get(chrome_loc).open_new_tab(link) #open link if no errors
