from distutils.core import setup
import py2exe

setup(
    windows=[{"script": "program.py"}],
    options={
        "py2exe": {"includes": ["sip", "pyaudio", "form", "sys", "PyQt4", "serial", "struct", "math"],
                   "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"]}
             },

    zipfile=None

)