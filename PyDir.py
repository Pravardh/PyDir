import requests
import sys
import subprocess
import os

def execute(flags):
	if '-s' in flags:
		direc = input("Enter the location of the wordlist, including the name of the file.\nPress enter to use default wordlist\n")
		direc.strip()
		if direc == "":
			print("Using default wordlist")
			#time.sleep(2)
			direc = open("wordlist.txt")
		else:
			try:
				direc = open(direc)
			except FileNotFoundError:
				print("File has not been found. Please check your file path!")
				exit()

		os.system("cls")
		con = direc.readlines()
		url = input("Enter the url\n")
		response = requests.get(url)
		t_url = url
		running = False
		
		if response.status_code == 200:
			for i in con:
				i.rstrip('\n')
				url = t_url+"/"+i
				res = requests.get(url)
				print(f"URL:{url} RESPONSE CODE:{res.status_code}")
					

		else:
			running = False
			print("Website is down. Please check url.")
			exit()


if __name__ == "__main__":
	Uargs = sys.argv
	Uargs.pop(0)
	Sargs = ['-s','-i','-h','-k']
	flags = []
	for i in Uargs:
		if i not in Sargs:
			print(f'Flag {i} is invalid. Try again')
			exit()
		else:
			flags.append(i)
	execute(flags)
			


