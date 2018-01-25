##################################################################################################################################
########################################UNIVERSITY OF MASSACHUSETTS LOWELL########################################################
#################################DEPARTMENT OF MECHANICAL ENGINEERING AND COMPUTER SCIENCE########################################
####################################################---R-A-D-A-R---###############################################################
######################################Sample code for reading values from RADAR device############################################
########################################################Fall 2017#################################################################




####--I-M-P-O-R-T-S---############################################################################################################
##################################################################################################################################
import time #built-in Time library, sleep function to pause CPU

##################################################################################################################################
import math #built-in Math library, math functions like sine, cos etc

##################################################################################################################################
# py-serial library provides various support functions for working with serial port devices which help automate our job.
import serial

##################################################################################################################################
# pandas is a data analysis support library that provides the necessary tools such as data structures and math functions on such
# strpductures 
import pandas as pd

##################################################################################################################################
# SciPy provides a discrete fourier transform library 
from scipy.fftpack import fft

##################################################################################################################################
# mathPlot library provides a function for plotting values on a graph
import matplotlib.pyplot as plt

##################################################################################################################################
# NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along
# with a large collection of high-level mathematical functions to operate on these arrays.
import numpy as np 

##################################################################################################################################
# SciPy is an open source Python library used for scientific computing and technical computing.
import scipy
##################################################################################################################################
    

##################################################################################################################################
#Setting up the Port and Data channel speed. Initialization of communications port.
ser = serial.Serial(
    port='COM4',
    baudrate=115200,
)
##################################################################################################################################
# Printing the connection to serial port status, if OK, then proceed.
print ser.isOpen()
##################################################################################################################################


##################################################################################################################################
# Initialize a small list of commands to be sent over the serial connection, which help to initialize, sweep, trace and collect the 
# radar data.
list_of_commands = [
    'hard:syst rs3400w',
    'hard:syst ?',
    'INIT',
    'SWEEP:MEASURE on',
    'SWEEP:NUMBERS 1',
    'TRIG:ARM',
    'TRACE:DATA ?',
    'TRACE:FFT:CALCulate',
    'FREQUENCY:IMMEDIATE ?',
    'TRACe:READ:DISTance ?',
    'Trace:read:FINDex ?',
    'Trace:read:PINDex ?'
]
##################################################################################################################################
# Initialize certain variables
measuredDist = 0.0          #Floating value initilization
##################################################################################################################################





##################################################################################################################################
#Start a try-catch block to handle exceptions and prevent program crash
try:                    
    # Loop over the list of commands one by one
    for command in list_of_commands:
        ser.write(command + '\r\n') # Push the command to RADAR device and expect to receive feedback from it.
        out = ''
        print command               # Display the current command to the user for feedback.
        if(command == 'TRACE:DATA ?'):
            print 'if'              # Tracing for debugging purposes
            time.sleep(1)
        else:
            print 'else'            # Tracing for debugging purposes
            time.sleep(0.4)
        # Check status and wait to receive the output from the RADAR.
        while ser.inWaiting() > 0:
            out += ser.read(1)      # This object holds the output data strings.
        print out
        # Showing the measuredData from RADAR.
        if(command == 'TRACe:READ:DISTance ?'):
            out = out.replace("\r\n","")
            measuredDist = float(out)
        else:
            print out
    # The serial library allows to close the serial port connection once done
    ser.close()
    # Accurate distance generation using curve fitted calibration formula
    dist = -0.003754 * measuredDist * measuredDist - 1.391992 * measuredDist + 128.851509
    print 'Distance(m):::'
    print dist
