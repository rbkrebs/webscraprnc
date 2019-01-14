# -*- coding: utf-8 -*-


import string
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from file import save_td_result, save_cod

d = webdriver.Firefox()

url = 'http://sistemas.agricultura.gov.br/snpc/cultivarweb/cultivares_registradas.php?acao=pesquisar&postado=1'

def run(link):



	if link is None:
		return

	d.get(link)

	for x in range(3):
		

		request = d.page_source

		soup = BeautifulSoup(request, "html.parser" )

		if soup is None:
			return
		dict_esp = {}
		

		for esp in soup.find_all('tr', class_= re.compile('td_resultado')):
			
			list_cult = []

			
			if esp.td is not None:

				
				nameCient = esp.td.contents[4].replace('\t', '').replace('(', '').replace(')','')
				nameComum = esp.td.contents[3].text
				
				
				for cult in esp.td.div.table.find_all('tr'):

					if cult.contents[3].text.startswith('CULTIVAR'):

													
						for word in cult.contents[1].stripped_strings:

							list_cult.append(word)

						dict_esp[nameCient]= {'nome':nameComum}

						dict_esp[nameCient].update({'cultivares': list_cult})


			
		print(dict_esp)
		

		element = WebDriverWait(d, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@title='Próxima Página']")));	
		
		element.click()
	
		d.get(link)
		print(x)

					
def find_esp(esp):

	for i in soup.find_all('div', id = lambda value:value and value.startswith('cod_especie')):

			if i is None:
				continue	
			
			
			for texto in i.table.find_all('tr'):

				if texto is None:
					continue			
				
				count = 0

				for texto2 in texto.find_all('td'):

					if count == 0:
						print(texto2.text.strip())
					elif count == 1:
						print(texto2.text.strip())

					count+=1

				print('------------------------------')


		
if __name__=="__main__":
	run(url)
	d.quit()