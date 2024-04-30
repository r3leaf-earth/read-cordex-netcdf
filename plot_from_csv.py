import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#dataframe = pd.read_csv("out/hostrada.txt", sep=";")
#dataframe = pd.read_csv("out/try.csv", sep=";", header=None, names=["time", "temperature"])
dataframe = pd.read_csv("out/try.csv", sep=";", header=None, names=["time", "temperature_year",
                                                                    "temperature_summer", "temperature_winter"])
print(dataframe)


# dataframe.plot(kind='line',
#                x='time',
#                y='temperature',
#                lw=1
#                )
# plt.title('Hostrada 2023, Loebauer 46')

dataframe.plot(kind='line',
               x='time',
               y=["temperature_year",
                  "temperature_summer",
                  "temperature_winter"],
               color=['pink','red', 'blue'],
               lw=1
               )
plt.title('TRY 2045, Loebauer 46')

plt.axhline(20, color='blue', lw=0.5)
plt.axhline(30, color='red', lw=0.5)
plt.axvline(2190, color='lightgray', lw=1)
plt.axvline(4380, color='lightgray', lw=0.5)
plt.axvline(6570, color='lightgray', lw=0.5)
plt.ylabel('Temperature [°C]')
plt.xlabel('Date and Time [mm-dd-hh]')
plt.minorticks_on()
# plt.grid(True)

plt.show()

# with open("out/test.txt", 'a') as outfile:
#    outfile.write("test")
#
#
# x = np.arange(0, 31, 1/24)
# y = np.arange(0, 31, 1/24)
#
# plot = plt.plot(x, y)
# fig = plt.figure()

# plt.show()