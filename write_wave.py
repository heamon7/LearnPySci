import wave
import numpy as np
import scipy.signal as signal
import pylab as pl

framerate = 44100
time = 10

# produce 10s 100Hz~1kHz wave of the frequency of 44.1kHz
t = np.arange(0,time,1.0/framerate)
wave_data = signal.chirp(t,100,time,1000,method='linear')*10000
wave_data = wave_data.astype(np.short)

file = wave.open(r"sweep.wav","wb")

# configure the channels,sampwidth,framerate
file.setnchannels(1)
file.setsampwidth(2)
file.setframerate(framerate)

# transform the wave)data to binary data and write it to the file
file.writeframes(wave_data.tostring())
file.close()

# plot the wave
pl.plot(t[::framerate/100],wave_data[::framerate/100])
# pl.xlabel("time(seconds)")
pl.show()