"""Approximate pi using a Monte Carlo simulation."""
import random
from math import sqrt

def in_circle(x, y):
    """If point x, y inside circle of radius 1, return True."""
    return sqrt(x*x + y*y) <= 1

def approx_pi(iteration_power=6, seed=1):
    """
    Approximate pi

    Parameters
    ----------
    iteration_power : int
        Simulation will run (10 ** iteration_power) iterations.
    seed : int
        Random seed number.
    """
    iterations = 10 ** iteration_power
    inside_count = 0
    random.seed(seed)

    for ii in range(iterations):
        x = random.random()
        y = random.random()

        if in_circle(x, y):
            inside_count += 1

    pi = 4 * inside_count / iterations
    return pi
