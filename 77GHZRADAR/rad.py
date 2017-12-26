import time
import serial
import pandas as pd
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy
import scipy.fftpack
import pylab

ser = serial.Serial(
    port='COM4',
    baudrate=115200,
)

print ser.isOpen()

list_of_commands = ['hard:syst rs3400w','hard:syst ?', 'INIT','SWEEP:MEASURE on', 'SWEEP:NUMBERS 1', 'TRIG:ARM', 'TRACE:DATA ?', 
                   'TRACE:FFT:CALCulate','FREQUENCY:IMMEDIATE ?', 'TRACe:READ:DISTance ?', 'Trace:read:FINDex ?', 'Trace:read:PINDex ?']
#
# list_of_commands = ['TRIG:ARM', 'TRACE:DATA ?', 'TRACE:FFT:CALCulate', 'TRACe:READ:DISTance ?']

x = 0.0
i = 0

try:
    for command in list_of_commands:
        i = i+1
        ser.write(command + '\r\n')
        out = ''
        print command

        
        if(command == 'TRACE:DATA ?'):
            print 'if'
            time.sleep(1)
        else:
            print 'else'
            time.sleep(.4 )
        
        while ser.inWaiting() > 0:
            out += ser.read(1)    
        print out
              
        if(command == 'TRACe:READ:DISTance ?'):
            out = out.replace("\r\n","")
            x = float(out)
        else:
            print out
            
    ser.close()

    dist = -0.003754*x*x - 1.391992*x + 128.851509 
    
#    dist = -1.954866*x + 149.9548
#    dist = 64.75547 - 0.3380736*x - 0.01540895*x*x
    print 'dist:::'
    print dist
    
#    signal = pd.read_csv('2mcommands7.csv', sep='\r',  header=None, error_bad_lines=False)
#    signal = signal.drop(signal.index[len(signal)-1])
##    signal.to_csv('2mcommand7.csv', encoding='utf-8', index=False)  
#    signal.columns = ['a']
#
##    print signal.describe()
#      
#    x = np.linspace(7.600000e+10, 7.700000e+10,  signal.count())
#    sweep_time = 5.005000e-02 
#    c = 2.998e+8 
#    freq_step = 9.999974e+05
#    freq_points = 1001
#    slope = (freq_step*freq_points)/(sweep_time);
#    signal[['a']] = signal[['a']].astype(float)   
#    signal = signal.applymap(lambda x: (c*x/(2*slope)))  
#    plt.plot(x, signal)
#    print signal.describe()

except:
    print "error"
    ser.close()