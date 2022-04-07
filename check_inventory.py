#check_inventory.py: Check PicknPull for car stock in different lots

import webbrowser

import requests
from requests.exceptions import HTTPError

car1 = ""

#while loop user input to check for car
while True:
  try:
    carInput = input("What car are you looking for?"
                     "\nEnter 'q' to quit. ").lower()
  except ValueError:
    continue
  else:
    print("")
    if carInput == "q":
      break
    elif any(carInput in car1):
      print("Found!")
      print("")
    else:
      print("{} is an invalid option.".format(carInput))
      print("")

#opening file to locate car identifier number
file1 = open("", "r")

#reading file contents
readfile = file1.read()

#checking if car is found within file
if car1 in readfile:
  print(car1, " found!")
else:
  print(car1, " not found!")
  
#closing file
file1.close()

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
