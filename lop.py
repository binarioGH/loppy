#-*-coding:utf-8-*-
from subprocess import run
def validate(ip):
	if ip[:4].lower() == "www.":
		return True
	ip = ip.split(".")
	if len(ip) != 4:
		return False
	for octet in ip:
		try:
			octet = int(octet)
		except:
			return False
		else:
			if octet >= 0 and octet <= 255:
				continue
			return False
	return True

def main():
	iplist = []
	ip = ""
	print("Write 'done' if you are done.")
	while ip != "done":
		ip = input("Input an Ip: ")
		ip = ip.lower()
		if validate(ip):
			iplist.append(ip)
		elif ip == "done":
			continue
		else:
			print("{} is not valid.".format(ip))
	for ip in iplist:
		print("\n\nPinging now {}\n".format(ip))
		print("-"*60+"\n\n")
		run("ping -n 3 {}".format(ip))
		print("\n\n"+"-"*60)



if __name__ == '__main__':
	main()