import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Cardio:
    '''Astrand Treadmill Test: The objective of this test is to monitor the development of the athlete's
general endurance (VO2max).
Required resources
To undertake this test you will require:
* Treadmill where the speed can be set at 5 mph (8.05 km/hr) and grade of
slope can be adjusted
* Stop watch
* Assistant.
How to conduct the test
* The treadmill is set up at the start with a speed of 8.05km/hr (5 mph) and
a grade of slope of 0%
* The athlete commences the test
* After 3 minutes the grade is set to 2.5% and then every 2 minutes the
grade is increased by 2.5%
* The assistant starts the stop watch at the start of the test and stops it
when the athlete is unable to continue.
Analysis
Analysis of the result is by comparing it with the results of previous tests. It is
expected that, with appropriate training between each test, the analysis would
indicate an improvement.
From the total running time an estimate of the athlete's VO2max can be
calculated as follows:
* VO2max = (Time x 1.444) + 14.99
* “Time” is the total time of the test expressed in minutes and fractions of
a minute.
Example:
The athlete stopped the test after 13 minutes 15 seconds of running (13.25
minutes).
* VO2max = (13.25 x 1.444) + 14.99
* VO2max = 34.123 mls/kg/min.
Target group
This test is suitable for endurance athletes and players of endurance sports
(eg football, rugby) but not for individuals where the test would be
contraindicated.
Reliability
Reliability would depend upon how strict the test is conducted and the
individual's level of motivation to perform the test.
'''
    
    
    
    def astrand_treadmill_test(time):
        VO2max = (time * 1.444) + 14.99
            
        return VO2max
        
    '''Balke Treadmill Test
The objective of this test is to monitor the development of the athlete's
general endurance (VO2max).
Required resources
To undertake this test you will require:
* Treadmill where speed and grade of slope can be adjusted
* Stop watch
* Assistant.
How to conduct the test
The athlete walks on a treadmill to exhaustion. At timed stages during the test
the grade of slope (%) of the treadmill is increased as follows:
* Active and sedentary men
* Treadmill speed set at 3.3 mph (5.3km/hr)
* Start – Grade is 0%
* After 1 minute – Grade set at 2%
* After 2 minutes and each minute thereafter the grade is increased by 1%
* Active and sedentary women
* Treadmill speed set at 3.0 mph (4.5 km/hr)
* Start – Grade is 0%
* After 3 minutes and every 3 minutes thereafter the grade is increased
by 2.5%
* The assistant starts the stop watch at the start of the test and stops it
when the athlete is unable to continue – this ideally should be between
9 and 15 minutes.
Analysis
Analysis of the result is by comparing it with the results of previous tests. It is
expected that, with appropriate training between each test, the analysis would
indicate an improvement.
Active and sedentary men – Pollock et al. 1976
From the total time an estimate of the athlete's VO2max can be calculated as
follows:
* VO2max = 1.444 x T + 14.99
* “T” is the total time of the test expressed in minutes and fractions of a
minute eg 13 minutes, 15 seconds = 13.25 minutes.
Active and sedentary women – Pollock et al. 1982
From the total time an estimate of the athlete's VO2max can be calculated as
follows:
* VO2max = 1.38 x T + 5.22
* “T” is the total time of the test expressed in minutes and fractions of
a minute.
Target group
This test is suitable for active and sedentary individuals but not for those
where the test would be contraindicated.
Reliability
Reliability would depend upon how strict the test is conducted and the
individual's level of motivation to perform the test '''
        
    def balke_treadmill_test(gender, time):
        
        if gender == 'M' or gender == 'Male' or gender == 'male' or gender == 'm':
            VO2max = (time * 1.444) + 14.99
        elif gender == 'F' or gender == 'Female' or gender == 'female' or gender == 'f':
            VO2max = (time * 1.38) + 5.22
        return  VO2max
    ''' Cooper VO2max Test
The objective of the Cooper test is to predict an athlete’s VO2max.
Required resources
To undertake this test you will require:
* 400 metre track – marked every 50m
* Stop watch
* Assistant.
How to conduct the test
The test comprises of seeing how far an athlete can run/walk in 12 minutes.
The assistant should record the total distance covered.
Performance assessment
Based on the distance covered an estimate of the athlete’s VO2max can be
calculated as follows:
* VO2max = (Distance covered in metres – 504.9) / 44.73
Example:
The athlete, a male football player, completes a total distance of 3400m in the
12 minutes.
VO2max = (3400 – 504.9) / 44.73
= 64.72 ml/kg/min.
Analysis
Analysis of the result is by comparing it with the results of previous tests. It is
expected that, with appropriate training between each test, the analysis would
indicate an improvement.
The result from the Cooper test can be used to:
* predict future performance
* indicate weaknesses
* measure improvement
* enable the coach to assess the success of his training programme
* place the athlete in appropriate training group
* motivate the athletes 
'''  

    
    def cooper_VO2max_test(distance):
        VO2max = (distance - 504.9) / 44.73
        return  VO2max
    
    
    
    ''' Critical Swim Speed
he Critical Swim Speed (CSS) test, devised by Ginn [1] in 1993, can be used
to monitor the athlete's aerobic capacity. The result of the test can also be
used to determine the appropriate target time for each repetition of a
swimmer’s aerobic training session. CSS is defined as “the maximum
swimming speed that can theoretically be maintained continuously
without exhaustion” [2] – just below the swimmer’s lactate threshold.
Required resources
To undertake the CSS test you will require:
* Swimming pool
* Stop watch
* Assistant.
Test process
The following protocol should be followed:
* Start each swim from a push start – not a dive in
* Allow a full recovery between each swim
* Record the time for each swim in seconds
* Calculate the athlete’s CSS.
How to conduct the test
The test comprises of two maximal swims over 400 metres and 50 metres.
A suitable rest period should be taken between each swim to allow the athlete
to fully recover. The assistant should record the times for each swim.
Analysis
Analysis of the result is by comparing it with the results of previous tests. It is
expected that, with appropriate training between each test, the analysis would
indicate an improvement.
Calculation of CSS
The calculation of the swimmer’s CSS, based on their 400m and 50m times,
and is as follows:
* CSS = (D2 – D1) / (T2 – T1)
'''
    
    def critical_swim_speed(d2,d1,t2,t1):
        css = (d2 - d1) / (t2 -t1)
        return  css