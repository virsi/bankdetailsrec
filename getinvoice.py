import requests
import conf

#авторизация пользователя
r = requests.post('https://api.officemeister.online/v1/auth', json={"api-key": conf.apikey})
result=r.json()

#запрашиваем журнал запросов на оплату
url = 'https://api.officemeister.online/v1/jorn/getItems' 
param_request = {'itemtype': '7'}   
headers = {'Authorization': 'Bearer '+result['token']}  
r = requests.get(url, headers=headers, params=param_request)
result=r.json()
#print(result['items'])


for item in result['items']:
	try:

		url = item['docs'][0]['filepath']
		response = requests.get(url)
		index_dot = response.headers['Content-Disposition'].index('.')
		header = response.headers['Content-Disposition'][index_dot + 1::]
		index = item['itemid']
		if header == 'pdf':
			with open(f'Счета/file_{index}.pdf', 'wb') as file:
				file.write(response.content)
		if header == 'jpg':
			with open(f'Счета/file_{index}.jpg', 'wb') as file:
				file.write(response.content)
		#if header == 'xls':
		#	with open(f'Счета/file_{index}.xls', 'wb') as file:
		#		file.write(response.content)

	except IndexError:

		pass

