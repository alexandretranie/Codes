import numpy as np
import random as rd
import matplotlib.pyplot as plt


def estimate_pi_monte_carlo(num_samples=10000):
    inside_circle = 0
    for _ in range(num_samples):
        x, y = rd.uniform(-1, 1), rd.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_estimate = (inside_circle / num_samples) * 4
    print(f"Estimated π: {pi_estimate}")
    return pi_estimate


# Graphic representation of the Monte Carlo simulation
def plot_circle(num_samples=10000):
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []
    for _ in range(num_samples):
        x, y = rd.uniform(-1, 1), rd.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)
    circle = plt.Circle((0, 0), 1, color='black', fill=False)
    plt.scatter(x_inside, y_inside, color='blue', s=1)
    plt.scatter(x_outside, y_outside, color='red', s=1)
    plt.gca().add_artist(circle)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Monte Carlo Simulation of π\nSamples: {num_samples}")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()


# Plot of the error depending on the number of samples in MC method
def error_plot():
    true_value = np.pi
    sample_sizes = [10, 100, 500, 1000, 5000, 10000, 50000, 100000, 1000000]
    errors = []

    for n in sample_sizes:
        est_pi = estimate_pi_monte_carlo(n)
        err = abs(true_value - est_pi)
        errors.append(err)

    plt.figure()
    plt.plot(sample_sizes, errors, 'ro-')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Number of Samples")
    plt.ylabel("Absolute Error")
    plt.title("Error in π Estimation (Monte Carlo)")
    plt.grid(True, which="both")
    plt.show()



if __name__ == "__main__":
    estimate_pi_monte_carlo()
    plot_circle()
    error_plot()
