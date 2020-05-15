### Arbitary Arguments on Function..
def my_function(*kids):
	print('Your Second Child is {}'.format(kids[1]))

my_function("Alex", "Doe", "Bonne")

### Keyword Arguments with Function..
def key_function(**user):
	print('First Name is {} and Last Name is {}'.format(user['fname'], user['lname']))

key_function(fname = "Asad", lname = "Anik")