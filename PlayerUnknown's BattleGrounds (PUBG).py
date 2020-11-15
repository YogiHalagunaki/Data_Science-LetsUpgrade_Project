# created by : Yogi Halagunaki
#
# Project Name : PUBG


import matplotlib.pyplot as plt
# all import lib is here
import pandas as pd
import seaborn as sb
import pytest
# task 1

pubg_data = pd.read_csv('pubg.csv')
print(pubg_data)
print()
# task 2
data_type = pubg_data.dtypes
print(data_type)
print()

# task 3
summary = pubg_data.describe()
print(summary)
print()

# task 4
average_person = pubg_data['kills'].mean()
print(F"Average {average_person} people kills")
print()
# task 5
how_many_kills = pubg_data['kills'].quantile(0.99)
print(F"99% people have {how_many_kills} kills")
print()

# task 6
most_kills = pubg_data['kills'].max()
print(F"{most_kills} most kills ever recorded.")
print()

# task 7
print(pubg_data.columns)
print()

# task 8
data_graph = (sb.distplot(pubg_data['matchDuration']))
print(plt.show())
data_graph_max_duration = (sb.distplot(pubg_data['matchDuration'].abs()))
print(data_graph_max_duration)

# print("Match duration high during 1250 to 1500 mostly.")
print()

# task 9

data_graph1 = sb.distplot(pubg_data['walkDistance'])
plt.show()

# task 10
# %matplotlib inline
plt.style.use('classic')
plt.figure()

plt.subplot(2, 1, 1)
plt.plot(pubg_data['matchDuration'], '-')
plt.xlabel("Match Duration")

plt.subplot(2, 1, 2)
plt.plot(pubg_data['walkDistance'], '--')
plt.xlabel("walkDistance")

plt.show()

print()

# task 11

plt.style.use('classic')
plt.figure()

plt.subplot(1, 2, 1)
plt.plot(pubg_data['matchDuration'], '-')
plt.xlabel("Match Duration")

plt.subplot(1, 2, 2)
plt.plot(pubg_data['walkDistance'])
plt.xlabel("walkDistance")
plt.show()
print()
#
# # task 12
# sb.pairplot(pubg_data, hue='maxPlace', palette='numGroups')
# plt.show()    # not exe
# print("12")

# task 13
unique_values = pd.unique(pubg_data["matchType"]);
print(F"unique value of match type is :{unique_values}");
l_uni = len(unique_values)
print(l_uni)
print(F"Count of unique value in matchType is  :{l_uni}")
print()

# task 14

sb.barplot(pubg_data['matchType'], pubg_data['killPoints']);
plt.show()
sb.barplot(pubg_data['matchType'],pubg_data['weaponsAcquired']);
# task 15
sb.barplot(pubg_data['matchType'],pubg_data['weaponsAcquired']);
plt.show()
print()

# task 16

Categorical_columns = pubg_data.select_dtypes('category').columns
print(Categorical_columns)
print()

# Task 17
sb.boxplot(x='matchType', y='winPlacePerc', data=pubg_data);
plt.show()
print()

# Task 18
sb.boxplot(x='matchType', y='matchDuration', data=pubg_data);
plt.show()
print()

# task 19
sb.boxplot(x='matchDuration', y='matchType', data=pubg_data);
plt.show()
print()

# Task 20
pubg_data['KILL'] = pubg_data['headshotKills'] + pubg_data['teamKills'] + pubg_data['roadKills']
print("KILL :", pubg_data['KILL'])

# task 21
print("winPlacePerc :", pubg_data['winPlacePerc'].round(decimals=2));
print()

# Task 22
mean = []
for i in range(100):
    for j in range(0, 1000, 50):
        temp = pubg_data['damageDealt'].head(j).mean()
        mean.append(temp)

sb.distplot(x=mean)
plt.show()


# Output :
# /home/yogi/Desktop/Python_Code/venv/bin/python "/home/yogi/Desktop/Python_Code/Lets_Upgrade_Assignments/Project/PlayerUnknown's BattleGrounds (PUBG).py"
#                   Id         groupId  ... winPoints  winPlacePerc
# 0     2f262dd9795e60  78437bcd91d40e  ...      1470        0.0000
# 1     a32847cf5bf34b  85b7ce5a12e10b  ...      1531        0.2222
# 2     1b1900a9990396  edf80d6523380a  ...         0        0.8571
# 3     f589dd03b60bf2  804ab5e5585558  ...         0        0.3462
# 4     c23c4cc5b78b35  b3e2cd169ed920  ...      1557        0.0690
# ...              ...             ...  ...       ...           ...
# 9995  ef4f474acd8e85  2eca2a8391f75d  ...      1471        0.8333
# 9996  cf0bf82fb4d80e  2eaf2765f93adb  ...      1500        0.7174
# 9997  a0a31a0b1dcbe1  8d50c64ccc5071  ...      1434        0.2083
# 9998  f6874657399d69  d31843d7e62ccb  ...      1534        0.2449
# 9999  90359b0b8f8b0d  61d5b1bb8da43f  ...         0        0.1875
#
# [10000 rows x 29 columns]
#
# Id                  object
# groupId             object
# matchId             object
# assists              int64
# boosts               int64
# damageDealt        float64
# DBNOs                int64
# headshotKills        int64
# heals                int64
# killPlace            int64
# killPoints           int64
# kills                int64
# killStreaks          int64
# longestKill        float64
# matchDuration        int64
# matchType           object
# maxPlace             int64
# numGroups            int64
# rankPoints           int64
# revives              int64
# rideDistance       float64
# roadKills            int64
# swimDistance       float64
# teamKills            int64
# vehicleDestroys      int64
# walkDistance       float64
# weaponsAcquired      int64
# winPoints            int64
# winPlacePerc       float64
# dtype: object
#
#             assists        boosts  ...   winPoints  winPlacePerc
# count  10000.000000  10000.000000  ...  10000.0000  10000.000000
# mean       0.234600      1.088500  ...    609.3440      0.469926
# std        0.575149      1.703279  ...    739.7924      0.304508
# min        0.000000      0.000000  ...      0.0000      0.000000
# 25%        0.000000      0.000000  ...      0.0000      0.200000
# 50%        0.000000      0.000000  ...      0.0000      0.458300
# 75%        0.000000      2.000000  ...   1495.0000      0.735100
# max        7.000000     18.000000  ...   1863.0000      1.000000
#
# [8 rows x 25 columns]
#
# Average 0.9134 people kills
#
# 99% people have 7.0 kills
#
# 35 most kills ever recorded.
#
# Index(['Id', 'groupId', 'matchId', 'assists', 'boosts', 'damageDealt', 'DBNOs',
#        'headshotKills', 'heals', 'killPlace', 'killPoints', 'kills',
#        'killStreaks', 'longestKill', 'matchDuration', 'matchType', 'maxPlace',
#        'numGroups', 'rankPoints', 'revives', 'rideDistance', 'roadKills',
#        'swimDistance', 'teamKills', 'vehicleDestroys', 'walkDistance',
#        'weaponsAcquired', 'winPoints', 'winPlacePerc'],
#       dtype='object')
#   warnings.warn(msg, FutureWarning)
# None
# /home/yogi/Desktop/Python_Code/venv/lib/python3.7/site-packages/seaborn/distributions.py:2551: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).
#   warnings.warn(msg, FutureWarning)
# /home/yogi/Desktop/Python_Code/venv/lib/python3.7/site-packages/seaborn/distributions.py:2551: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).
#   warnings.warn(msg, FutureWarning)
# AxesSubplot(0.125,0.11;0.775x0.77)
#
#
# /home/yogi/Desktop/Python_Code/venv/lib/python3.7/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
#   FutureWarning
#
# unique value of match type is :['squad-fpp' 'squad' 'duo-fpp' 'solo-fpp' 'duo' 'solo' 'crashfpp'
#  'flaretpp' 'normal-squad-fpp' 'normal-duo-fpp' 'flarefpp' 'normal-squad'
#  'normal-solo-fpp' 'crashtpp']
# 14
# Count of unique value in matchType is  :14
#
# /home/yogi/Desktop/Python_Code/venv/lib/python3.7/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
#   FutureWarning
# /home/yogi/Desktop/Python_Code/venv/lib/python3.7/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
#   FutureWarning
#
# Index([], dtype='object')
#
#
#
#
# KILL : 0       0
# 1       1
# 2       1
# 3       0
# 4       0
#        ..
# 9995    0
# 9996    0
# 9997    0
# 9998    0
# 9999    0
# Name: KILL, Length: 10000, dtype: int64
# winPlacePerc : 0       0.00
# 1       0.22
# 2       0.86
# 3       0.35
# 4       0.07
#         ...
# 9995    0.83
# 9996    0.72
# 9997    0.21
# 9998    0.24
# 9999    0.19
# Name: winPlacePerc, Length: 10000, dtype: float64
#
# /home/yogi/Desktop/Python_Code/venv/lib/python3.7/site-packages/seaborn/distributions.py:2551: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).
#   warnings.warn(msg, FutureWarning)
#
# Process finished with exit code 0
