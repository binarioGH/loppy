#-*- coding: utf-8-*-
from sys import argv
import subprocess

if __name__ == '__main__':
	if len(argv) != 5:
		print('''
			loppy ocupa 5 argumentos para funcionar
			lop.py -r (rango) -t (ip)''')
		exit()
	else:
		count = 0
		for a in argv:
			if a == "-r":
				rg = argv[count + 1]
				try:
					rg = int(argv[count +1])
				except:
					print("No se puede usar {} como rango".format(rg))
			elif a == "-t":
				ip = argv[count + 1]
			count += 1
		print("ip: {} \nrango: {}".format(ip, rg))



