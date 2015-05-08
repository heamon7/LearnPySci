from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,10,500,endpoint=False)
# sig = [0.7,0.3]*(len(t)/2)
plt.plot(t,signal.square(2 * np.pi * 1 * t))
plt.ylim(-2,2)
plt.xlim(0,10)
plt.show()