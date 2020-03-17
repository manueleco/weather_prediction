import numpy as np
import random as rm
import time


states = ["Soleado","Nublado"]

transitionName = [["SuSu","SuCl"],["ClCl","ClSu"]]

transitionMatrix = [[0.8,0.2],[0.4,0.6]]


if sum(transitionMatrix[0])+sum(transitionMatrix[1]) != 2:
    print("Error!")
    raise ValueError("Probabilities MUST ADD TO 1")



def weatherForecast(days):

    weatherToday = rm.choice(states)
    i = 0
    print("Starting weather: ",weatherToday)
    while i &lt; days:
        if weatherToday == "Soleado":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "SuSu":
                pass
            else:
                weatherToday = "Nublado"
        elif weatherToday == "Nublado":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "ClCl":
                pass
            else:
                weatherToday = "Soleado"
        print(weatherToday)
        i += 1
        time.sleep(0.2)


weatherForecast(10)