import numpy as np
from scipy.integrate import simpson, trapezoid

def interpolation_lagrange(x_points, y_points, x):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

def integration_trapeze(x, y):
    return trapezoid(y, x)

def integration_simpson(x, y):
    return simpson(y, x)

def euler_explicite(f, x0, y0, h, n):
    x = x0
    y = y0
    for i in range(n):
        y += h * f(x, y)
        x += h
    return y