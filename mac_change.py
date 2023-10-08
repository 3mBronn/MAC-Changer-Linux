import subprocess
import optparse
import re


def get_user_input():
    object_parse = optparse.OptionParser()
    object_parse.add_option("-i", "--interface", dest="interface" , help="Enter the interface")
    object_parse.add_option("-m" , "--mac" , dest="mac_address" , help="new MAC address")

    return object_parse.parse_args()

def commands(user_interface, user_mac):
    subprocess.call(["ifconfig" , user_interface , "down"])
    subprocess.call(["ifconfig" , user_interface , "hw" , "ether" , user_mac])
    subprocess.call(["ifconfig" , user_interface , "up"])

def check_mac(interface):
    check = subprocess.check_output(["ifconfig" , interface ])
    view_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(check))

    if view_mac:
        return view_mac.group(0)
    else:
        return None    

print("[+]MAC Changer has started!")

(inputs_user , arguments) = get_user_input()
commands(inputs_user.interface, inputs_user.mac_address)

final_mac = check_mac(str(inputs_user.interface))

print("[+]MAC address is succesfully changed!")
print("[+]New MAC address is " , final_mac)

