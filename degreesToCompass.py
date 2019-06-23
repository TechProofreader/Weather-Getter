# Author: Ryan Reyes, github.com/TechProofreader
# Program Name: Degrees to Compass Function
# Version: 1.0

import numpy

def compass(n):
    if n in numpy.arange(11.75, 33.75, 0.25):
        return 'NNE'
    elif n in numpy.arange(33.75, 56.25, 0.25):
        return 'NE'
    elif n in numpy.arange(56.25, 78.75, 0.25):
        return 'ENE'
    elif n in numpy.arange(78.75, 101.25, 0.25):
        return 'E'
    elif n in numpy.arange(101.25, 123.75, 0.25):
        return 'ESE'
    elif n in numpy.arange(123.75, 146.25, 0.25):
        return 'SE'
    elif n in numpy.arange(146.25, 168.65, 0.25):
        return 'SSE'
    elif n in numpy.arange(168.75, 191.25, 0.25):
        return 'S'
    elif n in numpy.arange(192.25, 213.75, 0.25):
        return 'SSW'
    elif n in numpy.arange(213.75, 236.25, 0.25):
        return 'SW'
    elif n in numpy.arange(236.25, 258.75, 0.25):
        return 'WSW'
    elif n in numpy.arange(258.75, 281.25, 0.25):
        return 'W'
    elif n in numpy.arange(281.25, 303.75, 0.25):
        return 'WNW'
    elif n in numpy.arange(303.75, 326.25, 0.25):
        return 'NW'
    elif n in numpy.arange(326.25, 348.75, 0.25):
        return 'NNW'
    elif n in numpy.arange(348.75, 365, 0.25):
        return 'N'
    elif n in numpy.arange(0, 11.25, 0.25):
        return 'N'