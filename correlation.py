#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#THE FOLLOWING CODE IS FROM THE DATA SCIENCE TEXTBOOK! ONLY MODITFIED TO TAKE IN MY DATA!! O
"""
Created on Mon May  8 19:07:17 2017

@author: derianescobar
"""
import numpy as np
import matplotlib.pyplot as plt

pRate = np.array(
    [0.005974363201714615, 0.005593970800628325, 0.003170951036709823, 0.004302911587395166, 0.0037330756383727403])
tRate = np.array(
    [0.0036648531310966397, 0.5060764089566804, 0.0025443045896065843, 0.01790464598824715, 0.002493618898564121])


def compute_error_for_line_given_points(b, m, pointsx, pointsy):
    totalError = 0
    for i in range(0, len(pointsx)):
        x = pointsx[i]
        y = pointsy[i]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(pointsx))


def step_gradient(b_current, m_current, pointsx, pointsy, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(pointsx))
    for i in range(0, len(pointsx)):
        x = pointsx[i]
        y = pointsy[i]
        b_gradient += -(2 / N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2 / N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]


def gradient_descent_runner(pointsx, pointsy, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, pointsx, pointsy, learning_rate)
    return [b, m]


def run():
    pointsx = pRate
    pointsy = tRate
    learning_rate = 0.0001
    initial_b = 0  # initial y-intercept guess
    initial_m = 0  # initial slope guess
    num_iterations = 1000
    print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m,
                                                                              compute_error_for_line_given_points(
                                                                                  initial_b, initial_m, pointsx,
                                                                                  pointsy)))
    print("Running...")
    [b, m] = gradient_descent_runner(pointsx, pointsy, initial_b, initial_m, learning_rate, num_iterations)
    print("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m,
                                                                      compute_error_for_line_given_points(b, m, pointsx,
                                                                                                          pointsy)))
    plt.scatter(pRate, tRate)
    m, b = np.polyfit(pointsx, pointsy, 1)

    plt.plot(pointsx, m * pointsx + b)
    plt.xlabel("Crime Rate")
    plt.ylabel("Taxi Rate")
    plt.title("Line of best fit for Crime with Taxis")
    plt.show()


if __name__ == '__main__':
    run()
