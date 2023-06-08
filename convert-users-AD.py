#!/usr/bin/python3

import sys


if str(sys.argv[1]) == '-h':
	print("\n[+] USAGE\n")
	print("> python3 convert_users_AD.py Users_file.txt\n\n")
	print("[+] Users_file.txt format:\n")
	print("Username1 Surname1")
	print("Username2 Surname2")
	print("Username3 Surname3")
	print("...")

try:
	file = open(sys.argv[1],'r')
	data=file.readlines()
	usuarios=[]
	for x in data:
		name = x.rstrip()
		usuarios.append(name.split()[0] + name.split()[1]) # NameSurname
		usuarios.append(name.split()[0][0] + name.split()[1]) # NSurname
		usuarios.append(name.split()[0] + name.split()[1][0]) # NameS
		usuarios.append(name.split()[0][0] + '.' + name.split()[1]) # N.Surname
		usuarios.append(name.split()[0] + '.' + name.split()[1][0]) # Name.S
	if len(usuarios)>=1:
		for x in usuarios:
			print(x)
except:
	if str(sys.argv[1]) != '-h':
		print("[!] Error while converting users\n\n")
		print("[+] Use -h option for usage")
