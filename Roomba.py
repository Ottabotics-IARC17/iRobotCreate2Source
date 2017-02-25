import serial


ser = serial.Serial('/dev/ttyUSB0', 115200) 
ser.write(b'128 132')
ser.write(b'140 0 1 62 32')
ser.write(b'141 0 ')
ser.close()
