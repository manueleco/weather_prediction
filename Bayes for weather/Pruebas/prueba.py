# A simple Markov chain model for the weather in Python

import numpy as np
import random as rm
import time

# Let's define the statespace
states = ["Sunny","Cloudy"]

# Possible sequences of events
transitionName = [["SuSu","SuCl"],["ClCl","ClSu"]]

# Probabilities matrix (transition matrix)
transitionMatrix = [[0.8,0.2],[0.4,0.6]]


# Check that probabilities add to 1. If not, raise ValueError
if sum(transitionMatrix[0])+sum(transitionMatrix[1]) != 2:
    print("Error!!!! Probabilities MUST ADD TO 1. Check transition matrix!!")
    raise ValueError("Probabilities MUST ADD TO 1")


# A functions which implements the Markov model to forecast the weather
def weatherForecast(days):
    # There is no reason to start from one state or another, let's just
    # pick one randomly
    weatherToday = rm.choice(states)
    i = 0
    print("Starting weather: ",weatherToday)
    while i &lt; days:
        if weatherToday == "Sunny":
            #numpy.random.choice(a, size=None, replace=True, p=None)
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "SuSu":
                pass
            else:
                weatherToday = "Cloudy"
        elif weatherToday == "Cloudy":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "ClCl":
                pass
            else:
                weatherToday = "Sunny"
        print(weatherToday)
        i += 1
        time.sleep(0.2)

# We forecast the weather for 100 days
weatherForecast(100)