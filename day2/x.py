def pgcd(a,b):  
   while a != b : 
      if a>b:
      	a-=b
      else:
      	b-=a
   return a
with open("input.txt","r") as f:
    lines = f.readlines()
b=0
a=0
for line in lines:
	line.strip('/n')
	extracted=[int(s) for s in line.split() if s.isdigit()]
	mini=min(map(int,extracted))
	maxi=max(map(int,extracted))
	b+= maxi-mini
# part 2
	for x in range(len(extracted)-1):
		for y in range(x+1,len(extracted)):	
			if pgcd(extracted[y],extracted[x])==extracted[x] or pgcd(extracted[y],extracted[x])==extracted[y]:
				if extracted[x]>extracted[y]:
					a+=extracted[x]//extracted[y]
				else:
					a+=extracted[y]//extracted[x]
				break

#print b
print a
	

