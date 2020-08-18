import pyaudio
import numpy as np

p = pyaudio.PyAudio()

volume = 0.25
fs = 44100
duration = 2
f = 1000.0

samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

stream.write(volume*samples)

stream.stop_stream()
stream.close()

p.terminate()
