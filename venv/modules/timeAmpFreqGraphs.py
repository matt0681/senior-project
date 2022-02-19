# Necessary Imports
import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.fftpack import fft

# https://www.youtube.com/watch?v=RHmTgapLu4s

"""
This file creates a window which displays two graphs. After reading input from the microphone, the first graph
displays the time/amplitude of the input audio signal. The seconf graph shows the time/frequency of the signal.
"""

# Variables
SAMPLES_PER_FRAME = 2048        # How many audio samples per frame to display
AUDIO_FORMAT = pyaudio.paInt16  # bytes per sample
CHANNELS = 1    # monosound
RATE = 44100    # samples per second (Hz)
Y_MAX = 10000
Y_MIN = -10000


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
fig, (axAmp, axFreq) = plt.subplots(2, figsize= (15, 8))


# Creates a range of x values for the time/amplitude graph.
# The values are every even number from 0 to two times the samples per frame.
# Ex. [0, 2, 4, 6, 8, ..., 4094] when SamplesPerFrame=2048
x_vals = np.arange(0, SAMPLES_PER_FRAME * 2, 2)
x_fft = np.linspace(0, RATE, SAMPLES_PER_FRAME)


# This graphs the x_vals and for the y values it takes a random number between 0 and 1.
# We will change the y values later on in the code.
# np.random.rand() creates a list of the same size as SAMPLES_PER_FRAME where each element
# is a random number between 0 and 1.
line, = axAmp.plot(x_vals, np.random.rand(SAMPLES_PER_FRAME), '-', lw= 2)
line_fft, = axFreq.semilogx(x_fft, np.random.rand(SAMPLES_PER_FRAME), '-', lw= 2)


axAmp.set_title("Audio Input Time/ Amplitude Graph")
axAmp.set_xlabel("Time (Samples)")
axAmp.set_ylabel("Amplitude")
axAmp.set_ylim(Y_MIN, Y_MAX)
axAmp.set_xlim(-10, SAMPLES_PER_FRAME)

axFreq.set_ylim(0, 1)
axFreq.set_xlim(10, 10000)

plt.show(block=False)


frame_count = 0
start_time = time.time()
while True:

    mic_in_data = stream.read(SAMPLES_PER_FRAME)

    formatted_data = np.frombuffer(mic_in_data, dtype= np.int16)

    # Updates the y values of our graph with the newly formatted data.
    # Draws the graph to the screen.
    line.set_ydata(formatted_data)

    y_fft = fft(formatted_data)
    line_fft.set_ydata(np.abs(y_fft[0:SAMPLES_PER_FRAME]) * 2 / (2000 * SAMPLES_PER_FRAME))

    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
        frame_count += 1
    except TclError:
        frame_rate = frame_count / (time.time() - start_time)
        print("average frame rate = {:.0f} FPS".format(frame_rate))
        break


# Ends the stream.
stream.stop_stream()
stream.close()
pyAudio.terminate()
print("Exited Successfully")
