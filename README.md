# Security-Manager
A Python program to control critical Windows system functions via Windows registry. 
**Warning:** The program potentially modifies critical Windows registry keys. Please use it in a virtual machine before using on a hardware system, and backup registry before using.

The program uses Python's winreg module to modify Windows registry values to control system functions.
The following functions are supported:
1. Block/Unblock USB ports access
2. Enable/Disable bluetooth
3. Enable/Disable command prompt
4. Block/Unblock facebook.com access

The program should run on all systems with Windows 7, Windows 8, Windows 8.1, Windows 10, or Windows 11. To start the program, run the executable file *security_manager.exe*.

#### Python version and modules 
- Python 3.10
- winreg (default)
- elevate 0.1.3

## Interface

Since most of the functions modify protected registry keys, the Python program (security_manager.py) must be run using a priviledged or admin Command Prompt or Powershell. 
In case the user runs the program in a normal Command Prompt or Powershell, the program automatically asks for Admin control using the UAC prompt. This is discussed in the [Privilege Escalation](#privilege-escalation) section. Adter gaining Admin control, the user must press S to start and access the functions list. To quit the program, any key other than S may be pressed. This prompt is displayed after every function execution.

The program provides a numbered list interface to the user, with each number assigned to a particular functionality:
1. Block USB ports
2. Disable bluetooth
3. Disable command prompt
4. Block Facebook
5. Unblock USB ports
6. Enable bluetooth
7. Enable command prompt
8. Unblock Facebook

A function can be invoked by pressing the key corresponding to that function.

## Functionality

### USB ports access
The functions that control the USB ports access are `blockUSB()` and `unblockUSB()`
The key that controls access to the USB ports in the registry is `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\USBSTOR`
To disable the ports, the value of `Start` must be set to 4. This is done be the function `blockUSB()`.
To enable the ports, the value of `Start` is set to 3, by the function `unblockUSB()`.

#### Working
Using the `OpenKey()` function of the `winreg` module, the `USBSTOR` key is opened with all access priviledges using the `KEY_ALL_ACCESS` argument. Then using the `SetValueEx()` function, the value of the `Start` DWORD is set to 3 for enabling, and to 4 for disabling the USB ports.

### Bluetooth Control
The functions that control bluetooth are `enableBluetooth()` and `disableBluetooth()`. 
The key that controls bluetooth is `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Connectivity\AllowBluetooth`
To enable bluetooth, the value of `value` DWORD is set to 2, while to disable bluetooth, the value is set to 0.
After using the `disableBluetooth()` function, Bluetooth becomes inaccessible, and the Bluetooth controls would be greyed out in the Windows Settings.

#### Working
Using the `OpenKey()` function of the `winreg` module, the `AllowBluetooth` key is opened with all access priviledges using the `KEY_ALL_ACCESS` argument. Then using the `SetValueEx()` function, the value of the `value` DWORD is set to 2 for enabling, and to 0 for disabling Bluetooth.

### Command Prompt Access
The functions that control access to Command Prompt are `enableCMD()` and `disableCMD()`.
By defaut, the keys to control the access to Command Prompt do not exist in the registry. The key `System` must be created under `HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows`.
Under the newly created key, a new DWORD value `DisableCMD` is created and is set to 2, to disable Command Prompt. To enable Command Prompt again, either the value can be deleted or set to 0. 

#### Working
Using the `OpenKey()` function of the `winreg` module, the `Windows` key is opened with all access priviledges using the `KEY_ALL_ACCESS` argument. Then using the `CreateKey()` function, the key `System` is created. Under the newly created key, the value for `DisableCMD` is set to 2 or 0 depending on the function, using the `SetValueEx()` function. The value is automatically added if it doesn't exist.

### Access to Facebook website (or any other website)
At the time of writing this document, no method is known to block access to a website across all browsers, that is, across the whole OS, using registry. Hence, for this project, only Google Chrome is blocked from accessing a website. The program controls only access to facebook.com, but the function can be updated to block any website in Google Chrome.

The key that controls access to websites in Google Chrome is `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\URLBlocklist`. By default, a fresh install of Google Chrome does not create the `Google` key under `Policies`. So it must be created along with the subkeys `Chrome` and `URLBlocklist`. Under the `URLBlocklist` key, a new String value is created with name as the serial number of the website, and value as the domain name. Since the program only handles facebook.com, the value created is `1` with value `facebook.com` (handled by `blockFacebook()`). To remove the block, this value must be deleted (handled by `unblockFacebook()`).

#### Working
Using the `OpenKey()` function of the `winreg` module, the `Policies` key is opened with all access priviledges using the `KEY_ALL_ACCESS` argument. Then using the `CreateKey()` function, the keys `Google`, `Chrome` and `URLBlocklist` are created. Under the `URLBlocklist` key, the String value for domain name is set using `SetValueEx()` function.

## Privilege Escalation
Since most functions like USB ports access control require modifying critical registry keys, the program requires Administrator privileges. While this can be achieved by running the Python script in an escalated Powershell or Command Prompt, a better approach is using the `elevate` module. At the beginning of the program, the `elevated` module's `elevate()` function attempts to get Administrator privileges using Windows User Account Control (UAC) prompt. 

## Executable
The Python program is converted into a Windows executable (exe) using the Pyinstaller module.

## Testing
The program was tested on Windows 10 virtual machine on VirtualBox with following specifications:
- OS: Windows 10 version 1903 (Build 18362.356)
- Virtual Box Version 6.1
- RAM: 12 GB (4 GB to virtual machine)
- Processor: Intel Core i5 3220M
