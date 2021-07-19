# Script to control CS 3000 Ametek 

# Source: https://www.dsinstruments.com/support/python-serial-control-example/

import serial 
import time     

# Opening serial port (needs to be automated!)
ser = serial.Serial('COM3',460800, timeout=1) 
if ser.isOpen():    # make sure port is open
    print(ser.name + 'open…')    # tell the user we are starting

# Device information
ser.write(b'*IDN?\n')   # send the standard SCPI identify command
myResponse = ser.readline()    # read the response
print(b'Device Info:' + myResponse) # print the unit information
time.sleep(1)

#%%
# Initial parameters
print('Initial device state information:')
ser.write(b'CURR?\n')
current = ser.readline()
print(b'Current Info:' + current) 
ser.write(b'FREQ?\n')
frequency = ser.readline()
print(b'Frequency Info:' + frequency)


#%%
# Programming On-Off keyed (OOK) signal
current=[0.5,1] #A
frequency=[60,1000,2000,2500,3000,3500,4000,4500,5000,6000]   #Hz
on_time = 2
off_time = 2
print('Starting the program...')
for i in frequency:
    for j in current:
        ser.write(b'CURR %f\n' % j)
        ser.write(b'FREQ %f\n' % i)
        ser.write(b'OUTP ON\n')
        time.sleep(on_time)
        ser.write(b'OUTP OFF\n')
        time.sleep(off_time)
print('End of program.')
ser.close()

#%%
'''
# Step-by-step program
print('Starting the program...')
ser.write(b'CURR 0.5\n')
ser.write(b'CURR?\n')
print(b'Current changed to:' + ser.readline())
ser.write(b'FREQ 500\n')
ser.write(b'FREQ?\n')
print(b'Frequency changed to:' + ser.readline())
print('Turning on the output now...')
ser.write(b'OUTP ON\n')
time.sleep(5)
ser.write(b'OUTP OFF\n')
time.sleep(10)
ser.write(b'CURR 1\n')
ser.write(b'CURR?\n')
print(b'Current changed to:' + ser.readline())
ser.write(b'FREQ 1000\n')
ser.write(b'FREQ?\n')
print(b'Frequency changed to:' + ser.readline())
print('Turning on the output again...')
ser.write(b'OUTP ON\n')
time.sleep(5)
ser.write(b'OUTP OFF\n')
print('End of program.')
'''

#%%
'''
# List mode
ser.write(b'CURRent:MODE LIST\n')
ser.write(b'FREQ:MODE LIST\n')
ser.write(b'LIST:CURR 0.120, 0.132, 0.108, 0.120, 0.132, 0.108, 0.120, 0.132, 0.108\n')
ser.write(b'LIST:FREQ 400, 400, 400, 440, 440, 440, 360, 360, 360\n')
ser.write(b'LIST:DWELL 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5\n')
ser.write(b'LIST:COUNt 1\n')
ser.write(b'LIST:STEP AUTO\n')
ser.write(b'OUTP ON\n')
#ser.write(b'OUTP OFF\n')
'''
