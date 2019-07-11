import pprint
import requests
import logging
import pprintpp


###### Example 1. Pprint with Lists Example ######
breakfast = ['bacon', 'eggs', 'toast', 'waffles', 'hash browns']

print("\n" + "----------Regular Print (List)------------" + "\n")
print(breakfast)

breakfast.insert(0, breakfast[:])
pp = pprint.PrettyPrinter(indent=4)

print("\n" + "----------PPrint Print (List) ------------" + "\n")
pp.pprint(breakfast)


###### Example 2. Pprint with Nested Tuple Example ######
breakfast_tup = ('bacon', ('eggs', ('toast', ('waffles', ('hash browns', ('sausage',
('biscuits', ('strawberries',))))))))
print("\n" + "----------Regular Print (Nested Tuple)------------" + "\n")
print(breakfast_tup)

pp = pprint.PrettyPrinter(depth=6)
print("\n" + "----------PPrint Print (Nested Tuple) ------------" + "\n")
pp.pprint(breakfast_tup)


###### Example 3. Using PPrint in an API Call ######
# Get an API key and uncomment the code to make this call run.
# Get a free API Key Here: https://openweathermap.org/city

# from pprint import pprint
# API_key = "" #Enter your API key in the empty string

# base_url = "http://api.openweathermap.org/data/2.5/weather?"

# print("\n" + "-------Pprint with Weather API-----------")
# zip_code = str(input("\n" + "Enter a Zip code to check the current weather: "))
# Final_url = base_url + "appid=" + API_key + "&zip=" + zip_code

# weather_data = requests.get(Final_url).json()

# print("\n Current Weather in: " + zip_code +":\n")
# print("------------------------------------------")
# pprint(weather_data) 


#### Example 4. Pprint with Derivative Function .pformat ######
from pprint import pformat

data=[(1,{'a':'A','b':'B','c':'C','d':'D'}),(2,{'e':'E','f':'F','g':'G','h':'H','i':'I','j':'J','k':'K','l':'L'}),(3,['m','n']),(4,['o','p','q','r','s','t','u','v','w']),(5,['x','y','z']),]

print("\n" + "---------- Pprint with Logging ----------")
logging.basicConfig(
       level=logging.DEBUG,
       format='%(levelname)-8s %(message)s',)
logging.debug('Logging pformatted data')

formatted=pformat(data)

for line in formatted.splitlines():
       logging.debug(line.rstrip())
       
###### Example 5. PPrintPP ######
print("\n" + "----------- PprintPP ----------")
pprintpp.pprint(data)