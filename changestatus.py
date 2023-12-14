import requests
import conf

def status_change(type):
#авторизация пользователя
    r = requests.post('https://api.officemeister.online/v1/auth', json={"api-key": conf.apikey})
    result=r.json()

#запрашиваем журнал запросов на оплату
#исходный статус счета, который нам нужен и который мы будем распознавать: 13 - согласован или 12 - новый
#статус куда мы переводим, если распознали удачно: 59 - распознан
#статус куда мы переводим, если распознали неудачно: 60 - ручной ввод 
    url = 'https://api.officemeister.online/v1/jorn/5768/changeStatus' 
    headers = {'Authorization': 'Bearer '+result['token']}  

    if type == 1:
        r = requests.post(url, headers=headers, json={'statusId': '59'} )
        print(r)
    if type == 0:
        r = requests.post(url, headers=headers, json={'statusId': '60'} )
        print(r)
    