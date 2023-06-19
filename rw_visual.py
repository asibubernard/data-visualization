import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(5000)
    rw.fill_walk()
   
    # set the size of the plotting window
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=5)
    
    # Emphasize the first and last points.
    plt.plot(0, 0, c='green')
    plt.plot(rw.x_values[-1], rw.y_values[-1])

    # Remove the axes.
    plt.axis('off')

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break


