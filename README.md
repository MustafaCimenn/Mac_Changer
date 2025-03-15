# MAC Changer for Kali Linux

This script allows you to change the MAC address of a network interface on Kali Linux using Python.

## Prerequisites
Before running the script, make sure that:
- You have Python installed on your system.
- You have `sudo` privileges to change the MAC address.
- The `ifconfig` tool is available on your system (usually pre-installed on Kali Linux).

## Usage
1. Clone or download the repository to your local machine.

2. Open a terminal in the directory where the script is located.

3. Run the script using the following command:

   ```bash
   sudo python3 mac_changer.py <interface> <new_mac>
