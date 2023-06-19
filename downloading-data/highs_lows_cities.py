import csv
from datetime import datetime

from matplotlib import pyplot as plt


# Get high temperatures from file
filename_one = 'death_valley_2014.csv'
filename_two = 'sitka_weather_2014.csv'
with open(filename_one) as f:
    reader_one = csv.reader(f)
    header_row_one = next(reader_one)

    dates_one, highs_one, lows_one = [], [],[]
    for row in reader_one:
        try:
            current_date_one = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[1])
        except  ValueError:
            print(current_date_one, "missing data in first file.")
        else:
            dates_one.append(current_date_one)
            highs_one.append(high)
            lows_one.append(high)


with open(filename_two) as g:
    reader_two = csv.reader(g)
    header_row_two = next(reader_two)

    dates_two, highs_two, lows_two = [], [], []
    for row in reader_two:
        try:
            current_date_two = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[2])
        except  ValueError:
            print(high, "missing data for second file.")
        else:
            dates_two.append(current_date_two)
            highs_two.append(high)
            lows_two.append(low)


# # Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))

# Data from Death Valley
plt.plot(dates_one, highs_one, c='red', alpha=0.5)
plt.plot(dates_one, lows_one, c='blue', alpha=0.5)
plt.fill_between(dates_one, highs_one, lows_one, facecolor='blue', alpha=0.1)

# Plot data from Sitka
plt.plot(dates_two, highs_two, c='red', alpha=0.5)
plt.plot(dates_two, lows_two, c='blue', alpha=0.5)
plt.fill_between(dates_two, highs_two, lows_two, facecolor='blue', alpha=0.1)


# # Format plot.
title = "Comparison of Daily high and low temperatures between \nDeath Valley and Sitka."
plt.title(title, fontsize=24)
plt.xlabel('Dates', fontsize=16)
fig.autofmt_xdate()  # this makes the date diagonally aligned.
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
