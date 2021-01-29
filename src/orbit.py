import math
from tqdm import tqdm

gran = 4
a = 2.3633 * 149597870691
ai = 2.3633 * 149597870691
e = 0.1459
msun = 1.989*10**30
msteins = 76*1000**(3)*1800
G = 6.67408*10**(-11)
E = -G * msun * msteins / (2*a)
PE = 2*E
t = 0
KE = -E
years = 0
v = (2*KE/msteins)**(1/2) 
for x in tqdm(range(133333333)):
	b = a*(1-e**(2))**(1/2)
	h = (a-b)**(2)/(a+b)**(2)
	C = math.pi*(a+b)*(1+(3*h)/(10+(4-3*h)**(1/2))) / gran
	W = C * -0.71401756407 
	E = E + W
	PE = 2*E
	KE = -E
	v = (2*KE/msteins)**(1/2)
	a = -G*msun*msteins/PE
	years = years + ((C/v)/(60*60*24*365))
print(v)
#print(C)
print(years)
print(ai)
print(a)
print(ai-a)




