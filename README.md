# Security-Manager
A Python program to control critical Windows system functions via Windows registry. 

The program uses Python's winreg module to modify Windows registry values to control system functions.
The following functions are supported:
1. Block/Unblock USB ports access
2. Enable/Disable bluetooth
3. Enable/Disable command prompt
4. Block/Unblock facebook.com access

### Interface

Since most of the functions modify protected registry keys, the Python program (security_manager.py) must be run using a priviledged or admin Command Prompt or Powershell. 
In case the user runs the program in a normal Command Prompt or Powershell, the program automatically asks for Admin control using the UAC prompt. This is discussed in the **Admin Control** section. Adter gaining Admin control, the user must press S to start and access the functions list. To quit the program, any key other than S may be pressed. This prompt is displayed after every function execution.

The program provides a numbered list interface to the user, with each number assigned to a particular functionality:
1. Block USB ports
2. Disable bluetooth
3. Disable command prompt
4. Block Facebook
5. Unblock USB ports
6. Enable bluetooth
7. Enable command prompt
8. Unblock Facebook



### USB ports access
The functions that control the USB ports access are `blockUSB()` and `unblockUSB()`
The key that controls access to the USB ports in the registry is `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\USBSTOR`
To disable the ports, the value of `Start` must be set to 4. This is done be the function `blockUSB()`.
To enable the ports, the value of `Start` is set to 3, by the function `unblockUSB()`.

#### Working
Using the `OpenKey()` function of the `winreg` module, the `USBSTOR` key is opened with all access priviledges using the `KEY_ALL_ACCESS` argument. Then using the `SetValueEx()` function, the value of the `Start` DWORD is set to 3 for enabling, and to 4 for disabling the USB ports.
