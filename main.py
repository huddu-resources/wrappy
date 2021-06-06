import requests


class Wrapper:
    def __init__(self, base, headers, append_slash=True):
        self.base = base
        self.headers = headers
        self.append_slash

    def get(self, url, params={}):
        if self.append_slash:
            url = url + "/"

        res = requests.get(f"{self.base}{url}", params=params, headers=self.headers)
        return res

    def post(self, url, payload={}):
        if self.append_slash:
            url = url + "/"

        res = requests.post(f"{self.base}{url}", data=payload, headers=self.headers)
        return res

    def put(self, url, payload={}):
        if self.append_slash:
            url = url + "/"

        res = requests.put(f"{self.base}{url}", data=payload, headers=self.headers)
        return res

    def patch(self, url, payload={}):
        if self.append_slash:
            url = url + "/"

        res = requests.patch(f"{self.base}{url}", data=payload, headers=self.headers)
        return res

    def delete(self, url):
        if self.append_slash:
            url = url + "/"

        res = requests.delete(f"{self.base}{url}", headers=self.headers)
        return res
