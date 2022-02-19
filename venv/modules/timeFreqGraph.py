import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
import time

# matplotlib tk

CHUNK = 1024 * 4           # How many audio samples per frame to display
FORMAT = pyaudio.paInt16   # bytes per sample
CHANNELS = 1               # monosound
RATE = 44100               # samples per second (Hz)

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

fig, ax = plt.subplots()

x = np.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, np.random.rand(CHUNK))

ax.set_ylim(-150, 150)
ax.set_xlim(0, CHUNK)
plt.show(block=False)

tstart = time.time()
num_plots = 0
while time.time()-tstart < 20:
    data = stream.read(CHUNK)
    data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype='b')[::2] + 127
    line.set_ydata(data_int)
    fig.canvas.draw()
    fig.canvas.flush_events()

