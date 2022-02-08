import requests
import json

with open('/Users/artemstarodubtsev/PycharmProjects/pythonProject/Files/course_profile.txt', 'r') as file_object:
    token = file_object.readlines()[3].strip()

url = 'https://cloud-api.yandex.net/v1/disk/resources/'
headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(token)}


def make_new_directory(directory_name):
    params = {'path': directory_name}
    req = requests.put(url = url, params = params, headers = headers)
    if req.status_code == 201:
        print(f'Папка {directory_name} создана.')

    elif req.status_code == 409:
        print(f'Папка {directory_name} уже существует.')

    else:
        print(f'Bad response {req.status_code}')
        print(req.text)

    return req.status_code


if __name__ == '__main__':

    def directory_name_request():
        directory_name = str(input('Введите название папки, в которую загрузить фотографии на Яндекс.Диск: '))
        return directory_name

    directory = directory_name_request()
    make_new_directory(directory)
