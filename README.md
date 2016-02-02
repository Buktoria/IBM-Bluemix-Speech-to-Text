# IBM-Bluemix-Speech-to-Text
---

This workshop is here to give you an introduction to IBM Bluemix and their speech-to-text api. I have written a simple wrapper for making http requests to their api.

## References

Feel free to use  the code that is provided in this workshop.

[Bluemix Speech to Text Api Docs](https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/speech-to-text/api/v1/)

[Other samples using Bluemix Api's](https://github.com/watson-developer-cloud)

### Step One: Create a service

1. Log in to your Bluemix account
2. Go to API's or Catalog
3. Under Watson services click on Personality Insights
4. Click create "Create"

### Step Two: Setup

1. Make a new python virtual environment for the tutorial in python3. You can do this by doing the following, `virtualenv -p python3 speech_venv` Then to activate, `source speech_venv/bin/activate` Then do a pip install for requests by doing the following `pip install requests`

2. Get your service credentials. To do this go to "Service Credentials"

3. Copy and paste your credentials into the `Speech_to_Text_interface.py` file.

### Step Three: Create an audio recording

1. Make a recording

2. Make sure its in a ".wav" format. If not go to http://media.io/ to convert it to a ".wav" format.

3. Change the file name in the `Speech_to_Text_interface.py` file to your recording.

4. Run the program!

5. Next try a youtube video! Find a video you want to convert to text. Go to http://www.onlinevideoconverter.com/mp3-converter to convert the video to a ".wav" file.

5. Change the file name in the `Speech_to_Text_interface.py` file to your recording.

6. Run the program!
