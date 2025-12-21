import requests
from config import Config

class ProjectApi():
    def __init__(self, url):
        self.url = url
        self.base_url = f"{Config.API_URL}/projects"
        self.headers = Config.HEADERS
        self.company_id = None
        self.token = None
        self.project_id = None
        self.new_project_id = None

    # Получить ID компании
    def get_company_id(self, login='rbatmanov@mail.ru', password='4245590Rb', name='Руслан Батманов'):
        creds = {
            'login': login,
            'password': password,
           # 'name': name 
        }
        resp = requests.post(self.url + '/auth/companies', json=creds)
        result = resp.json()
        self.company_id = result['content'][0]['id']
        return {'id': self.company_id} 
    
    # Получить токен авторизации
    def get_token(self, login='rbatmanov@mail.ru', password='4245590Rb'):
        creds = {
            'login': login,
            'password': password,
            'companyId': self.company_id  
        }
        resp = requests.post(self.url + '/auth/keys', json=creds)
        result = resp.json()
        self.token = result.get('key')
        self.headers['Authorization'] = f"Bearer {self.token}"  # Обновление заголовков
        return result

    # Создать проект
    def create_project(self, title='Test Project'):
        project = {
            'title': title
        }
        resp = requests.post(self.base_url, json=project, headers=self.headers)
        result = resp.json()
        self.project_id = result.get('id')
        return result
    
    # Негативный
    def create_project_negative(self, title=None):
        project = {
            'title': title
        }
        resp = requests.post(self.base_url, json=project, headers=self.headers)
        print(f"Status Code: {resp.status_code}")
        print(f"Response Body: {resp.text}")
        return resp

    # Изменить проект
    def update_project(self, new_title='Project_Test123'):
        project = {
            'new_title': new_title,
            'title': new_title
        }
        resp = requests.put(self.base_url + f'/{self.project_id}', json=project, headers=self.headers)
        result = resp.json()
        self.new_project_id = result.get('id')
        return result
    
    # Изменить проект негативный
    def update_project_negative(self, new_title='ProjectNegativ'):
        project = {
            'new_title': new_title,
            'title': new_title
        }
        resp = requests.put(self.url + f'/projects/{None}', json=project)
        result = resp.json()
        self.project_update_id = result.get('id')
        return result

    # Получить по ID
    def get_project_by_ID(self):
        resp = requests.get(self.base_url + f'/{self.project_id}', headers=self.headers)
        print(f"Status Code: {resp.status_code}")
        print(f"Response Body: {resp.text}")
        return resp.json()
    
    # Получить по ID негативный
    def get_project_by_ID_negative(self):
        resp = requests.get(self.url + f'/projects')
        return resp.json()
