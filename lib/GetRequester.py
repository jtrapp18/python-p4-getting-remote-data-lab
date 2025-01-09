import requests
import json

class GetRequester: 

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response = requests.get(self.url)
        return response.json()


url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
req = GetRequester(url)

print(req.get_response_body())
print(req.load_json())

