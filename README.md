# Summer 2025 Assignment 2 - Group 7

ip_valid()

**Ranjan Ghorsaini:**

- This function checks if the input string is a valid IP address or a valid hostname.

- First, it uses the ipaddress.ip_address() method to check if it’s a valid IP address.

- If that fails, it tries to resolve the string as a hostname using socket.gethostbyname().

- If either one works, the function returns True.

- If both checks fail, it returns False, meaning the input is invalid.

- This prevents the script from scanning unreachable or incorrect hosts.

- Example valid input: "127.0.0.1", "google.com"

- Example invalid input: "999.999.999.999", "wronghost"


