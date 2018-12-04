import random
l = ['do', 'py', 'fulcrum', 'sdk', 'turbine', 'marketplace', 'data-ocean', 'trimble']
r = ''
for i in l:
	if random.random() > 0.5:
		r = r + i
	if random.random() > 0.5:
		r = r + '-'
print(r)
