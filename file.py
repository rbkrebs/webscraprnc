import os


def save_cod(text):

	

	BASE_PATH = os.path.dirname(os.path.abspath(__file__))

	file = open(BASE_PATH + '/_cod.csv', 'a')

	file.write(text+',')
	
	file.close()

def save_td_result(text):


	BASE_PATH = os.path.dirname(os.path.abspath(__file__))

	file = open(BASE_PATH + '/_td_result', 'a')

	file.write(text+'\n')
	file.write("######################\n")
	file.write("######################\n")
	file.write("######################\n")

	file.close()
