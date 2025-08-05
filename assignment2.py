#!/usr/bin/env python3

import argparse
import socket
import ipaddress

'''
Network Port Scanner

    sample text for testing program in a2_test_samples.txt
    to test individual funtions run a2test.py 
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
    # Team Member Name - John Cherubini
    # take 3 arguments, string, list, list
    # returns nothing - prints report
    # Function formats data into a report and prints it to terminal

    print("\nScanned IP address: ", ip_string)
    print("-------------------------------")
    ports = 0
    while ports < len(ports_list):
        port = ports_list[ports]
        if port_statuses[ports]:
            state = "Open"
        else:
            state = "Closed"
        print("Port " + str(port) + ": " + state)
        print("")
        ports += 1




if __name__ == '__main__':
    # Team Member Name - Sandra Foster
    
    # get arguments from terminal
    ip_string, port_string, timeout = read_args()

    # check if ip address or hostname is valid
    if ip_valid(ip_string) == False:
        # print error if ip or host is invalid
        print('Error: Invalid ip address or hostname')
    else:
        # validate and format ports argument
        port_list = define_ports(port_string)
        if 'Error' in port_list: # if define_ports() returns error code, print error code
            print(port_list)
        else:
            # print statement so that user knows it is working 
            print(f'Scanning {ip_string}: ... please wait')

            # empty list for status of ports
            port_statuses = []

            # loop through ports, checking status of each one
            for port in port_list:
                port_statuses.append(scan_port(ip_string, port, timeout))

            # print report to terminal
            make_report(ip_string, port_list, port_statuses)
        