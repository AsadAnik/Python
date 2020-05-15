###The Looping methods with python...
### While.. (Fibonacci Series Numbers)
a, b = 0, 1

while b < 150:
	print(b, end=' ')
	a, b = b, a + b

print('\n')

### For.. (Many Examples)
some_string = "Hello how are your all !"

for item in some_string:
	print(item)

print('\n')

for item in some_string:
	print(item, end='')

print('\n')

## Get Items and Keys with traverse..
for index, item in enumerate(some_string):
	print('Index [{}] -> {}'.format(index, item))

print('\n')

## With Conditions.
for index, item in enumerate(some_string):
	if item == 'o': print('index {} = {}'.format(index, item))

print('\n')

for item in some_string:
	if item == 'o':
		continue
	print(item, end='')

print('\n')

for item in some_string:
	if item == 'y':
		break
	print(item, end='')

print('\n')

###Traversing the iterator with while loop manually and Else...
i = 0
while i < len(some_string):
	print(some_string[i], end='')
	i += 1
else:
	print('ELSED')
