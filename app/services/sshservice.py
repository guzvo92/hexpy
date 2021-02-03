import paramiko

outputfile ="paramiko.log"

def paramikoop(hostname,command):
	print("Paramiko op")

	try: 
		port = 22
		client = paramiko.SSHClient()
		client.load_system_host_keys()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(hostname, port=22, username="gman", password="nkgc69mk")
		(stdin,stdout,stderr) = client.exec_command(command)
		cmd_output= stdout.read()
		print("[Log print]: ",command,cmd_output)

		with open(outputfile,"w+") as file:
			file.write(str(cmd_output))
			return outputfile
	finally:
		client.close()

paramikoop("192.168.15.10","ls")