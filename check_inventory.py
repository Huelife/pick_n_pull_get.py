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
    file1 = open("", "r") #opening file to locate car identifier number
    readfile = file1.read() #reading file contents
    
    if carInput == "q":
      break
    elif carInput in readfile: #checking if car is found within file
      print(carInput, " found!")
      print("")
    else:
      print("{} not found!".format(carInput))
      print("")
    file1.close() #closing file
    continue
  
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
