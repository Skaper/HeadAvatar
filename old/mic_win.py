# open a microphone in pyAudio and listen for taps
import serial
import pyaudio
import struct
import time, sys
#from win_unicode_console import streams
#streams.enable()

#import codecs
#sys.stdout = codecs.getwriter('cp1251')(sys.stdout,'replace')

import math
open_Mouth  	       = 'M>125'
close_Mouth 	       = 'M>45'
PORT                   = 'COM3'
BAUD_RATE              = 115200
PORT_ACTIVE            = False
SOUND_LEVEL            = 0.045

INITIAL_TAP_THRESHOLD  = 0.010
FORMAT                 = pyaudio.paInt16
SHORT_NORMALIZE        = (1.0/32768.0)
CHANNELS               = 2
RATE                   = 44100
INPUT_BLOCK_TIME       = 0.01
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)
try:
    port = serial.Serial(PORT, baudrate=BAUD_RATE, dsrdtr=1, timeout=3.0)
    PORT_ACTIVE = True
    print "OK COM3"
except:
    print "Not found " + PORT
    PORT_ACTIVE = False
    #time.sleep(5)

# if we get this many noisy blocks in a row, increase the threshold
OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME
# if we get this many quiet blocks in a row, decrease the threshold
UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME
# if the noise was longer than this many blocks, it's not a 'tap'
MAX_TAP_BLOCKS = 0.15/INPUT_BLOCK_TIME


def get_rms( block ):
    # RMS amplitude is defined as the square root of the
    # mean over time of the square of the amplitude.
    # so we need to convert this string of bytes into
    # a string of 16-bit samples...

    # we will get one short out for each
    # two chars in the string.
    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, block )

    # iterate over the block.
    sum_squares = 0.0
    for sample in shorts:
        # sample is a signed short in +/- 32768.
        # normalize it to 1.0
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt( sum_squares / count )

class TapTester(object):
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()
        self.tap_threshold = INITIAL_TAP_THRESHOLD
        self.noisycount = MAX_TAP_BLOCKS+1
        self.quietcount = 0
        self.errorcount = 0
        self.mouthIsOpen = 1

    def stop(self):
        self.stream.close()

    def find_input_device(self):
        device_index = None
        for i in range( self.pa.get_device_count() ):
            devinfo = self.pa.get_device_info_by_index(i)
            print( "Device %d: %s"%(i,devinfo["name"]) )

            for keyword in ["mic","input"]:
                if keyword in devinfo["name"].lower():
                    print( "Found an input: device %d - %s"%(i,devinfo["name"]) )
                    device_index = i
                    return device_index

        if device_index == None:
            print( "No preferred input found; using default input device." )

        return device_index

    def open_mic_stream( self ):
        device_index = self.find_input_device()

        stream = self.pa.open(   format = FORMAT,
                                 channels = CHANNELS,
                                 rate = RATE,
                                 input = True,
                                 input_device_index = device_index,
                                 frames_per_buffer = INPUT_FRAMES_PER_BLOCK)

        return stream

    def tapDetected(self):
        print "Tap!"

    def listen(self):
        try:
            block = self.stream.read(INPUT_FRAMES_PER_BLOCK)
        except IOError, e:
            # dammit.
            self.errorcount += 1
            print( "(%d) Error recording: %s"%(self.errorcount,e) )
            self.noisycount = 1
            return

        amplitude = get_rms( block )
        #print amplitude
        if amplitude > SOUND_LEVEL:
            #print amplitude
            if not self.mouthIsOpen:
                if PORT_ACTIVE:
                    port.write(open_Mouth + '\n')
                    self.mouthIsOpen = 1
                    print self.mouthIsOpen
        else:
            if self.mouthIsOpen:
                if PORT_ACTIVE:
                    port.write(close_Mouth + '\n')
                    self.mouthIsOpen = 0
                    print self.mouthIsOpen

if __name__ == "__main__":
    tt = TapTester()
    #a = raw_input("Please Enter to start! ")
    if PORT_ACTIVE:
        while 1:
            tt.listen()
    else:
        print "Not connect to robot! Check COM3! Exit."
