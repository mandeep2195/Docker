import requests
import os
import json

def call():
    city = input("enter the city you want to know the weather of: ")
    url = f"https://api.weatherapi.com/v1/current.json?key=b42507561ff84ffea3d50021232007&q={city}"
    # url consists of url of the api, my api key, &q= for parameters.

    # getting the response from the api by combining all factors in the link.
    response = requests.get(url).json()
    # importing json is important to get (calling) the keys and values from the api.
    print(response['location']['name'] + ", " + response['location']['region'])
    print(response['location']['localtime'])
    print(f"The Current Temperature in {city} is ", response['current']['temp_c'], "Degree Celsius")
    print("The current atmosphere is:", response['current']['condition']['text'])
    print("You can visit this link for viewing the icon: ", response['current']['condition']['icon'])
    print("The current level of Humidity is", response['current']['humidity'], "percent.")
    print("The current weather feels like:", response['current']['feelslike_c'], "Degree Celsius")
    print("The current Visibility level is", response['current']['vis_km'], "KM.")

call()
while True:
    choice = int(input('''\nEnter 1 to know the weather of another place.
Enter 0 to Exit
==>'''))
    match choice:
        case 1:
            os.system('cls')
            call()
        case 0:
            exit()