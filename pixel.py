import pyautogui as pag
import pyaudio
import numpy as np

while True:
    sc = pag.screenshot()
    px = sc.getpixel(xy=(400, 400))
    sound = ((px[0] + px[1] + px[2])/3)*4

    p = pyaudio.PyAudio()

    volume = 0.1
    fs = 44100
    duration = 1
    f = sound

    samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    stream.write(volume * samples)

    stream.stop_stream()
    stream.close()

    p.terminate()
