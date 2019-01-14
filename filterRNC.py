import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))



def filter_file_rnc(file):

	file = open(file)
	print('file openned')
	file_read = file.read()
	list_rnc = []
	for i in file_read:
		while i != ''
	file.close()
	print(len(list_rnc))


file = BASE_PATH+'/_cod.csv'
print(file)

filter_file_rnc(file)