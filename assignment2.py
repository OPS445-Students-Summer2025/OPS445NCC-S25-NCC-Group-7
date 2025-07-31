#!/usr/bin/env python3

import argparse
import socket
import ipaddress

'''
Put your name inside the function that you are going to code, as a comment. 
Comments in functions are there as guides, change them as necessary. 
Main block has test code and instructions for testing the functions,
so that we can test our functions with out waiting for other functions to complete.
'''

def read_args():
    # Team Member Name - 
    # takes no arguments, as these will be taken from the command line/terminal 
    # returns a list
    # Function uses ‘argparse’ module to get the arguments passed when running the script in the terminal.
    # terminal arguments will be ip address (or hostname) and ports
    # option - add timeout argument later, if time
    # on the terminal running 'python3 ./assignment2.py 127.0.0.1 80' should return a list ['127.0.0.1', '80'] from this function.
    # running 'python3 ./assignment2.py 127.0.0.1 80,23,25' should return a list ['127.0.0.1', '80,23,25']
    pass 


def ip_valid(ip_string):
    # Team Member Name - Ranjan Ghorsaini
    # takes 1 argument, a string 
    # Function checks if ip_string argument is a valid ip address or hostname
    # First, it will checks if it's a valid IP using the ipaddress module.
    # If that fails, it tries to resolve it as a hostname using socket.
    # returns boolean - True if valid, False not valid


    # Check if it's a valid IP address
    try:
        ipaddress.ip_address(ip_string)
        return True
    except ValueError:
        pass  # It's not a valid IP

    # Check if it's a valid hostname
    try:
        socket.gethostbyname(ip_string)
        return True
    except socket.error:
        return False       # It's not a valid ip or hostname


def define_ports(port_string):
    # Team Member Name - 
    # take 1 argument, a string 
    # returns a list
    # Function converts port_string to a list 
    # port_string could be a single port or a multiple ports seperated by commas, eg '80' or '20,22,23' 
    # if port_string is not valid then return an error message
    pass


def scan_port(ip_string, port_int, timeout = 1):
    # Team Member Name - 
    # take 3 arguments, ip_string=string, port_int=integer, timeout=integer
    # returns Boolean - True if port is open, False if closed
    # default for timeout is 1 second
    # attempts a socket connection using ‘socket’ module 
    pass


def make_report(ip_string, ports_list, port_statuses):
    # Team Member Name - 
    # take 3 arguments, string, list, list
    # returns nothing - prints report
    # Function formats data into a report and prints it to terminal
    pass


if __name__ == '__main__':
    # Temp testing code
 
# read_args() testing has to be done by running script in terminal with arguments
    # running 'python3 ./assignment2.py 127.0.0.1 80' should return a list ['127.0.0.1', '80']
    print("read_args() test: output should be ['127.0.0.1', '80'] -->", read_args())
    print()


    # Other functions can be tested without running assignment2.py script with arguments
    # (pwd is the assigment2 directory)

# ip_valid() testing
    # run 'python3 a2test.py ip_valid' in terminal

# define_ports() testing
    # run 'python3 a2test.py define_ports' in terminal

# scan_port() testing
    # run 'python3 a2test.py scan_port' in terminal
    # To open a port on your computer for temporary testing:
    # - in a new terminal run this code 'python3 -m http.server 8000'
    # - After testing type CTRL+C, in other terminal to stop process

# make_report() testing
    # run 'python3 a2test.py make_report' in terminal

# test all
    # run 'python3 a2test.py all' in terminal

