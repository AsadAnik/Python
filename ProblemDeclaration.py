# ###The bookstall applications backend...
# #!/usr/bin/python3
#
# # def main():
# #     print('Hello')
# #
# # if __name__ == "__main__" : main()
#
#
# ##Testing the code for python syntex
# print('hi')
#
# ##UserDefined Function..
# def userDefined(username = 'AsadAnik'):
# 	if username is 'AsadAnik':
# 		return 'Welcome!'
# 	else:
# 		return 'User Is invalid here!'
#
# ##The Main function..
# def main():
# 	userDefined()
#
# 	##Get index number with python...
# 	string_text = 'I am just a programmer so!'
#
# 	for index, item in enumerate(string_text):
# 		print('Index {} -> item {}'.format(index, item))
#
# 		if string_text == 'a':
# 			print('index of a is {}'.format(index))
#
# 	##String with loop and controled Else...
# 	s = 'this is our else string'
# 	i = 0
#
# 	while(i < len(s)):
# 		print(s[i], end='')
# 		i += 1
# 	else:
# 		print('Executed Else!')
#
# if __name__ == "__main__" : main()

def main():
	# file = open('READMe2.txt', "a")
	# file.write("fileObject.readline( size )")
	# file.close()
	
	# file = open('READMe2.txt', "r")
	# print(file.read())

	# fileSystemTwo = open('README.txt', "x")

	# fileSystemTwo = open('README.txt', "w")
	# fileSystemTwo.write('I am your Lover, ')

	# fileSystemTwo = open('README.txt', "a")
	# fileSystemTwo.write(' Ohh seems like your another bf comes after me!')

	# fileSystemTwo = open('README.txt', "r")
	# READf = fileSystemTwo.read()
	# print(READf)

	a = open('README.txt', 'w')
	write1 = a.write('PYTHON is my core language')

	a = open('README.txt', 'a')
	write2 = a.write(', First language is C')

	a = open('README.txt', 'r')
	print(a.readline())

	a.close()



if __name__ == "__main__" : main()