import turtle
import random
import matplotlib.pyplot as plt
import numpy as np


win = turtle.Screen()
win.screensize(10000, 10000)
win.bgcolor("light blue")
win.title("Sine Wave")

bob = turtle.Turtle()
turtle.speed(0)

# A Wave!
A_x_data = np.linspace(0, 0.01, 1000)
A_y_data = np.sin(np.pi * 880 * A_x_data)

# C# Wave!
Cs_x_data = np.linspace(0, 0.01, 1000)
Cs_y_data = np.sin(np.pi * 1100 * Cs_x_data)

# E Wave!
E_x_data = np.linspace(0, 0.01, 1000)
E_y_data = np.sin(np.pi * 1320 * E_x_data)

# A-C#-E Chord Wave
chord_x_data = np.linspace(0, 0.1, 10000)
chord_y_data = np.sin(np.pi * 880 * chord_x_data) + np.sin(np.pi * 1100 * chord_x_data) + np.sin(np.pi * 1320 * chord_x_data)

#
# GRAPHING OF THE WAVE
#
Xvals = chord_x_data
Yvals = [np.abs((i) * 360) for i in chord_y_data]

for i in Yvals:
    turtle.setheading(np.abs(i) * 360)
    turtle.forward(8)


turtle.hideturtle()
turtle.done()

