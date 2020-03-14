from db import rus, eng
action = input('Eng or Rus:\n')
if action == 'Rus':
	s = input()
	out = ''
	input = []
	output = []
	for i in s:
		input.append(i)
	for c in input:
		output.append(rus[c])
	for x in output:
		out+=x
	print(out)
if action == 'Eng':
	s = input()
	out = ''
	input = []
	output = []
	for i in s:
		input.append(i)
	for c in input:
		output.append(eng[c])
	for x in output:
		out+=x
	print(out)
