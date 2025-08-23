import pytest
import requests
from ClassForTest import base_option


#"id": "d15204b2-4309-4f23-90ae-67b6a404e626",
#"name": "Поток_98.2",
#"isAdmin": true
base_url = "https://ru.yougile.com"
api = base_option("https://ru.yougile.com")




def test_create_company():
    id = api.companny_list()
    token = api.get_token()
    my_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    body = {
        "title": "NextDoor",
        "users": {}
    }
    my_new_company = requests.post(base_url+"/api-v2/projects", json=body, headers=my_headers)
    my_new_company.json()
    assert id == my_new_company.json()['id'] #Негативная
    assert my_new_company.status_code == 201
    assert my_new_company.json()["title"] == "Nextdoor" #Негативная

def test_change_in_company():
    id = api.companny_list()
    token = api.get_token()
    body = {
        "deleted": True,
        "title": "Поток_98.2",
        "users": {}
    }
    
    my_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer +{token}'
    }

    changed_company_id = requests.put(base_url+ f"/api-v2/projects/{id}", json=body, headers=my_headers)
    changed_company_id.json()
    assert changed_company_id.status_code == 200
    assert id == changed_company_id.json()['id']
    assert changed_company_id.json()["deleted"] == False #Негативная



def test_get_with_id():
    
    id = api.companny_list()
    token = api.get_token()
    my_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    get_id = requests.get(base_url+ f"/api-v2/projects/{id}", headers=my_headers)
    get_id.json()
    assert get_id.status_code == 200
    assert get_id.json()["id"] == None #Негативная