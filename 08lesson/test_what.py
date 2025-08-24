import requests
from ClassForTest import base_option


base_url = "https://ru.yougile.com"
api = base_option("https://ru.yougile.com")


def test_create_project():
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
    my_new_project = requests.post(base_url+"/api-v2/projects",
    json=body, headers=my_headers)
    my_new_project.json()
    assert my_new_project.status_code == 201
    assert id != my_new_project.json()["id"]
    
    

def test_change_in_project():
    api.companny_list()
    token = api.get_token()
    project = api.get_new_project("BOOO")
    body = {
        "deleted": True,
        "title": "BOOO",
        "users": {}
    }
    my_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    changed_company_id = requests.put(base_url + f"/api-v2/projects/{project}",
    json=body, headers=my_headers)
    changed_company_id.json()
    assert changed_company_id.status_code == 200
    assert project == changed_company_id.json()['id']


def test_get_with_id():  
    api.companny_list()
    token = api.get_token()
    project = api.get_new_project("New one")
    my_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    get_id = requests.get(base_url + f"/api-v2/projects/{project}",
    headers=my_headers)
    get_id.json()
    assert get_id.status_code == 200
    assert get_id.json()["id"] == project