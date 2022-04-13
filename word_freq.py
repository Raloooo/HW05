import sys
import re
print(sys.argv)
filename = sys.argv[1]
n = int(sys.argv[2])

c=0
file = open(filename, mode = 'r')
lines = file.readlines()

dic = dict()
for line in lines:
	line = line.strip()
	new_line = re.sub(r"[^a-zA-Z0-9]"," ", line)
	real_new_line = new_line.split()
	for name in real_new_line:
		dic[name] = dic.get(name,0) + 1

d2 = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))

for key,value in d2.items():
	print("%-10s" %key, "%5d" %value)
	
	c += 1
	if(c==n):
		break
	


file.close()



