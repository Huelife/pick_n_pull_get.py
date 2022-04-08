#check_inventory.py: Check PicknPull for car stock in different lots

import webbrowser

import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

car1 = ""

#while loop user input to check for car
while True:
  try:
    carInput = input("What car are you looking for?"
                     "\nEnter 'q' to quit. ")
  except ValueError:
    continue
  else:
    file1 = open("", "r") #opening file to locate car identifier number
    readfile = file1.read() #reading file contents
    soup = BeautifulSoup(readfile, 'html.parser')
    
    if carInput == "q":
      break
    elif carInput in readfile: #checking if car is found within file
      print(carInput, " found!")
      for option in soup.find_all('option'):  #finding car value pair
        if option.text == carInput:
          car1 = (option['value'])
          print((option['value']))
      break
    else:
      print("{} not found!".format(carInput))
      continue
    file1.close() #closing file

#figure out link 
link = ("https://www.picknpull.com/check-inventory/vehicle-search?"
        "make={}&model=&distance=25&zip=94578&year=".format(car1))
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
    webbrowser.get(chrome_loc).open_new_tab(link) #open link if no errors
