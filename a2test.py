#!/usr/bin/env python3

from assignment2 import *
import argparse
# Team Member Name - Sandra Foster

'''
This script is to test the individual functions of assignment2 with out having to have all of the other functions complete
    check pwd is the assigment2 directory

ip_valid() testing
    run 'python3 a2test.py ip_valid' in terminal

define_ports() testing
    run 'python3 a2test.py define_ports' in terminal

scan_port() testing
    # run 'python3 a2test.py scan_port' in terminal
    # To open a port on your computer for temporary testing:
    # - in a new terminal run this code 'python3 -m http.server 8000'
    # - After testing type CTRL+C, in other terminal to stop process

make_report() testing
    # run 'python3 a2test.py make_report' in terminal

test all
    # run 'python3 a2test.py all' in terminal
'''

parser = argparse.ArgumentParser()
parser.add_argument("func", nargs='?', default='all', help="Enter function to run")
args = parser.parse_args()


def test_read_args():
    print('read_args() testing has to be done by running script in terminal with arguments')
    print('This was for testing before the main was written, and is not necessary now')
    print("running 'python3 ./assignment2.py 127.0.0.1 80' should return a list ['127.0.0.1', '80']")
    print()

def test_ip_valid():
    # ip_valid() testing
    print('ip_valid() test: 127.0.0.1 - output should be "True" -->', ip_valid('127.0.0.1'))        # valid ip address
    print('ip_valid() test: 127.0.0 - output should be "False" -->', ip_valid('127.0.0'))         # invalid ip address
    print('ip_valid() test: 12700 - output should be "False" -->', ip_valid('12700'))         # invalid ip address
    print('ip_valid() test: scanme.nmap.org - output should be "True" -->', ip_valid('scanme.nmap.org'))  # valid hostname
    print('ip_valid() test: scanmenmaporg - output should be "False" -->', ip_valid('scanmenmaporg'))  # valid hostname

    print()

def test_define_ports():
    # define_ports() testing
    print('define_ports() test: output should be [80] -->', define_ports('80'))
    print('define_ports() test: output should be Error message -->', define_ports('not a port'))
    # multi port test 
    print('define_ports() test: output should be [20, 23, 25] -->', define_ports('20,23,25'))
    print()

def test_scan_port():
    print('scan_port() test: output for "127.0.0.1, 20" should be False -->', scan_port('127.0.0.1', 20))
    print('scan_port() test: output for "scanme.nmap.org, 80" should be True -->', scan_port('scanme.nmap.org', 80))
    print('scan_port() test: output for "scanme.nmap.org, 23" should be False -->', scan_port('scanme.nmap.org', 23))
    print()
    print('To open a port on your computer for temporary testing:')
    print("- in a new terminal run this code 'python3 -m http.server 8000'")
    print('- After testing type CTRL+C, in other terminal to stop process') 
    print('scan_port() test: output for "127.0.0.1, 8000" should be True -->', scan_port('127.0.0.1', 8000))
    print()

def test_make_report():
    # make_report() testing
    print('make_report() test: output should be: \nIP address - 127.0.0.1\nPort 20 is Closed\n-->\n', make_report('127.0.0.1', [20], [False]))
    print()
    print('make_report() test: output should be: \nIP address - 127.0.0.1\nPort 20 is Open\nPort 23 is Closed\nPort 25 is Closed\n-->\n', make_report('127.0.0.1', [20, 23, 25], [True, False,False]))
    print()

print(f'Testing {args.func} function')
print('- text before and after --> should match')
if args.func == 'read_args':
    test_read_args()
elif args.func == 'ip_valid':
    test_ip_valid()
elif args.func == 'define_ports':
    test_define_ports()
elif args.func == 'scan_port':
    test_scan_port()
elif args.func == 'make_report':
    test_make_report()
elif args.func == 'all':
    test_read_args()
    test_ip_valid()
    test_define_ports()
    test_scan_port()
    test_make_report()

else:
    print('Please enter valid argument.')