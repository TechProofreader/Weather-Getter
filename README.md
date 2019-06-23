# Weather-Getter
Powered by the Dark Sky API, this clean and simple weather app gets the current weather conditions for the address that you input. Valid inputs include partial addresses, full addresses, and zipcodes.

Since the Dark Sky API outputs the weather data via JSON and utilizes degrees for the wind direction, I had to write a function that converts bearing degrees to compass points. [This file](degreesToCompass.py) contains the function that I wrote to convert degrees to compass points for user readability. For example, Dark Sky might output 79° for the JSON value of the `windBearing` key, which when converted by my function, is translated and output to 'E' for "East," which is instantly understandable for the user, rather than trying to figure out what the directional degrees represent.

[Here is an image of the app's main screen](WeatherGetterMainScreen.png) & [Here is an image of what the current weather data output looks like](WeatherGetterOutputScreen.png).
