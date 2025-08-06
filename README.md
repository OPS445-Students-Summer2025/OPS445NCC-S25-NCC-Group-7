![Header](./github-header-banner.png)


# NETWORK PORT SCANNER    

> [!IMPORTANT]  
> Please use responsibly and ethically. Only scan ports that you are permitted to!

## Summer 2025 Assignment 2 - Group 7 :sunny:

## What is it? :woman_technologist: :artificial_satellite:
This is a Python based network port scanner. It takes in terminal arguments of an IP address or hostname, a list of ports, and an optional timeout. It scans the specified ports of the given IP address/hostname, and prints a report to the command line whether the ports are open or closed.   

This was completed, in an Linux environment, as part of a group project, for OPS445, at Seneca Polytechnic. 

## Installation :hammer_and_wrench:  
[![My Skills](https://skillicons.dev/icons?i=py)](https://www.python.org/) Install python3 in your coding environment.

## Usage
On terminal run:  

> python3 ./assignment2.py \<hostname or ipaddress\> \<portnumbers\> --timeout \<timeout value\>    

- _Port numbers can be an individual port, or comma separated, with no spaces._   
- _Timeout is entered in seconds and is optional. It defaults to 0.5 seconds._

Example: <br>  
```python
python3 ./assignment2.py scanme.nmap.org 80,23,25
```  
```python
python3 ./assignment2.py 127.0.0.1 8000 --timeout 3
```

## Our functions :brain:

```main block```  
Sandra Foster:  

- Get command line arguments using read_args()
- Checks if IP address/hostname is valid using ip_valid()  
    - Error message if IP or hostname is invalid  
- Validates and formats ports argument using define_ports()  
    - Error message if ports argument is invalid  
- Loops through and tests each given port using scan_port()  
- Calls make_report() 

<br>

```read_args()```
Lalit Budhathoki:

This function uses the `argparse` module to read terminal arguments passed to the script.  
It accepts:
- `ip`: Target IP address or hostname 
- `ports`: Comma-separated list of ports to scan 
- `timeout`: Timeout value of 0.5 seconds

It returns: `(ip, ports, timeout)`  

```ip_valid()```  
Ranjan:  
<br>  

```define_ports()```  
Tirth:  
<br>  

```scan_port()```
Lalit Budhathoki:

This function attempts to connect to a given port on a given IP address using the `socket` module.  
It accepts:
- `ip_string`: Target IP address or hostname
- `port_int`: Port number to check
- `timeout`: Time to wait for a response ( 1 second)

It returns
`True`: If the port is open.
`False`:If the port is closed or unreachable.

```make_report()```  
John: 



## Additional Files :card_index_dividers:
 
```a2test.py```  
Sandra Foster:  

This script tests each individual function of assignment 2. It allows you to test a function without needing any other functions to be complete. Enables asynchronous code completion.  

Full instructions on how to use this script are commented inside the file.

```a2_test_samples.txt```  
Sandra Foster:   

This text document contains example command line prompts for testing the completed assignment 2. It provides different prompts that should run either successfully or with error codes.
## Contributors:
Sandra Foster  
Lalit Budhathoki  
Ranjan Ghorsaini  
Tirth Shah  
John Cherubini

## References:

- Great website for responsible and permitted network scanning practise:  

http://scanme.nmap.org/  
<br>  

- argparse Python module documentation:  

https://docs.python.org/3/library/argparse.html  
<br>  

- argparse Python tutorial:  

https://docs.python.org/3/howto/argparse.html  
<br>

- socket Python module documentation:  

https://docs.python.org/3/library/socket.html  
<br>

- ipaddress Python module documentation:  

https://docs.python.org/3/library/ipaddress.html  
<br>

- Introduction to ipaddress module:  

https://docs.python.org/3/howto/ipaddress.html  
<br>  

- How to create a GitHub README:   

https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes  
<br>


