import re

x=""

with open("C:\\Users\\administrator\\Desktop\\hacky2018\\9.txt") as f:
	for line in f:
		s = re.compile("vol:\s\d{1,3}")
		m = s.search(line)
		if m:
			x += chr(int(m.group(0).replace("vol: ", "")))
print x