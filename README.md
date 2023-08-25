# Security-Manager
A Python program to control critical Windows system functions via Windows registry. 

The program uses Python's winreg module to modify Windows registry values to control system functions.
The following functions are supported:
1. Block/Unblock USB ports access
2. Enable/Disable bluetooth
3. Enable/Disable command prompt
4. Block/Unblock facebook.com access

### USB ports access
The key that controls access to the USB ports in the registry is '''HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\USBSTOR'''
To disable the ports, the value of '''Start''' must be set to 4. This is done be the function '''blockUSB()'''.
To enable the ports, the value of '''Start''' is set to 3, by the function '''unblockUSB()'''.
