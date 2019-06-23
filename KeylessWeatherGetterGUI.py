# Author: Ryan Reyes, github.com/techproofreader
# Program Name: Weather Getter
# Version: 1.0

import json
import requests
import PySimpleGUI as sg
from geopy import Nominatim
from degreesToCompass import compass

menu_def = [['File', ['About']]
            ]
     
layout = [ [sg.Menu(menu_def, tearoff=False)],
           [sg.Txt('Enter your address to get the current weather', font=("Noteworthy", 20), text_color='#f4d1ab', background_color='#ad9b88')],      
           [sg.In(size=(57, 1), key='address', justification="left")],              
           [sg.Button('Get my weather!', bind_return_key=True, font=("Noteworthy", 18))]]   
     
window = sg.Window('Weather Getter, powered by Dark Sky', layout, background_color='#ad9b88')      
     
while True:
    event, values = window.Read()     

    if event == 'About':
        sg.Popup('Author: Ryan Reyes, https://github.com/TechProofreader',
                 'Program Name: Weather Getter',
                 'Version: 1.0',
                 'The weather data generated by this program was provided by the Dark Sky API, https://darksky.net/dev.',
                 'The geocoding was made possible with geopy, https://github.com/geopy/geopy, which utilizes the MIT License.',
                 'The Numpy package was utilized to create the function that translates the wind directions. Numpy is licensed under the BSD License and can be found at: https://www.numpy.org/.',
                 'The GUI of this program was created with the PySimpleGUI Framework, which is licensed under the GNU Lesser General Public License v3.0.',
                 'The creator of PySimpleGUI is: https://github.com/MikeTheWatchGuy.',
                 'This "Weather Getter" program is licensed under the GNU Lesser General Public License v3.0.', font=('Noteworthy', 18), text_color='#f4d1ab', background_color='#ad9b88')

    elif event == 'Get my weather!': # Note: Don't forget to type your Dark Sky Developer Key in the "url" function bewlow; insert it where it says 'your Dark Sky Developer Key goes here'.
        try:
            geolocator = Nominatim(user_agent="WeatherGetter")
            location = geolocator.geocode(values['address'])
            url = 'https://api.darksky.net/forecast/'+'your Dark Sky Devoloper Key goes here'+/'+str(location.latitude)+','+str(location.longitude)+'?exclude=minutely,hourly,daily'
            r = requests.get(url)
            info = json.loads(r.text)
            direction = str(compass(info['currently']['windBearing']))
            sg.Popup('Current weather: '+str(info['currently']['summary'])+', '+str(round((info['currently']['temperature']), 2))+'°F.',
                     'It feels like '+str(round((info['currently']['apparentTemperature']), 2))+'°F'+' with '+str(round((info['currently']['humidity']*100), 2))+'% Humidity.',
                     'There is '+str(round((info['currently']['precipProbability']*100), 2))+'% chance of rain.',
                     'There is '+str(round((info['currently']['cloudCover']*100), 2))+'%'+' cloud cover'+' with '+str(round((info['currently']['visibility']), 2))+' miles of visibility.',
                     'The wind is blowing '+direction+' '+str(round((info['currently']['windSpeed']), 2))+' mph with a gust of '+str(round((info['currently']['windGust']), 2))+' mph.',
                     'The Dew Point is '+str(round((info['currently']['dewPoint']), 2))+'°F.',
                     'The UV Index is '+str(info['currently']['uvIndex'])+'.', font=('Noteworthy', 18), text_color="#f4d1ab", background_color='#ad9b88')
        except:
            sg.Popup('Please enter a valid address', font=('Noteworthy', 20), text_color='#f4d1ab', background_color='#ad9b88')
    else:    
        break
