import wave 
import pylab as pl
import numpy as np
import os

file = wave.open(r"/Users/heamon7/Project/Python/learnPySci/ding.wav","rb")

# read the format
# (nchannels,sampwidth,framerate,nframes,comptype,compname)
params = file.getparams()
nchannels,sampwidth,framerate,nframes = params[:4]

print "[DEBUG]params: "  
print params

# read the wave data
str_data = file.readframes(nframes)
file.close()

# transform the data to array
wave_data = np.fromstring(str_data,dtype=np.short)
wave_data.shape = (-1,2)
wave_data = wave_data.T
time = np.arange(0,nframes)*(1.0/framerate)    #the time of the audio

# plot the wave
pl.subplot(211)
pl.plot(time,wave_data[0])
pl.subplot(212)
pl.plot(time,wave_data[1],c="g")
pl.xlabel("time(seconds)")
pl.show()



