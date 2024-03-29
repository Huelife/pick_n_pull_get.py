#check_Toyota_Camry.py: Check for Toyota Camrys at PicknPull nearby and open link

import webbrowser

import requests
from requests.exceptions import HTTPError

link = ("https://www.picknpull.com/check-inventory/vehicle-search?"
        "make=234&model=4352&distance=25&zip=94578&year=")
chrome_loc = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

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
    webbrowser.get(chrome_loc).open_new_tab(link)  #open link if no errors
