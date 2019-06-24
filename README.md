# Weather-Getter
Powered by the Dark Sky API, this clean and simple desktop weather app gets the current weather conditions for the address that you input. Valid inputs include cities, states, zip codes, or any combination of the three, such as `Honolulu, Hawaii, 96817`. If you would instead like to view the overall weather conditions of an entire country, simply type the country's name in, as that is also an acceptable input type for international purposes. This desktop app works worldwide and is compatible with MacOS, Windows OS, and Linux. Although I only wrote the app in English, it is able to take and process user inputs from most other languages, which I believe is due to the language support from Geopy and the services it pulls data from. Note, however, that the output data will still be displayed in English because I only speak English, but I am looking into creating functionality to translate the output data into the language that the user inputs. Also note, that in order to succesfully use this weather app, you must register for a free developer Dark Sky API Key in order for the app to be able to interface with the Dark Sky API. You can register for a key here: https://darksky.net/dev.

Since the Dark Sky API outputs the weather data via JSON and utilizes degrees for the wind direction, I had to write a function that converts bearing degrees to compass points. [This file](degreesToCompass.py) contains the function that I wrote to convert degrees to compass points for user readability. For example, Dark Sky might output 79° for the JSON value of the `windBearing` key, which when converted by my function, is translated and output to 'E' for "East," which is instantly understandable for the user, rather than trying to figure out what the directional degrees represent.

[Here is an image of the app's main screen](WeatherGetterMainScreen.png) & [Here is an image of what the current weather data output looks like](WeatherGetterOutputScreen.png).
