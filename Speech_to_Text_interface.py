import pprint
import requests #http://docs.python-requests.org/en/latest/user/quickstart/

pp = pprint.PrettyPrinter(indent=2)
username = "e6f835c5-d844-42dc-9ad4-dd909aaaf99e"
password = "j9pEuCnmgZio"


class SpeechToTextInterface(object):

    def __init__(self, username, password):
        self.url = "https://stream.watsonplatform.net/speech-to-text/api"
        self.auth = requests.auth.HTTPBasicAuth(username, password)

    def models(self):
        response = requests.get(
            self.url + "/v1/models",
            auth=self.auth,
        )
        return response.json()

    def model(self, model_id):
        response = requests.get(
            self.url + "/v1/models/{}".format(model_id),
            auth=self.auth,
        )
        return response.json()

    def recognize(self, file_path, model='en-US_BroadbandModel', timestamps=False,
        word_confidence=False, inactivity_timeout=30, audio_type='wav'):

        with open(file_path, 'rb') as fp:
            file = fp.read()

            response = requests.post(
                self.url + "/v1/recognize",
                auth=self.auth,
                headers={"content-type": "audio/{}".format(audio_type)},
                data=file,
                params={
                    'model': model,
                    'timestamps': timestamps,
                    'word_confidence': word_confidence,
                    'inactivity_timeout': inactivity_timeout,
                }
            )


        return response.json()

if __name__ == '__main__':

    speech_to_text = SpeechToTextInterface(username, password)

    # See different language models
    #pp.pprint(speech_to_text.models())

    # See specific model info
    #pp.pprint(speech_to_text.model('en-US_BroadbandModel'))

    # Recognize audio file
    pp.pprint(speech_to_text.recognize("Taxidermy_a_Squirrel.wav"))
