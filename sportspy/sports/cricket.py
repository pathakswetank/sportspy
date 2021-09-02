import numpy as np
class Cricket:

    
    # A function that implements the Markov model to forecast the state/mood.
    def batting_forecast(bowl):
    
            # The statespace
        states = ["Miss","Out","Run"]

        # Possible sequences of events
        transitionName = [["MM","MO","MR"],["OM","OR","OO"],["RM","RO","RR"]]

        # Probabilities matrix (transition matrix)
        transitionMatrix = [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]

        # Choose the starting state
        nextbowl = "Miss"
        print("Start state: " + nextbowl)
        # Shall store the sequence of states taken. So, this only has the starting state for now.
        activityList = [nextbowl]
        i = 0
        # To calculate the probability of the next bowl
        prob = 1
        while i != bowl:
            if nextbowl == "Miss":
                change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
                if change == "MM":
                    prob = prob * 0.2
                    activityList.append("Miss")
                    pass
                elif change == "MO":
                    prob = prob * 0.6
                    nextbowl = "Out"
                    activityList.append("Out")
                else:
                    prob = prob * 0.2
                    nextbowl = "Run"
                    activityList.append("Run")
            elif nextbowl == "Out":
                change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
                if change == "OM":
                    prob = prob * 0.5
                    activityList.append("Miss")
                    pass
                elif change == "OR":
                    prob = prob * 0.2
                    nextbowl = "Run"
                    activityList.append("Run")
                else:
                    prob = prob * 0.3
                    nextbowl = "Out"
                    activityList.append("Out")
            elif nextbowl == "Run":
                change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
                if change == "RM":
                    prob = prob * 0.1
                    activityList.append("Miss")
                    pass
                elif change == "RO":
                    prob = prob * 0.2
                    nextbowl = "Out"
                    activityList.append("Out")
                else:
                    prob = prob * 0.7
                    nextbowl = "Run"
                    activityList.append("Run")
            i += 1  
        a = str(activityList)
        b = str(bowl) 
        c= nextbowl
        d =  str(prob)
        
        forecast = {"Possible states": a, "End state after": b, " activity": c,
                    "Probability of the possible sequence of states":d }
         
        return forecast
    