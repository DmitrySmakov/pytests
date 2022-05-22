from datetime import date
import requests
import pprint


class YaDisk:
    def __init__(self, token_ya_file):
        with open(token_ya_file, "r", encoding="utf-8") as file:
            self.token = file.read()
        self.folder = str(date.today())  # +'/'  нужна ли эта переменная она используется внутри одного метода

    def headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': 'OAuth ' + self.token}

    def get_link(self, path):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        # print(self.folder)
        # print(path)
        path = self.folder+'/'+path    # не самое удачное место
        params = {"path": path, "overwrite": "true"}
        # print(path)
        response = requests.get(url=url, headers=self.headers(), params=params)
        # print(response.json())
        return response.json()

    def new_folder(self, folder):
        # folder = str(input('Введите имя папки (Enter: по умолчанию текущая дата): '))
        if folder.strip():
            self.folder = folder

        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {"path": self.folder, "overwrite": "true"}
        response = requests.put(url=url, headers=self.headers(), params=params)
        return response

    def upload(self, filename):
        href = self.get_link(filename)['href']
        # print(href)
        response = requests.put(href, headers=self.headers(), data=open(filename, "rb"))
        return response

    def ckeck_file(self, filename ):
        url = "https://cloud-api.yandex.net/v1/disk/resources/"
        path = filename
        params = {"path": path}
        response = requests.get(url=url, headers=self.headers(), params=params)
        return response


    def upload_from_url(self, filename):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        path = filename
        url_param = 'https://sun9-19.userapi.com/s/v1/ig2/-oXfur1-uux9L9KiwVRouw2oiZvMKyMC5BGz-av5ttR5fUqQo__Ec1cW3Q4xYoi_MkvITWHlYCszmAH1ws5fFt_3.jpg?size=1388x1852&quality=95&type=album'
        params = {"path": path ,"url": url_param}
        response = requests.post(url=url, headers=self.headers(), params=params)
        return response


# ya = YaDisk('token_ya.txt')
# # ya.new_folder()
# res = ya.ckeck_file('IMG_3397.JPG')
# print(res.content)
# print(res.status_code)
# # filename = str(input('Введите имя для файла :'))
# # ya.upload_from_url(filename)

# folder = str(input('Введите имя папки (Enter: по умолчанию текущая дата): '))
# res = ya.new_folder(folder)
# print(res.status_code)
