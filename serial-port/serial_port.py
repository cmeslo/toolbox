import serial
import time

if __name__ == "__main__":

    # card query
    command1 = [0x02,0x02,0x00,0x30,0x00,0x32,0x03]
    bArray1 = bytearray(command1)

    # card consume
    command2 = [0x02,0x10,0x00,0x40,0x00,0x00,0x00,0x00,0x00,0x10,0x10,0x20,
                0x18,0x10,0x03,0x08,0x17,0x56,0x05,0x04,0x46,0x75,0x03]
    bArray2 = bytearray(command2)

    ser = serial.Serial("COM1", 9600, timeout=3)
    # ser.open()
    ser.write(bArray1)
    # out = ser.readline()
    out = ser.readall()
    print(''.join('{:02x} '.format(x) for x in out))
    # time.sleep(3)

    ser.write(bArray2)
    out = ser.readall()
    print(''.join('{:02x} '.format(x) for x in out))
    ser.close()
