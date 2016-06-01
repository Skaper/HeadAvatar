import sys, tty, termios, serial, time, socket
import binascii
_waitConnect    =   False
port            =   5003
portname        =   '/dev/ttyACM0'
speedHeadMove   =   4
if _waitConnect:
    sock = socket.socket()
    sock.bind(('', port))
    sock.listen(1)
    conn, addr = sock.accept()
    #sock.setblocking(False)




arrow = 27#str(0b11011)
fingers_all_keys = ['q', 'w', 'e', 'r', 't', 'u', 'i', 'o', 'p', '[', ']']
hot_key_arrow = {
    'A': 'up',
    'B': 'down',
    'D': 'left',
    'C': 'right'
}
fingers_stat = {
    'q': 0, #Mizinec L
    'w': 0, #bezim L
    'e': 0, #Sregnyi L
    'r': 0, #ykaz L
    't': 0, # bigL

    'u': 0, #Mizinec R
    'i': 0, #bezim R
    'o': 0, #Sregnyi R
    'p': 0, #ykaz R
    '[': 0, # big R
    ']': 0, # Hand R

    #'y': {'pin': '6', 'value': '98'}, # HandL
}
servo_ports = {
    'up': '12',
    'down': '12',
    'left': '11',
    'right': '11',
    'q': {'pin': '1', 'value': '107'}, #Mizinec L
    'w': {'pin': '2', 'value': '180'}, #bezim L
    'e': {'pin': '3', 'value': '125'}, #Sregnyi L
    'r': {'pin': '4', 'value': '125'}, #ykaz L
    't': {'pin': '7', 'value': '123'}, # bigL
    #'y': {'pin': '6', 'value': '98'}, # HandL

    'q2': {'pin': '1', 'value': '19'}, #Mizinec L
    'w2': {'pin': '2', 'value': '40'}, #bezim L
    'e2': {'pin': '3', 'value': '12'}, #Sregnyi L
    'r2': {'pin': '4', 'value': '0'}, #ykaz L
    't2': {'pin': '7', 'value': '3'}, # bigL
    #'y2': {'pin': '6', 'value': '0'}, # HandL

    'u': {'pin': '28', 'value': '60'}, #Mizinec R
    'i': {'pin': '29', 'value': '115'}, #bezim R
    'o': {'pin': '30', 'value': '130'}, #Sregnyi R
    'p': {'pin': '31', 'value': '135'}, #ykaz R
    '[': {'pin': '32', 'value': '115'}, # big R
    ']': {'pin': '27', 'value': '120'}, # Hand R

    'u2': {'pin': '28', 'value': '0'}, #Mizinec R
    'i2': {'pin': '29', 'value': '5'}, #bezim R
    'o2': {'pin': '30', 'value': '0'}, #Sregnyi R
    'p2': {'pin': '31', 'value': '15'}, #ykaz R
    "[2": {'pin': '32', 'value': '0'}, # bigR
    "]2": {'pin': '27', 'value': '5'}, # HandL
}

class KeboardControl():
    def __init__(self, port):
        self.listen = True
        self.port = port
        self.headX = 90
        self.headY = 90
        #'S|D'+str(pin) +'>'+str(pos)
        self.connection()
        while self.listen:
            self.listenKey()
            print 'fas'
            #self.linesplit(sock)

    def connection(self):
        try:
            self.robotPort = serial.Serial(self.port, baudrate=115200, dsrdtr = 1,  timeout=1)
            print "OK Conection"
        except:
            print 'Error 1.1.3: Port %s not found'
            self.robotPort = ''

    def getKeyChar(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            binKey = int(binascii.hexlify(ch), 16)#bin(int(binascii.hexlify(ch), 16))
            #print binKey
            if binKey == arrow:
                ch = sys.stdin.read(2)
                return hot_key_arrow[ch[1]]
                '''
                if ch[1] == 'A':
                    return 'up'
                elif ch[1] == 'B':
                    return 'down'
                elif ch[1] == 'D':
                    return 'left'
                elif ch[1] == 'C':
                    return 'right'
                '''
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def linesplit(self, sock):
        buffer = sock.recv(4096)
        buffering = True
        while buffering:
            if "\n" in buffer:
                (line, buffer) = buffer.split("\n", 1)
                #yield line + "\n"
                print line + "\n"
            else:
                more = sock.recv(4096)
                if not more:
                    buffering = False
                else:
                    buffer += more
        if buffer:
            #yield buffer
            print buffer

    def listenKey(self):

        key = self.getKeyChar()
        if len(key) > 1:
            try:
                servo = servo_ports[key]
            except KeyError as e:
                print e
        elif len(key) == 1:
            try:
                pin, value = servo_ports[key]['pin'], servo_ports[key]['value']
            except KeyError as e:
                print e


        if key != "":
            print "key: " + key
        if key == "left":
            self.headX -= speedHeadMove
            if self.headX < 0: self.headX = 0
            self.robotPort.write("S|D"+servo+">"+str(self.headX)+"\n")
        elif key == "right":
            self.headX += speedHeadMove
            if self.headX > 180: self.headX = 180
            self.robotPort.write("S|D"+servo+">"+str(self.headX)+"\n")
        elif key == "down":
            self.headY -= speedHeadMove
            if self.headY < 0: self.headY = 0
            self.robotPort.write("S|D"+servo+">"+str(self.headY)+"\n")
        elif key == "up":
            self.headY += speedHeadMove
            if self.headY > 180: self.headY = 180
            self.robotPort.write("S|D"+servo+">"+str(self.headY)+"\n")
        elif key == "+": self.listen = False
        elif key in fingers_all_keys:

            stat = fingers_stat[key]
            if stat == 0:
                try:
                    pin, value = servo_ports[key]['pin'], servo_ports[key]['value']
                except KeyError as e:
                    print e
                data = "S|D"+pin+">"+value+"\n"
                print data
                self.robotPort.write(data)
                fingers_stat[key] = 1
            elif stat == 1:
                try:
                    pin, value = servo_ports[key]['pin'], servo_ports[key+'2']['value']
                except KeyError as e:
                    print e
                data = "S|D"+pin+">"+value+"\n"
                print data
                self.robotPort.write(data)
                fingers_stat[key] = 0
            print stat
            print value



        key = ""
        time.sleep(0.01)

# This section of code defines the methods used to determine


# Infinite loop that will not end until the user presses the
# exit key
if __name__ == "__main__":
    KeboardControl(portname)


