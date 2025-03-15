import argparse
import subprocess
import re
# MAC Changer for Kali Linux #
#You should use sudo for run this file#

def args():
    parser = argparse.ArgumentParser(description="Change the MAC address.")
    parser.add_argument("interface", help="The network interface whose MAC address will be changed.")
    parser.add_argument("mac", help="New MAC address.")
    return parser.parse_args()

def new_Mac_Control(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)

    if new_mac:
        return new_mac.group(0)
    else:
        return None

def mac_Change(interface, new_mac):
    print(interface + " interface is shutting down...")
    subprocess.call(["ifconfig", interface, "down"])

    print("New MAC address is being set to " + new_mac)
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

    print(interface + " interface is coming back up...")
    subprocess.call(["ifconfig", interface, "up"])

def main():
    arguments = args()

    print("Network interface: " + arguments.interface)
    print("New MAC address: " + arguments.mac)

    current_mac = new_Mac_Control(arguments.interface)
    if current_mac:
        print("Current MAC address: " + current_mac)

    mac_Change(arguments.interface, arguments.mac)

    updated_mac = new_Mac_Control(arguments.interface)
    if updated_mac == arguments.mac:
        print("MAC address successfully changed to " + updated_mac)
    else:
        print("Error: MAC address change failed.")

if __name__ == "__main__":
    main()