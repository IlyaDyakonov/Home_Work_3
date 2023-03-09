import requests
from pprint import pprint
import json

token = "y0_AgAAAAAzrw5RAADLWwAAAADd26C4gnb22TsxRIeN6EFmr8L29TR5EOs"

class YaUploader:
    def __init__(self, token):
        self.token = token
        self.yandex_url = "https://cloud-api.yandex.net/"

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
    
    def get_files_list(self):
        files_url = f'{self.yandex_url}v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(url = files_url, headers=headers)
        return response.json()

    def upload(self, disk_file_path):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = f'{self.yandex_url}v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href_response = self.upload(disk_file_path=disk_file_path)
        href = href_response.get("href", "")
        response = requests.put(url=href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    ya = YaUploader(token = token)
    ya.upload_file_to_disk('HomeWorks/HW_text.txt', filename='text.txt')