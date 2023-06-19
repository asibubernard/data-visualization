import matplotlib.pyplot as plt

# values
# cubic_numbers = [1, 8, 27, 64, 125]
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

# Plot
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues)

# Set chart title and label axes
plt.title("Cubic Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

# Save and show chart
plt.savefig('cubic_numbers_plot.png')

# Show chart
plt.show()
