# Author: Ryan Reyes, github.com/TechProofreader
# Program Name: Degrees to Compass Function
# Version: 1.0

def compass(n):
    if (11.75 < n < 33.75):
        return 'NNE'
    elif  (33.75 < n < 56.25):
        return 'NE'
    elif  (56.25 < n < 78.75):
        return 'ENE'
    elif  (78.75 < n < 101.25):
        return 'E'
    elif  (101.25 < n < 123.75):
        return 'ESE'
    elif  (123.75 < n < 146.25):
        return 'SE'
    elif  (146.25 < n < 168.65):
        return 'SSE'
    elif  (168.75 < n < 191.25):
        return 'S'
    elif  (192.25 < n < 213.75):
        return 'SSW'
    elif  (213.75 < n < 236.25):
        return 'SW'
    elif  (236.25 < n < 258.75):
        return 'WSW'
    elif  (258.75 < n < 281.25):
        return 'W'
    elif  (281.25 < n < 303.75):
        return 'WNW'
    elif  (303.75 < n < 326.25):
        return 'NW'
    elif  (326.25 < n < 348.75):
        return 'NNW'
    elif  (348.75 < n < 365):
        return 'N'
    elif  (0 < n < 11.25):
        return 'N'