import sys
import telnetlib
import time

password = "pw"
command = "sh ver"
term = "term len 0"

data = open("hostlist.txt")
for line in data:
    cmd1 = "enable"
    tn = telnetlib.Telnet(line.rstrip())
    tn.set_debuglevel(1)
    time.sleep(2)
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    time.sleep(2)
    tn.write(cmd1.encode('ascii') + b"\n")
    time.sleep(2)
    tn.write(password.encode('ascii') + b"\n")
    time.sleep(2)
    tn.write(term.encode('ascii') + b"\n")
    tn.write(command.encode('ascii') + b"\n")
    time.sleep(2)
    tn.write(b"\n")
    time.sleep(2)
    tn.write(b"\n")
    time.sleep(2)
    tn.write(b"exit\n")
    lastpost = tn.read_all().decode('ascii')
    print(lastpost)
    op=open ("output.txt", "a").write(lastpost)
    tn.close()