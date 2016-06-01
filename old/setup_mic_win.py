from distutils.core import setup
import py2exe

setup(
    console=['mic_win.py'],
    #windows=[{"script":"mic_win.py"}],
    options={"py2exe": {"includes":["sip","serial","pyaudio","struct", "time", "sys", "math"]}},
    zipfile=None

)