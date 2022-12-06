import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
from numpy.random import randn
import random
import matplotlib.pyplot as plt
import random

DATA_LIMIT = 200

horse1 = (abs(randn(DATA_LIMIT) + randn(1) + 2) * 10).cumsum()
horse2 = (abs(randn(DATA_LIMIT) + randn(1)) * 10).cumsum()
horse3 = (abs(randn(DATA_LIMIT) + randn(1)) * 10).cumsum()
horse4 = (abs(randn(DATA_LIMIT) + randn(1)) * 10).cumsum()
horse5 = (abs(randn(DATA_LIMIT) + randn(1)) * 10).cumsum()
horse6 = (abs(randn(DATA_LIMIT) + randn(1)) * 10).cumsum()
horse7 = (abs(randn(DATA_LIMIT) + randn(1)) * 10).cumsum()
horse8 = (abs(randn(DATA_LIMIT) + randn(1)) * 10).cumsum()

horse1_record = []
horse2_record = []
horse3_record = []
horse4_record = []
horse5_record = []
horse6_record = []
horse7_record = []
horse8_record = []

is_break = False
for index in range(DATA_LIMIT):
    horse1_record.append(horse1[index])
    horse2_record.append(horse2[index])
    horse3_record.append(horse3[index])
    horse4_record.append(horse4[index])
    horse5_record.append(horse5[index])
    horse6_record.append(horse6[index])
    horse7_record.append(horse7[index])
    horse8_record.append(horse8[index])

    if is_break == True:
        break
    else:
        pass
    if horse1[index] > 1000:
        print(f'라이스샤워 우승 기록: {index}초')
        print(horse1[index])
        is_break = True
    if horse2[index] > 1000:
        print(f'티엠오페라오 우승 기록: {index}초')
        print(horse2[index])
        is_break = True
    if horse3[index] > 1000:
        print(f'보드카 우승 기록: {index}초')
        print(horse2[index])
        is_break = True
    if horse4[index] > 1000:
        print(f'에어그루브 우승 기록: {index}초')
        print(horse4[index])
        is_break = True
    if horse5[index] > 1000:
        print(f'엘콘돌파사 우승 기록: {index}초')
        print(horse4[index])
        is_break = True
    if horse6[index] > 1000:
        print(f'스페셜위크 우승 기록: {index}초')
        print(horse4[index])
        is_break = True
    if horse7[index] > 1000:
        print(f'골드쉽 우승 기록: {index}초')
        print(horse4[index])
        is_break = True
    if horse8[index] > 1000:
        print(f'위닝티켓 우승 기록: {index}초')
        print(horse4[index])
        is_break = True