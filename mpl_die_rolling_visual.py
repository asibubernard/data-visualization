from die import Die
import matplotlib.pyplot as plt


# Create a D6 and a D10
die = Die()

# Make some rolls, and store results in a list.
results = [die.roll() for roll_num in range(100)]
print("Results: ", results)

# Analyze results by counting how many times each number is rolled
frequencies = [results.count(value) for value in range(1, die.num_sizes+1)]

print('Frequencies', frequencies)



# plt.plot(results, frequencies, linewidth=5)

# Set chart title and label axes.
#plt.title("Rolling a Die 1000 times", fontsize=24)
#plt.xlabel("Results", fontsize=14)
#plt.ylabel("Frequencies of Results", fontsize=14)

# Set size of tick labels.
#plt.tick_params(axis='both', labelsize=14)

#plt.show()
