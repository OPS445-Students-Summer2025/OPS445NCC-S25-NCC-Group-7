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
    # Team Member Name - Lalit Budhathoki 
    # takes no arguments, as these will be taken from the command line/terminal 
    # returns a list
    # Function uses ‘argparse’ module to get the arguments passed when running the script in the terminal.
    # terminal arguments will be ip address (or hostname) and ports
    # option - add timeout argument later, if time
    # on the terminal running 'python3 ./assignment2.py 127.0.0.1 80' should return a list ['127.0.0.1', '80'] from this function.
    # running 'python3 ./assignment2.py 127.0.0.1 80,23,25' should return a list ['127.0.0.1', '80,23,25']
   
   # Create an ArgumentParser object with a description
    parser = argparse.ArgumentParser(description="Network Port Scanner")

    # Required IP argument
    parser.add_argument("ip", help="Target IP address or hostname to scan")

    # Required ports list
    parser.add_argument("ports", help="Comma-separated list of ports to scan")

    # Optional timeout argument
    parser.add_argument("--timeout", type=float, default=0.5, help="Connection timeout in seconds (default: 0.5)")

    args = parser.parse_args()

    # Validate IP address format
    try:
        socket.gethostbyname(args.ip)
    except socket.error:
        parser.error("Invalid IP address or hostname.")

    # Parse and validate ports list
    try:
        port_list = [int(p) for p in args.ports.split(",")]
    except ValueError:
        parser.error("Ports must be comma-separated integers (e.g., 80,443,8080)")

    for port in port_list:
        if port < 1 or port > 65535:
            parser.error(f"Port {port} is out of valid range (1–65535)")

    return args.ip, port_list, args.timeout


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
    # Team Member Name - Tirth Shah 
    # take 1 argument, a string 
    # returns a list
    # Function converts port_string to a list 
    # port_string could be a single port or a multiple ports seperated by commas, eg '80' or '20,22,23' 
    # if port_string is not valid then return an error message
    ports = port_string.split(',')  # Split string by comma
    port_list = []  # Empty list to store valid ports

    for port in ports:
        port = port.strip()  # Remove any extra spaces
        if not port.isdigit():  #Checks if the number is correct or not
            return "Error: One or more ports are not valid numbers."
        port_num = int(port)     #Checks if the port is within the desired range
        if port_num < 1 or port_num > 65535:
            return "Error: Port numbers must be between 1 and 65535."
        port_list.append(port_num)  # Add valid port to list

    return port_list
    pass


def scan_port(ip_string, port_int, timeout = 1):
    # Team Member Name - Lalit Budhathoki 
    # take 3 arguments, ip_string=string, port_int=integer, timeout=integer
    # returns Boolean - True if port is open, False if closed
    # default for timeout is 1 second
    # attempts a socket connection using ‘socket’ module 
    try:
# Create a TCP socket connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout) # Set timeout for the socket
            result = s.connect_ex((ip_string, port_int))
            return result == 0 # Return True if port is open
    except socket.error:
             return False  # Return False if connection fails


def make_report(ip_string, ports_list, port_statuses):
    # Team Member Name - 
    # take 3 arguments, string, list, list
    # returns nothing - prints report
    # Function formats data into a report and prints it to terminal
    pass


if __name__ == '__main__':
    # For read_args and scan_ports by Lalit Budhathoki
    ip, ports, timeout = read_args()
     # Scan and print status of each port
    for port in ports:
        result = scan_port(ip, port, timeout)
        print(f"Port {port}: {'Open' if result else 'Closed'}") 



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

