import requests
import conf

def status_change(status_doc, itemid):
#авторизация пользователя
    r = requests.post('https://api.officemeister.online/v1/auth', json={"api-key": conf.apikey})
    result=r.json()

#запрашиваем журнал запросов на оплату
#исходный статус счета, который нам нужен и который мы будем распознавать: 13 - согласован или 12 - новый
#статус куда мы переводим, если распознали удачно: 59 - распознан
#статус куда мы переводим, если распознали неудачно: 60 - ручной ввод 
    url = f'https://api.officemeister.online/v1/jorn/{itemid}/changeStatus' 
    headers = {'Authorization': 'Bearer '+result['token']}  

    if status_doc == 1:
        r = requests.post(url, headers=headers, json={'statusId': '59'} )
        print(r)
    if status_doc == 0:
        r = requests.post(url, headers=headers, json={'statusId': '60'} )
        print(r.text)
    