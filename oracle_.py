import os
import random

import numpy as np
import pandas as pd
from scipy import stats
import pandas as pd

CSV_FILE_PATH = r"C:\Users\user\Desktop\probability and statistics analyzer for shop sales\Online Retail.xlsx"

def simulate_dice(rolls=1000):
    sample_space = [1, 2, 3, 4, 5, 6]
    count = 0
    for _ in range(rolls):
        if random.choice(sample_space >4):
            count += 1
    return count / rolls

def exact_probability(sample_space, event_rule):
    event = [x for x in sample_space if event_rule(x)]
    return len(event) / len(sample_space)