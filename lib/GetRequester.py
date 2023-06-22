import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Return the response body as bytes

    def load_json(self):
        response_body = self.get_response_body()
        return eval (response_body)  # Convert the response body to a Python object

