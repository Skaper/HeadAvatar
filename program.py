import sys, pyaudio, serial, struct, math
from PyQt4 import QtCore, QtGui
from form import Ui_MainWindow
import glob
open_Mouth  	       = 'M>125'
close_Mouth 	       = 'M>45'
PORT                   = 'COM6'
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
# if we get this many noisy blocks in a row, increase the threshold
OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME
# if we get this many quiet blocks in a row, decrease the threshold
UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME
# if the noise was longer than this many blocks, it's not a 'tap'
MAX_TAP_BLOCKS = 0.15/INPUT_BLOCK_TIME

port = ''
'''
try:
    port = serial.Serial(PORT, baudrate=BAUD_RATE, dsrdtr=1, timeout=3.0)
    PORT_ACTIVE = True
    print "OK COM3"
except:
    print "Not found " + PORT
    PORT_ACTIVE = False
    #time.sleep(5)
'''

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

class MicListen(QtCore.QThread):
    #arrayImg = QtCore.pyqtSignal(QtCore.QImage)#np.ndarray)
    def __init__(self):
        QtCore.QThread.__init__(self)
        print "Start MicListen"
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()
        self.tap_threshold = INITIAL_TAP_THRESHOLD
        self.noisycount = MAX_TAP_BLOCKS + 1
        self.quietcount = 0
        self.errorcount = 0
        self.mouthIsOpen = 1

    def stop(self):
        self.stream.close()

    def find_input_device(self):
        device_index = None
        for i in range(self.pa.get_device_count()):
            devinfo = self.pa.get_device_info_by_index(i)
            print("Device %d: %s" % (i, devinfo["name"]))

            for keyword in ["mic", "input"]:
                if keyword in devinfo["name"].lower():
                    print("Found an input: device %d - %s" % (i, devinfo["name"]))
                    device_index = i
                    return device_index

        if device_index == None:
            print("No preferred input found; using default input device.")

        return device_index

    def open_mic_stream(self):
        device_index = self.find_input_device()

        stream = self.pa.open(format=FORMAT,
                              channels=CHANNELS,
                              rate=RATE,
                              input=True,
                              input_device_index=device_index,
                              frames_per_buffer=INPUT_FRAMES_PER_BLOCK)

        return stream

    def tapDetected(self):
        print "Tap!"

    def listen(self):
        try:
            block = self.stream.read(INPUT_FRAMES_PER_BLOCK)
        except IOError, e:
            # dammit.
            self.errorcount += 1
            print("(%d) Error recording: %s" % (self.errorcount, e))
            self.noisycount = 1
            return

        amplitude = get_rms(block)
        self.emit(QtCore.SIGNAL('mouthValue(float)'), amplitude)

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            self.listen()

class PortSend(QtCore.QThread):
    def __init__(self, port):
        QtCore.QThread.__init__(self)
        self.port = port
        print "Start PortSend"

    def __del__(self):
        self.wait()

    def dataConnect(self, sender):
        self.connect(sender, QtCore.SIGNAL('sendData(QString)'), self.sendData)
        self.connect(sender, QtCore.SIGNAL('setPort(QString)'), self.setPort)

    def setPort(self, port):
        print port
    def sendData(self, text):
        print text
        try:
            port.write(str(text))
        except:
            pass
    def run(self):
        while True:
            try:
                data = port.readline()
                data = QtCore.QString(data)
                self.emit(QtCore.SIGNAL('printDataFromController(QString)'), data)
            except:
                pass
            #self.emit(QtCore.SIGNAL('addImage(QImage)'), image)


class Program(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print "ui coplite"
        try:
            self.MicListen_thread = MicListen()
            self.connect(self.MicListen_thread, QtCore.SIGNAL('mouthValue(float)'), self.mouthValue)
            self.MicListen_thread.start()
            self.ui.micStat.setText("OK!")
        except:
            self.ui.micStat.setText("Not found microphone!")
        print ""
        self.gui_Connect()
        print "gui connect complite"
        self.lastMaxProgressBarValue = 100

        self.lastTextSend = 0
        self.colorsButtons =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.colorsButtonsList = [
            """
                background-color: rgb(255,0,0);
                border:1px solid rgb(0,0,0);
                """,
            """
                background-color: rgb(255,255,0);
                border:1px solid rgb(0,0,0);
                """,
            """
                background-color: rgb(0,255,255);
                border:1px solid rgb(0, 0, 0);
                """,
            """
                background-color: rgb(255,0,255);
                border:1px solid rgb(0, 0, 0);
                """,
            """
                background-color: rgb(0,0,0);
                border:1px solid rgb(0, 0, 0);
                """
        ]
        self.shortColorsButtonsList = [
            "255,0,0",
            "255,255,0",
            "0,255,255",
            "255,0,255",
            "0,0,0",
            "255,192,203",#pink
            "0,0,139", #darkblue
            "255,255,255", #white
            "0,110,0", #darkgreen
            "255, 215, 0" #gold
        ]
        self.loadColorGui()
        # self.connect(self.get_thread, QtCore.SIGNAL("finished()"), self.done)
        print "load color gui complite"
        self.updatePortList()
        #self.ui.portBox.activated['QString'].connect(self.updatePort)
        self.connect(self.ui.portBox, QtCore.SIGNAL('activated(QString)'),
                     self.updatePort)
        #self.ui.portBox.clicked.connect(self.updatePortList)

    def loadColorGui(self):
        for i in xrange(10):
            #print self.shortColorsButtonsList[i]

            self.colorsButtons[i] = QtGui.QPushButton("")
            self.colorsButtons[i].clicked.connect(self.sendColor)
            color = """
                background-color: rgb("""+self.shortColorsButtonsList[i]+""");
                border:1px solid rgb(0,0,0);
                """
            self.colorsButtons[i].setStyleSheet(color)
            self.colorsButtons[i].setMaximumWidth(23)
            self.colorsButtons[i].setMaximumHeight(23)
            self.colorsButtons[i].setMinimumWidth(23)
            self.colorsButtons[i].setMinimumHeight(23)
            if i>=5:
                self.ui.colorLayout.addWidget(self.colorsButtons[i], 1, i-5)
            else:
                self.ui.colorLayout.addWidget(self.colorsButtons[i], 0, i)

    def getPortList(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    def updatePortList(self):
        port_name = self.getPortList()
        self.ui.portBox.clear()
        print port_name
        for i in port_name:
            print i
            self.ui.portBox.addItem(i)
    def updatePort(self, name):
        global port, PORT_ACTIVE
        try:
            port.close()
        except:
            try:
                port = serial.Serial(str(name), baudrate=BAUD_RATE, dsrdtr=1, timeout=3.0)
                PORT_ACTIVE = True
                self.ui.arduinoStat.setText("Connection: " + name)
            except:
                self.ui.arduinoStat.setText("Connection lost")
                PORT_ACTIVE = False


    def sendColor(self):
        colorIndex = self.colorsButtons.index(self.sender())
        colors = self.shortColorsButtonsList[colorIndex].split(",")
        sendData = "DR" + colors[0] + "G" + colors[1] + "B" + colors[2] + "\n"

        self.emit(QtCore.SIGNAL('sendData(QString)'), sendData)
    def gui_Connect(self):
        self.connect(self.ui.sevoPosSlider, QtCore.SIGNAL('valueChanged(int)'),
                     self.sevoPosSliderEvent)

        self.connect(self.ui.sevoPosSlider, QtCore.SIGNAL('valueChanged(int)'),
                     self.ui.posValue, QtCore.SLOT('setNum(int)'))

        self.connect(self.ui.delaySlider, QtCore.SIGNAL('valueChanged(int)'),
                     self.ui.delayValue, QtCore.SLOT('setNum(int)'))

        self.connect(self.ui.openSlider, QtCore.SIGNAL('valueChanged(int)'),
                     self.ui.openValue, QtCore.SLOT('setNum(int)'))

        self.connect(self.ui.open12Slider, QtCore.SIGNAL('valueChanged(int)'),
                     self.ui.open12Value, QtCore.SLOT('setNum(int)'))

        self.connect(self.ui.closeSlider, QtCore.SIGNAL('valueChanged(int)'),
                     self.ui.closeValue, QtCore.SLOT('setNum(int)'))
        ###For headtrecker###
        self.connect(self.ui.minXSlider, QtCore.SIGNAL('valueChanged(int)'),
                     self.headTreckXSettingsEvent)

        self.connect(self.ui.maxXSlider, QtCore.SIGNAL('valueChanged(int)'),
                     self.headTreckXSettingsEvent)

        self.connect(self.ui.minYSlider, QtCore.SIGNAL('valueChanged(int)'),
                     self.headTreckYSettingsEvent)

        self.connect(self.ui.maxYSlider, QtCore.SIGNAL('valueChanged(int)'),
                     self.headTreckYSettingsEvent)

        self.connect(self.ui.xHeadSlider, QtCore.SIGNAL('valueChanged(int)'),
                     self.headRotationXEvent)
        self.connect(self.ui.xHeadSlider, QtCore.SIGNAL('valueChanged(int)'),
                     self.ui.xHeadValue, QtCore.SLOT('setNum(int)'))

        self.connect(self.ui.yHeadSlider, QtCore.SIGNAL('valueChanged(int)'),
                     self.headRotationYEvent)
        self.connect(self.ui.yHeadSlider, QtCore.SIGNAL('valueChanged(int)'),
                     self.ui.yHeadValue, QtCore.SLOT('setNum(int)'))

        self.connect(self.ui.delaySliderHead,  QtCore.SIGNAL('valueChanged(int)'),
                     self.delayHeadTrekerEvent )
        self.connect(self.ui.delaySliderHead, QtCore.SIGNAL('valueChanged(int)'),
                     self.ui.delayValueHead, QtCore.SLOT('setNum(int)'))

    def headRotationXEvent(self):
        value = self.ui.xHeadSlider.value()
        sendData = "S|D12" + ">" + str(value) + "\n"
        self.emit(QtCore.SIGNAL('sendData(QString)'), sendData)

    def headRotationYEvent(self):
        value = self.ui.yHeadSlider.value()
        sendData = "S|D11" + ">" + str(value) + "\n"
        self.emit(QtCore.SIGNAL('sendData(QString)'), sendData)

    def delayHeadTrekerEvent(self):
        timeDelay = self.ui.delaySliderHead.value()
        sendData = "T" + "H" + str(timeDelay) + "\n"
        self.emit(QtCore.SIGNAL('sendData(QString)'), sendData)

    def headTreckXSettingsEvent(self):
        minX = self.ui.minXSlider.value()
        maxX = self.ui.maxXSlider.value()
        self.ui.minXValue.setText(str(minX))
        self.ui.maxXValue.setText(str(maxX))
        sendData = "QX"+"L" + str(minX) + "B" + str(maxX) + "R1"  + "\n"
        self.emit(QtCore.SIGNAL('sendData(QString)'), sendData)

    def headTreckYSettingsEvent(self):
        minY = self.ui.minYSlider.value()
        maxY = self.ui.maxYSlider.value()
        self.ui.minYValue.setText(str(minY))
        self.ui.maxYValue.setText(str(maxY))
        sendData = "QY"+"L" + str(minY) + "B" + str(maxY) + "R1" + "\n"
        self.emit(QtCore.SIGNAL('sendData(QString)'), sendData)

    def mouthValue(self, value):
        gain = self.ui.gainBox.value()
        checkMouth = self.ui.mouthCheck.isChecked()
        bigValue = value*100*gain
        openValue = int(self.ui.openValue.text())
        open12Value = int(self.ui.open12Value.text())
        closeValue = int(self.ui.closeValue.text())

        openMouth12Value = self.ui.sredValue.text()
        openMouthValue = self.ui.maxValue.text()
        closeMouthValue = self.ui.minValue.text()

        #self.lastTextSend = closeMouthValue
        if checkMouth:
            if bigValue > self.lastMaxProgressBarValue:
                self.ui.soundProgress.setMaximum(bigValue)
                self.lastMaxProgressBarValue = bigValue
                print self.lastMaxProgressBarValue

            if bigValue > openValue and self.lastTextSend!=openMouthValue:
                sendData = "M>" + openMouthValue + "\n"
                self.emit(QtCore.SIGNAL('sendData(QString)'), sendData)
                self.lastTextSend = openMouthValue
            elif bigValue < openValue and bigValue > open12Value and self.lastTextSend != openMouth12Value:
                sendData = "M>" + openMouth12Value + "\n"
                self.emit(QtCore.SIGNAL('sendData(QString)'), sendData)
                self.lastTextSend = openMouth12Value
            elif (int(bigValue) <= closeValue or int(bigValue) < open12Value)and self.lastTextSend!=closeMouthValue:
                sendData = "M>" + closeMouthValue + "\n"
                self.emit(QtCore.SIGNAL('sendData(QString)'), sendData)
                self.lastTextSend = closeMouthValue

        self.ui.soundProgress.setValue(bigValue)


    def sevoPosSliderEvent(self, value):
        #text = self.ui.openValue.text()
        #text2 = self.ui.open12Value.text()

        #self.emit(QtCore.SIGNAL('setPort(QString)'), text2)
        #self.ui.openValue.setText(str(value))
        data = QtCore.QString("M>"+str(value)+"\n")
        self.emit(QtCore.SIGNAL('sendData(QString)'), data)
        pass
    def dataConnect(self, thread):
        self.connect(thread, QtCore.SIGNAL('printDataFromController(QString)'), self.printDataFromController)
    def printDataFromController(self, data):
        try:
            data = str(data)
            data = data.split("T")
            data = data[1].split("A")
            self.ui.tempValue.setText(data[0])
        except:
            pass
thread = ""
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Program()
    thread = PortSend("com4")
    thread.dataConnect(myapp)
    thread.start()
    myapp.dataConnect(thread)
    myapp.show()
    sys.exit(app.exec_())