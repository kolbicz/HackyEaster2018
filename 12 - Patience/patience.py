import hashlib

h = hashlib.sha1('genesis'+'100000')
print h.hexdigest()

for i in range(99999,0,-1):

	h = hashlib.sha1(h.hexdigest()+str(i))

	
print 'https://hackyeaster.hacking-lab.com/hackyeaster/images/eggs/'+h.hexdigest()+'.png'

