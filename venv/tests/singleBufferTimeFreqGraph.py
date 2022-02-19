import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
import time



# Various needed Variables
SAMPLES_PER_FRAME = 4096     # How many audio samples per frame to display
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

# Reads in SAMPLES_PER_FRAME amount of microphone input data.
mic_in_data = stream.read(SAMPLES_PER_FRAME)
print(f"input data: {mic_in_data}")

# This section of code takes the input data and formats it so it can be plotted.
# It takes data in in a binary format and converts it to integers spaced every 2 x_vals
# formatted_data = np.array(struct.unpack(str(SAMPLES_PER_FRAME * 2) + 'B', mic_in_data), dtype= 'b')[::2] + 127
formatted_data = np.frombuffer(mic_in_data, dtype= np.int16)
print(f"formated data: {formatted_data}")

fig, ax = plt.subplots()
ax.plot(formatted_data, '-')
ax.set_ylim(-512, 512)
ax.set_xlim(-10, SAMPLES_PER_FRAME)
plt.show()

