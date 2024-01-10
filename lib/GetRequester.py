import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url = self.url
        response = requests.get(url)
        return response.content
        pass

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)
        pass

get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
get_requester.load_json()