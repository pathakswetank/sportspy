# Sportspy

Are You Prepared to Meet The Next Level of Competition? 
The various approach to demystify the data is to quantify it appropriately through key performance indicator could be stated as sports and performance metrics; that differs from sports to sports and body to body. When soever a player is participating in various training or events there is a roll-out of lots of data in two forms human body performance and sports specific data.
“The objectives of sports science data scientist is not only to look after match day metrics but also the bodily changes that may cause an impact of the performance.”
With context to human performance and sports analyst, in the first version:
1. Anthropometry
2. Load Monitoring
3. Cricket
4. Performance Evaluation
	a. Cardio

version="0.0.3"
   
## Installation

pip install sportspy

## Usage

It will be going to help sports statisticians or sports analysts and even though sports scientists analyze the team or individual athlete in terms of their fitness and performance.
###anthropometry

>>> from sportspy.anthropometry import Somatotype
>>> Somatotype.endomorphy(14,7,5)
2.6193264000000003

>>> from sportspy.anthropometry import Somatotype
>>> Somatotype.mesomorphy(7,8,26.2,24.2,165)
2.5207999999999977

>>> from sportspy.anthropometry import Somatotype
>>> Somatotype.ectomorphy(165,68)
1.0866720588698513


###load monitoring
>>> from sportspy.load import AMS
>>> AMS.load_morning(8,40)
   Second Week Load  Third Week Load  Fourth Week Load  ...  Chronic Load  Freshness Index  Acute Chronic Workload Ratio
0                 0                0                 0  ...          80.0            240.0                           4.0


### cricket
>>> from sports.cricket import Cricket
>>> Cricket.batting_forecast(2) #Markov Chain Algorithm
Start state: Miss
{'Possible states': "['Miss', 'Out', 'Run']", 'End state after': '2', ' activity': 'Run', 'Probability of the possible sequence of states': '0.12'}


### performance_evaluation
>>> from performance_evaluation.endurance import Cardio
>>> Cardio.balke_treadmill_test('f',12)
21.779999999999998
>>> Cardio.balke_treadmill_test('m',12)
32.318

## Contributing

Author :Swetank Pathak

Author_email : swetankpathak@gmail.com


## License

Copyright (c) 2021 Swetank Pathak

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.