import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class AMS:
    # for morning session data use this function
    def load_morning(session_rpe, duration):
        session_load = session_rpe * duration
        session_load = pd.Series(session_load)
        first_week = sum(session_load.iloc[0:7])
        second_week = sum(session_load.iloc[7:14])
        third_week = sum(session_load.iloc[14:21])
        fourth_week = sum(session_load.iloc[21:28])
        acute_load = first_week
        chronic_load = (first_week+second_week+third_week+fourth_week) * 0.25
        freshness_index =  acute_load - chronic_load
        ACWR = acute_load/chronic_load
        athlete = pd.DataFrame({"Second Week Load": second_week, "Third Week Load": third_week,
                   "Fourth Week Load": fourth_week, "Acute Load" : acute_load, "Chronic Load": chronic_load,
                   "Freshness Index": freshness_index,
                   "Acute Chronic Workload Ratio" :ACWR},index=[0]) 
    
        return athlete

    # for evening session data use this function
    def load_evening(session_rpe, duration):
        session_load = session_rpe * duration
        session_load = pd.Series(session_load)
        first_week = sum(session_load.iloc[0:7])
        second_week = sum(session_load.iloc[7:14])
        third_week = sum(session_load.iloc[14:21])
        fourth_week = sum(session_load.iloc[21:28])
        acute_load = first_week
        chronic_load = (first_week+second_week+third_week+fourth_week) * 0.25
        freshness_index =  acute_load - chronic_load
        ACWR = acute_load/chronic_load
        athlete = pd.DataFrame({"Second Week Load": second_week, "Third Week Load": third_week,
                   "Fourth Week Load": fourth_week, "Acute Load" : acute_load, "Chronic Load": chronic_load,
                   "Freshness Index": freshness_index,
                   "Acute Chronic Workload Ratio" :ACWR},index=[0]) 
        return athlete
    
    