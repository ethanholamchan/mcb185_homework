import json
import sys
import gzip

transfac = {'id': '', 'pwm': []}
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		words = line.split()
		
		if words[0] == '//':
			print(json.dumps(transfac, indent=4))
			transfac['pwm'] = []
		
		if words[0] == 'ID': transfac['id'] = words[1]
			
		if line[0] in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}: 
			pwm = {'A': words[1], 'C': words[2], 'G': words[3], 'T': words[4]}
			transfac['pwm'].append(pwm)		
		

