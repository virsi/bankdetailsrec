import requests
import conf

def getPoruchenie(inn='Не распознано', kpp='Не распознано', bik='Не распознано', account='Не распознано', req='Не распознано', sum='Не распознано'):
	#авторизация пользователя
	r = requests.post('https://api.officemeister.online/v1/auth', json={"api-key": conf.apikey})
	result=r.json()

	url = 'https://api.officemeister.online/v1/jorn/addItem' 
	headers = {'Authorization': 'Bearer '+result['token']}  
	r = requests.post(url, headers=headers, json={'description': 'Распознано роботом', 'itemsubtypeid': 107, 
			'notnamedatributes': {'inn': inn, 'kpp': kpp, 'bik': bik, 'account': account,
			'req': req, 'sum': sum}})
	print(r)
