import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
import time



# Various needed Variables
SAMPLES_PER_FRAME = 4096        # How many audio samples per frame to display
AUDIO_FORMAT = pyaudio.paInt16  # bytes per sample
CHANNELS = 1    # monosound
RATE = 44100    # samples per second (Hz)


# Creates an instance of PyAudio
pyAudio = pyaudio.PyAudio()


# Creates and starts a stream for reading input from the microphone and creating buffers for output.
stream = pyAudio.open(
    format= AUDIO_FORMAT,
    channels= CHANNELS,
    rate= RATE,
    input= True,
    output= True,
    frames_per_buffer= SAMPLES_PER_FRAME
)


# Creates a graph to plot the microphone input onto.
fig, ax = plt.subplots()


# Creates a range of x values for the time/amplitude graph.
# The values are every even number from 0 to two times the samples per frame.
# Ex. [0, 2, 4, 6, 8, ..., 4094] when SamplesPerFrame=2048
x_vals = np.arange(0, SAMPLES_PER_FRAME * 2, 2)


# This graphs the x_vals and for the y values it takes a random number between 0 and 1.
# We will change the y values later on in the code.
# np.random.rand() creates a list of the same size as SAMPLES_PER_FRAME where each element
# is a random number between 0 and 1.
line, = ax.plot(x_vals, np.random.rand(SAMPLES_PER_FRAME))


# Sets the x and y range of the graph and shows the plot.
ax.set_ylim(-512, 512)
ax.set_xlim(-10, SAMPLES_PER_FRAME)
plt.show(block=False)


# Starts the real-time plotting of the microphone's input.
# Only stops when graph window is exited.
while True:
    # Reads in SAMPLES_PER_FRAME amount of microphone input data.
    mic_in_data = stream.read(SAMPLES_PER_FRAME)

    # This section of code takes the input data and formats it so it can be plotted.
    # It takes data in in a binary format and converts it to integers spaced every 2 x_vals
    formatted_data = np.frombuffer(mic_in_data, dtype= np.int16)

    # Updates the y values of our graph with the newly formatted data.
    # Draws the graph to the screen.
    line.set_ydata(formatted_data)
    fig.canvas.draw()
    fig.canvas.flush_events()


# Ends the stream.
stream.stop_stream()
stream.close()
pyAudio.terminate()
print("Exited Successfully")
