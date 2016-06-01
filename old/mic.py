import alsaaudio, time, audioop, serial, socket
from threading import Thread
open_Mouth  	=	 'M>170'
close_Mouth 	= 	 'M>45'
sound_Level 	=  	  600
port			= 	  5003
connection		=     False
if connection:
	sock = socket.socket()
	sock.connect(('192.168.1.50', port)) #6526
else:
	port = serial.Serial("/dev/ttyACM0", baudrate=115200, dsrdtr=1, timeout=3.0)

# Open the device in nonblocking capture mode. The last argument could
# just as well have been zero for blocking mode. Then we could have
# left out the sleep call in the bottom of the loop 32734 port.write('S|D11>70'+'\n')
alsaaudio.cards()
card = 'sysdefault:CARD=Device'
inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)

# Set attributes: Mono, 8000 Hz, 16 bit little endian samples
inp.setchannels(1)
inp.setrate(16000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)


# The period size controls the internal number of frames per period.
# The significance of this parameter is documented in the ALSA api.
# For our purposes, it is suficcient to know that reads from the device
# will return this many frames. Each frame being 2 bytes long.
# This means that the reads below will return either 320 bytes of data
# or 0 bytes of data. The latter is possible because we are in nonblocking
# mode.
inp.setperiodsize(160)
timer= time.time()
#port.write("S|D10>70"+"\n")
mouth=0
oldLevel = 6500


while True:
	while True:
		# Read data from device
		l,data = inp.read()
		if l:
			level = audioop.max(data, 2)
		# Return the maximum of the absolute value of all samples in a fragment.
		#print level

			if level > sound_Level:
				print level
				#if time.time()-timer>0.01:

				timer= time.time()
				if not mouth:
					#port.write('S|D10>89'+'\n')
					print mouth
					mouth = 1
					try:
						#port.write('M>89' + '\n')
						if connection:
							sock.send(open_Mouth+ '\n')
						else:
							port.write('M>100' + '\n')
					except:
						pass
					'''
					if math.fabs(oldLevel - level) > 5000:
						#port.write('S|D10>89' + '\n')
						port.write('M>89' + '\n')
					else:
						#port.write('S|D10>29' + '\n')
						port.write('M>29' + '\n')
					oldLevel = level
					'''

			elif level < sound_Level:
				#if time.time()-timer>0.01:
				timer= time.time()
				if mouth:

					try:
						# port.write('S|D10>29'+'\n')
						if connection:
							sock.send(close_Mouth + '\n')
						else:
							port.write('M45' + '\n')
					except:
						pass

					print mouth
					mouth = 0
			#time.sleep(.01)
