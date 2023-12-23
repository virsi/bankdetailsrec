import requests
import conf

def getPoruchenie(massiv):
	#авторизация пользователя
	r = requests.post('https://api.officemeister.online/v1/auth', json={"api-key": conf.apikey})
	result=r.json()

	url = 'https://api.officemeister.online/v1/jorn/addItem' 
	headers = {'Authorization': 'Bearer '+result['token']}  
	r = requests.post(url, headers=headers, json={'description': 'Распознано роботом', 'itemsubtypeid': 107, 
			'notnamedatributes': {'inn': massiv['инн'], 'kpp': massiv['кпп'], 'bik': massiv['бик'], 'account': massiv['сч. №'],
			'req': None, 'sum': None}})
	print(r)
