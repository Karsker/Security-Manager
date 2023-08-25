import winreg as wrg
import os
import elevate

# Function to check if the current session has admin priviledges
def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False

access_reg = wrg.ConnectRegistry(None, wrg.HKEY_LOCAL_MACHINE)


# Function to unblock USB ports
def unblockFacebook():
	try:
		policies = wrg.OpenKey(access_reg, r'SOFTWARE\\Policies', 0, wrg.KEY_ALL_ACCESS | wrg.KEY_WOW64_64KEY)
		try:
			google = wrg.CreateKey(policies, 'Google')
			chrome = wrg.CreateKey(google, 'Chrome')
			blocklist = wrg.CreateKey(chrome, 'URLBlocklist')
			wrg.DeleteValue(blocklist, '1')
			print("Successfully unblocked facebook.com")
		except:
			print("Error deleting key")
	except:
		print("Error opening base key")

# Function to block facebook (can work for any website)
def blockFacebook():
	try:
		policies = wrg.OpenKey(access_reg, r'SOFTWARE\\Policies', 0, wrg.KEY_ALL_ACCESS | wrg.KEY_WOW64_64KEY)
		try:
			google = wrg.CreateKey(policies, 'Google')
			chrome = wrg.CreateKey(google, 'Chrome')
			blocklist = wrg.CreateKey(chrome, 'URLBlocklist')
			wrg.SetValueEx(blocklist, '1', 0, wrg.REG_SZ, 'facebook.com')
			print("Successfully blocked facebook.com")
		except:
			print("Error creating key")
	except:
		print("Error opening base key")

# Function to unblock USB ports
def unblockUSB():
	# Store the path to the key
	try:
		usbstor = wrg.OpenKey(access_reg, 'SYSTEM\\CurrentControlSet\\Services\\USBSTOR', 0, wrg.KEY_ALL_ACCESS | wrg.KEY_WOW64_64KEY)
	except:
		print("Could not open the key")
	# print(usbstor)

	try:
		wrg.SetValueEx(usbstor, "Start", 0, wrg.REG_DWORD, 3)
		print("Successfully unblocked the USB ports")
	except:
	 	print("Couldn't unblock the USB ports")
	if usbstor:
		wrg.CloseKey(usbstor)
	# input("Press Enter to continue")

# Function to block USB ports
def blockUSB():
	# Store the path to the key
	try:
		usbstor = wrg.OpenKey(access_reg, 'SYSTEM\\CurrentControlSet\\Services\\USBSTOR', 0, wrg.KEY_ALL_ACCESS | wrg.KEY_WOW64_64KEY)
	except:
	 	print("Could not open the key")
	# print(usbstor)

	try:
		wrg.SetValueEx(usbstor, "Start", 0, wrg.REG_DWORD, 4)
		print("Successfully blocked the USB ports")
	except:
	 	print("Couldn't block the USB ports")
	if usbstor:
		wrg.CloseKey(usbstor)


# Function to disable bluetooth (requires reboot)
def disableBluetooth():
	try:
		bluetooth = wrg.OpenKey(access_reg, r'SOFTWARE\\Microsoft\\PolicyManager\\default\\Connectivity\\AllowBluetooth', 0, wrg.KEY_ALL_ACCESS | wrg.KEY_WOW64_64KEY)
	except:
		print('Could not open the key')
	# print(bluetooth)

	try:
		wrg.SetValueEx(bluetooth, "value", 0, wrg.REG_DWORD, 0)
		print("Successfully disabled bluetooth")
	except:
		print("Couldn't disable bluetooth")
	if bluetooth:
		wrg.CloseKey(bluetooth)

# Function to enable bluetooth
def enableBluetooth():
	try:
		bluetooth = wrg.OpenKey(access_reg, r'SOFTWARE\\Microsoft\\PolicyManager\\default\\Connectivity\\AllowBluetooth', 0, wrg.KEY_ALL_ACCESS | wrg.KEY_WOW64_64KEY)
	except:
		print('Could not open the key')
	# print(bluetooth)

	try:
		wrg.SetValueEx(bluetooth, "value", 0, wrg.REG_DWORD, 2)
		print("Successfully enabled bluetooth")
	except:
		print("Could not enable bluetooth")
	if bluetooth:
		wrg.CloseKey(bluetooth)

# Function to disable CMD
def disableCMD():
	path = wrg.ConnectRegistry(None, wrg.HKEY_CURRENT_USER)
	try:
		windows = wrg.OpenKey(path, r'Software\\Policies\\Microsoft\\Windows', 0, wrg.KEY_ALL_ACCESS | wrg.KEY_WOW64_64KEY)
	except:
		print("Error opening base key")
	try:

		system = wrg.CreateKey(windows,'System')
		# print(system)
		try:
			wrg.SetValueEx(system, "DisableCMD", 0, wrg.REG_DWORD, 2)
			print("Succesfully disabled CMD")
		except:
			print("Error disabling CMD")
	except:
			print("Error creating key")
	if path:
		wrg.CloseKey(path)

# Function to enable CMD
def enableCMD():
	path = wrg.ConnectRegistry(None, wrg.HKEY_CURRENT_USER)
	try:
		windows = wrg.OpenKey(path, r'Software\\Policies\\Microsoft\\Windows', 0, wrg.KEY_ALL_ACCESS | wrg.KEY_WOW64_64KEY)
	except:
		print("Error opening base key")
	try:

		system = wrg.CreateKey(windows,'System')
		# print(system)
		try:
			wrg.SetValueEx(system, "DisableCMD", 0, wrg.REG_DWORD, 0)
			print("Succesfully enabled CMD")
		except:
			print("Error enabling CMD")
	except:
			print("Error creating key")
	if path:
		wrg.CloseKey(path)

def main():
	# Provide a list interface to the user
	print("Select operation to perform: ")
	print("1. Block USB ports")
	print("2. Disable bluetooth")
	print("3. Disable command prompt")
	print("4. Block Facebook")
	print("5. Unblock USB ports")
	print("6. Enable bluetooth")
	print("7. Enable command prompt")
	print("8. Unblock Facebook")
	op = int(input("Enter function number: "))
	if op == 1:
		blockUSB()
	elif op == 2:
		disableBluetooth()
	elif op == 3:
		disableCMD()
	elif op == 4:
		blockFacebook()
	elif op == 5:
		unblockUSB()
	elif op == 6:
		enableBluetooth()
	elif op == 7:
		enableCMD()
	elif op == 8:
		unblockFacebook()



if __name__=='__main__':
	elevate.elevate() # Get admin priviledges
	while(True): # Keep running the program until the user wants to quit
		print("Press S to start, Q to quit: ")
		choice = input()
		if (choice == 'S'):
			main()
		else:
			break