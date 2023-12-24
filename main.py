from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import os
import conf
import requests
import pars_main
import changestatus
import createnewitem

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/5.3.3/bin/tesseract'

#авторизация пользователя
r = requests.post('https://api.officemeister.online/v1/auth', json={"api-key": conf.apikey})
result=r.json()
token=result['token']

#запрашиваем общее количество страниц
url = 'https://api.officemeister.online/v1/jorn/getItems' 
param_request = {'itemtype': '39','page': 11,'range':30}   
headers = {'Authorization': 'Bearer '+token}  
r = requests.get(url, headers=headers, params=param_request)
result=r.json()

for element in range(int(result['pages'])):
	#print(element)
	#запрашиваем общее количество страниц
	url = 'https://api.officemeister.online/v1/jorn/getItems' 
	param_request = {'itemtype': '39','page': element,'range':30}   
	headers = {'Authorization': 'Bearer '+token}  
	r = requests.get(url, headers=headers, params=param_request)
	result=r.json()
	#print(result['items'])

	for item in result['items']:
		if item['statusid'] == '12' or item['statusid'] == '13':
			try:
				
				url = item['docs'][0]['filepath']
				response = requests.get(url)
				index_dot = response.headers['Content-Disposition'].index('.')
				header = response.headers['Content-Disposition'][index_dot + 1::]
				index = item['itemid']
				
				# Обработка файлов PDF
				if header == 'pdf':
					
					# Преобразование файла PDF в JPG
					with open(f'Счета/file_{index}.pdf', 'wb') as file:
						file.write(response.content)
					pages = convert_from_path(f'Счета/file_{index}.pdf', 500, poppler_path='/usr/local/bin')
					for i, page in enumerate(pages):
						if i == 0:
							page.save(f'Счета/file_{index}.jpg', 'JPEG')
						
					# Удаление файла PDF
					os.remove(f'Счета/file_{index}.pdf')
					
					# Преобразование файла JPG в TXT 
					image = Image.open(f'Счета/file_{index}.jpg')
					string = pytesseract.image_to_string(image, lang="rus")
					with open(f'image2text/chek2text{index}.txt', 'a') as f:
						f.write(string.strip()+'\n')

				# Обработка файлов JPG		
				if header == 'jpg':
					
					# Преобразование файла JPG в TXT 
					with open(f'Счета/file_{index}.jpg', 'wb') as file:
						file.write(response.content)
					image = Image.open(f'Счета/file_{index}.jpg')
					string = pytesseract.image_to_string(image, lang="rus")
					with open(f'image2text/chek2text{index}.txt', 'a') as f:
						f.write(string.strip()+'\n')

			# Извлечение реквизитов
				lines_with_AO = pars_main.find_lines_with_keyword_in_first_20_lines(f'image2text/chek2text{index}.txt', 'АО')
				lines_with_OOO = pars_main.find_lines_with_keyword_in_first_20_lines(f'image2text/chek2text{index}.txt', 'ООО')
				pars_result = pars_main.parse_text_file(f'image2text/chek2text{index}.txt', lines_with_AO, lines_with_OOO)
				print(pars_main.parse_text_file(f'image2text/chek2text{index}.txt', lines_with_AO, lines_with_OOO))

				#Создание платежного поручения
				#createnewitem.getPoruchenie(pars_result) # необходимо разобраться с аргументами
				#Смена статуса счета
				#changestatus.status_change(0, item['itemid']) # необходимо разобраться с аргументами

				# Удаление файлов
				os.remove(f'Счета/file_{index}.jpg')
				os.remove(f'image2text/chek2text{index}.txt')

			except IndexError:
				pass
			except ValueError:
				pass
			except FileNotFoundError:
				pass
