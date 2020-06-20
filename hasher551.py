##################################################
                #importing libs
import compileall
import  os
import hashlib
import base64
import time
import json
import random
##################################################
                # About
os.system('clear')
Clg = "\033[92m"
info = '''
-----------------------------------------------------
                INFORMATION
          Author      	   Lester551
          Name        	   Anas
          Facebook         Āñås
          Date             ...
          Version          1

* if you find any errors or problems , please contact me

-----------------------------------------------------'''
######################################################
                #colors
Cy = "\033[93m"
Cr = "\033[31m"
Cb = "\033[34m"
Cg = "\033[32m"
Cp = "\033[95m"
###############
Clb = "\033[94m"
Clg = "\033[92m"
Clr = "\033[91m"
Cu = "\033[04m"
###############
###############
Cbr = "\033[41m"
Cbg = "\033[42m"
Cbb = "\033[44m"
Cre = "\033[0m"
#######################################################
def start():
	os.system('clear')
	try:
		os.system('figlet Lester551')
		
	except:
		try:
			os.system('pkg install figlet')
		except:
			pass
	try:
		print (info)
		print (Cre+Cu+'\n\tWelcome to L-crypt tool '+Cy+';)'+Cre+'\n')
		print (Clg+'There are  3 options that you can use ..\n')
		print (Clr+'[☆] '+Cg+'option 0 ==> '+Cre+Cp+'\"0\" '+Cre+Cy+'to exit\n')
		print (Clr+'[☆] '+Cg+'option 1 ==> '+Cre+Cp+'\"compileall\" '+Cre+Cy+'[!] to hash a python script and he will still work\n')
		print (Clr+'[☆] '+Cg+'option 2 ==> '+Cre+Cp+'\"hashlib\" '+Cre+Cy+'[*] md5, base64, base32, sha1, sha512........\n')
		print (Clr+'[☆] '+Cg+'option 3 ==> '+Cre+Cp+'\"crack hash\" '+Cre+Cy+'[*] cracking a hash with a  wordlist'+'\n')
		print (Clr+'[☆] '+Cg+'option 4 ==> '+Cre+Cp+'\"update\" '+Cre+Cy+'looking for a new version'+'\n')
		opt = int(input(Cre+Clb+"please choose an option [0/1/2/3/4] : "+Cre))
	except:
		os.system('clear')
		start()
	try:
		if opt == 1 :
			Compile()
		elif opt == 2 :
			HASHLIB2()
		elif opt == 3 :
			crack()
		elif opt == 0 :
			print (Clg+'[●] thanks for using my tool')
			exit()
		elif opt == 4 :
			try:
				os.system('cd .. && rm -rf hasher551/')
				os.system('cd .. && git clone https://github.com/lester551/hasher551.git')
			except:
				os.system('apt-get install git')
			exit()
		else:
			print (Clg+'\nError, please choose an option from 0 to 4\n')
	except:
		exit()
########################################################
def check():
	list_of_types = ['base64', 'base32','blake2b', 'sha512', 'sha256', 'md5', 'sha3_256', 'sha224', 'sha3_224', 'sha3_512', 'blake2s', 'sha3_384', 'shake_256', 'sha1', 'shake_128', 'sha384']	
	loading = ['.   ','.. ','...']
	if not os.path.exists('saved/') :
		print (Cg+'[●] creating folder '+Clb+'\"saved/\"')
		os.mkdir('saved')
		time.sleep(1)
		print (Clg+'[+] folder '+Clb+'\"saved/\" has been created ...')
		for i in list_of_types:
			try:
				os.makedirs('saved/'+i)
				time.sleep(1)
				print (Clg+'[+] '+Clr+'creating '+'\''+i+'\''+' folder...')
			except FileExistsError :
				pass
	else:
		try:
			time.sleep(1)
			print (Clg+'[●] Checking files...'+Cy)
			time.sleep(1)
			for ii in list_of_types:
				try:
					time.sleep(0)
					os.makedirs('saved/'+ii)
					time.sleep(0)
				except FileExistsError :
					pass
		except FileExistsError :
			pass
		print (Clg+'[●] folders is all exists'+Cy)
		time.sleep(1)
########################################################
def save(type,y,function):
	time.sleep(0)
	print (Cy+'\n╔═══Save this ?'+Cp+' [s] : ')
	print (Cy+'║')
	print (Cy+'╚═══Try again ?'+Cp+' [t] : \n')
	print (Cy+'╔═══Go back '+Cp+' [q] : ')
	print (Cy+'║')
	print (Cy+'╚═══Exit '+Cp+' [any key to exit] : ')
	w = input(Cy+'>>> ')
	if w == 's' or w == 'S' :
		check()
		def s():
			filename = input (Cy+"save file with name  :  "+Cre)
			if not os.path.exists('saved/'+type+'/'+filename):
				file = open('saved/'+type+'/'+filename,'w')
				file.write(y)
				file.close()
			else:
				print (Clr+'[!] this file is already exists')
				s()
		s()
		time.sleep(1)
		print (Clg+'[*] file \"'+filename+'\" was saved')
		time.sleep(0)
		exit()
	elif w == 't' or w == 'T' :
		exec(function)
	elif w == 'q' or w == 'Q' :
		start()
		exit()
	else: 
		print (Clg+'[●] thanks for using my tool')
		exit()
########################################################
								#		option1
def Compile():
	try:
		os.system('figlet Compile')
	except:
		pass
	print (Clr+'#############################################################\n')
	print (Clg+'[*] please enter the \'directory\' name ...\n')
	print (Clg+'[!] the '+Cu+'script '+Cre+Clg+'that you want to hash must be in there\n ')
	print ('[!] enter '+Cu+Cr+'\"q\"'+Cre+Clg+' to go back..')
	x = input(Cy+'\n[●] '+Cy+"the folder name : ")
	if x == "q" :
		start()
		exit()
	else:
		a = compileall
		a.compile_dir(x)
		print (Cg+'[●] Done...\n')
		again = True
		while again == True:
			re = input (Cre+Cy+"do you want to try again [y/n/"+Clr+"q"+Cy+"] : ")
			if re == 'y' or re == 'Y' or re == 'yes' or re == 'YES' :
				Compile()
			elif re == 'n' or re == 'N' or re == 'NO' or re == 'no' :
				print (Clg+'[●] thanks for using my tool')
				exit()
			elif re == 'q'or re == 'Q' :
				start()
				exit()
########################################################
def crack():
	try:
		os.system('figlet cracking')
	except:
		pass
	print (Clr+'#############################################################\n')
	print (Cg+'\"q\" to go back')
	wordlist = input(Cy+"enter your wordlist here : "+Cre)
	if wordlist == 'q' :
		start()
		exit()
	elif wordlist == '' :
		print (Clg+'[●] thanks for using my tool')
		exit()
	try:
		wordlist = open(wordlist,"r").read()
	except:
		print (Clr+'Error, file not found')
		exit()
	hash = input(Cy+"enter your hash here : "+Cre)
	try:
		h128 = int(input("shake_128 needs a key , enter a number for \"shake_128\" : "))
		h256 = int(input("shake_256 needs a key , enter a number for \"shake_256\" : "))
	except:
		print ('Error, please enter a number')
		exit()
	default = 10
	if hash == 'q' :
		exit()
	wordlist = wordlist.split()
	Stime = time.time()
	counter = 1
	for i in wordlist :
		hashedmd5 = hashlib.md5(i.encode()).hexdigest()
		hashedsha1 = hashlib.sha1(i.encode()).hexdigest()
		hashedsha224 = hashlib.sha224(i.encode()).hexdigest()
		hashedsha512 = hashlib.sha512(i.encode()).hexdigest()
		hashedsha384 = hashlib.sha384(i.encode()).hexdigest()
		hashedsha256 = hashlib.sha256(i.encode()).hexdigest()
		hashedblake2b = hashlib.blake2b(i.encode()).hexdigest()
		hashedblake2s = hashlib.blake2s(i.encode()).hexdigest()
		hashedsha3_224 = hashlib.sha3_224(i.encode()).hexdigest()
		hashedsha3_256 = hashlib.sha3_256(i.encode()).hexdigest()
		hashedsha3_384 = hashlib.sha3_384(i.encode()).hexdigest()
		hashedsha3_512 = hashlib.sha3_512(i.encode()).hexdigest()
		hashedshake_256 = hashlib.shake_256(i.encode()).hexdigest(h128)
		hashedshake_128 = hashlib.shake_128(i.encode()).hexdigest(h256)
		time.sleep(0.1)
		counter = str(counter)
		print (Cg+counter+Cr+' : trying >>> '+Clr+i)
		counter = int(counter)
		counter += 1
		counter = str(counter)
		if hashedmd5 == hash :
			print (Clg+'\n[+] Target has been found \n')
			print (hash+Clr+' ===> '+Clg+i)
			print (Cy+'\nthe type is : '+Cp+'md5'+Cre)
			break
		else:
			if hashedblake2s == hash :
				print (Clg+'\n[+] Target has been found \n')
				print (hash+Clr+' ===> '+Clg+i)
				print (Cy+'\nthe type is : '+Cp+'blake2s'+Cre)
				break
			else:
				if hashedblake2b == hash :
					print (Clg+'\n[+] Target has been found \n')
					print (hash+Clr+' ===> '+Clg+i)
					print (Cy+'\nthe type is : '+Cp+'blake2b'+Cre)
					break
				else:
					if hashedsha1 == hash :
						print (Clg+'\n[+] Target has been found \n')
						print (hash+Clr+' ===> '+Clg+i)
						print (Cy+'\nthe type is : '+Cp+'sha1'+Cre)
						break
					else:
						if hashedsha224 == hash :
							print (Clg+'\n[+] Target has been found \n')
							print (hash+Clr+' ===> '+Clg+i)
							print (Cy+'\nthe type is : '+Cp+'sha224'+Cre)
							break
						else:
							if hashedsha256 == hash :
								print (Clg+'\n[+] Target has been found \n')
								print (hash+Clr+' ===> '+Clg+i)
								print (Cy+'\nthe type is : '+Cp+'sha256'+Cre)
								break
							else:
								if hashedsha512 == hash :
									print (Clg+'\n[+] Target has been found \n')
									print (hash+Clr+' ===> '+Clg+i)
									print (Cy+'\nthe type is : '+Cp+'sha512'+Cre)
									break
								else:
									if hashedsha384 == hash :
										print (Clg+'\n[+] Target has been found \n')
										print (hash+Clr+' ===> '+Clg+i)
										print (Cy+'\nthe type is : '+Cp+'sha384'+Cre)
										break
									else:
										if hashedsha3_256 == hash :
											print (Clg+'\n[+] Target has been found \n')
											print (hash+Clr+' ===> '+Clg+i)
											print (Cy+'\nthe type is : '+Cp+'sha3_256'+Cre)
											break
										else:
											if hashedsha3_224 == hash :
												print (Clg+'\n[+] Target has been found \n')
												print (hash+Clr+' ===> '+Clg+i)
												print (Cy+'\nthe type is : '+Cp+'sha3_224'+Cre)
												break
											else:
												if hashedsha3_384 == hash :
													print (Clg+'\n[+] Target has been found \n')
													print (hash+Clr+' ===> '+Clg+i)
													print (Cy+'\nthe type is : '+Cp+'sha3_384'+Cre)
													break
												else:
													if hashedsha3_512 == hash :
														print (Clg+'\n[+] Target has been found \n')
														print (hash+Clr+' ===> '+Clg+i)
														print (Cy+'\nthe type is : '+Cp+'sha3_512'+Cre)
														break
													else:
														if hashedshake_128 == hash :
															print (Clg+'\n[+] Target has been found \n')
															print (hash+Clr+' ===> '+Clg+i)
															print (Cy+'\nthe type is : '+Cp+'shake_128'+Cre)
															break
														else:
															if hashedshake_256 == hash :
																print (Clg+'\n[+] Target has been found \n')
																print (hash+Clr+' ===> '+Clg+i)
																print (Cy+'\nthe type is : '+Cp+'shake_256'+Cre)
																break

	Etime = time.time()
	Ttime = Stime - Etime
	Ttime = int(Ttime)
	Ttime = str(Ttime)
	print (Cy+'\nfinished')
	print (Clg+'Elapsed time '+Cre+'-'+Cre+Ttime+'s')
########################################################
class Encoding():

        def __init__(self):
                pass

        def encodeMd5(self):
                x = input(Cy+"enter your text here : "+Cre)
                y = hashlib.md5(x.encode()).hexdigest()
                print (Cre+Cg+'>>>> '+Cre+y)
                save('md5',y,'Anas.encodeMd5()')

        def encodeSha512(self):
                x = input(Cy+"enter your text here : "+Cre)
                y = hashlib.sha512(x.encode()).hexdigest()
                print (Cre+Cg+'>>>> '+Cre+y)
                save('sha512',y,'Anas.encodeSha512()')

        def encodeSha1(self):
                x = input(Cy+"enter your text here : "+Cre)
                y = hashlib.sha1(x.encode()).hexdigest()
                print (Cre+Cg+'>>>> '+Cre+y)
                save('sha1',y,'Anas.encodeSha1')

        def encodeSha224(self):
                x = input(Cy+"enter your text here : "+Cre)
                y = hashlib.sha224(x.encode()).hexdigest()
                print (Cre+Cg+'>>>> '+Cre+y)
                save('sha224',y,'Anas.encodeSha224()')

        def encodeSha384(self):
                x = input(Cy+"enter your text here : "+Cre)
                y = hashlib.sha384(x.encode()).hexdigest()
                z = str(y)
                print (Cre+Cg+'>>>> '+Cre+z)
                save('sha384',z,'Anas.encodeSha384()')

        def encodeSha256(self):
                x = input(Cy+"enter your text here : "+Cre)
                y = hashlib.sha256(x.encode()).hexdigest()
                print (Cre+Cg+'>>>> '+Cre+y)
                save('sha256',y,'Anas.encodeSha256()')

        def encodeBlake2b(self):
                x = input(Cy+"enter your text here : "+Cre)
                y = hashlib.blake2b(x.encode()).hexdigest()
                print (Cre+Cg+'>>>> '+Cre+y)
                save('blake2b',y,'Anas.encodeBlake2b()')

        def encodeSha3_256(self):
                x = input(Cy+"enter your text here : "+Cre)
                y = hashlib.sha3_256(x.encode()).hexdigest()
                print (Cre+Cg+'>>>> '+Cre+y)
                save('sha3_256',y,'Anas.encodeSha3_256()')

        def encodeSha3_224(self):
                x = input(Cy+"enter your text here : "+Cre)
                y = hashlib.sha3_224(x.encode()).hexdigest()
                print (Cre+Cg+'>>>> '+Cre+y)
                save('sha3_224',y,'Anas.encodeSha3_224()')

        def encodeSha3_512(self):
                x = input(Cy+"enter your text here : "+Cre)
                y = hashlib.sha3_512(x.encode()).hexdigest()
                print (Cre+Cg+'>>>> '+Cre+y)
                save('sha3_512',y,'Anas.encodeSha3_512()')

        def encodeSha3_384(self):
                x = input(Cy+"enter your text here : "+Cre)
                y = hashlib.sha3_384(x.encode()).hexdigest()
                print (Cre+Cg+'>>>> '+Cre+y)
                save('sha3_384',y,'Anas.encodeSha3_384()')

        def encodeBlake2s(self):
                x = input(Cy+"enter your text here : "+Cre)
                y = hashlib.blake2s(x.encode()).hexdigest()
                print (Cre+Cg+'>>>> '+Cre+y)
                save('blake2s',y,'Anas.encodeBlake2s()')

        def encodeShake_256(self):
                x = input(Cy+"enter your text here : "+Cre)
                m = int(input("shake_256 needs a key , enter a number, ! what ever !  : "))
                y = hashlib.shake_256(x.encode()).hexdigest(m)
                print (Cre+Cg+'>>>> '+Cre+y)
                save('shake_256',y,'Anas.encodeShake_256()')

        def encodeShake_128(self):
                x = input(Cy+"enter your text here : "+Cre)
                m = int(input("shake_128 needs a key , enter a number, ! what ever !  : "))
                y = hashlib.shake_128(x.encode()).hexdigest(m)
                print (Cre+Cg+'>>>> '+Cre+y)
                save('shake_128',y,'Anas.encodeShake_128()')

        def encodeBase64(self):
                x = input(Cy+"enter your text here : "+Cre).encode()
                y = base64.b64encode(x)
                z = str(y)
                print (Cre+Cg+'>>>> '+Cre+z)
                save('base64',z,'Anas.encodeBase64()')

        def encodeBase32(self):
                x = input(Cy+"enter your text here : "+Cre).encode()
                y = base64.b32encode(x)
                z = str(y)
                print (Cre+Cg+'>>>> '+Cre+z)
                save('base32',z,'Anas.encodeBase32()')

class Decoding():

        def decodeBase64(self):
                x = input(Cy+"enter your text here : "+Cre).encode()
                y = base64.b64decode(x)
                z = str(y)
                print (Cre+Cg+'>>>> '+Cre+z)
                save('base64',z,'Harbass.decodeBase64()')

        def decodeBase32(self):
                x = input(Cy+"enter your text here : "+Cre).encode()
                y = base64.b32decode(x)
                z = str(y)
                print (Cre+Cg+'>>>> '+Cre+z)
                save('base32',z,'Harbass.decodeBase32()')

Anas = Encoding()
Harbass = Decoding()
########################################################
									#		option2
def HASHLIB2():
	try:
		os.system('figlet hashlib')
		print (Clr+'#############################################################'+Cre)
	except:
		pass
	print (Cy+'hash a text >>> 1')
	print ('choose a file >>> 2')
	try:
		f_or_t = int(input(">>> : "+Cre))
	except:
		HASHLIB2()
		exit()
	if f_or_t == 2 :
		file = input(Cy+"your file : "+Cre)
		try:
			file = open(file,"r").read()
		except:
			print (Clr+'[!]'+Clg+'file not found')
		print (Clr+'#############################################################'+Cre)
		print ('''\n{'base64', 'base32','blake2b', 'sha512', 'sha256', 'md5', 'sha3_256', 'sha224', 'sha3_224', 'sha3_512', 'blake2s', 'sha3_384', 'shake_256', 'sha1', 'shake_128', 'sha384\n'}''')
		print (Cg+'[!] enter '+Cu+Cr+'\"q\"'+Cre+Cg+' to go back !!\n')
		type = input(Cy+'choose a type of hashing : '+Cre)
		def encodeMd5():
			x = file
			y = hashlib.md5(x.encode()).hexdigest()
			print (Cre+Cg+'>>>> '+Cre+y)
			save('md5',y,'encodeMd5()')
		def encodeSha512():
			x = file
			y = hashlib.sha512(x.encode()).hexdigest()
			print (Cre+Cg+'>>>> '+Cre+y)
			save('sha512',y,'Anas.encodeSha512()')
		def encodeSha1():
			x = file
			y = hashlib.sha1(x.encode()).hexdigest()
			print (Cre+Cg+'>>>> '+Cre+y)
			save('sha1',y,'Anas.encodeSha1')
		def encodeSha224():
			x = file
			y = hashlib.sha224(x.encode()).hexdigest()
			print (Cre+Cg+'>>>> '+Cre+y)
			save('sha224',y,'Anas.encodeSha224()')
		def encodeSha384():
			x = file
			y = hashlib.sha384(x.encode()).hexdigest()
			z = str(y)
			print (Cre+Cg+'>>>> '+Cre+z)
			save('sha384',z,'Anas.encodeSha384()')
		def encodeSha256():
			x = file
			y = hashlib.sha256(x.encode()).hexdigest()
			print (Cre+Cg+'>>>> '+Cre+y) 
			save('sha256',y,'Anas.encodeSha256()')
		def encodeBlake2b():
			x = file
			y = hashlib.blake2b(x.encode()).hexdigest()
			print (Cre+Cg+'>>>> '+Cre+y)
			save('blake2b',y,'Anas.encodeBlake2b()')
		def encodeSha3_256():
			x = file
			y = hashlib.sha3_256(x.encode()).hexdigest()
			print (Cre+Cg+'>>>> '+Cre+y)
			save('sha3_256',y,'Anas.encodeSha3_256()')
		def encodeSha3_224():
			x = file
			y = hashlib.sha3_224(x.encode()).hexdigest()
			print (Cre+Cg+'>>>> '+Cre+y)
			save('sha3_224',y,'Anas.encodeSha3_224()')
		def encodeSha3_512():
			x = file
			y = hashlib.sha3_512(x.encode()).hexdigest()
			print (Cre+Cg+'>>>> '+Cre+y)
			save('sha3_512',y,'Anas.encodeSha3_512()')
		def encodeSha3_384():
			x = file
			y = hashlib.sha3_384(x.encode()).hexdigest()
			print (Cre+Cg+'>>>> '+Cre+y)
			save('sha3_384',y,'Anas.encodeSha3_384()')
		def encodeBlake2s():
			x = file
			y = hashlib.blake2s(x.encode()).hexdigest()
			print (Cre+Cg+'>>>> '+Cre+y)
			save('blake2s',y,'Anas.encodeBlake2s()')
		def encodeShake_256():
			x = file
			m = int(input("shake_256 needs a key , enter a number, ! what ever !  : "))
			y = hashlib.shake_256(x.encode()).hexdigest(m)
			print (Cre+Cg+'>>>> '+Cre+y)
			save('shake_256',y,'Anas.encodeShake_256()')
		def encodeShake_128():
			x = file
			m = int(input("shake_128 needs a key , enter a number, ! what ever !  : ")) 
			y = hashlib.shake_128(x.encode()).hexdigest(m)
			print (Cre+Cg+'>>>> '+Cre+y)
			save('shake_128',y,'Anas.encodeShake_128()')
		def encodeBase64():
			x = file.encode()
			y = base64.b64encode(x)
			z = str(y)
			print (Cre+Cg+'>>>> '+Cre+z)
			save('base64',z,'Anas.encodeBase64()')
		def encodeBase32():
			x = file.encode()
			y = base64.b32encode(x)
			z = str(y)
			print (Cre+Cg+'>>>> '+Cre+z)
			save('base32',z,'Anas.encodeBase32()')
		def decodeBase64():
			x = file.encode()
			y = base64.b64decode(x)
			z = str(y)
			print (Cre+Cg+'>>>> '+Cre+z)
			save('base64',z,'Harbass.decodeBase64()')
		def decodeBase32():
			x = file.encode()
			y = base64.b32decode(x)
			z = str(y)
			print (Cre+Cg+'>>>> '+Cre+z)
			save('base32',z,'Harbass.decodeBase32()')
		try:
			if type == 'q' :
				start()
			elif type == 'md5' :
				encodeMd5()
			elif type == 'sha512' :
				encodeSha512()
			elif type == 'sha256' :
				encodeSha512()
			elif type == 'sha224' :
				encodeSha224()
			elif type == 'sha384' :
				encodeSha384()
			elif type == 'sha1' :
				encodeSha1()
			elif type == 'base64' :
				print (Cy+'encode >>> 1\ndecode >>> 2'+Cre)
				m = input ('>>> ')
				if m == '1' :
					encodeBase64()
				elif m == '2' :
					decodeBase64()
			elif type == 'base32' :
				print (Cy+'encode >>> 1\ndecode >>> 2'+Cre)
				m = input('>>> ')
				if m == '1' :
					encodeBase32()
				elif m == '2' :
					decodeBase32()
			elif type == 'blake2b':
				encodeBlake2b()
			elif type == 'blake2s':
				encodeBlake2s()
			elif type == 'shake_256':
				encodeShake_256()
			elif type == 'shake_128':
				encodeShake_128()
			elif type == 'sha3_256' :
				encodeSha3_256()
			elif type == 'sha3_224' :
				encodeSha3_224()
			elif type == 'sha3_384' :
				encodeSha3_384()
			elif type == 'sha3_512' :
				encodeSha3_512()
		except:
			exit()
	elif f_or_t == 1 :
		print (Clr+'#############################################################'+Cre)
		print ('''\n{'base64', 'base32','blake2b', 'sha512', 'sha256', 'md5', 'sha3_256', 'sha224', 'sha3_224', 'sha3_512', 'blake2s', 'sha3_384', 'shake_256', 'sha1', 'shake_128', 'sha384\n'}''')
		print (Cg+'[!] enter '+Cu+Cr+'\"q\"'+Cre+Cg+' to go back !!\n')
		type = input(Cy+'choose a type of hashing : '+Cre)
		if type == 'q' :
			start()
		try:
			if type == 'md5' :
				Anas.encodeMd5()
			elif type == 'sha512' :
				Anas.encodeSha512()
			elif type == 'sha256' :
				Anas.encodeSha512()
			elif type == 'sha224' :
				Anas.encodeSha224()
			elif type == 'sha384' :
				Anas.encodeSha384()
			elif type == 'sha1' :
			    Anas.encodeSha1()
			elif type == 'base64' :
				print (Cy+'encode >>> 1\ndecode >>> 2'+Cre)
				m = input ('>>> ')
				if m == '1' :
					Anas.encodeBase64()
				elif m == '2' :
					Harbass.decodeBase64()
			elif type == 'base32' :
				print (Cy+'encode >>> 1\ndecode >>> 2'+Cre)
				m = input('>>> ')
				if m == '1' :
					Anas.encodeBase32()
				elif m == '2' :
					Harbass.decodeBase32()
			elif type == 'blake2b':
				Anas.encodeBlake2b()
			elif type == 'blake2s':
				Anas.encodeBlake2s()
			elif type == 'shake_256':
				Anas.encodeShake_256()
			elif type == 'shake_128':
				Anas.encodeShake_128()
			elif type == 'sha3_256' :
				Anas.encodeSha3_256()
			elif type == 'sha3_224' :
				Anas.encodeSha3_224()
			elif type == 'sha3_384' :
				Anas.encodeSha3_384()
			elif type == 'sha3_512' :
				Anas.encodeSha3_512()
		except:
			exit()
start()