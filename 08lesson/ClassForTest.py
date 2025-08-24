import requests


class base_option:

    def __init__(self, url):
        self.base_url = url
        self.login = "rabota.chuguev@gmail.com"
        self.password = "Uoj067ap"
        self.response = None
        self.token = None

    def companny_list(self):
        url = self.base_url + "/api-v2/auth/companies"
        payload = {
        'login': self.login,
        'password': self.password,
        'name': ''}
        headers = {'Content-Type': 'application/json'}
        self.response = requests.post(url, json=payload, headers=headers)
        return self.response.json()["content"][0]['id']

    def get_token(self):
        url = self.base_url + "/api-v2/auth/keys/get"
        payload = {
            'login': self.login,
            'password': self.password,
            'companyId': self.response.json()["content"][0]["id"]}
        headers = {'Content-Type': 'application/json'}
        result = requests.post(url, json=payload, headers=headers)
        self.res_id = result.json()
        return self.res_id[0]["key"]
    
    def get_new_project(self, title):
        url = self.base_url + "/api-v2/projects"
        my_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {self.res_id[0]["key"]}'}
        body = {
        "title": title,
        "users": {}}
        response = requests.post(url, json=body, headers=my_headers)
        return response.json()["id"]