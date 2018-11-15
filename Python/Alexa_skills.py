
#!/usr/bin/python

#This script is to work with an alexa skill


#Imports

from alexa_skill.intents import BuildInIntents



#Code




buildin_intents = BuildInIntents(
    help_message='Say to Alexa: "tell me a joke"',
    not_handled_message="Sorry, I don't understand you. Could you repeat?",
    stop_message='stop',
    cancel_message='cancel',
)








import requests
from alexa_skill.intents import BaseIntents

class JokeIntents(BaseIntents):
    @property
    def mapper(self):
        return {'random_joke': self.random_joke}

    def random_joke(self):
        joke_response = requests.get('http://api.icndb.com/jokes/random')
        if joke_response.status_code != 200:
            return self.response('Sorry, I did not find any joke. Please try again'), False

        return self.response(joke_response['value']['joke']), True






#Gunicorn stuff


def app(environ, start_response):
        data = b"Hello, World!\n"
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])



























