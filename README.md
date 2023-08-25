# Security-Manager
A Python program to control critical Windows system functions via Windows registry. 

The program uses Python's winreg module to modify Windows registry values to control system functions.
The following functions are supported:
1. Block/Unblock USB ports access
2. Enable/Disable bluetooth
3. Enable/Disable command prompt
4. Block/Unblock facebook.com access

### USB ports access
The functions that control the USB ports access are `blockUSB()` and `unblockUSB()`
The key that controls access to the USB ports in the registry is `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\USBSTOR`
To disable the ports, the value of `Start` must be set to 4. This is done be the function `blockUSB()`.
To enable the ports, the value of `Start` is set to 3, by the function `unblockUSB()`.

#### Working
Using the `OpenKey()` function of the `winreg` module, the `USBSTOR` key is opened with all access priviledges using the `KEY_ALL_ACCESS` argument. Then using the `SetValueEx()` function, the value of the `Start` DWORD is set to 3 for enabling, and to 4 for disabling the USB ports.
