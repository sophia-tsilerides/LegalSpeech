#### Transcribing with Google’s Speech-to-Text API
1. Enable Speech-to-Text API
Go to project in GCP
Search for “Speech-to-Text” in the search bar
2. Install Google Cloud SDK (if you haven’t already)
https://www.youtube.com/watch?v=k-8qFh8EfFA
3. Configure your machine to gcloud

`gcloud components update`				should run this regularly

`gcloud auth login`					to log into the system

`gcloud config set project ak8096-biasjudge-d38a`     Configure local setup

4. Create a service account key 

- In console, go to APIs&Services > Credentials 
- In Service Accounts section Click on the Service Account link 
- In Keys section, Add Key  > Create New Key > JSON (downloads JSON)
- Put the JSON somewhere where you can access it easily (don’t ever put this in code or 
public repos!!)
- In terminal: `export GOOGLE_APPLICATION_CREDENTIALS=`"[PATH OF JSON]" 
	Ex.  `export GOOGLE_APPLICATION_CREDENTIALS=/Users/sophiatsilerides/Desktop/1006/akxxxx-biasjudge-xxxx-xxxxxxxxxxxx.json`
5. pip install google-cloud-speech (if you haven’t already)
6. Transcribe

Have in the file you are cd’d into the .flac file you want to transcribe and the GoogleSpeech.py file from github
`python GoogleSpeech.py sample.flac`

7. Disable API & delete service key

8. Commands if needed:
- ffmpeg -i input.wav -codec:a libmp3lame -qscale:a 2 output.mp3	.wav to .mp3
- ffmpeg -i output.mp3 -ac 1 -ar 16000 sample.flac			.mp3 to .flac
