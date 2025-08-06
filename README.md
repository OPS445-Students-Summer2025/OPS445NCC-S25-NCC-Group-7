# Summer 2025 Assignment 2 - Group 7
## Lalit Budhathoki
### read_args()
This function uses the `argparse` module to read command-line arguments.  
It takes:
- a required IP address or hostname
- a required list of ports 
- an `--timeout` value

###  For `scan_port()`:
This function attempts a TCP connection to the given port on the IP or hostname.  
It uses the `socket` module to check if the port is open or closed.

*It returns:
True: if the port is open.
False: if the port is closed.

