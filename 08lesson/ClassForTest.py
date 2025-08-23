import requests

class base_option:

    def __init__(self, url):
        self.base_url = url
        self.login = "real_login_here"
        self.password = "real_password_here"
        self.response = None 


    def companny_list(self):
        url = self.base_url +"/api-v2/auth/companies"
        payload = {
        'login': self.login,
        'password': self.password,
        'name': ''}
        headers = {'Content-Type': 'application/json'}
        self.response = requests.post(url, json=payload, headers=headers)
        return self.response.json()["content"][0]['id']



    def get_token(self):
        url = self.base_url +"/api-v2/auth/keys/get"
        payload = {
            'login': self.login,
            'password': self.password,
            'companyId': self.response.json()["content"][0]["id"]
        }
        headers = {'Content-Type': 'application/json'}
        result = requests.post(url, json=payload, headers=headers)
        res_id = result.json()
        return res_id[0]["key"]
