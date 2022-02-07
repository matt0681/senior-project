import scipy
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import write
from scipy.fft import fft, fftfreq, rfft, rfftfreq


SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # Seconds

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

## Generate a 2 hertz sine wave that lasts for 5 seconds
# x, y = generate_sine_wave(2, SAMPLE_RATE, DURATION)
# plt.plot(x, y)
# plt.show()


## Generates two sounds (y-vals only) of a normal pitch and a high pitch tone
## the noise is the high pitch sound
## The noise sound is lowered in power and combined with the normal sound.
_, nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION)
_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
noise_tone = noise_tone * 0.3
mixed_tone = nice_tone + noise_tone

## Most audio files need the audio in a 16-bit integer
## This command scales the audio bits to be between -1 and 1 (kinda like a percentage)
# It then scales it up to between exactly -32768 to 32767 for the int16 format.
normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

## Plotting our new sound (only the first 1000 x-values, or 'samples' are shown)
# plt.plot(normalized_tone[:1000])
# plt.show()

## If we want to hear our sound, we can store it in a .wav file.
# write("mysinewave.wav", SAMPLE_RATE, normalized_tone)
## If you play it back and listen carefully you should hear two sounds on top of eachother.
## One high and one medium/low.


## The FFT is an algorithm which uses the DFT method. The DFT takes a signal from the time
## domain and decomposes it into the frequency domain.

## The number of samples in the normalized_tone
NUM_SAMPLES = SAMPLE_RATE * DURATION

## fft - calculates the fourier transform itself using the values from the normalized_tone
## fftfreq - calculates the frequencies of each "bin" in the output of fft
y_f = rfft(normalized_tone)
x_f = rfftfreq(NUM_SAMPLES, 1 / SAMPLE_RATE)

print(len(y_f))
## This plots the new fourier transform.
plt.plot(x_f, np.abs(y_f))
plt.show()

