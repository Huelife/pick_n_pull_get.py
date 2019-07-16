#pick_n_pull_get.py: Check for Toyota Camrys at PicknPull nearby and open link

import webbrowser

import requests
from requests.exceptions import HTTPError

link = ("https://www.picknpull.com/check_inventory.aspx?Zip=94578&"
        "Make=234&Model=4352&Year=&Distance=25")
chrome_loc = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
